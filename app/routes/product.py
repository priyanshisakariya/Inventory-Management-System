from fastapi import APIRouter, Query
from app.schemas import Product

from app.services.product_service import (
    create_product,
    fetch_all_products,
    fetch_product_by_id,
    update_existing_product,
    delete_existing_product,
    search_product_by_name,
    filter_products_by_category,
    sort_all_products,
    get_paginated_products
)

router = APIRouter()

# POST
@router.post("/products")
def add_product(product: Product):
    return create_product(product)

# GET ALL
@router.get("/products")
def get_products():
    return fetch_all_products()

# SEARCH  <-- MUST COME BEFORE {product_id}
@router.get("/products/search")
def search_product(name: str = Query(...)):
    return search_product_by_name(name)

# FILTER Products by Category
@router.get("/products/filter")
def filter_product(category: str = Query(...)):

    # Call Service Layer
    return filter_products_by_category(category)

@router.get("/products/pagination")
def pagination(page: int = 1, size: int = 5):
    return get_paginated_products(page, size)

# GET BY ID
@router.get("/products/{product_id}")
def get_product(product_id: int):
    return fetch_product_by_id(product_id)

# UPDATE
@router.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    return update_existing_product(product_id, product)

# DELETE
@router.delete("/products/{product_id}")
def delete_product_by_id(product_id: int):
    return delete_existing_product(product_id)

# SORT Products
@router.get("/products/sort")
def sort_product():
    return sort_all_products()
