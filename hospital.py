# Спроектувати базу даних для лікарні,
# що буде містити дані про працівників, пацієнтів, їхні візити та записи до лікарів, дані про виписані рецепти.

import sqlite3

def create_tables(cr):
    cr.execute('''
    CREATE TABLE IF NOT EXISTS doctor (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        phone_number VARCHAR(64),
        email VARCHAR(255),
        medical_field VARCHAR(255),
        work_experience VARCHAR(64),
        appointment_price VARCHAR(64)
    )
    ''')
    cr.execute('''
    CREATE TABLE IF NOT EXISTS patient (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        phone_number INTEGER,
        email VARCHAR(255)
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS hospital (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        adress VARCHAR(255),
        type VARCHAR(64)
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS prescription (
        id INTEGER PRIMARY KEY NOT NULL,
        discharge date DATE,
        drug_name VARCHAR(255),
        dosage VARCHAR(255),
        reciption_method VARCHAR(255),
        admission_duration VARCHAR(64),
        number_of_packages NUMERIC
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS appointment (
        id INTEGER PRIMARY KEY NOT NULL,
        time VARCHAR(64),
        health_complaints VARCHAR(255)
    )
    ''')


def fill_test_data(cr):
    cr.execute('''
    INSERT INTO patient VALUES
    (1, 'Alex', '0987654321', 'alex.kiyv2004@gmail.com'),
    (2, 'Mike', '0987436253', 'mike.work1989@gmail.com'),
    (3, 'Ted', '0968574382', 'pro.gamer228777@gmail.com'),
    (4, 'Sancho', '0912834853', 'sancho.ss1999@gmail.com')
    ''')

    cr.execute('''
    INSERT INTO doctor VALUES
    (1, 'Mark', '0983694326', 'mark.work@gmail.com', 'Dermatology', '4 years', 'free'),
    (2, 'Jeff', '0983228326', 'jeff.work@gmail.com', 'Pediatrics', '2 years', 'free'),
    (3, 'Steve', '0984694777', 'steve.work@gmail.com', 'Neurologist', '3 years', 'free')
    ''')

    cr.execute('''
    INSERT INTO hospital VALUES
    (1, 'emergency hospital', '9, Ivan Mykolaychuk str., Lviv, Lviv region', 'public hospital')
    ''')

    cr.execute('''
    INSERT INTO prescription VALUES
    (1, '20/07/2023', '?', '?', '?', '6 mounths', 7),
    (2, '17/07/2023', '?', '?', '?', '1 mounths', 3),
    (3, '25/07/2023', '?', '?', '?', '3 mounths', 5.5)
    ''')

    cr.execute('''
    INSERT INTO appointment VALUES
    (1, '20/07/2023', 'problems with the skin'),
    (2, '17/07/2023', 'pain in the ear'),
    (3, '25/07/2023', 'severe headache')
    ''')

with sqlite3.connect("hospital.db") as db:
    cr = db.cursor()
    create_tables(cr)
    cr.execute('SELECT id FROM patient LIMIT 1')
    if not cr.fetchone():
        fill_test_data(cr)

    cr.execute('SELECT * FROM patient')
    result = cr.fetchall()
    print('\nAll patients: \n')
    for row in result:
        print(row)

    cr.execute('SELECT * FROM doctor')
    result = cr.fetchall()
    print('\nAll doctors: \n')
    for row in result:
        print(row)

    cr.execute('SELECT * FROM hospital')
    result = cr.fetchall()
    print('\nHospital: \n')
    for row in result:
        print(row)

    cr.execute('SELECT * FROM prescription')
    result = cr.fetchall()
    print('\nAll prescriptions: \n')
    for row in result:
        print(row)

    cr.execute('SELECT * FROM appointment')
    result = cr.fetchall()
    print('\nAll appointments: \n')
    for row in result:
        print(row)
