from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('zimera')

rows = session.execute('SELECT e_fullname, e_address, e_dept, e_role FROM employees')
for row in rows:
    print(row.e_fullname, row.e_address, row.e_dept, row.e_role)

