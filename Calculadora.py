from tkinter import *
from Funciones.Matematicas import *

root = Tk()
root.title("Calculadora")
root.iconbitmap("coffee.ico")
root.config(bd=15)
root.resizable(False, False)


n1 = StringVar()
n2 = StringVar()
r = StringVar()
error_message = StringVar()


frame1 = Frame(root)
frame1.pack()
Label(frame1, text="Numero 1").grid(row=0, column=0)
Entry(frame1, justify="left", textvariable= n1).grid(row=0, column=1) # Primero numero
Label(frame1, text="Numero 2").grid(row=1, column=0)
Entry(frame1, justify="left", textvariable= n2).grid(row=1, column=1) # Segundo numero
Label(frame1, text="Resultado").grid(row=3, column=0)
Entry(frame1, justify="left", textvariable= r, state="disabled").grid(row=3, column=1) # Resultado

frame2 = Frame(root)
frame2.pack()
Button(frame2, text= "Sumar", command=lambda: sumar(n1, n2, r, error_message)).pack(side="left")
Button(frame2, text= "Resta", command=lambda:  restar(n1, n2, r, error_message)).pack(side="left")
Button(frame2, text= "Multiplicacion", command=lambda: multiplicar(n1, n2, r, error_message)).pack(side="left")
Button(frame2, text= "Division", command=lambda: dividir(n1, n2, r, error_message)).pack(side="left")
Button(frame2, text= "Potencia", command=lambda: potencia(n1, n2, r, error_message)).pack(side="left")

frame3 = Frame(root)
frame3.pack()

Label(frame3, textvariable=error_message).pack()




root.mainloop()