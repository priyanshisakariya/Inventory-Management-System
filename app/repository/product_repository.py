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