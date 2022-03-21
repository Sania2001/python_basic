# import sqlite3
# conn = sqlite3.connect('customer.db')
# c = conn.cursor()
# sqlite_query = '''CREATE TABLE customer_new(customer_id INTEGER PRIMARY KEY ,
#                  first_name TEXT NOT NULL,
#                  last_name TEXT NOT NULL,
#                  salary INTEGER NOT NULL )'''
# c.execute(sqlite_query)
# # print("Executed Successfully")
# insert_query = '''INSERT INTO customer_new
#                          (customer_id, first_name, last_name,  salary) VALUES
#                          (1, 'Sania', 'Shinde', 20000),
#                          (2, 'Karan', 'Singh', 11000),
#                          (3, 'Mohan', 'Chand', 9000),
#                          (4, 'Omkar', 'Patil', 12000),
#                          (5, 'Aditya', 'Kulkarni', 15000)'''
# c.execute(insert_query)
# conn.commit()
# print('Data of the customer table are:')
# c.execute(''' DELETE FROM customer_new WHERE salary BETWEEN 9000 AND 17000 ''')
# print(c.fetchall())
# conn.close()
#
#
#
#
#
# import sqlite3
# conn = sqlite3.connect('client.db')
# c = conn.cursor()
# sqlite_query = '''CREATE TABLE client_table(customer_id INTEGER PRIMARY KEY ,
#                  first_name TEXT NOT NULL,
#                  last_name TEXT NOT NULL,
#                  salary INTEGER NOT NULL )'''
# c.execute(sqlite_query)
# # print("Executed Successfully")
# insert_query = '''INSERT INTO client_table
#                          (customer_id, first_name, last_name,  salary) VALUES
#                          (1, 'Sania', 'Shinde', 20000),
#                          (2, 'Karan', 'Singh', 11000),
#                          (3, 'Mohan', 'Chand', 9000),
#                          (4, 'Omkar', 'Patil', 12000),
#                          (5, 'Aditya', 'Kulkarni', 15000)'''
# c.execute(insert_query)
# conn.commit()
# print('Data of the client table are:')
# c.execute(''' SELECT * FROM client_table ORDER BY first_name ASC''')
# print(c.fetchall())
# conn.close()
