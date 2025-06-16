# 🛒 E-commerce Backend API using FastAPI

This project is a simple and scalable **E-commerce backend** built using **FastAPI**, designed to handle product management, cart operations, and order processing. It demonstrates modular design, clean routing, and RESTful API practices.

---

## 🚀 Features

* **Product Management:** Listing and adding products.
* **Shopping Cart:** Efficient shopping cart management.
* **Order Processing:** Seamless order placement.
* **Wishlist:** Manage user wishlists.
* **User Management:** Handle user-related operations.
* **Database Integration:** Utilizes **PostgreSQL** via `psycopg2-binary`.
* **Modular Design:** Clean and organized folder structure using FastAPI routers.

---

## 🧰 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Uvicorn** (ASGI server)
* **PostgreSQL** (via `psycopg2-binary`)

---

## 📁 Project Structure


E-commerce/
├── main.py
├── routers/
│   ├── cart.py
│   ├── history.py
│   ├── products_buyer_pov.py
│   ├── products_seller_pov.py
│   ├── user.py
│   └── wishlist.py
├── models/
│   └── all_models_defs.py
├── db/
│   ├── db_setup.py
│   └── tables_setup.py
├── config/
│   └── queries.py
├── requirements.txt
└── README.md

---


## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/pihu58/E-commerce.git
cd E-commerce
```

### 2. Setup virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


---


##🧪 Testing

You can test APIs using:

Swagger UI: http://127.0.0.1:8000/docs
Postman or cURL

