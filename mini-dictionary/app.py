from flask import Flask, render_template, request, redirect
import os
import psycopg2

app = Flask(__name__)

# Database connection details
DB_URL = os.getenv("DATABASE_URL")  # Render-managed Postgres
DB_NAME = "bookdb"
DB_USER = "postgres"
DB_PASSWORD = "255202"   # <-- replace with your postgres password
DB_HOST = "localhost"
DB_PORT = "5432"

def get_conn():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('content', '').strip()

        # Block empty input and the word "and" (case-insensitive)
        if text and text.lower() != 'and':
            with get_conn() as conn:
                with conn.cursor() as cur:
                    # Case-insensitive duplicate check
                    cur.execute("SELECT 1 FROM texts WHERE LOWER(content) = LOWER(%s);", (text,))
                    exists = cur.fetchone()

                    if not exists:
                        cur.execute("INSERT INTO texts (content) VALUES (%s);", (text,))
                        conn.commit()

        return redirect('/')

    # GET: fetch all texts sorted ascending, excluding "and"
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT content FROM texts
                WHERE LOWER(content) != 'and'
                ORDER BY LOWER(content) ASC;
            """)
            rows = cur.fetchall()

    entries = [r[0] for r in rows]
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
