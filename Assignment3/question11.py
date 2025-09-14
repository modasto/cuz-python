import requests
import sqlite3
import os

# --- Part 1: API and GET Requests with the 'requests' library ---

# What is an API?
# An API (Application Programming Interface) is a set of rules and protocols that
# allows different software applications to communicate with each other. It defines
# the methods and data formats that applications can use to request and exchange
# information. For web services, APIs often use HTTP to handle requests and
# responses, commonly in JSON or XML format.

def demonstrate_api_get_request():
    """
    Demonstrates how to make a GET request to a public API.
    A GET request is used to retrieve data from a specified resource (URL).
    """
    print("--- Demonstrating API GET Request ---")
    # 1. Define the URL of the API endpoint.
    # We'll use JSONPlaceholder, a free fake online REST API for testing.
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        # 2. Make the GET request using requests.get().
        # This sends an HTTP GET request to the specified URL.
        response = requests.get(url)

        # 3. Check the status code of the response.
        # A status code of 200 means the request was successful.
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

        # 4. Parse the JSON response.
        # The .json() method parses the JSON content from the response into a Python dictionary.
        data = response.json()

        print(f"Successfully fetched data from {url}")
        print(f"Post Title: {data.get('title')}")
        print(f"Post Body: {data.get('body')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
    print("-" * 35 + "\n")


# --- Part 2: Connecting to a SQLite Database ---

# How to connect to a SQLite database using Python:
# Python has a built-in library called `sqlite3` for working with SQLite databases.
# The process involves the following steps:

# 1. Import the `sqlite3` module:
#    `import sqlite3`
#    This gives you access to the necessary functions and objects.

# 2. Connect to the database:
#    `conn = sqlite3.connect('mydatabase.db')`
#    This function opens a connection to a SQLite database file. If the file
#    does not exist, it will be created in the current directory. It returns
#    a Connection object.

# 3. Create a Cursor object:
#    `cursor = conn.cursor()`
#    The Cursor object is used to execute SQL commands. It allows you to
#    interact with the database, row by row.

# 4. Execute SQL commands:
#    `cursor.execute('SQL QUERY')`
#    You can run any valid SQL query, such as CREATE TABLE, INSERT, SELECT,
#    UPDATE, or DELETE.

# 5. Commit the transaction (for data-modifying operations):
#    `conn.commit()`
#    This saves the changes (like INSERT, UPDATE, DELETE) to the database file.
#    If you don't call commit, the changes will be lost when the connection is closed.

# 6. Close the connection:
#    `conn.close()`
#    This closes the connection to the database, releasing the file lock. It's
#    crucial to close the connection to prevent data corruption and free up resources.
#    Using a `try...finally` block or a `with` statement is best practice to ensure
#    the connection is always closed.

def demonstrate_sqlite_connection():
    """
    Demonstrates creating, connecting to, and interacting with a SQLite database.
    """
    print("--- Demonstrating SQLite Database Connection ---")
    db_file = "university.db"
    conn = None  # Initialize conn to None

    try:
        # Step 2: Connect to the database (creates the file if it doesn't exist)
        conn = sqlite3.connect(db_file)
        print(f"Successfully connected to database '{db_file}'")

        # Step 3: Create a Cursor object
        cursor = conn.cursor()

        # Step 4: Execute SQL commands
        # Create a table (if it doesn't already exist)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                major TEXT NOT NULL
            )
        ''')
        print("Table 'students' created or already exists.")

        # Insert some data (using parameterized queries to prevent SQL injection)
        students_to_add = [
            (1, 'Alice', 'Computer Science'),
            (2, 'Bob', 'Physics')
        ]
        # Use executemany for multiple inserts, ignoring if primary key already exists
        cursor.executemany('INSERT OR IGNORE INTO students (id, name, major) VALUES (?, ?, ?)', students_to_add)
        print("Data inserted into 'students' table.")

        # Step 5: Commit the transaction to save the changes
        conn.commit()
        print("Transaction committed.")

        # Execute a SELECT query to retrieve data
        print("\nFetching data from 'students' table:")
        cursor.execute('SELECT * FROM students')

        # Fetch and print the results
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Name: {row[1]}, Major: {row[2]}")

    except sqlite3.Error as e:
        print(f"A database error occurred: {e}")

    finally:
        # Step 6: Close the connection if it was opened
        if conn:
            conn.close()
            print("\nDatabase connection closed.")
            # Optional: Clean up the created database file
            if os.path.exists(db_file):
                os.remove(db_file)
                print(f"Cleaned up and removed '{db_file}'.")
    print("-" * 35)


if __name__ == "__main__":
    demonstrate_api_get_request()
    demonstrate_sqlite_connection()