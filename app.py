from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "database.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS journal 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         date TEXT UNIQUE, 
                         title TEXT, 
                         content TEXT)''')
    print("Database initialized.")

@app.route('/')
def home():
    return render_template('inder.html')

@app.route('/api/entries', methods=['GET'])
def get_entries():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, title, content FROM journal")
        data = [{"start": row[0], "title": row[1], "extendedProps": {"content": row[2]}} for row in cursor.fetchall()]
    return jsonify(data)

@app.route('/api/save', methods=['POST'])
def save_entry():
    data = request.json
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO journal (date, title, content) VALUES (?, ?, ?)
                            ON CONFLICT(date) DO UPDATE SET title=excluded.title, content=excluded.content''',
                         (data['date'], data['title'], data['content']))
            conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)