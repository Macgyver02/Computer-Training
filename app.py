from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import database  # Import the database module

app = Flask(__name__)
app.static_folder = 'static'

# Database setup
conn = sqlite3.connect('training.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    return render_template('courses.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_details(course_id):
    c.execute("SELECT * FROM courses WHERE id=?", (course_id,))
    course = c.fetchone()
    c.execute("SELECT * FROM modules WHERE course_id=?", (course_id,))
    modules = c.fetchall()
    return render_template('course_details.html', course=course, modules=modules)

@app.route('/module/<int:module_id>')
def module_details(module_id):
    c.execute("SELECT * FROM modules WHERE id=?", (module_id,))
    module = c.fetchone()
    c.execute("SELECT * FROM lessons WHERE module_id=?", (module_id,))
    lessons = c.fetchall()
    return render_template('module_details.html', module=module, lessons=lessons)

# Other routes (login, register, dashboard) remain the same

if __name__ == '__main__':
    app.run(debug=True)