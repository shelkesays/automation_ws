import mysql.connector
from mysql.connector import Error


def connect_to_db(host, port, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT,
        department VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    print("Table 'employees' created (if not exists).")

def insert_data(cursor, values):
    insert_query = """
    INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, values)
    print(f"Inserted: {cursor.rowcount} row(s).")

def update_data(cursor, values):
    update_query = """
    UPDATE employees SET age = %s WHERE name = %s
    """
    cursor.execute(update_query, values)
    print(f"Updated: {cursor.rowcount} row(s).")

def delete_data(cursor, value):
    delete_query = """
    DELETE FROM employees WHERE name = %s
    """
    cursor.execute(delete_query, value)
    print(f"Deleted: {cursor.rowcount} row(s).")

def read_data(cursor):
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("Data in 'employees' table:")
    for row in rows:
        print(row)

# Main program
if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "your_username",
        "password": "your_password",
        "database": "your_database"
    }
    
    connection = connect_to_db(**db_config)
    if connection:
        cursor = connection.cursor()

        try:
            # Create table
            create_table(cursor)

            # Insert data
            values = ("Alice", 30, "HR")
            insert_data(cursor, values)

            # Update data
            values = (32, "Alice")
            update_data(cursor)

            # Read data
            read_data(cursor)

            # Delete data
            value = ("Alice",)
            delete_data(cursor)

            # Commit changes
            connection.commit()

        except Error as e:
            print(f"Error: {e}")
            connection.rollback()

        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
