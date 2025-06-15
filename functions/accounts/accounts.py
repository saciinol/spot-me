# import datetime
# import sqlite3
# import sys
# import os

# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# sys.path.insert(0, parent_dir)

# from app import db
# print(db)

# class Accounts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(200), nullable=False) 
#     username = db.Column(db.String(200), nullable=False) 
#     password = db.Column(db.String(200), nullable=False) 

# def create(email, username, password, confirmation):
#     if password == confirmation:
#         user = Accounts(
#             email=email,
#             username=username,
#             password=password,
#         )

#         db.session.add(user)
#         db.session.commit()

# DATABASE_FILE = "accounts.db"

# def initialize_database():
#     try:
#         conn = sqlite3.connect(DATABASE_FILE)
#         cursor = conn.cursor()
        
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS accounts(
#                 account_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 email TEXT,
#                 username TEXT,
#                 password TEXT
#             )
#         """)
        
#         conn.commit()
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Error: {e}")


# def check(email_username, password):
#     try:
#         conn = sqlite3.connect(DATABASE_FILE) 
#         cursor = conn.cursor()

#         cursor.execute("""
#             SELECT * FROM accounts WHERE email = ? OR username = ?
#         """, (email_username, email_username))
#         user = cursor.fetchone()
        
#         conn.close()

#         if user and password == user[3]:
#             return user[2]
#     except sqlite3.Error as e:
#         print(f"Error: {e}")

# def delete(email, username, password):
#     try:
#         conn = sqlite3.connect(DATABASE_FILE) 
#         cursor = conn.cursor()

#         cursor.execute("""
#             DELETE FROM accounts WHERE email = ? AND username = ? AND password = ?
#         """, (email, username, password))
#         deleted_rows = cursor.rowcount 

#         conn.commit() 
#         conn.close()

#         if deleted_rows > 0:
#             return True
#         else:
#             return False
#     except sqlite3.Error as e:
#         print(f"Error: {e}")
        
# def change(email, username, password, confirmation):
#     if password == confirmation:
#         try:
#             conn = sqlite3.connect(DATABASE_FILE) 
#             cursor = conn.cursor()

#             cursor.execute("""
#                 UPDATE accounts SET password = ?
#                 WHERE email = ? OR username = ?
#             """, (password, email, username))

#             conn.commit() 

#             cursor.execute("""
#                 SELECT * FROM accounts WHERE email = ? OR username = ? AND password = ?
#             """, (email, username, password))
#             user = cursor.fetchone()
            
#             conn.close()

#             if user:
#                 return True
#         except sqlite3.Error as e:
#             print(f"Error: {e}")

# def create_tables(username):
#     conn = sqlite3.connect(DATABASE_FILE)
#     cursor = conn.cursor()
    
#     try:
#         table_name = username + "_barbell_curl"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_dumbbell_bicep_curl"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)
        
#         table_name = username + "_bench_press"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_dumbbell_bench_press"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_barbell_press"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_dumbbell_press"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_lateral_raises"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_pull_ups"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_barbell_rows"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_squat"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         table_name = username + "_deadlift"
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS '{table_name}' (
#                 set_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 date TEXT,
#                 repetitions INTEGER
#             )
#         """)

#         conn.commit()
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Error: {e}")

# def add_exercise(username, count, exercise):
#     table_name = username + "_" + exercise
#     date = datetime.datetime.now()
    
#     date_formatted = date.strftime("%m/%d/%Y %I:%M:%S%p")
    
#     try:
#         conn = sqlite3.connect(DATABASE_FILE) 
#         cursor = conn.cursor()

#         cursor.execute(f"""
#             INSERT INTO '{table_name}' (date, repetitions)
#             VALUES (?, ?)
#         """, (date_formatted, count))
        
#         conn.commit()
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Error: {e}")
    
# def get_exercise(username, exercise):
#     table_name = username + "_" + exercise

#     try:
#         conn = sqlite3.connect(DATABASE_FILE) 
#         cursor = conn.cursor()

#         cursor.execute(f"""
#             SELECT set_id, date, repetitions FROM '{table_name}'
#         """)
#         data = cursor.fetchall()

#         conn.close()

#         return data
#     except sqlite3.Error as e:
#         print(f"Error: {e}")

# def delete_exercise(username, _id, exercise):
#     table_name = username + "_" + exercise

#     try:
#         conn = sqlite3.connect(DATABASE_FILE) 
#         cursor = conn.cursor()

#         cursor.execute(f"""
#             DELETE FROM '{table_name}' WHERE set_id = '{_id}'
#         """)

#         conn.commit()
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Error: {e}")