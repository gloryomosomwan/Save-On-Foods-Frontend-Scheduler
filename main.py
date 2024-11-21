import sqlite3
#import os

def read_employee_records():
    document = []
    file = open('employee_data.csv', 'r')
    # print(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            temp = line.split(',', 5)
            temp2 = tuple(temp)

            teammember_ID = temp[0]
            name = temp2[1]
            hourly_wage = temp[2]
            opening_closing = temp[3]
            fulltime_partime = temp[4]
            hire_date = temp2[5]

            cleaned_line = (int(teammember_ID), name, float(hourly_wage), int(opening_closing), int(fulltime_partime), int(hire_date[7:]))
            document.append(cleaned_line)
        
        i += 1
    return document

def select(cursor):
    res = cursor.execute('SELECT * FROM employees WHERE hourly_wage = 22.22')
    print(res.fetchall())

def create_table(cursor):
    cursor.execute('CREATE TABLE employees (teammember_ID integer PRIMARY KEY NOT NULL, name text, hourly_wage real, opening_closing integer, fulltime_parttime integer, hire_date integer)')

def initialize(cursor, document):
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)', document) 

def delete_record(cursor, unique_ID):
    cursor.execute("""DELETE from employees where teammember_ID = ?""", unique_ID)

def insert_record(cursor):
    cursor.execute('INSERT INTO employees VALUES (NULL, "do", 22.22, 0, 0, 20200304)')

def main():
    # Schema: (514926, "John Doe", 16.50, 0, 0, "20200228"), date schema: yyyymmdd
    conn = sqlite3.connect('toy.db')
    cursor = conn.cursor()

    create_table(cursor)
    document = read_employee_records()
    initialize(cursor, document)

    # insert_record(cursor)
    # select(cursor)
    
    conn.commit()
    conn.close()

try:
    main()
except Exception as e:
    print(e, "Check file for missing or incorrect entries!")
