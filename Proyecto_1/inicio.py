from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
import subprocess
import webbrowser
import os
#Abre el arhivo que se desea editar
def open_txt():
    clearTextInput()
    global text_file1
    text_file1 = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),("all files","*.*")))
    try:
        miArchivo = open(text_file1, "r",encoding = "ISO-8859-1")   
        global lectura
        lectura = miArchivo.read()
        tkinter.messagebox.showinfo("Informacion","Archivo cargado correctamente")
        
    except ValueError:
        tkinter.messagebox.showerror("Error","Formato incorrecto")
        return None
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error","Archivo dañado \n o no seleccionado")
        return None
    name = text_file1
    name = name.replace("C:/gui/", "")
    name = name.replace(".txt", "")
    text_file1 = open(text_file1, 'r',encoding = "ISO-8859-1")
    stuff = text_file1.read()
    my_text.insert(END, stuff)
    text_file1.close()

    my_text.place(x=340, y=0, height=150, width=360)
    text_scroll1.grid(column=3, row=0, rowspan=6,sticky=N+S+W)
    l1.grid(row=0,column=2, sticky=W+E, padx=5)
    text_scroll2.grid(column=2, row=6,sticky=S+E+W)
#Borra lo que se inserto en el objeto texto   
def clearTextInput():
    my_text.delete("1.0","end")

#Sobreescribe el archivo que se abrio
def save_txt():
    try:
        text_file =text_file1.name
        text_file = open(text_file, 'w', encoding = "ISO-8859-1")
        text_file.write(my_text.get(1.0, END))
        tkinter.messagebox.showinfo("Informacion","Archivo guardado correctamente.")
    except:
        tkinter.messagebox.showerror("Error","No se pudo guardar el archivo")
    if my_text.place_info() != {}:
        my_text.place_forget()
        text_scroll1.grid_forget()
        text_scroll2.grid_forget()
        l1.grid_forget()
#Guarda el archivo con el nombre que se quiera
def save_as():
    file=filedialog.asksaveasfile()
    if file is None:
        return
    filetext=str(my_text.get(1.0,END))
    file.write(filetext)
    file.close()
#Se creo para ocultar el text area cuando ya se quiera
def info():
    if l2.grid_info() != {}:
        l2.grid_forget()
        l3.grid_forget()
        l4.grid_forget()
        l5.grid_forget()
        l6.grid_forget()
        l7.grid_forget()
        l8.grid_forget()
        l9.grid_forget()
    else:
        l2.grid(row=0,column=2,sticky=W+E, columnspan=2)
        l3.grid(row=1,column=2,sticky=W,columnspan=2)
        l4.grid(row=2,column=2,sticky=W,columnspan=2)
        l5.grid(row=3,column=2,sticky=W,columnspan=2)
        l6.grid(row=4,column=2,sticky=W,columnspan=2)
        l7.grid(row=5,column=2,sticky=W,columnspan=2)
        l8.grid(row=6,column=2,sticky=W,columnspan=2)
        l9.grid(row=6,column=3,sticky=E)
#Se creo para ocultar el text area cuando ya se quiera
def info1():
    if my_text.place_info() != {}:
        my_text.place_forget()
        text_scroll1.grid_forget()
        text_scroll2.grid_forget()
        l1.grid_forget()
        l10.grid_forget()

#Analiza el archivo de entrada
def analizar():
    from analizar import main,errores
    main()
    errores()
    from analizar import cadenaf
    clearTextInput()
    my_text.insert(END, cadenaf)
    my_text.place(x=340, y=0, height=150, width=360)
    text_scroll1.grid(column=3, row=0, rowspan=6,sticky=N+S+W)
    l1.grid(row=0,column=2, sticky=W+E, padx=5)
    text_scroll2.grid(column=2, row=6,sticky=S+E+W)
    l10.grid(row=7,column=2,sticky=E)
    
#Abre el archivo html
def errr():
    try:
        webbrowser.open('file://' + os.path.realpath("errores/ERRORES_202002912.html"))
    except:
        tkinter.messagebox.showerror("Error","No se han cargado errores")

#Abre el pdf del manual
def manual_t():
    path = 'Manual Tecnico.pdf'
    subprocess.Popen([path], shell=True)

