from flask import Flask, jsonify, request
import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

app = Flask(__name__)


@app.route('/api/data', methods=['GET'])
def get_data():

    # Example query: Fetching data from a table named 'users'
    CURSOR.execute("SELECT * FROM users")
    rows = CURSOR.fetchall()
    CONN.close()

    # Convert the result to a list of dictionaries
    users = [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]
    
    return jsonify(users)

@app.route('/api/data', methods=['POST'])
def add_data():

    new_user = request.json
    CURSOR.execute("INSERT INTO users (name, email) VALUES (?, ?)", (new_user['name'], new_user['email']))
    CONN.commit()
    CONN.close()

    return jsonify({"message": "User added successfully!"}), 201

