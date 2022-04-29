As a long time [PostgreSQL](https://www.postgresql.org/) user, it's normal that [YugabyteDB](https://www.yugabyte.com/) got my attention. It's a distributed SQL database which features-compatible with PostgreSQL so that I don't need to lose my investation. YugabyteDB reuses PostgreSQL's query layer, so I can use my development tools as usual. It gives me more since there is also Cassandra query layer. Using YugabyteDB I can reuse my SQL skill and development tools, enhanced with NOSQL data model (especially **wide-column store**), while I have NewSQL's resiliency, scalability, and high performance.

In this article, I am going to setup YugabyteDB for local cluster, populate data, and access the data using Python3.

## Install and Configure YugabyteDB

Installation is very easy and straightforward. No source code compilation (well, unless you really want to dig that deep). Just [download](https://download.yugabyte.com/local) YugabyteDB, extract, then execute `bin/post-install.sh`. When this step has finished, make sure that `path/to/extracted/yugabytedb/bin` is in the $PATH. Here's what I did:

**Fish Shell**

```bash
$ set -x path/to/extracted/yugabytedb/bin $PATH
```

**Bash Shell**

```bash
$ export PATH=path/to/extracted/yugabytedb/bin:$PATH
``` 

> **Note**: to avoid writing the same thing over and over again, I usually put the `set` or `export` statements above inside a file and then whenever I want to use YugabyteDB, I just `source the-file.sh`.

Next, we need to configure YugabyteDB. To configure YugabyteDB, see [YugabyteDB configuration](https://docs.yugabyte.com/latest/deploy/manual-deployment/system-config/). The documentation is complete but to have everything works, all I need to do is changing `/etc/security/limits.conf` to:

```bash
# /etc/security/limits.conf
#
#Each line describes a limit for a user in the form:
...
...
...
#<domain>      <type>  <item>         <value>
#

*                -       core            unlimited
*                -       data            unlimited
*                -       fsize           unlimited
*                -       sigpending      119934
*                -       memlock         64
*                -       rss             unlimited
*                -       nofile          1048576
*                -       msgqueue        819200
*                -       stack           8192
*                -       cpu             unlimited
*                -       nproc           12000
*                -       locks           unlimited

# End of file
```
Depends on your situation, maybe you need to restart or just logout-login back. 

All data, logs, configurations, etc for YugabyteDB reside in `$HOME/var/`. Do check `$HOME/var/conf/yugabytedb.conf` for more configuration:

```bash
{
    "tserver_webserver_port": 9000, 
    "master_rpc_port": 7100, 
    "universe_uuid": "dabc3d28-6982-4585-8b10-5faa7352da02", 
    "webserver_port": 7200, 
    "ysql_enable_auth": false, 
    "cluster_member": true, 
    "ycql_port": 9042, 
    "data_dir": "/home/bpdp/var/data", 
    "tserver_uuid": "71ad70b8eef149ae945842572e0fff75", 
    "use_cassandra_authentication": false, 
    "log_dir": "/home/bpdp/var/logs", 
    "polling_interval": "5", 
    "listen": "0.0.0.0", 
    "callhome": true, 
    "master_webserver_port": 7000, 
    "master_uuid": "1ef618e573a04e1d835f4ed4364825d7", 
    "master_flags": "", 
    "node_uuid": "6ae31951-7199-4c22-b30b-e8f235cef7db", 
    "join": "", 
    "ysql_port": 5433, 
    "tserver_flags": "", 
    "tserver_rpc_port": 9100
}                                                          
```

> **Note**: PostgreSQL usually uses port 5432, but YugabyteDB default port is 5433. Pay attention to this since we are going to use this when we write our code.

So many things we can do with YugabyteDB, but for this article, I will concentrate more on Python app development. Therefore, it's enough now to have local cluster. Let's set it up!.

Let's run YugabyteDB:

```bash
$ yugabyted start
Starting yugabyted...
✅ System checks           

+--------------------------------------------------------------------------------------------------+
|                                            yugabyted                                             |
+--------------------------------------------------------------------------------------------------+
| Status              : Running. Leader Master is present                                          |
| Web console         : http://127.0.0.1:7000                                                      |
| JDBC                : jdbc:postgresql://127.0.0.1:5433/yugabyte?user=yugabyte&password=yugabyte  |
| YSQL                : bin/ysqlsh   -U yugabyte -d yugabyte                                       |
| YCQL                : bin/ycqlsh   -u cassandra                                                  |
| Data Dir            : /home/bpdp/var/data                                                        |
| Log Dir             : /home/bpdp/var/logs                                                        |
| Universe UUID       : dabc3d28-6982-4585-8b10-5faa7352da02                                       |
+--------------------------------------------------------------------------------------------------+
🚀 yugabyted started successfully! To load a sample dataset, try 'yugabyted demo'.
🎉 Join us on Slack at https://www.yugabyte.com/slack
👕 Claim your free t-shirt at https://www.yugabyte.com/community-rewards/
$
```

Check the status:

```bash
$ yugabyted status

+--------------------------------------------------------------------------------------------------+
|                                            yugabyted                                             |
+--------------------------------------------------------------------------------------------------+
| Status              : Running. Leader Master is present                                          |
| Web console         : http://127.0.0.1:7000                                                      |
| JDBC                : jdbc:postgresql://127.0.0.1:5433/yugabyte?user=yugabyte&password=yugabyte  |
| YSQL                : bin/ysqlsh   -U yugabyte -d yugabyte                                       |
| YCQL                : bin/ycqlsh   -u cassandra                                                  |
| Data Dir            : /home/bpdp/var/data                                                        |
| Log Dir             : /home/bpdp/var/logs                                                        |
| Universe UUID       : dabc3d28-6982-4585-8b10-5faa7352da02                                       |
+--------------------------------------------------------------------------------------------------+
```

Just in case you need to shutdown YugabyteDB:

```bash
$ yugabyted stop
Stopped yugabyted using config /home/bpdp/var/conf/yugabyted.conf.
$
```

Ok, now let YugabyteDB runs. We will use that for later processes.

## Data Preparation

Now, it gets more interesting. Using one YugabyteDB server instance, we can use both SQL and Cassandra data model. Let's aggregate some data into PostgreSQL layer and Cassandra layer. For this purpose, we still use default user and password. Later on, you can manage the security side of YugabyteDB.

> **Note**: default username and password for PostgreSQL layer: **yugabyte:yugabyte**, while for Cassandra: **cassandra:cassandra**. 

### SQL Data

YugabyteDB provides [sample datasets](https://docs.yugabyte.com/latest/sample-data/) for SQL data. We are going to use [Northwind Traders Database](https://docs.yugabyte.com/latest/sample-data/northwind/). Get the `DDL` and `Data` scripts from the Northwind sample datasets URL. Follow this sceen dump to prepare the database, tables, and populate the data. The **<database-name>#** pompt is the place to write command.

```bash
$ ysqlsh -U yugabyte
ysqlsh (11.2-YB-2.7.2.0-b0)
Type "help" for help.

yugabyte=# create database northwind;
CREATE DATABASE
yugabyte=# \l
                                   List of databases
      Name       |  Owner   | Encoding | Collate |    Ctype    |   Access privileges   
-----------------+----------+----------+---------+-------------+-----------------------
 northwind       | yugabyte | UTF8     | C       | en_US.UTF-8 | 
 postgres        | postgres | UTF8     | C       | en_US.UTF-8 | 
 system_platform | postgres | UTF8     | C       | en_US.UTF-8 | 
 template0       | postgres | UTF8     | C       | en_US.UTF-8 | =c/postgres          +
                 |          |          |         |             | postgres=CTc/postgres
 template1       | postgres | UTF8     | C       | en_US.UTF-8 | =c/postgres          +
                 |          |          |         |             | postgres=CTc/postgres
 yugabyte        | postgres | UTF8     | C       | en_US.UTF-8 | 
(6 rows)

yugabyte=# \c northwind
You are now connected to database "northwind" as user "yugabyte".
northwind=# \i northwind_ddl.sql 
SET
SET
SET
SET
SET
SET
SET
SET
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
northwind=# \d
                 List of relations
 Schema |          Name          | Type  |  Owner   
--------+------------------------+-------+----------
 public | categories             | table | yugabyte
 public | customer_customer_demo | table | yugabyte
 public | customer_demographics  | table | yugabyte
 public | customers              | table | yugabyte
 public | employee_territories   | table | yugabyte
 public | employees              | table | yugabyte
 public | order_details          | table | yugabyte
 public | orders                 | table | yugabyte
 public | products               | table | yugabyte
 public | region                 | table | yugabyte
 public | shippers               | table | yugabyte
 public | suppliers              | table | yugabyte
 public | territories            | table | yugabyte
 public | us_states              | table | yugabyte
(14 rows)

northwind=# \i northwind_data.sql
...
...
...
INSERT 0 1
INSERT 0 1
INSERT 0 1
northwind=# select * from products;
 product_id |           product_name           | supplier_id | category_id |  quantity_per_unit   | unit_price | units_in_s
tock | units_on_order | reorder_level | discontinued 
------------+----------------------------------+-------------+-------------+----------------------+------------+-----------
-----+----------------+---------------+--------------
          4 | Chef Anton's Cajun Seasoning     |           2 |           2 | 48 - 6 oz jars       |         22 |           
  53 |              0 |             0 |            0
         46 | Spegesild                        |          21 |           8 | 4 - 450 g glasses    |         12 |           
  95 |              0 |             0 |            0
         73 | Röd Kaviar                       |          17 |           8 | 24 - 150 g jars      |         15 |           
 101 |              0 |             5 |            0
         29 | Thüringer Rostbratwurst          |          12 |           6 | 50 bags x 30 sausgs. |     123.79 |           
   0 |              0 |             0 |            1
         70 | Outback Lager                    |           7 |           1 | 24 - 355 ml bottles  |         15 |           
  15 |             10 |            30 |            0
         25 | NuNuCa Nuß-Nougat-Creme          |          11 |           3 | 20 - 450 g glasses   |         14 |           
  76 |              0 |            30 |            0
         54 | Tourtière                        |          25 |           6 | 16 pies              |       7.45 |           
  21 |              0 |            10 |            0
...
...
...
         17 | Alice Mutton                     |           7 |           6 | 20 - 1 kg tins       |         39 |           
   0 |              0 |             0 |            1
         59 | Raclette Courdavault             |          28 |           4 | 5 kg pkg.            |         55 |           
  79 |              0 |             0 |            0
(77 rows)

northwind=#  
```

Finish with SQL data, it's about the time to populate column-wide - Cassandra data.

### NOSQL Column-wide Data - Apache Cassandra

We will use a simple keyspace: one keyspace, consists of one table. Create a CQL script file (here, the file name is `zimera-employees.cql`):

```sql
CREATE KEYSPACE zimera
  WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};

USE zimera;

CREATE TABLE employees(
   e_id int PRIMARY KEY,
   e_fullname text,
   e_address text,
   e_dept text,
   e_role text
   );

INSERT INTO employees (e_id, e_fullname, e_address, e_dept, e_role) VALUES(1,'Zaky A. Aditya', 'Dusun Medelan, RT 01, Umbulmartani, Ngemplak, Sleman, DIY, Indonesia', 'Information Technology', 'Machine Learning Developer');
```

Execute the script:

```bash
$ ycqlsh -f zimera-employees.cql 
$
```

Check whether succeed or not:

```bash
$ ycqlsh -u cassandra
Password: 
Connected to local cluster at 127.0.0.1:9042.
[ycqlsh 5.0.1 | Cassandra 3.9-SNAPSHOT | CQL spec 3.4.2 | Native protocol v4]
Use HELP for help.
cassandra@ycqlsh> use zimera;
cassandra@ycqlsh:zimera> select * from employees;

 e_id | e_fullname     | e_address                                                            | e_dept                 | e_role
------+----------------+----------------------------------------------------------------------+------------------------+----------------------------
    1 | Zaky A. Aditya | Dusun Medelan, RT 01, Umbulmartani, Ngemplak, Sleman, DIY, Indonesia | Information Technology | Machine Learning Developer

(1 rows)
cassandra@ycqlsh:zimera> 
$
```

## Python - Drivers

Since we are going to use both PostgreSQL and Apache Cassandra data model, we need to install those two drivers: [psycopg2](https://www.psycopg.org/) for PostgreSQL and [Python Driver for Apache Cassandra](https://github.com/datastax/python-driver). 

> **Note**: currently, `psycopg` is still developing [psycopg3](https://www.psycopg.org/psycopg3/). We do not use psycopg3 since it is still in early development stage, but once `psycopg3` is released, there should be easy to migrate.

**Install Cassandra Driver**
 
```bash
$ conda install cassandra-driver
...
...
...
  added / updated specs:
    - cassandra-driver


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cassandra-driver-3.25.0    |   py39h27cfd23_0         3.0 MB
    ------------------------------------------------------------
                                           Total:         3.0 MB

The following NEW packages will be INSTALLED:

  blas               pkgs/main/linux-64::blas-1.0-mkl
  cassandra-driver   pkgs/main/linux-64::cassandra-driver-3.25.0-py39h27cfd23_0
  intel-openmp       pkgs/main/linux-64::intel-openmp-2021.3.0-h06a4308_3350
  libev              pkgs/main/linux-64::libev-4.33-h7b6447c_0
  mkl                pkgs/main/linux-64::mkl-2021.3.0-h06a4308_520
  mkl-service        pkgs/main/linux-64::mkl-service-2.4.0-py39h7f8727e_0
  mkl_fft            pkgs/main/linux-64::mkl_fft-1.3.0-py39h42c9631_2
  mkl_random         pkgs/main/linux-64::mkl_random-1.2.2-py39h51133e4_0
  numpy              pkgs/main/linux-64::numpy-1.20.3-py39hf144106_0
  numpy-base         pkgs/main/linux-64::numpy-base-1.20.3-py39h74d4b33_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_0


Proceed ([y]/n)? y
...
...
...
$
```

**Install PostgreSQL Driver**

```bash
$ conda install psycopg2                                                              ...
...
...
  added / updated specs:
    - psycopg2


The following NEW packages will be INSTALLED:

  krb5               pkgs/main/linux-64::krb5-1.19.2-hac12032_0
  libedit            pkgs/main/linux-64::libedit-3.1.20210714-h7f8727e_0
  libpq              pkgs/main/linux-64::libpq-12.2-h553bfba_1
  psycopg2           pkgs/main/linux-64::psycopg2-2.8.6-py39h3c74f83_1


Proceed ([y]/n)? y
...
...
$
```

> **Note**: I use `conda` for package management, but you don't need to. You can also use `pip`, in this case just `pip install psycopg2` and `pip install cassandra-driver`.

## Let's Code!

### Accessing SQL Data

```python
# code-sql.py
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
```

Results:

```bash
$ python code-sql.py
(4, "Chef Anton's Cajun Seasoning", 2, 2, '48 - 6 oz jars', 22.0, 53, 0, 0, 0)
$
```

### Accessing Cassandra Data Model

```python
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('zimera')

rows = session.execute('SELECT e_fullname, e_address, e_dept, e_role FROM employees')
for row in rows:
    print(row.e_fullname, row.e_address, row.e_dept, row.e_role)
```

Results:

```bash
$ python code-cassandra.py 
Zaky A. Aditya Dusun Medelan, RT 01, Umbulmartani, Ngemplak, Sleman, DIY, Indonesia Information Technology Machine Learning Developer
$
```

What if we want to use both data model in one python source code? Here you go:

```python
# code-all.py
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
```

Results:

```bash
$ python code-all.py
(4, "Chef Anton's Cajun Seasoning", 2, 2, '48 - 6 oz jars', 22.0, 53, 0, 0, 0)
Zaky A. Aditya Dusun Medelan, RT 01, Umbulmartani, Ngemplak, Sleman, DIY, Indonesia Information Technology Machine Learning Developer
$
```

Aren't they cool? Happy coding!

