from flask import Flask, jsonify, send_from_directory
import psycopg2
import os

app = Flask(__name__, static_folder='public')

# Database connection helper function
def get_db_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="Glamix1!",
        host="localhost",
        port="5432",
        database="postgres"
    )
    return connection

# Serve your main website homepage from the 'public' folder
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# API endpoint to get your database records
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