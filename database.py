import sqlite3

def init_db():
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        name TEXT,
        country TEXT,
        device TEXT,
        purpose TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_request(data):
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO requests(user_id, username, name, country, device, purpose, status)
    VALUES(?,?,?,?,?,?,?)
    """, data)
    req_id = cur.lastrowid
    conn.commit()
    conn.close()
    return req_id

def set_status(req_id, status):
    conn = sqlite3.connect("vpn.db")
    cur = conn.cursor()
    cur.execute("UPDATE requests SET status=? WHERE id=?", (status, req_id))
    conn.commit()
    conn.close()
