import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="yugabyte",
    port="5433",
    password="yugabyte")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM products")

# Retrieve query results
records = cur.fetchall()
print(records[0])
