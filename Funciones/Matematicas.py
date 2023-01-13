def sumar(n1, n2, r, error_message):
    try:
        r.set(float(n1.get()) + float(n2.get()))
    except ValueError:
        error_message.set("Ingresa solo datos numericos") 
    else:
        error_message.set("")
    finally:
        borrar(n1, n2)

def restar(n1, n2, r, error_message):
    try:
        r.set(float(n1.get()) - float(n2.get()))
    except ValueError:
        error_message.set("Ingresa solo datos numericos") 
    else:
        error_message.set("")
    finally:
        borrar(n1, n2)

def multiplicar(n1, n2, r, error_message):
    try:
        r.set(float(n1.get()) * float(n2.get()))
    except ValueError:
        error_message.set("Ingresa solo datos numericos") 
    else:
        error_message.set("")
    finally:
        borrar(n1, n2)

def dividir(n1, n2, r, error_message):
    try:
        r.set(float(n1.get()) / float(n2.get()))
    except ValueError:
        error_message.set("Ingresa solo datos numericos") 
    except ZeroDivisionError:
        error_message.set("No es posible dividir entre cero")
    else:
        error_message.set("")
    finally:
        borrar(n1, n2)

def potencia(n1, n2, r, error_message):
    try:
        r.set(float(n1.get()) ** float(n2.get()))
    except ValueError:
        error_message.set("Ingresa solo datos numericos") 
    else:
        error_message.set("")
    finally:
        borrar(n1, n2)

def borrar(n1, n2):
    n1.set("")
    n2.set("")