from fastapi import FastAPI, Request
from routers import products_buyer_pov, cart, wishlist, history, user, products_seller_pov
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.include_router(products_buyer_pov.router, prefix="/products_buyer_pov")
app.include_router(cart.router, prefix="/cart")
app.include_router(wishlist.router, prefix="/wishlist")
app.include_router(history.router, prefix="/history")
app.include_router(user.router, prefix="/user")
app.include_router(products_seller_pov.router, prefix="/products_seller_pov")



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    blank_errors = [err for err in exc.errors() if "blank" in err["msg"].lower()]
    if blank_errors:
        message = "One or more fields are blank. Please fill in all required fields."
    else:
        message = "Invalid input. Please enter only the prescribed datatype."
    
    return JSONResponse(
        status_code=422,
        content={
            "error": message,
            "details": exc.errors(),
            "body": exc.body
        },
    )
 
