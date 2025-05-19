import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos_guardados = []#agregamos la dimencion 

def mensaje_uno():#cambiamos el nombre de la funcion  
    area_limpia()#cambiamos la fumcion 
    tk.Label(area_dinamica, text="presiona el boton para la bienvenida", font=("Arial", 14)).pack(pady=10)#cambiamos la etiqueta
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida:", command=lambda: messagebox.showinfo("Título", "Bienvenido 😼")).pack()#cambiamos la etiqueta😼

def mensaje_dos():
    area_limpia()
    tk.Label(area_dinamica, text="Aquí escribe tu nombre y opciones", font=("Arial", 14)).pack(pady=10)#colocamos nuevo letrero 

    tk.Label(area_dinamica, text="Nombre del alumno:").pack()#etiqueta
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="opcion A:").pack() #etiqueta 
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Opción 1", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Opción 2", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Que opcion quieres:").pack()# etiqueta nueva 
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    etiqueta_datos = tk.Label(area_dinamica, text="", font=("Arial", 12), fg="blue") #pusimos color y agregamos etiqueta para que muestre los datos en lista 
    etiqueta_datos.pack(pady=10)
    
    
    def accion_guardar():
        valor = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        lista = combo.get()
        
        # almacenamos los datos en la lista
        datos_guardados.append(f"Nombre: {valor}, Selección: {seleccion}, Lista: {lista}")
        
        # se fueron acumulando los datos 
        etiqueta_datos.config(text="\n".join(datos_guardados))
 
        messagebox.showinfo("Datos del usuario", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")

    tk.Button(area_dinamica, text="mostrar datos", command=accion_guardar).pack(pady=10) # etiqueta guardar

def mensaje_tres():
    area_limpia()
    tk.Label(area_dinamica, text="Cambia el color", font=("Arial", 14)).pack(pady=10) # etiqueta

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack() 

    def diferente_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: diferente_color(col)).pack(pady=2)

def mensaje_cuatro():
    area_limpia()
    tk.Label(area_dinamica, text="Explicacion del alumno", font=("Arial", 14)).pack(pady=10) # etiqueta 
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

# cambiamos letreros del texto
tk.Button(menu_lateral, text="Inicio:", command=mensaje_uno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="seleccion de datos", command=mensaje_dos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="color", command=mensaje_tres, width=15).pack(pady=10)
tk.Button(menu_lateral, text="preguntas", command=mensaje_cuatro, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

mensaje_uno()
ventana_principal.mainloop()


#cambiamos etiquetas y funciones 
