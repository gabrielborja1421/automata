from tkinter import *
from tkinter import filedialog, ttk
from main import *
raiz = Tk()

raiz.title("Automatas")
#.rasizable(ancho,alto) 0 false 1 true y biseversa blokeo de tamaño
raiz.resizable(0,0)


raiz.geometry("800x600")

raiz.config(bg="white")

def abrirArchivo():

    # Mostrar el diálogo para abrir un archivo.
    filename = filedialog.askopenfilename(initialdir="C:/",
        filetypes=(("Archivos de texto","*.txt")
        ,("Todos los archivos", "*.*"))
    )
    # ('C:/Users/Gabri/OneDrive/Escritorio/tests/prueba.txt', 'Text files (*.txt)')
    # Imprimir la ruta del archivo seleccionado por el usuario.
    main.nombreArchivo(filename)
    print(filename)

boton = ttk.Button(text='Selecciona el archivo .txt', command=abrirArchivo)
boton.grid(row=4,column=2)
raiz.mainloop()