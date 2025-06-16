from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    pid : Optional[int]
    pname: Optional[str]
    pprice: Optional[float]
    ptype: Optional[str]
    prating: Optional[float]
    pquantity: Optional[int]
    

class CartItem(BaseModel):
    pname: Optional[str] 
    pquantity: Optional[int]



class WishlistItem(BaseModel):
    pname: Optional[str]
    pquantity: Optional[int]


class User(BaseModel):
    uid: Optional[int]
    uname: Optional[str]
    ubalance: Optional[float]