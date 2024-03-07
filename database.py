import sqlite3

# Connect to the database
conn = sqlite3.connect('training.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS courses
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS modules
             (id INTEGER PRIMARY KEY AUTOINCREMENT, course_id INTEGER, name TEXT, description TEXT, FOREIGN KEY(course_id) REFERENCES courses(id))''')

c.execute('''CREATE TABLE IF NOT EXISTS lessons
             (id INTEGER PRIMARY KEY AUTOINCREMENT, module_id INTEGER, name TEXT, content TEXT, FOREIGN KEY(module_id) REFERENCES modules(id))''')

# Add courses
c.execute("INSERT INTO courses (name, description) VALUES (?, ?)", ('Software Development', 'Learn various programming languages and techniques for software development.'))
c.execute("INSERT INTO courses (name, description) VALUES (?, ?)", ('Networking', 'Understand computer networking concepts, protocols, and configurations.'))
c.execute("INSERT INTO courses (name, description) VALUES (?, ?)", ('Cybersecurity', 'Explore ethical hacking, security protocols, and threat mitigation strategies.'))

# Add modules and lessons for Software Development
software_dev_id = c.lastrowid
c.execute("INSERT INTO modules (course_id, name, description) VALUES (?, ?, ?)", (software_dev_id, 'Python', 'Learn Python programming language.'))
python_module_id = c.lastrowid
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (python_module_id, 'Introduction to Python', 'Introduction to Python programming...'))
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (python_module_id, 'Data Structures and Algorithms', 'Python data structures and algorithms...'))

# Add modules and lessons for Networking
networking_id = c.lastrowid
c.execute("INSERT INTO modules (course_id, name, description) VALUES (?, ?, ?)", (networking_id, 'Routing and Switching', 'Configure routers and switches.'))
routing_module_id = c.lastrowid
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (routing_module_id, 'Configuring Cisco Routers', 'Cisco router configuration commands...'))
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (routing_module_id, 'Configuring Cisco Switches', 'Cisco switch configuration commands...'))

# Add modules and lessons for Cybersecurity
cybersecurity_id = c.lastrowid
c.execute("INSERT INTO modules (course_id, name, description) VALUES (?, ?, ?)", (cybersecurity_id, 'Ethical Hacking', 'Learn ethical hacking techniques.'))
ethical_hacking_module_id = c.lastrowid
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (ethical_hacking_module_id, 'Introduction to Ethical Hacking', 'Ethical hacking concepts and methodologies...'))
c.execute("INSERT INTO lessons (module_id, name, content) VALUES (?, ?, ?)", (ethical_hacking_module_id, 'Vulnerability Assessment', 'Techniques for vulnerability assessment...'))

# Commit and close the connection
conn.commit()
conn.close()