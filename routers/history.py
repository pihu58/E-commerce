from fastapi import APIRouter, HTTPException
from db.db_setup import cursor
from typing import List

router = APIRouter(tags=["buying_history"])

@router.get("/bought_items", summary="Buying history")
def view_history() -> List:
    """
    view buyer history
    """
    try:
        cursor.execute("SELECT * FROM BOUGHT_ITEMS")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving history: {str(e)}")
