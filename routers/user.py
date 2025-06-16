from fastapi import APIRouter, HTTPException
from db.db_setup import conn, cursor
from typing import List


router = APIRouter(tags=["user"])


@router.get("/view", summary="View user details")
def view_user_details() -> List:
    """
    view user details
    """
    try:
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user details: {str(e)}")
    

@router.put("/modify", summary="update user balance")
def modify_user_balance(ubalance: float = None) -> List:
    """
    modify user balance
    """
    try:
        cursor.execute("UPDATE users SET ubalance = %s + ubalance WHERE uid = 1223", (ubalance,))
        conn.commit()
        cursor.execute("SELECT * FROM users")
        return(cursor.fetchall())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user balance: {str(e)}")



