from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getPage')
def get_page():
    page_id = request.args.get('id', default=1, type=int)
    conn = sqlite3.connect('book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM pages WHERE id = ?", (page_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({"title": row[0], "content": row[1]})
    else:
        return jsonify({"title": "Not found", "content": "No content available."})

if __name__ == '__main__':
    app.run(debug=True)
