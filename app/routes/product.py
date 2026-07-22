# Import APIRouter from FastAPI
from fastapi import APIRouter

# Import Product schema
from app.schemas import Product

from app.services.product_service import(
create_product, fetch_all_products,  fetch_product_by_id,)

# Create Router object
router = APIRouter()

# POST API
@router.post("/products")
def add_product(product: Product):

    # Call Service Layer
    return create_product(product)

# GET API
@router.get("/products")
def get_products():

    # Call Service Layer
    return fetch_all_products()

# GET Product By ID
@router.get("/products/{product_id}")
def get_product(product_id: int):

    # Call Service Layer
    return fetch_product_by_id(product_id)