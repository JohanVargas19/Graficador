import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from tkinter import*
import numpy as np
from tkinter import ttk
from sympy import*

root=Tk()
fig, ax= plt.subplots()
root.geometry("850x925")
root.resizable(0,0)

#variables
grado=StringVar()
selgrados=StringVar()
A=IntVar()
B=IntVar()
C=IntVar()
D=IntVar()
Lineal=StringVar()
Cuadratica=StringVar()
Cubica=StringVar()
liminferior=IntVar()
limsuperior=IntVar()
inicial=IntVar()

def cream():

    gradoslabel=Label(frame, text="INGRESE LOS COEFICIENTES DE CADA GRADO")
    gradoslabel.grid(row=7,column=1,columnspan=4,pady=10)
    
    Continuar.grid_remove()

    if selgrados.get()=="Lineal":
        Cx.grid(row=8,column=1,columnspan=2,padx=5,pady=5)
        coeficienteC.grid(row=9,column=1,columnspan=2,padx=5,pady=5)
        
        Dx.grid(row=8,column=3,columnspan=2,padx=5,pady=5)
        coeficienteD.grid(row=9,column=3,columnspan=2,padx=5,pady=5)
    
    if selgrados.get()=="Cuadratica":
        Bx.grid(row=8,column=2,padx=5,pady=5)
        coeficienteB.grid(row=9,column=2,padx=5,pady=5)

        Cx.grid(row=8,column=3,padx=5,pady=5)
        coeficienteC.grid(row=9,column=3,padx=5,pady=5)

        Dx.grid(row=8,column=4,padx=5,pady=5)
        coeficienteD.grid(row=9,column=4,padx=5,pady=5)

    if selgrados.get()=="Cubica":
        Ax.grid(row=8,column=1,padx=5,pady=5)
        coeficienteA.grid(row=9,column=1,padx=5,pady=5)

        Bx.grid(row=8,column=2,padx=5,pady=5)
        coeficienteB.grid(row=9,column=2,padx=5,pady=5)

        Cx.grid(row=8,column=3,padx=5,pady=5)
        coeficienteC.grid(row=9,column=3,padx=5,pady=5)

        Dx.grid(row=8,column=4,padx=5,pady=5)
        coeficienteD.grid(row=9,column=4,padx=5,pady=5)
        
    if selgrados.get()=="Exponencial":
        Ex.grid(row=8,column=2,columnspan=2,padx=5,pady=5)
        coeficienteA.grid(row=9,column=2,padx=5,pady=5)

        Fx.grid(row=8,column=3,padx=5,pady=5)
        coeficienteB.grid(row=9,column=3,padx=5,pady=5)
        
    
def cambio():
    Continuar.grid()
    gradoslabel.grid_forget()
    coeficienteA.grid_forget()
    coeficienteB.grid_forget()
    coeficienteC.grid_forget()
    coeficienteD.grid_forget()
    Ax.grid_forget()
    Bx.grid_forget()
    Cx.grid_forget()
    Dx.grid_forget()
    Ex.grid_forget()
    Fx.grid_forget()


def graficar():
    if selgrados.get()=="Lineal":
        global x
        ax.clear()
        ax.grid(axis="both",linestyle="dotted")
        x=np.arange(liminferior.get(),limsuperior.get(), 0.1)
        ax.set_xlim([liminferior.get(),limsuperior.get()])
        #ax.set_ylim([-50,50])
        y=C.get()*x+D.get()
        ax.plot(x,y)
        canvas.draw()
        
    if selgrados.get()=="Cuadratica":
        ax.clear()
        ax.grid(axis="both",linestyle="dotted")
        x=np.arange(liminferior.get(),limsuperior.get(),0.1)
        ax.set_xlim([liminferior.get(),limsuperior.get()])
        #ax.set_ylim([-50,50])
        y=B.get()*x**2+C.get()*x+D.get()
        ax.plot(x,y)
        canvas.draw()
        
    if selgrados.get()=="Cubica":
        ax.clear()
        ax.grid(axis="both",linestyle="dotted")
        x=np.arange(liminferior.get(),limsuperior.get(),0.1)
        ax.set_xlim([liminferior.get(),limsuperior.get()])
        #ax.set_ylim([-50,50])
        y=A.get()*x*x*x+B.get()*x**2+C.get()*x+D.get()
        ax.plot(x,y)
        canvas.draw()
    
    if selgrados.get()=="Exponencial":
        ax.clear()
        ax.grid(axis="both",linestyle="dotted")
        x=np.arange(liminferior.get(),limsuperior.get(),0.1)
        ax.set_xlim([liminferior.get(),limsuperior.get()])
        #ax.set_ylim(-50,50 )
        y=(A.get())*np.exp(B.get()*x)
        ax.plot(x,y)
        canvas.draw()

