import psycopg2

try:
    # Connect to your local database
    connection = psycopg2.connect(
        user="postgres",
        password="Glamix1!", # Replace with your real password
        host="localhost",
        port="5432",
        database="postgres"
    )
    
    cursor = connection.cursor()
    
    # Insert a new record
    name_to_insert = "Godfred - Python Test"
    insert_query = "INSERT INTO sample_data (name) VALUES (%s);"
    cursor.execute(insert_query, (name_to_insert,))
    
    # Commit the transaction to save changes
    connection.commit()
    
    print("SUCCESS! Record inserted into PostgreSQL.")
    
    cursor.close()
    connection.close()

except Exception as error:
    print("INSERT FAILED:", error)