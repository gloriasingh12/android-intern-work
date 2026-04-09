# =================================================================
# PROJECT: Expense Tracker Tool
# DESCRIPTION: Tracks expenses, categorizes them, and saves to SQLite.
# DELIVERABLE: A Python script with Data Persistence (SQLite).
# =================================================================

import sqlite3

def setup_database():
    """Creates a local SQLite database and an expense table."""
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            amount REAL,
            category TEXT
        )
    ''')
    conn.commit()
    return conn

def add_expense(conn, item, amount, category):
    """Saves an expense entry to the database."""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (item, amount, category) VALUES (?, ?, ?)', 
                   (item, amount, category))
    conn.commit()
    print(f"✅ Added: {item} | ₹{amount} | Category: {category}")

def show_summary(conn):
    """Fetches data and displays a summary of expenses."""
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    rows = cursor.fetchall()
    
    print("\n--- EXPENSE SUMMARY (By Category) ---")
    if not rows:
        print("No data found.")
    for row in rows:
        # Drawing a simple text-based chart/bar for visualization
        bar = "█" * int(row[1] // 100) 
        print(f"{row[0]:<12}: ₹{row[1]:<6} {bar}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Initialize Database
    connection = setup_database()

    print("TASK: EXPENSE TRACKER SYSTEM")
    print("-" * 35)

    # 2. Adding Sample Data
    add_expense(connection, "Office Lunch", 250, "Food")
    add_expense(connection, "Petrol", 500, "Travel")
    add_expense(connection, "Keyboard", 1200, "Gadgets")
    add_expense(connection, "Coffee", 150, "Food")
    add_expense(connection, "Uber Ride", 300, "Travel")

    # 3. Displaying Summary (Simulating Charts)
    show_summary(connection)

    # Close connection
    connection.close()
    print("-" * 35)
    print("NOTE: Data is saved in 'expenses.db'. Run again to see persistent data!")
