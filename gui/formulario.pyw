from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import messagebox
from tkinter import IntVar, StringVar
import mysql.connector

root = Tk()
root.resizable(0,0)
root.geometry("300x300")
root.title("Formulario")

vnombre = StringVar()
vapellidos = StringVar()
vdireccion = StringVar()
vlocalidad = StringVar()
vcp = IntVar()

def insertar_bd():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = ""
        )
        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists pruebas")
        mycursor.execute("use pruebas")
        mycursor.execute("create table if not exists pruebas ( \
            id int(3) auto_increment, \
            vnombre char(30), \
            vapellidos char(30), \
            vlocalidad char(30), \
            vcp int(5), \
            primary key(id))"
        )
        sql = "insert into pruebas (vnombre, vapellidos, vlocalidad, vcp) values (%s, %s, %s, %s)"
        val = [vnombre.get(), vapellidos.get(), vlocalidad.get(), vcp.get()]
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Información", "Registro insertado correctamente.")
    except:
        messagebox.showerror("Error", "Se ha producido un error.")

def insertar_fichero():
    try:
        f = open("datos.dat", "a+")
        f.write(vnombre.get()+", "+vapellidos.get()+", "+vdireccion.get()+", "+vlocalidad.get()+","+vcp.get()+"\n")
        f.close()
        messagebox.showinfo("Información", "Datos insertados correctamente.")
    except:
        messagebox.showerror("Error", "Se ha producido un error.")

f1 = Frame(root, width=300, height=50)
f2 = Frame(root, width=300, height=200)
f3 = Frame(root, width=300, height=50)

f1.grid(row=0, sticky="nsew")
f2.grid(row=1, sticky="nsew")
f3.grid(row=2, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

Label(f1, text='''
    Introduce tus datos en el siguiente formulario.\n
    Pulsa "Insertar en DB" para guardar en una BD.\n
    Pulsa "Insertar en fichero" para guardar en fichero.
''').grid(sticky="nsew")

Label(f2, text="Nombre: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
Label(f2, text="Apellidos: ").grid(row=1, column=0, padx=5, pady=5, sticky="e")
Label(f2, text="Dirección: ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
Label(f2, text="Localidad: ").grid(row=3, column=0, padx=5, pady=5, sticky="e")
Label(f2, text="C.P.: ").grid(row=4, column=0, sticky="e")

vnombre = Entry(f2)
vnombre.grid(row=0, column=1, padx=5, pady=5, sticky="e")
vapellidos = Entry(f2)
vapellidos.grid(row=1, column=1, padx=5, pady=5, sticky="e")
vdireccion = Entry(f2)
vdireccion.grid(row=2, column=1, padx=5, pady=5, sticky="e")
vlocalidad = Entry(f2)
vlocalidad.grid(row=3, column=1, padx=5, pady=5, sticky="e")
vcp = Entry(f2)
vcp.grid(row=4, column=1, padx=5, pady=5, sticky="e")

Button(f3, text="Insertar en DB", command=insertar_bd).grid(row=0, column=0, padx=5, pady=5)
Button(f3, text="Insertar en fichero", command=insertar_fichero).grid(row=0, column=1, padx=5, pady=5)

root.mainloop()