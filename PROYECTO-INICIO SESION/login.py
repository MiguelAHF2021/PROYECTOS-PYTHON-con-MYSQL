import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
import pymysql

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("logo.ico")

    image=PhotoImage(file="logo.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al sistema",bg="navy", fg="white",width="300",height="3",font=("Calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1,text="Por Favor ingrese su usuario y contraseña", bg="navy", fg="white",width="300",height="3",font=("Calibri",15)).pack()
    Label(pantalla1,text="").pack()

    global nombreusuario_verify
    global claveusuario_verify

    nombreusuario_verify=StringVar()
    claveusuario_verify=StringVar()

    global nombre_usuario_entry
    global clave_usuario_entry

    Label(pantalla1,text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1,textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Contraseña").pack()
    clave_usuario_entry = Entry(pantalla1,show="*",textvariable=claveusuario_verify)
    clave_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar Sesion",command=validarDatos).pack()

def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("logo.ico")

    global nombreusuario_entry
    global clave_entry

    nombreusuario_entry=StringVar()
    clave_entry=StringVar()

    Label(pantalla2,text="Ingrese un usuario y una contraseña", bg="navy", fg="white",width="300",height="3",font=("Calibri",15)).pack()
    Label(pantalla2,text="").pack()

    Label(pantalla2,text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2,text="Contraseña").pack()
    clave_entry = Entry(pantalla2,show="*")
    clave_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2,text="Registrar",command=insertarDatos).pack()

def insertarDatos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bdsesion"
    )
    fcursor=bd.cursor()
    sql="INSERT INTO login(usuario,clave) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(),clave_entry.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Se ha registrado correctamente",title="Aviso")
    except:
        bd.rollback(message="No se ha registrado correctamente",title="Aviso")
    
    bd.close()


def validarDatos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bdsesion"
    )

    fcursor=bd.cursor()

    fcursor.execute("SELECT clave FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and clave='"+claveusuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo("Datos ingresados correctos",message="Usuario y contraseña correcta")
    else:
        messagebox.showinfo("Datos ingresados incorrectos",message="Usuario y contraseña incorrecta")
    
    bd.close()

menu_pantalla()