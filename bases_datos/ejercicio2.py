# Fran Gálvez. 2º ASIR. 08/01/2020

import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root", 
    passwd = "", 
    database = "personal"
)

mycursor = mydb.cursor()
mycursor.execute("select * from mujeres where sueldo < 600")
myresult = mycursor.fetchall()
print(mycursor.rowcount, " registros extraidos.")
for x in myresult:
    print(x)

mycursor.execute("update mujeres set sueldo = sueldo + (sueldo*0.23) where sueldo < 600")
mycursor.execute("select * from mujeres")
myresult = mycursor.fetchall()

print("\n", mycursor.rowcount, " registros extraidos.")
for x in myresult:
    print(x)