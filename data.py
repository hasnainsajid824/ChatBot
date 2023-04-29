import mysql.connector

conn = mysql.connector.connect(user="root", password="", host="localhost", database="ubot")
cursor = conn.cursor()

def get_data(name, depart, satisfaction):
        cursor.execute("INSERT INTO feedback (Name, Department, Satisfied) VALUES (%s, %s, %s)",(name,depart, satisfaction))
        conn.commit()

cursor.execute("SELECT * FROM `feedback`")
data_list = cursor.fetchall()
header = ['ID', 'Name', "Department", "Satisfaction"]
data_list = [list(d) for d in data_list]
 