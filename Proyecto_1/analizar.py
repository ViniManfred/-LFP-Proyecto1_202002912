from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
import math
import os
import sys
from string import Template

class Automata:
    def __init__(self,matriz):
        self.matriz = matriz

    def automata(self):
        self.estado = 0
        self.contador=0
        self.validos=[]
        self.errors=[]
        self.operaciones=[]
        global trac1
        trac1=self.errors
        print("Tamano de la matriz:",len(self.matriz))
        for fila in range(len(self.matriz)):
            self.cadena= self.matriz[fila]           
            self.contador+=1
            for i in range(0,len(self.cadena)):
                self.transicion =self.cadena[i]
                ############### ESTADO 0 ###############
                if self.estado==0:
                    if self.transicion=="<":
                        self.estado=1
                    elif isinstance(self.transicion, str):
                        if self.matriz[fila-1]=="<texto>":
                            if i==len(self.cadena)-1:
                                self.estado=100
                            else:
                                self.estado=0
                        elif self.matriz[fila+1]=="</texto>":
                            if i==len(self.cadena)-1:
                                self.estado=100
                            else:
                                self.estado=0
                        else:
                            self.errors.append(self.transicion)
                            self.errors.append(i)
                            return False
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 1 ###############
                elif self.estado==1:
                    if str.isalpha(self.transicion):
                        if self.cadena[0]=="<":
                            self.estado=2
                        elif str.isalpha(self.cadena[0]):
                            self.estado=1
                        else:
                            self.errors.append(self.transicion)
                            self.errors.append(i)
                            return False
                    elif self.transicion=="/":
                        self.estado=2
                    elif self.transicion==".":
                        self.estado=100
                    elif self.transicion==",":
                        self.estado=3
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 2 ###############
                elif self.estado==2:
                    if str.isalpha(self.transicion):
                        if str.isalpha(self.cadena[1]):
                            if str.isalpha(self.cadena[0]):
                                self.estado=3
                            elif self.cadena[0]=="<":
                                self.estado=2
                            else:
                                self.errors.append(self.transicion)
                                self.errors.append(i)
                                return False
                        elif self.cadena[1]=="/":
                            self.estado=3
                        else:
                            self.errors.append(self.transicion)
                            self.errors.append(i)
                            return False
                    elif self.transicion==">":
                        if len(self.cadena) in range(6,9):
                            self.estado=100
                        elif len(self.cadena)>8:
                            self.estado=3
                        else:
                            self.errors.append(self.transicion)
                            self.errors.append(i)
                            return False
                    elif self.transicion=="=":
                        self.estado=3
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 3 ###############
                elif self.estado==3:
                    if str.isalpha(self.transicion):
                        if "<titulo>" in self.cadena or "color" in self.cadena:
                            self.estado=4
                        else:
                            self.estado=3
                    elif self.transicion==">":
                        self.estado=100
                        if "operacion" in self.cadena: 
                            self.operaciones.append(self.cadena)
                    elif str.isdigit(self.transicion):
                        self.estado=4
                    elif self.transicion==".":
                        self.estado=100
                    elif self.transicion==",":
                        self.estado=2
                    elif self.transicion=="[":
                        self.estado=4
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 4 ###############
                elif self.estado==4:
                    if str.isdigit(self.transicion):
                        self.estado=4
                    elif str.isalpha(self.transicion):
                        if "<descripcion>" in self.cadena or "<contenido>" in self.cadena:
                            self.estado=5
                        else:
                            self.estado=4
                    elif self.transicion==".":
                        self.estado=5
                    elif self.transicion=="=":
                        self.estado=5
                    elif self.transicion=="<":
                        self.estado=7
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 5 ###############
                elif self.estado==5:
                    if str.isdigit(self.transicion):
                        self.estado=6
                    elif str.isalpha(self.transicion):
                        self.estado=5
                    elif self.transicion=="]":
                        self.estado=6
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 6 ###############
                elif self.estado==6:
                    if str.isdigit(self.transicion):
                        self.estado=6
                    elif self.transicion=="<" or self.transicion=="/":
                        self.estado=7
                    elif self.transicion==">":
                        self.estado=100
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 7 ###############
                elif self.estado==7:
                    if self.transicion=="/":
                        self.estado=8
                    elif str.isalpha(self.transicion):
                        self.estado=9
                    elif self.transicion==">":
                        self.estado=100
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 8 ###############
                elif self.estado==8:
                    if str.isalpha(self.transicion):
                        self.estado=9
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                ############### ESTADO 9 ###############
                elif self.estado==9:
                    if str.isalpha(self.transicion):
                        self.estado=9
                    elif self.transicion==">":
                        self.estado=100
                        if "numero" in self.cadena:
                            self.operaciones.append(self.cadena)
                    else:
                        self.errors.append(self.transicion)
                        self.errors.append(i)
                        return False
                else:
                    self.errors.append(self.transicion)
                    self.errors.append(i)
                    return False
            if self.estado==100:
                self.validos.append(self.contador)
                self.estado=0
            else:
                self.errors.append(self.transicion)
                self.errors.append(i)
                return False
            global crack
            crack=self.validos
            if len(self.matriz)==self.contador:
                return True
    
    def gestion(self):
        crack=[]
        global cadenaf
        cadenaf="Generacion de Archivo HTML\n"
        for linea in self.operaciones:
            linea=str(linea).replace("numero","")
            linea=str(linea).replace("/","")
            linea=str(linea).replace("<","")
            linea=str(linea).replace(">","") 
            crack.append(linea)
        cadena=""
        try:
            for line in range(len(crack)):
                if len(crack[line])>9 and not any(chr.isdigit() for chr in str(crack[line])):
                    crack[line]=str(crack[line]).replace("="," ")
                    cadena+="\n"+crack[line]+":\n"
                elif crack[line]=="operacion" and not any(chr.isdigit() for chr in str(crack[line])):
                    cadena+="\n"+crack[line]+"\n"
                else:
                    if any(chr.isalpha() for chr in str(crack[line+1])):
                        if crack[line+1]=="operacion":
                            cadena+=crack[line]
                        else:
                            cadena+=crack[line]+","    
                    else:
                        cadena+=crack[line]+","

            lista_cadena=cadena.split("\n")
            matriz_2 = [elemento_lista for elemento_lista in lista_cadena if elemento_lista != ""]
            final1=[]
            count=0
        except:
            cadenaf+="Error en la linea: "+self.matriz[len(crack)]
        for line1 in range(len(matriz_2)): 
            if any(chr.isdigit() for chr in str(matriz_2[line1])):
                if len(matriz_2[line1+1])>9:
                    count+=1
            if ":" in matriz_2[line1] and ":" in matriz_2[line1+1]:
                count+=1
        
            if matriz_2[line1]=="operacion suma:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","+")
            elif matriz_2[line1]=="operacion resta:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","-")
            elif matriz_2[line1]=="operacion multiplicacion:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","*")
            elif matriz_2[line1]=="operacion division:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","/")
            elif matriz_2[line1]=="operacion potencia:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","**")
            elif matriz_2[line1]=="operacion raiz:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","**(1/(")
            elif matriz_2[line1]=="operacion mod:":
               matriz_2[line1+1]=matriz_2[line1+1].replace(",","%")

            final1.append(matriz_2[line1])
        final2=[]
        for line2 in range(len(final1)-count):
            if ':' in final1[line2] and ":" in final1[line2+1]:
                final1.pop(line2+1)
            if any(chr.isdigit() for chr in str(final1[line2])): 
                if len(final1[line2+1])>9:
                    final1.pop(line2+1)
                if any(chr.isdigit() for chr in str(final1[line2+1])):
                    final1[line2+1]="("+str(final1[line2+1])+")"  
            else:
                line2=line2
            final2.append(final1[line2])
        print(final2)
        final3=[]
        for line2 in range(len(final2)):
            if len(final2[line2])>9 and not any(chr.isdigit() for chr in str(final2[line2])):
                if any(chr.isdigit() for chr in str(final2[line2+1])):
                    if any(chr.isdigit() for chr in str(final2[line2+2])): 
                        final2[line2]="operacion compleja:"
            final3.append(final2[line2])
        matriz_3 = [elemento_lista for elemento_lista in final3 if elemento_lista != "operacion"]
        cadena1=""
        for line in range(len(matriz_3)):
            if any(chr.isalpha() for chr in str(matriz_3[line])):
                cadena1+=","+str(matriz_3[line])+","    
            else:
                cadena1+=str(matriz_3[line])
        lista_cadena1=cadena1.split(",")
        matriz_4 = [elemento_lista for elemento_lista in lista_cadena1 if elemento_lista != ""]

        cadena2=""
        for line in range(len(matriz_4)):
            if "(1/" in matriz_4[line]:
                matriz_4[line]=str(matriz_4[line])+"))"
            elif "inverso" in matriz_4[line]:
                matriz_4[line+1]="("+str(matriz_4[line+1])+")**(-1)"
            elif "seno" in matriz_4[line]:
                matriz_4[line+1]="math.sin("+str(matriz_4[line+1])+")"
            elif "coseno" in matriz_4[line]:
                matriz_4[line+1]="math.cos("+str(matriz_4[line+1])+")"
            elif "tangente" in matriz_4[line]:
                matriz_4[line+1]="math.tan("+str(matriz_4[line+1])+")"
            if any(chr.isdigit() for chr in str(matriz_4[line])):
                respuesta=eval(str(matriz_4[line])) 
                respuesta1=round(respuesta, 2)  
            if ":" in str(matriz_4[line]):
                cadena2+=","+str(matriz_4[line])+","    
            else:
                cadena2+=str(matriz_4[line])+"="+str(respuesta1)
        lista_cadena2=cadena2.split(",")
        matriz_final = [elemento_lista for elemento_lista in lista_cadena2 if elemento_lista != ""]
        print(matriz_final)
        for linea in matriz_final:
            cadenaf+=linea+"\n"
        print(cadenaf)
    