#///
def raices():
    global i, y, yderivada,funcion
    x=Symbol('x')
    y=A.get()*x*x*x+B.get()*x**2+C.get()*x+D.get()
    yderivada=y.diff(x)
    x=inicial.get()

    for i in range(0,12):
        yeval=eval(str(y))
        yderval=eval(str(yderivada))
        funcion=x-(yeval/yderval)
        x=funcion
    
    mostrarraiz.config(text=funcion)
    plt.axvline(funcion,-50,50,color="red",linestyle="dashed") #se utiliza para hacer una recta perpendicular al eje x
    canvas.draw()

#///
        
            
frame=Frame(root)
titulo=Label(frame,text="GRAFICADOR DE FUNCIONES")
titulo.config(font=("Roboto",32))
titulo.grid(row=1,column=1,columnspan=4,padx=5,pady=5)
frame.pack()
canvas=FigureCanvasTkAgg(fig,master=frame)
canvas.get_tk_widget().grid(row=3,column=1,columnspan=4,padx=5,pady=5)

#botones
gradofuncion=Label(frame,text="SELECCIONE EL GRADO DE LA FUNCION")
gradofuncion.grid(row=5,column=1,columnspan=4,pady=10)

selecciondegrados=ttk.Combobox(frame, values=["Lineal","Cuadratica","Cubica","Exponencial"],state="readonly",textvariable=selgrados)
selecciondegrados.grid(row=6,column=1,columnspan=2,pady=4)

#///

gradoslabel=Label(frame, text="INGRESE LOS COEFICIENTES DE CADA GRADO")
gradoslabel.grid(row=7,column=1,columnspan=4,pady=10)

coeficienteA=ttk.Entry(frame,textvariable=A)
coeficienteA.grid(row=9,column=1,padx=5,pady=5)
    
coeficienteB=ttk.Entry(frame,textvariable=B)
coeficienteB.grid(row=9,column=2,padx=5,pady=5)
    
coeficienteC=ttk.Entry(frame,textvariable=C)
coeficienteC.grid(row=9,column=3,padx=5,pady=5)

coeficienteD=ttk.Entry(frame,textvariable=D)
coeficienteD.grid(row=9,column=4,padx=5,pady=5)
    

#///

Ax=Label(frame,text="Ax^3")
Ax.grid(row=8,column=1,padx=5,pady=5)
Bx=Label(frame,text="+ Bx^2")
Bx.grid(row=8,column=2,padx=5,pady=5)
Cx=Label(frame,text="+ Cx")
Cx.grid(row=8,column=3,padx=5,pady=5)
Dx=Label(frame,text="+ D")
Dx.grid(row=8,column=4,padx=5,pady=5)
Ex=Label(frame,text="A*")
Ex.grid(row=8,column=4,padx=5,pady=5)
Ex.grid_forget()
Fx=Label(frame,text="e^Bx")
Fx.grid(row=8,column=4,padx=5,pady=5)
Fx.grid_forget()

#///

inf=Label(frame,text="Limite Inferior:")
inf.grid(row=10,column=1,padx=5,pady=5)

datoinferior=Entry(frame,textvariable=liminferior)
datoinferior.grid(row=10,column=2,padx=5,pady=5)

sup=Label(frame,text="Limite Superior:")
sup.grid(row=10,column=3,padx=5,pady=5)

datosuperior=Entry(frame,textvariable=limsuperior)
datosuperior.grid(row=10,column=4,padx=5,pady=5)

#////

Continuar=Button(frame,text="Ok",command=cream)
Continuar.grid(row=6,column=3)
Continuar.grid_remove()

cambiol=Button(frame,text="clc",command=cambio)
cambiol.grid(row=6,column=4)

botongraficas=Button(frame,text="Graficar", command=graficar)
botongraficas.grid(row=11,column=2,columnspan=2,pady=15)

#//

inraiz=Label(frame,text="BUSQUEDA DE RAICES")
inraiz.grid(row=12,column=2,columnspan=2,padx=5,pady=5)

raiz=Button(frame,text="BUSCAR RAIZ",command=raices)
raiz.grid(row=13,column=1,columnspan=2,padx=5,pady=5)

valin=Entry(frame,textvariable=inicial)
valin.grid(row=13,column=3,columnspan=2,padx=5,pady=5)

mostrarraiz2=Label(frame,text="LA RAIZ ES :")
mostrarraiz2.grid(row=14,column=2,padx=5,pady=5)

mostrarraiz=Label(frame,text="")
mostrarraiz.grid(row=14,column=3,padx=5,pady=5)


root.mainloop()