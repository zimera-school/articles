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
