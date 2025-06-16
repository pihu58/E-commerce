from fastapi import APIRouter, HTTPException
from db.db_setup import conn, cursor
from typing import List
from models.all_model_defs import Product

router = APIRouter(tags=["buying_seller_pov"])

@router.post("/create", summary="creating new product")
def create_new_product(item: Product = None):
    """
    create new product.
    product has 
    pid : int
    pname: str
    pprice: float
    ptype: str
    prating: float
    pquantity: int
    """
    pid = item.pid
    pname = item.pname.lower()
    pquantity = item.pquantity
    pprice = item.pprice
    ptype = item.ptype.lower()
    prating = item.prating
 
    try:
        cursor.execute("INSERT INTO PRODUCTS VALUES(%s,%s,%s,%s,%s,%s)", (pid, pname, pprice, ptype, prating, pquantity))
        conn.commit()
        return {"message": "Product creation successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding new item: {str(e)}")
    
@router.put("/modify", summary="update product quantity")
def modify_product_quantity(pid: int = None, pname: str = None, pquantity: int = None) -> List:
    """
    modify product quantity
    """
    pname = pname.lower()
    try:
        cursor.execute("UPDATE PRODUCTS SET pquantity = %s WHERE pid = %s", (pquantity, pid,))
        conn.commit()
        cursor.execute("SELECT * FROM PRODUCTS where pid = %s",(pid,))
        return(cursor.fetchall())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product quantity: {str(e)}")


