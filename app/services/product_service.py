# Import repository functions
from app.repository.product_repository import (
    add_product, get_all_products, get_product_by_id,)

# Service function
def create_product(product):

    # Business Rule 1
    if product.price < 0:
        return {"error": "Price cannot be negative"}

    # Business Rule 2
    if product.quantity < 0:
        return {"error": "Quantity cannot be negative"}

    # If all validations pass,
    # call repository to insert into database
    return add_product(product)

# Service function to fetch all products
def fetch_all_products():

    # No business logic for now
    return get_all_products()

# Service function to fetch a product by ID
def fetch_product_by_id(product_id):

    # Call repository
    product = get_product_by_id(product_id)

    # Check if product exists
    if product is None:
        return {"message": "Product Not Found"}

    # Return product
    return product