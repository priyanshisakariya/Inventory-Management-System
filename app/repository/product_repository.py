# Import the database connection from database.py
from app.database import connection


# Function to insert a new product into PostgreSQL
def add_product(product):

    # Create a cursor object.
    # Cursor is used to execute SQL queries.
    cursor = connection.cursor()

    # SQL query
    query = """
    INSERT INTO products(name, category, price, quantity)
    VALUES (%s, %s, %s, %s)
    """

    # Execute SQL query
    cursor.execute(
        query,
        (
            product.name,
            product.category,
            product.price,
            product.quantity
        )
    )

    # Save changes permanently
    connection.commit()

    # Close cursor
    cursor.close()

    return "Product Added Successfully"


# Function to get all products
def get_all_products():

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = "SELECT * FROM products"

    # Execute query
    cursor.execute(query)

    # Fetch all rows from PostgreSQL
    products = cursor.fetchall()

    # Close cursor
    cursor.close()

    # Return data
    return products

# Function to get a single product by ID
def get_product_by_id(product_id):

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    SELECT * FROM products
    WHERE id = %s
    """

    # Execute query
    cursor.execute(query, (product_id,))

    # Fetch only one row
    product = cursor.fetchone()

    # Close cursor
    cursor.close()

    # Return product
    return product

# Function to update product
def update_product(product_id, product):

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    UPDATE products
    SET name = %s,
        category = %s,
        price = %s,
        quantity = %s
    WHERE id = %s
    """

    # Execute query
    cursor.execute(
        query,
        (
            product.name,
            product.category,
            product.price,
            product.quantity,
            product_id
        )
    )

    # Save changes
    connection.commit()

    # Close cursor
    cursor.close()

    return {"message": "Product Updated Successfully"}


# Function to delete a product
def delete_product(product_id):

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    DELETE FROM products
    WHERE id = %s
    """

    # Execute query
    cursor.execute(query, (product_id,))

    # Save changes
    connection.commit()

    # Close cursor
    cursor.close()

    # Return message
    return {"message": "Product Deleted Successfully"}


# Function to search products by name
def search_products(name):

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    SELECT *
    FROM products
    WHERE name ILIKE %s
    """

    # Execute query
    cursor.execute(query, (f"%{name}%",))

    # Fetch matching products
    products = cursor.fetchall()

    # Close cursor
    cursor.close()

    return products

# Filter products by category
def filter_products(category):

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    SELECT *
    FROM products
    WHERE category = %s
    """

    # Execute query
    cursor.execute(query, (category,))

    # Fetch data
    products = cursor.fetchall()

    # Close cursor
    cursor.close()

    return products

# Sort products by price
def sort_products():

    # Create cursor
    cursor = connection.cursor()

    # SQL Query
    query = """
    SELECT *
    FROM products
    ORDER BY price ASC
    """

    # Execute query
    cursor.execute(query)

    # Fetch data
    products = cursor.fetchall()

    # Close cursor
    cursor.close()

    return products

# Pagination
def paginate_products(limit, offset):

    cursor = connection.cursor()

    query = """
    SELECT *
    FROM products
    LIMIT %s OFFSET %s
    """

    cursor.execute(query, (limit, offset))

    products = cursor.fetchall()

    cursor.close()

    return products