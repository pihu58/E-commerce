getting_all_cart_items = "SELECT * FROM CART"
updating_product_quantity_checkout = """UPDATE PRODUCTS SET pquantity = pquantity - (
                            SELECT CART.pquantity FROM CART 
                            WHERE CART.pid = PRODUCTS.pid AND CART.uid = 1223
                          ) WHERE EXISTS (
                            SELECT 1 FROM CART WHERE CART.pid = PRODUCTS.pid AND CART.uid = 1223
                          )"""