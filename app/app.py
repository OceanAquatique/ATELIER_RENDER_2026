from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Flask + Docker + GHCR + Terraform + Render"


@app.route("/health")
def health():
    return {"status": "Tout est ok ou pas"}


@app.route("/info")
def info():
    return {
        "app": "Flask Render",
        "student": "Oceane",
        "version": "v1"
    }


@app.route("/env")
def env():
    return {"env": os.getenv("ENV")}


def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("La variable DATABASE_URL est absente")
    return psycopg.connect(database_url)


@app.route("/api/students")
def get_students():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, role FROM students ORDER BY id")
                rows = cur.fetchall()

        students = []
        for row in rows:
            students.append({
                "id": row[0],
                "name": row[1],
                "role": row[2]
            })

        return jsonify(students)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
