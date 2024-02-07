import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("NMS")  # Título de la ventana

# Obtener las dimensiones de la ventana
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana en la pantalla
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Establecer las dimensiones y posición de la ventana
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Crear un widget Label para mostrar el título centrado
title_label = tk.Label(root, text="NMS (SNMP v3)", font=("Helvetica", 24))
title_label.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
