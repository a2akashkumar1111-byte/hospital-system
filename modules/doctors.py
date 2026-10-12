from database import get_db

def get_all_doctors():
    conn = get_db()
    data = conn.execute("SELECT * FROM doctors").fetchall()
    conn.close()
    return data

def add_doctor_db(name, specialization, phone):
    conn = get_db()
    conn.execute("INSERT INTO doctors (name, specialization, phone) VALUES (?,?,?)", (name, specialization, phone))
    conn.commit()
    conn.close()