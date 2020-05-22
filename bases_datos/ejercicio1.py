# Fran Gálvez. 2º ASIR. 08/01/2020

import csv # Importo la librería csv para trabajar con este tipo de ficheros.
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root", 
    passwd = ""
)

mycursor = mydb.cursor()
mycursor.execute("create database if not exists personal")
mycursor.execute("use personal")
mycursor.execute("drop table if exists hombres, mujeres")
mycursor.execute("create table hombres (dni int(9) primary key, nombre char(20), apellidos char(20), edad int(3), sueldo int(5))")
mycursor.execute("create table mujeres (dni int(9) primary key, nombre char(20), apellidos char(20), edad int(3), sueldo int(5))")

# Abro tres ficheros: personal.csv(r), mujeres.csv(w), hombres.csv(w)
with open('personal.csv') as personal, open('hombres.csv', mode = 'w', newline = '') as hombres, open('mujeres.csv', mode = 'w', newline = '') as mujeres:
    personal_leer = csv.reader(personal, delimiter = ';') # personal.csv: lectura
    hombres_escribir = csv.writer(hombres, delimiter = ';') # mujeres.csv: escritura
    mujeres_escribir = csv.writer(mujeres, delimiter = ';') # hombres.csv: escritura

    # mujeres_escribir.writerow(['DNI', 'nombre', 'apellidos', 'edad', 'sueldo']) # Escribo cabecera mujeres.csv
    # hombres_escribir.writerow(['DNI', 'nombre', 'apellidos', 'edad', 'sueldo']) # Escribo cabecera hombres.csv
    
    #################################################################################
    # Estructura del fichero personal.csv                                           #
    # DNI -> row[0]                                                                 #
    # nombre -> row[1]                                                              #
    # apellidos -> row[2]                                                           #
    # edad -> row[3]                                                                #
    # sexo -> row[4]                                                                #
    # sueldo -> row[5]                                                              #
    #################################################################################

    for row_personal in personal_leer:
        if row_personal[4] == "F": # Verifico el sexo de la persona e inserto en fichero correspondiente.
            mujeres_escribir.writerow((row_personal[0], row_personal[1], row_personal[2], row_personal[3], row_personal[5]))
        else:
            hombres_escribir.writerow((row_personal[0], row_personal[1], row_personal[2], row_personal[3], row_personal[5]))

with open('hombres.csv') as hombres:
    hombres_leer = csv.reader(hombres, delimiter = ';')
    for row_hombres in hombres_leer:
        if row_hombres:
            sql = "insert into hombres(dni, nombre, apellidos, edad, sueldo) values (%s, %s, %s, %s, %s)"
            values = [(row_hombres[0]), (row_hombres[1]), (row_hombres[2]), (row_hombres[3]), (row_hombres[4])]
            mycursor.execute(sql, values)
            mydb.commit()

with open('mujeres.csv') as mujeres:
    mujeres_leer = csv.reader(mujeres, delimiter = ';')
    for row_mujeres in mujeres_leer:
        if row_mujeres:
            sql = "insert into mujeres(dni, nombre, apellidos, edad, sueldo) values (%s, %s, %s, %s, %s)"
            values = [(row_mujeres[0]), (row_mujeres[1]), (row_mujeres[2]), (row_mujeres[3]), (row_mujeres[4])]
            mycursor.execute(sql, values)
            mydb.commit()