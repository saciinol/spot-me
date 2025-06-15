import sqlite3

DATABASE_FILE = "terminologies.db"

def initialize_terminologies():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS terminologies(
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                info TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")

def get_terminologies(term):
    try:
        conn = sqlite3.connect(DATABASE_FILE) 
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT name, info FROM terminologies 
            WHERE LOWER(name) LIKE LOWER(?) ORDER BY name
        """, ('%' + term + '%',))

        data = cursor.fetchall()
        conn.close()

        return data
    except sqlite3.Error as e:
        print(f"Error: {e}")

def get_all_terminologies():
    try:
        conn = sqlite3.connect(DATABASE_FILE) 
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT * FROM terminologies ORDER BY name
        """)

        data = cursor.fetchall()
        conn.close()

        return data
    except sqlite3.Error as e:
        print(f"Error: {e}")