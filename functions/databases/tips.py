import sqlite3

DATABASE_FILE = "tips.db"

def initialize_tips():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tips(
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                info TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")

def get_tips(tip):
    try:
        conn = sqlite3.connect(DATABASE_FILE) 
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT name, info FROM tips 
            WHERE LOWER(name) LIKE LOWER(?) ORDER BY name
        """, ('%' + tip + '%',))

        data = cursor.fetchall()
        conn.close()

        return data
    except sqlite3.Error as e:
        print(f"Error: {e}")

def get_all_tips():
    try:
        conn = sqlite3.connect(DATABASE_FILE) 
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT * FROM tips ORDER BY name
        """)

        data = cursor.fetchall()
        conn.close()

        return data
    except sqlite3.Error as e:
        print(f"Error: {e}")