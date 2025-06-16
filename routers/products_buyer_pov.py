from fastapi import APIRouter, HTTPException
from db.db_setup import cursor
from typing import List


router = APIRouter(tags=["products_buyer_pov"])


@router.get("/list", summary="Getting all products")
async def get_all_products_categories() -> List:
    """
    view all available categories
    """
    try:
        cursor.execute("SELECT DISTINCT ptype FROM PRODUCTS")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/search", summary="Search products by category")
def search_products(Ptype: str = None) -> List:
    """
    search products of a particular product category
    """
    if Ptype is None:
        raise HTTPException(status_code=400, detail="Please provide input")
    Ptype = Ptype.lower()
    try:
        cursor.execute("SELECT * FROM PRODUCTS WHERE ptype = %s", (Ptype,))
        data = cursor.fetchall()
        if not data:
            raise HTTPException(status_code=404, detail="No products found in this category.")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching for products: {str(e)}")
