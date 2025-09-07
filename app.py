from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Inicializar DB
def init_db():
    conn = sqlite3.connect("portfolio.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre TEXT, email TEXT, mensaje TEXT, fecha TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    tecnologias = ["Python", "Flask", "SQLite", "Power Automate", "Docker", "GitHub"]
    return render_template("home.html", tecnologias=tecnologias)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]

        conn = sqlite3.connect("portfolio.db")
        c = conn.cursor()
        c.execute("INSERT INTO messages (nombre, email, mensaje, fecha) VALUES (?, ?, ?, ?)",
                  (nombre, email, mensaje, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
