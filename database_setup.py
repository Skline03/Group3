import sqlite3

# Imports the sqlite3 library to interact with an SQLite database.

def setup_database():
    """
    Sets up the database for the phishing simulation. Creates a `click_log` table if it does not already exist.

    The `click_log` table records:
    - A unique identifier for each log entry.
    - The `user_id` of the individual who interacted with the phishing link.
    - A timestamp indicating when the interaction occurred.
    """
    conn = sqlite3.connect('phishing_simulation.db')
    # Establishes a connection to the SQLite database named 'phishing_simulation.db'.
    # If the database file does not exist, it is created.

    c = conn.cursor()
    # Creates a cursor object for executing SQL commands.

    c.execute('''
        CREATE TABLE IF NOT EXISTS click_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Executes a SQL command to create the `click_log` table if it does not already exist.
    # - `id`: An auto-incrementing primary key for each record.
    # - `user_id`: Stores the identifier (e.g., email) of the user who clicked the phishing link.
    # - `timestamp`: Records the time of the interaction. Defaults to the current timestamp.

    conn.commit()
    # Saves (commits) the changes made to the database.

    conn.close()
    # Closes the database connection.

# Run the setup
if __name__ == "__main__":
    """
    Ensures the `setup_database` function is executed only when the script is run directly.
    This prevents the function from being executed if the script is imported as a module.
    """
    setup_database()
    # Calls the `setup_database` function to set up the database and create the required table.
