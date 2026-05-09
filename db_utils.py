import sqlite3
from datetime import datetime

def check_reuse(password):
    # Connect to database (creates file if not exists)
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # Create a well-defined table with columns
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS used (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pwd TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # Check if password already exists
    cursor.execute("SELECT * FROM used WHERE pwd=?", (password,))
    reused = cursor.fetchone()

    if not reused:
        # Insert new password with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO used (pwd, created_at) VALUES (?, ?)", (password, timestamp))
        conn.commit()

        # Keep only the last 5 passwords
        cursor.execute("SELECT id FROM used ORDER BY created_at DESC")
        all_ids = [row[0] for row in cursor.fetchall()]

        if len(all_ids) > 5:
            # Delete oldest passwords beyond the 5 most recent
            ids_to_delete = all_ids[5:]
            cursor.executemany("DELETE FROM used WHERE id=?", [(i,) for i in ids_to_delete])
            conn.commit()

    conn.close()
    return reused is not None
