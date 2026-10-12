import sqlite3

def get_db():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS patients
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, disease TEXT, phone TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS doctors
                 (id INTEGER PRIMARY KEY, name TEXT, specialization TEXT, phone TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS appointments
                 (id INTEGER PRIMARY KEY, patient_name TEXT, doctor_name TEXT, date TEXT, time TEXT)''')
    conn.commit()
    conn.close()