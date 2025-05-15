import tkinter as tk
from tkinter import filedialog

# Crea una ventana oculta
root = tk.Tk()
root.withdraw()

# Definimos varios tipos de archivo
tipos_archivo = [
    ("Archivos de texto", "*.txt"),
    ("Imágenes PNG", "*.png"),
    ("Imágenes JPEG", "*.jpg;*.jpeg"),
    ("Todos los archivos", "*.*")
]

# Abre el diálogo
ruta_archivo = filedialog.asksaveasfilename(
    title="Guardar como...",
    defaultextension=".txt",
    filetypes=tipos_archivo
)

# Mostrar resultado
if ruta_archivo:
    print(f"Archivo se guardará en: {ruta_archivo}")
else:
    print("No se seleccionó ninguna ruta.")
