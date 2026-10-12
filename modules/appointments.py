from database import get_db

def get_all_appointments():
    conn = get_db()
    data = conn.execute("SELECT * FROM appointments").fetchall()
    conn.close()
    return data

def add_appointment_db(p_name, d_name, date, time):
    conn = get_db()
    conn.execute("INSERT INTO appointments (patient_name, doctor_name, date, time) VALUES (?,?,?,?)", (p_name, d_name, date, time))
    conn.commit()
    conn.close()