import psycopg2
#This creates a connection between Python and PostgreSQL.Think of it like plugging a USB cable between your laptop and your phone.Without the cable, they can't communicate.
connection = psycopg2.connect( 
    host="localhost",
    database="inventory_db",
    user="postgres",
    password="priyanshi123",
    port="5432"
)

print("Database Connected Successfully!")