from fastapi import APIRouter, HTTPException
from db.db_setup import conn, cursor
from typing import List, Dict
from models.all_model_defs import CartItem
from config.queries import getting_all_cart_items, updating_product_quantity_checkout

router = APIRouter(tags=["cart"])

@router.post("/add", summary="Add to cart")
def add_to_cart(item: CartItem = None) -> List:
    """
    Add products to cart.
    CartItem has pname and pquantity
    """
    pname = item.pname.lower()
    pquantity = item.pquantity
    try:
        cursor.execute("SELECT * FROM PRODUCTS WHERE pname = %s", (pname,))
        data = list(cursor.fetchone())
        if not data:
            raise HTTPException(status_code=404, detail="Product not found.")
        if type(pquantity) != int:
            raise HTTPException(detail="Incorrect data type give. Please enter integers only.")
        if pquantity > data[5]:
            raise HTTPException(status_code=400, detail="Requested quantity unavailable.")
        
        data[5] = pquantity
        cursor.execute("INSERT INTO CART VALUES(%s,%s,%s,%s,%s,%s)", (1223, data[0], data[1], data[2], data[5], data[2]*data[5]))
        conn.commit()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding to cart: {str(e)}")
 

@router.get("/view", summary="View cart")
def view_cart() -> List:
    """
    view cart
    """
    try:
        cursor.execute(getting_all_cart_items)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching cart: {str(e)}")
    

@router.put("/modify", summary="Modify cart quantity")
def modify_cart(item: CartItem = None) -> List:
    """
    modify product quantity in cart
    """
    pname = item.pname.lower()
    pquantity = item.pquantity
    try:
        cursor.execute("UPDATE CART SET pquantity = %s WHERE name = %s AND uid = 1223", (pquantity, pname))
        cursor.execute("UPDATE CART SET ptotalprice = pquantity*pprice WHERE name = %s AND uid = 1223", (pname,))
        conn.commit()
        cursor.execute("SELECT * FROM CART WHERE name = %s", (pname,))
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error modifying cart: {str(e)}")
    


@router.delete("/remove", summary="Remove item from cart")
def del_from_cart(item : CartItem = None) -> List:
    """
    remove item from cart
    """
    pname = item.pname.lower()
    try:
        cursor.execute("DELETE FROM CART WHERE name = %s", (pname,))
        conn.commit()
        cursor.execute(getting_all_cart_items)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error removing from cart: {str(e)}")


@router.get("/checkout", summary="Cart checkout")
def checkout() -> Dict:
    """
    cart checkout
    """
    try:
        cursor.execute("SELECT SUM(ptotalprice) FROM CART")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT ubalance FROM users")
        balance = cursor.fetchone()[0]
        if total is None:
            raise HTTPException(status_code=400, detail="Cart is empty.")
        if total > balance:
            raise HTTPException(status_code=402, detail="Insufficient funds.")

        cursor.execute("INSERT INTO BOUGHT_ITEMS SELECT * FROM CART")
        cursor.execute(updating_product_quantity_checkout)
        cursor.execute(f"UPDATE users SET ubalance = ubalance - {total}")
        cursor.execute("DELETE FROM CART WHERE uid = 1223")
        conn.commit()
        return {"message": "Payment successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during checkout: {str(e)}")
