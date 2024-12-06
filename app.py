from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="cs157aproject.c1eumiik0lu4.us-west-1.rds.amazonaws.com",
            user="admin",
            password="Ta1RZxd7etSKZP25K9gq",
            database="Inventory_Management_System"
        )
        return connection
    except Error as e:
        print(f"Could not connect: {e}")
        return None


@app.route('/run_query', methods=['POST'])
def run_query():
    query = request.json.get('query', '')  
    connection = create_connection()

    if not connection:
        return jsonify({"success": False, "error": "Failed to connect to the database."})

    cursor = connection.cursor(dictionary=True)  
    try:
        cursor.execute(query)

        # Fetch all rows for queries like SHOW TABLES
        if query.strip().lower().startswith(('select', 'show', 'describe')):
            results = cursor.fetchall()
            return jsonify({"success": True, "results": results})
        else:
            connection.commit()  
            return jsonify({"success": True, "message": "Query executed successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})  
    finally:
        try:
            # Always fetch all results to prevent unread results error
            if cursor and not cursor.closed:
                cursor.fetchall()
        except Exception:
            pass
        cursor.close()
        connection.close()  # Always close the database connection

if __name__ == '__main__':
    app.run(debug=True, port=5000)

