import sqlite3

from flask import Flask, request

# Creates a Flask application instance. This instance is the central object for routing and handling requests.
app = Flask(__name__)

def log_click(user_id):
    """
    Logs a click event into a SQLite database by storing the `user_id`.

    Args:
        user_id (str): The ID of the user who clicked the phishing simulation link.
    """
    conn = sqlite3.connect('phishing_simulation.db')
    # Establishes a connection to the SQLite database named 'phishing_simulation.db'.
    c = conn.cursor()
    # Creates a cursor object, which is used to execute SQL commands.

    c.execute("INSERT INTO click_log (user_id) VALUES (?)", (user_id,))
    # Inserts the `user_id` into the `click_log` table in the database.
    # The `?` is a placeholder to prevent SQL injection by safely binding the parameter.

    conn.commit()
    # Saves (commits) the changes made to the database.
    conn.close()
    # Closes the database connection.

@app.route('/phishing')
# Defines a route in the Flask application for the URL path `/phishing`.
def phishing():
    """
    Handles GET requests to the `/phishing` endpoint. Logs user clicks and displays a phishing simulation message.
    
    Returns:
        str: HTML response indicating this is a phishing simulation and providing educational content.
    """
    user_id = request.args.get('id')
    # Retrieves the `id` parameter from the query string of the HTTP GET request.
    if user_id:
        log_click(user_id)
        # If an `id` parameter is present, calls `log_click` to log the event into the database.

    return """
    <h1>Phishing Simulation</h1>
    <p>This was a simulated phishing attempt. Please review cybersecurity guidelines to help identify phishing emails.</p>
    """
    # Returns an HTML string as the HTTP response. This is the message displayed to the user.

if __name__ == "__main__":
    """
    Ensures the application runs only when this script is executed directly, not when imported as a module.
    """
    app.run(debug=True, host="0.0.0.0", port=80)
    # Starts the Flask application with debugging enabled, listens on all network interfaces (0.0.0.0), and uses port 80.
    # Use 0.0.0.0 to allow external access.