def errores():
    if len(trac1)>0:
        filein=open('Plantilla/Plantilla.html')
        src=Template(filein.read())
        dic={"numero":1, "lexema":trac1[0],"tipo":"Error", "columna":trac1[1],"fila":len(crack)}
        resultt=src.substitute(dic)
        try:
            os.mkdir("errores")
            filein2=open("Errores/"+"ERRORES_202002912"+".html","w")
            filein2.writelines(resultt)
        except OSError:
            if os.path.exists("errores"):
                filein2=open("Errores/"+"ERRORES_202002912"+".html","w")
            filein2.writelines(resultt)

        
def main():
    matriz=[]
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
    
    print("LECTURA LINEA POR LINEA")
    texto = open(text_file1, "r",encoding = "ISO-8859-1")
    lineas = texto.readlines()
    for Linea in lineas:
        Linea = Linea.replace(" ","")
        Linea = Linea.replace("\n","")
        Linea = Linea.replace("\t","")
        Linea = Linea.replace("Ã³","o")
        Linea = Linea.replace("Ã¡","a")
        Linea = Linea.replace("Ã\xad","i")
        Linea = Linea.replace("Ã©","e")
        Linea = Linea.replace("Ãº","u")
        line =Linea.lower()
        matriz.append(line)
    matriz_1 = [elemento_lista for elemento_lista in matriz if elemento_lista != ""]
    # Esta sección es siempre ejecutada
    texto.close()
    #llamada a clase automata
    AFD=Automata(matriz_1)
    if AFD.automata() == True:
        print("Archivo con Formato Valido\n")
        AFD.gestion()
    else:
        list1=["<",">","/",".",",","="]
        global cadenaf
        cadenaf=("Archivo contiene errores. \n")+"Error en la linea: "+str(len(crack))+"\n"+matriz_1[len(crack)]+"\n"
        if trac1[0] in list1 or str(trac1[0]).isalpha():
            cadenaf+="Syntax Error -> "+trac1[0]+" | En la columna -> "+str(trac1[1])
        else:
            cadenaf+="Error Lexico -> "+trac1[0]+" | En la columna -> "+str(trac1[1])

        