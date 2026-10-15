from flask import Flask, request
from markupsafe import escape
import sqlite3
import subprocess
import ipaddress

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Coding Review Lab"

@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    result = conn.execute(query, (username, password)).fetchone()
    conn.close()

    if result:
        return "Login successful"
    return "Invalid login"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {escape(name)}!</h1>"

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    try:
        ipaddress.ip_address(host)
    except ValueError:
        return "Invalid IP address", 400

    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "Ping timed out."

    return f"<pre>{escape(output)}</pre>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
