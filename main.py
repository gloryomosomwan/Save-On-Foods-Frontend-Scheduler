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

def read_availability_records():
    document = []
    file = open('availability.csv', 'r')
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            temp = line.split(',', 3)
            temp2 = tuple(temp)

            teammember_ID = temp2[0]
            day_of_the_week = temp2[1]
            start_time = temp2[2]
            end_time = temp2[3]

            cleaned_line = (int(teammember_ID), day_of_the_week, int(start_time), int(end_time))
            document.append(cleaned_line)
        i += 1
    return document

def select(cursor, name_of_table, constraints):
    statement = "SELECT * FROM {tablename} WHERE {condition}".format(tablename = name_of_table, condition=constraints)
    res = cursor.execute(statement)
    print(res.fetchall())

def create_table(cursor):
    cursor.execute('CREATE TABLE employees (teammember_ID integer PRIMARY KEY NOT NULL, name text, hourly_wage real, opening_closing integer, fulltime_parttime integer, hire_date integer)')

def create_availability_table(cursor):
    cursor.execute('CREATE TABLE availability (teammember_ID integer, day_of_week text, start_time integer, end_time integer)')

def initialize(cursor, document):
    cursor.executemany('INSERT INTO availability VALUES (?, ?, ?, ?)', document) 

def delete_record(cursor, unique_ID):
    cursor.execute("""DELETE from employees where teammember_ID = ?""", unique_ID)

def insert_record(cursor):
    cursor.execute('INSERT INTO employees VALUES (NULL, "do", 22.22, 0, 0, 20200304)')

def drop_table(cursor, name_of_table):
    statement = "DROP TABLE {tablename}".format(tablename = name_of_table)
    cursor.execute(statement)

def main():
    # Schema: (514926, "John Doe", 16.50, 0, 0, "20200228"), date schema: yyyymmdd
    conn = sqlite3.connect('sof.db')
    cursor = conn.cursor()

    # document = read_availability_records()
    # create_availability_table(cursor)
    # initialize(cursor, document)
    select(cursor, 'availability', 'teammember_ID = 387901')
    
    conn.commit()
    conn.close()

main()
''''
try:
    
except Exception as e:
    print(e, "Check file for missing or incorrect entries!")
'''