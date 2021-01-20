from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
  connection = sqlite3.connect('webapp.db')
  connection.row_factory = sqlite3.Row

  cursor = connection.cursor()
  cursor.execute("SELECT Full_Name, Screen_Name, Identity FROM People2")

  rows = cursor.fetchall()
  return render_template('TASK4_3.html', rows = rows)

app.run(host='0.0.0.0', port=8080)