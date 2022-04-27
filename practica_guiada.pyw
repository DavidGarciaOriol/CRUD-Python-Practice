from tkinter import *
from tkinter import messagebox
import sqlite3

## -- -- -- -- ## FUNCIONES BACKEND ## -- -- -- -- ##

## CONEXIÓN

def conexionBBDD():
    mi_conexion=sqlite3.connect("practica_guiada/Usuarios")

    mi_cursor = mi_conexion.cursor()

    try:

        mi_cursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(30),
            APELLIDO VARCHAR(40),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(200)
        )
        ''')

        messagebox.showinfo("BBDD", "BBDD Creada correctamente.")

    except:

        messagebox.showwarning("BBDD", "La BBDD ya existe.")

    
def salir_aplicacion():

    value = messagebox.askquestion("Salir", "¿Desea salir de la apliacion?")

    if value == "yes":
        root.destroy()

# BORRAR CAMPOS

def limpiar_campos():
    mi_id.set("")
    mi_nombre.set("")
    mi_pass.set("")
    mi_apellido.set("")
    mi_direccion.set("")

    texto_comentario.delete(1.0, END)

## CRUD EVENTS

def crear():
    mi_conexion = sqlite3.connect("practica_guiada/Usuarios")
    mi_cursor = mi_conexion.cursor()

    datos = mi_nombre.get(),mi_pass.get(),mi_apellido.get(),mi_direccion.get(),texto_comentario.get("1.0", END)

    #mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + mi_nombre.get() + 
    #"','" + mi_pass.get() + 
    #"','" + mi_apellido.get() + 
    #"','" + mi_direccion.get() + 
    #"','" + texto_comentario.get("1.0", END) + "')")

    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)", (datos))

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado correctamente.")

def leer():
    mi_conexion = sqlite3.connect("practica_guiada/Usuarios")
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())

    el_usuario = mi_cursor.fetchall()

    for usuario in el_usuario:
        mi_id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_pass.set(usuario[2])
        mi_apellido.set(usuario[3])
        mi_direccion.set(usuario[4])
        texto_comentario.insert(1.0, usuario[5])

    mi_conexion.commit()

def actualizar():
    mi_conexion = sqlite3.connect("practica_guiada/Usuarios")
    mi_cursor = mi_conexion.cursor()

    datos = mi_nombre.get(),mi_pass.get(),mi_apellido.get(),mi_direccion.get(),texto_comentario.get("1.0", END)


    #mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + mi_nombre.get() + 
    #"', PASSWORD='" + mi_pass.get() + 
    #"', APELLIDO='" + mi_apellido.get() + 
    #"', DIRECCION='" + mi_direccion.get() + 
    #"', COMENTARIOS='" + texto_comentario.get("1.0", END) + 
    #"' WHERE ID=" + mi_id.get())

    mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?"
    + "WHERE ID=" + mi_id.get(), (datos))

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado correctamente.")

def borrar():
    mi_conexion = sqlite3.connect("practica_guiada/Usuarios")
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro eliminado correctamente.")

## -- -- -- -- ## BARRA DE MENU ## -- -- -- -- ##

root = Tk() 
root.title("Práctica CRUD")

barra_menu = Menu(root)
root.config(menu = barra_menu, width=480, height=800)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexionBBDD)
bbdd_menu.add_command(label="Salir", command=salir_aplicacion)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos", command=limpiar_campos)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=borrar)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

## -- -- -- -- ## COMIENZO DE CAMPOS ## -- -- -- -- ##

mi_frame = Frame(root)
mi_frame.pack()

mi_id = StringVar()
mi_nombre = StringVar()
mi_apellido = StringVar()
mi_pass = StringVar()
mi_direccion = StringVar()

id_label = Label(mi_frame, text="ID:")
id_label.grid(row=0, column=0, padx=6, pady=6)
cuadro_id = Entry(mi_frame, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=6, pady=6)

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=1, column=0, padx=6, pady=6)
cuadro_nombre = Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=6, pady=6)

pass_label = Label(mi_frame, text="Password:")
pass_label.grid(row=2, column=0, padx=6, pady=6)
cuadro_pass = Entry(mi_frame, textvariable=mi_pass)
cuadro_pass.grid(row=2, column=1, padx=6, pady=6)

apellido_label = Label(mi_frame, text="Apellido:")
apellido_label.grid(row=3, column=0, padx=6, pady=6)
cuadro_apellido = Entry(mi_frame, textvariable=mi_apellido)
cuadro_apellido.grid(row=3, column=1, padx=6, pady=6)

direccion_label = Label(mi_frame, text="Dirección:")
direccion_label.grid(row=4, column=0, padx=6, pady=6)
cuadro_direccion = Entry(mi_frame, textvariable=mi_direccion)
cuadro_direccion.grid(row=4, column=1, padx=6, pady=6)

texto_comentario = Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=5, column=1, padx=6, pady=6)
scroll_vertical = Scrollbar(mi_frame, command=texto_comentario.yview)
scroll_vertical.grid(row=5, column=2, sticky="nsew")

## -- -- -- -- ## CAMPO DE BOTONES ## -- -- -- -- ##

mi_frame_2 = Frame(root)
mi_frame_2.pack()

boton_crear = Button(mi_frame_2, text="Crear", command=crear)
boton_crear.grid(row=1, column=0, padx=6, pady=6)

boton_leer = Button(mi_frame_2, text="Leer", command=leer)
boton_leer.grid(row=1, column=1, padx=6, pady=6)

boton_actualizar = Button(mi_frame_2, text="Actualizar", command=actualizar)
boton_actualizar.grid(row=1, column=2, padx=6, pady=6)

boton_borrar = Button(mi_frame_2, text="Borrar", command=borrar)
boton_borrar.grid(row=1, column=3, padx=6, pady=6)


texto_comentario.config(yscrollcommand=scroll_vertical.set)

root.mainloop()
