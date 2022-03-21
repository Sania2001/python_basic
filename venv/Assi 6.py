# import sqlite3
# con = sqlite3.connect('employee.db')
# cur = con.cursor()
# sqlite_query = '''CREATE TABLE employee_table(employee_id INTEGER PRIMARY KEY ,
#                  first_name TEXT NOT NULL,
#                  last_name TEXT NOT NULL,
#                  salary INTEGER NOT NULL )'''
# # cur.execute(sqlite_query)
# sqlite_insert_query = '''INSERT INTO employee_table
#                          (employee_id, first_name, last_name,  salary) VALUES
#                          (1, 'Sania', 'S', 20000),
#                          (2, 'Sankalp', 'K', 50000),
#                          (3, 'Sushant', 'M', 10000),
#                          (4, 'Mavi', 'KOUR', 45000)'''
# #cur.execute(sqlite_insert_query)
# con.commit()
# print('Content of the employee table')
# cur.execute(''' SELECT * FROM employee_table WHERE first_name = 'Sushant' AND last_name = 'M' ''')
# print(cur.fetchall())
# con.close()

# import sqlite3
# con = sqlite3.connect('event.db')
# cur = con.cursor()
# sqlite_query1 = '''CREATE TABLE event_table(id INTEGER ,
#                  event_name VARCHAR NOT NULL,
#                  month TEXT NOT NULL)'''
# # cur.execute(sqlite_query1)
# sqlite_insert_query1 = '''INSERT INTO event2_table
#                          (id, event_name, month) VALUES
#                          (3, 'Holi', 'March'),
#                          (4, 'Birthday Party', 'April'),
#                          (8, 'Rakhi ceremony', 'August')'''
# # cur.execute(sqlite_insert_query1)
# con.commit()
# print('Content of the event table:')
# cur.execute(''' SELECT * from event_table WHERE month = 'Aug' ''')
# print(cur.fetchall())

# import sqlite3
# con = sqlite3.connect('nobelwinner.db')
# cur = con.cursor()
# sqlite_query1 = '''CREATE TABLE nobel_table(Winner_name TEXT NOT NULL ,
#                  Domain TEXT NOT NULL,
#                  Year datetime NOT NULL)'''
# cur.execute(sqlite_query1)
# print('table is created sucessfully')
# sqlite_insert_query1 = '''INSERT INTO nobel_table
#                          (Winner_name, Domain, Year) VALUES
#                          ('Robert', 'World Peace', 1988),
#                          ('Ahmed', 'Literature', 1971),
#                          ('Phoebe', 'Physics', 2012),
#                          ('Chandler', 'Chemistry', 1998)'''
# cur.execute(sqlite_insert_query1)
# con.commit()
# print('Content of the nobel table:')
# cur.execute(''' SELECT * FROM nobel_table WHERE Domain = 'Literature' AND Year = 1971 ''')
# print(cur.fetchall())
# con.close()

# import sqlite3
# con = sqlite3.connect('customer1.db')
# cur = con.cursor()
# sqlite_query1 = '''CREATE TABLE customer_table(customer_id INTEGER ,
#                  cust_name TEXT NOT NULL,
#                  city TEXT NOT NULL,
#                  grade INTEGER NOT NULL,
#                  salesman_id INTEGER NOT NULL)'''
# # cur.execute(sqlite_query1)
# print('table is created sucessfully')
# sqlite_insert_query1 = '''INSERT INTO customer_table
#                          (customer_id, cust_name, city, grade, salesman_id) VALUES
#                          (1, 'Sania', 'New York', 101,  1001),
#                          (2, 'Sankalp', 'New York', 20, 1002),
#                          (3, 'Sushant', 'Delhi', 30, 1003)'''
# cur.execute(sqlite_insert_query1)
# con.commit()
# print('Contents of the customer table')
# cur.execute(''' SELECT * FROM customer_table WHERE city = 'New York' AND grade>100 ''')
# print(cur.fetchall())
# con.close()

# import sqlite3
# con = sqlite3.connect('employee.db')
# cur = con.cursor()
# sqlite_query = '''CREATE TABLE employee_table(employee_id INTEGER PRIMARY KEY ,
#                  first_name TEXT NOT NULL,
#                  last_name TEXT NOT NULL,
#                  salary INTEGER NOT NULL )'''
# # cur.execute(sqlite_query)
# sqlite_insert_query = '''INSERT INTO employee_table
#                          (employee_id, first_name, last_name,  salary) VALUES
#                          (100, 'Sania', 'S', 20000),
#                          (200, 'Sankalp', 'K', 4000),
#                          (300, 'Sushant', 'M', 10000),
#                          (400, 'Mavi', 'KOUR', 45000)'''
# cur.execute(sqlite_insert_query)
# con.commit()
# print('Content of the employee table:')
# cur.execute(''' SELECT first_name, last_name, salary FROM employee_table WHERE salary < 6000 ''')
# print(cur.fetchall())
# con.close()



