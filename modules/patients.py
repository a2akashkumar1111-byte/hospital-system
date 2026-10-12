from database import get_db

def get_all_patients():
    conn = get_db()
    data = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return data

def add_patient_db(name, age, gender, disease, phone):
    conn = get_db()
    conn.execute("INSERT INTO patients (name, age, gender, disease, phone) VALUES (?,?,?,?,?)", (name, age, gender, disease, phone))
    conn.commit()
    conn.close()