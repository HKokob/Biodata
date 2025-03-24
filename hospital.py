from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database setup
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123kokob123',  # Change this to your actual MySQL password
    'database': 'PGR_207528_177'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Patients page
@app.route('/patients')
def patients():
    return render_template('patients.html')

# Doctors page
@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

# Submit patient data
@app.route('/submit_patient', methods=['POST'])
def submit_patient():
    patient_id = request.form['patient_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    contact_info = request.form['contact_info']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO patients (patient_id, first_name, last_name, date_of_birth, gender, contact_info) VALUES (%s, %s, %s, %s, %s, %s)', 
                   (patient_id, first_name, last_name, date_of_birth, gender, contact_info))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('patients'))

# Submit doctor data
@app.route('/submit_doctors', methods=['POST'])
def submit_doctor():
    doctor_id = request.form['doctor_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    specialty = request.form['specialty']
    contact_info = request.form['contact_info']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO doctors (doctor_id, first_name, last_name, specialty, contact_info) VALUES (%s, %s, %s, %s, %s)', 
                   (doctor_id, first_name, last_name, specialty, contact_info))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('doctors'))


@app.route('/submit_bioinformatics', methods=['POST'])
def submit_bioinformatics():
    record_id = request.form['record_id']
    patient_id = request.form['patient_id']
    gene_sequence = request.form['gene_sequence']
    analysis = request.form['analysis']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bioinformatics(record_id, patient_id, gene_sequence, analysis) VALUES (%s, %s, %s, %s)', 
                   (record_id, patient_id, gene_sequence, analysis))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('bioinformatics'))


@app.route('/bioinformatics')
def bioinformatics():
    return render_template('bioinformatics.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

