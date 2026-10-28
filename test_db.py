import psycopg2

try:
    # Connect to your local PostgreSQL database
    connection = psycopg2.connect(
        user="postgres",
        password="Glamix1!",
        host="localhost",
        port="5432",
        database="postgres"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    db_time = cursor.fetchone()
    
    print("SUCCESS! Connected to PostgreSQL.")
    print("Database live time:", db_time[0])
    
    cursor.close()
    connection.close()

except Exception as error:
    print("CONNECTION FAILED:", error)