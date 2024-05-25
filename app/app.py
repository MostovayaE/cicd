import os
from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'kubsu'),
        user=os.getenv('DB_USER', 'kubsu'),
        password=os.getenv('DB_PASSWORD', 'kubsu'),
        port=os.getenv('DB_PORT', 5432))
    return conn


@app.route('/')
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
