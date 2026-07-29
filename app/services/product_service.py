# Import repository functions
from app.repository.product_repository import (
    add_product, get_all_products, get_product_by_id,update_product,
    delete_product,search_products,filter_products,sort_products,paginate_products)

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

def update_existing_product(product_id, product):
    return update_product(product_id, product)

# Service function to delete a product
def delete_existing_product(product_id):

    # Call Repository
    return delete_product(product_id)

# Service function to search products
def search_product_by_name(name):
    return search_products(name)

# Service function to filter products by category
def filter_products_by_category(category):

    # Call Repository Layer
    return filter_products(category)

# Service function
def sort_all_products():
    return sort_products() 

def get_paginated_products(page, size):

    offset = (page - 1) * size

    return paginate_products(size, offset)