from flask import Flask, render_template, request, redirect
import os
import psycopg2

app = Flask(__name__)

# Render will inject DATABASE_URL into environment variables
DB_URL = os.getenv("DATABASE_URL")

def get_conn():
    if DB_URL:
        # Use Render's managed PostgreSQL (requires SSL)
        return psycopg2.connect(DB_URL, sslmode="require")
    # Fallback for local development
    return psycopg2.connect(
        dbname="bookdb",
        user="postgres",
        password="255202",  # <-- replace with your local postgres password
        host="localhost",
        port="5432"
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
