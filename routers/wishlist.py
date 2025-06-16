from fastapi import APIRouter, HTTPException
from db.db_setup import conn, cursor
from typing import List
from models.all_model_defs import WishlistItem


router = APIRouter(tags=["wishlist"])

@router.post("/add", summary="Add to wishlist")
def add_to_wishlist(item: WishlistItem = None) -> List:
    """
    add to wishlist.
    WishListItem has pname and pquantity
    """
    pname = item.pname.lower()
    pquantity = item.pquantity
    try:
        cursor.execute("SELECT * FROM PRODUCTS WHERE pname = %s", (pname,))
        data = cursor.fetchone()
        if not data:
            raise HTTPException(status_code=404, detail="Product not found.")
        data = list(data)
        if pquantity > data[5]:
            raise HTTPException(status_code=400, detail="Requested quantity unavailable.")
        data[5] = pquantity
        cursor.execute("INSERT INTO WISHLIST VALUES(%s,%s,%s,%s,%s,%s)", (1223, data[0], data[1], data[2], data[5], data[2]*data[5]))
        conn.commit()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding to wishlist: {str(e)}")

@router.get("/view", summary="View wishlist")
def view_wishlist() -> List:
    """
    view wishlist.
    """
    try:
        cursor.execute("SELECT * FROM WISHLIST")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching wishlist: {str(e)}")
    

@router.put("/modify", summary="Modify wishlist quantity")
def modify_wishlist(item: WishlistItem = None) -> List:
    """
    modify product quantity in wishlist.
    WishListItem has pname and pquantity
    """
    pname = item.pname.lower()
    pquantity = item.pquantity
    try:
        cursor.execute("UPDATE WISHLIST SET pquantity = %s WHERE name = %s AND uid = 1223", (pquantity, pname))
        cursor.execute("UPDATE WISHLIST SET ptotalprice = pquantity*pprice WHERE name = %s AND uid = 1223", (pname,))
        conn.commit()
        cursor.execute("SELECT * FROM WISHLIST WHERE name = %s", (pname,))
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error modifying wishlist: {str(e)}")

@router.delete("/remove", summary="Remove from wishlist")
def del_from_wishlist(item: WishlistItem = None) -> List:
    """
    remove item from wishlist.
    WishListItem has pname and pquantity
    """
    pname = item.pname.lower()
    try:
        cursor.execute("DELETE FROM WISHLIST WHERE name = %s", (pname,))
        conn.commit()
        cursor.execute("SELECT * FROM WISHLIST")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error removing from wishlist: {str(e)}")

