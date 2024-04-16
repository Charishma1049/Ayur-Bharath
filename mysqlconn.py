import mysql.connector
from datetime import datetime

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="host",
    user="admin",
    password="admin",
    database="DraftData"
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Insert sensor data into a table
def insert_sensor_data(sensor_value):
    try:
        # Get the current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # SQL query to insert data into the 'sensor_data' table
        sql_query = "INSERT INTO sensor_data (timestamp, value) VALUES (%s, %s)"
        data_to_insert = (current_time, sensor_value)

        # Execute the query
        cursor.execute(sql_query, data_to_insert)

        # Commit changes to the database
        db_connection.commit()

        print("Sensor data inserted successfully.")
    except Exception as e:
        print(f"Error inserting sensor data: {e}")
        # Rollback changes in case of an error
        db_connection.rollback()

# Example usage: Insert sensor data with a value of 25
insert_sensor_data(25)

# Close the cursor and database connection
cursor.close()
db_connection.close()
