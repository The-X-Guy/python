# Fran Gálvez. 2º ASIR. 08/01/2020

import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root", 
    passwd = "", 
    database = "personal"
)

mycursor = mydb.cursor()
mycursor.execute("select * from hombres where apellidos = 'Peroto' or apellidos like 'Pa%'")
myresult = mycursor.fetchall()
print(mycursor.rowcount, " registros extraidos.")

hombres = open('apellidos.txt', 'w')
i = 0
for row in myresult:
    hombres.write(str(row[4] - (row[4]*0.18)))
    hombres.write("\n")
    i += 1
print(i, " registros guardados en apellidos.txt")