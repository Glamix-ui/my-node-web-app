from flask import Flask, jsonify, send_from_directory
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__, static_folder='public')

# Database connection helper function using secure environment variables
def get_db_connection():
    connection = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )
    return connection

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/data')
def get_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, name, created_at FROM sample_data;")
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        results = []
        for row in rows:
            results.append({
                "id": row[0],
                "name": row[1],
                "created_at": str(row[2])
            })
            
        return jsonify(results)
        
    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)