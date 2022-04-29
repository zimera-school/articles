import psycopg2
from cassandra.cluster import Cluster

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

cluster = Cluster()
session = cluster.connect('zimera')

rows = session.execute('SELECT e_fullname, e_address, e_dept, e_role FROM employees')
for row in rows:
    print(row.e_fullname, row.e_address, row.e_dept, row.e_role)