def manual_u():
    path = 'Manual de Usuario.pdf'
    subprocess.Popen([path], shell=True)

#Creacion de interfaz
ventana=Tk()
ventana.geometry("+800+400")
aplicacion=Menu(ventana)
ventana.title("Proyecto 1")
principal=Frame(ventana)
principal.grid(row=0,column=0,columnspan=3,pady=0)
#Labels
Label(principal,borderwidth = 2,relief="groove", text="Archivo",bg="BLACK",fg="WHITE").grid(row=0,column=0,sticky=W+E)
Label(principal,borderwidth = 2,relief="groove", text="Ayuda",bg="BLACK",fg="WHITE").grid(row=0,column=1, sticky=W+E)
l1 = Label(principal,text="",padx=175)
l1.grid(row=0,column=2, sticky=W+E, padx=5)
l2 = Label(principal,borderwidth = 2,relief="groove", text="Informacion del Creador",bg="BLACK",fg="WHITE")
l2.grid(row=0,column=2,sticky=W+E, columnspan=2)
l3 = Label(principal, text="Nombre: Vinicio Manfredo López Pérez")
l3.grid(row=1,column=2,sticky=W, columnspan=2)
l4 = Label(principal, text="Carné: 202002912")
l4.grid(row=2,column=2, sticky=W, columnspan=2)
l5 = Label(principal, text="Lugar: Guatemala")
l5.grid(row=3,column=2, sticky=W,columnspan=2)
l6 = Label(principal, text="Curso: Lenguajes Formales de Programación")
l6.grid(row=4,column=2,sticky=W,columnspan=2)
l7 = Label(principal, text="Año de Creacion: 2022")
l7.grid(row=5,column=2,sticky=W,columnspan=2)
l8 = Label(principal, text="Sección: A+")
l8.grid(row=6,column=2,sticky=W)
#Botones
ttk.Button(principal,text="Abrir",command=open_txt).grid(row=1,column=0,sticky=W+E)
ttk.Button(principal,text="ㅤㅤㅤㅤㅤGuardarㅤㅤㅤㅤㅤ",command=save_txt).grid(row=2,column=0,sticky=W+E)
ttk.Button(principal,text="Guardar Como",command=save_as).grid(row=3,column=0,sticky=W+E)
ttk.Button(principal,text="Analizar",command=analizar).grid(row=4,column=0,sticky=W+E)
ttk.Button(principal,text="Errores", command=errr).grid(row=5,column=0,sticky=W+E)
ttk.Button(principal,text="Salir",command=ventana.destroy).grid(row=6,column=0,sticky=W+E)
ttk.Button(principal,text="Manual de Usuario",command=manual_u).grid(row=1,column=1,sticky=W+E)
ttk.Button(principal,text="ㅤㅤㅤManual Técnicoㅤㅤㅤ",command=manual_t).grid(row=2,column=1,sticky=W+E)
ttk.Button(principal,text="Temas de Ayuda",command=info).grid(row=3,column=1,sticky=W+E)
l9 = ttk.Button(principal,text="Ocultar",command=info)
l9.grid(row=6,column=3,sticky=E)
l10 = ttk.Button(principal,text="Ocultar",command=info1)
l10.grid(row=7,column=2,sticky=E)
# Crear scrollbar
text_scroll1 = Scrollbar(principal)
text_scroll1.grid(column=3, row=0, rowspan=6,sticky=N+S+W)
text_scroll2 = Scrollbar(principal, orient=HORIZONTAL)
text_scroll2.grid(column=2, row=6,sticky=S+E+W)
my_text = Text(principal,wrap=NONE,yscrollcommand=text_scroll1.set,xscrollcommand=text_scroll2.set)
my_text.place(x=340, y=0, height=150, width=360)
# Configurar scrollbar
text_scroll1.config(command=my_text.yview)
text_scroll2.config(command=my_text.xview)
#Ocultar al iniciar el programa
my_text.place_forget()
text_scroll1.grid_forget()
text_scroll2.grid_forget()
l1.grid_forget()
l2.grid_forget()
l3.grid_forget()
l4.grid_forget()
l5.grid_forget()
l6.grid_forget()
l7.grid_forget()
l8.grid_forget()
l9.grid_forget()
l10.grid_forget()
#Ejecucion de la ventana
ventana.mainloop()