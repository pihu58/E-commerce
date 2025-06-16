from db.db_setup import conn, cursor


all_table_defs = ["CREATE TABLE USERS (UID INT PRIMARY KEY, UNAME VARCHAR(40), UAGE INT, UBALANCE FLOAT )",
                  "CREATE TABLE PRODUCTS (Pid int PRIMARY KEY, Pname VARCHAR(50), Pprice float, Ptype VARCHAR(40), Prating float, Pquantity int)",
                  "CREATE TABLE CART UID int, pid int, name VARCHAR(50), Pprice float, Pquantity int, ptotalprice float,FOREIGN KEY (UID) REFERENCES USERS(UID)",
                  "CREATE TABLE BOUGHT_ITEMS UID int, pid int, name VARCHAR(50), Pprice float, Pquantity int, ptotalprice float,FOREIGN KEY (UID) REFERENCES USERS(UID)",
                  "CREATE TABLE WISHLIST (UID int, pid int, name VARCHAR(50), Pprice float, Pquantity int, ptotalprice float,FOREIGN KEY (UID) REFERENCES USERS(UID))"
                  ]

def all_tables_setup(all_table_defs):
    for i in all_table_defs:
        try:
            cursor.execute(i)
            conn.commit()
        except Exception as e:
            print(e)

all_tables_setup(all_table_defs=all_table_defs)
