import sqlite3

def check_reuse(password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS used (pwd TEXT)")
    cursor.execute("SELECT * FROM used WHERE pwd=?", (password,))
    reused = cursor.fetchone()
    if not reused:
        cursor.execute("INSERT INTO used VALUES (?)", (password,))
        conn.commit()
    conn.close()
    return reused is not None
