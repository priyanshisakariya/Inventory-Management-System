# 📦 Inventory Management System REST API

A backend Inventory Management System developed using **Python, FastAPI, and PostgreSQL** following a layered architecture. The project provides RESTful APIs for managing inventory products with CRUD operations and demonstrates clean code practices.

---

## 🚀 Features

- Create Product
- Get All Products
- Get Product by ID
- Update Product (In Progress)
- Delete Product (In Progress)
- Layered Architecture (Route → Service → Repository)
- PostgreSQL Database Integration
- Raw SQL Queries
- FastAPI Validation using Pydantic
- Interactive Swagger UI Documentation

---

## 🛠️ Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Pydantic

---

## 📂 Project Structure

```
InventoryManagement/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   ├── repository/
│   │     └── product_repository.py
│   ├── services/
│   │     └── product_service.py
│   └── routes/
│         └── product.py
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/InventoryManagement.git
```

Move into the project

```bash
cd InventoryManagement
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## ✅ Implemented APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /products | Add Product |
| GET | /products | Get All Products |
| GET | /products/{id} | Get Product By ID |

---

## 🗄️ Database

PostgreSQL

Table: **products**

Columns

- id
- name
- category
- price
- quantity

---

## 👩‍💻 Author

**Priyanshi Sakariya**

MCA Student | Python Backend Developer | FastAPI | PostgreSQL