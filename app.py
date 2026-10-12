from flask import Flask, render_template, request, redirect
from database import init_db, get_db
from modules.patients import get_all_patients, add_patient_db
from modules.doctors import get_all_doctors, add_doctor_db
from modules.appointments import get_all_appointments, add_appointment_db

app = Flask(__name__)
init_db()

@app.route('/')
def dashboard():
    conn = get_db()
    p_count = conn.execute("SELECT COUNT(*) FROM patients").fetchone()[0]
    d_count = conn.execute("SELECT COUNT(*) FROM doctors").fetchone()[0]
    a_count = conn.execute("SELECT COUNT(*) FROM appointments").fetchone()[0]
    conn.close()
    return render_template('dashboard.html', p_count=p_count, d_count=d_count, a_count=a_count)

@app.route('/patients', methods=['GET','POST'])
def patients():
    if request.method == 'POST':
        add_patient_db(request.form['name'], request.form['age'], request.form['gender'], request.form['disease'], request.form['phone'])
        return redirect('/patients')
    return render_template('patients.html', patients=get_all_patients())

@app.route('/doctors', methods=['GET','POST'])
def doctors():
    if request.method == 'POST':
        add_doctor_db(request.form['name'], request.form['spec'], request.form['phone'])
        return redirect('/doctors')
    return render_template('doctors.html', doctors=get_all_doctors())

@app.route('/appointments', methods=['GET','POST'])
def appointments():
    if request.method == 'POST':
        add_appointment_db(request.form['patient'], request.form['doctor'], request.form['date'], request.form['time'])
        return redirect('/appointments')
    return render_template('appointments.html', appointments=get_all_appointments(), patients=get_all_patients(), doctors=get_all_doctors())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)