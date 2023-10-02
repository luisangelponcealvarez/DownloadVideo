import tkinter as tk
from pytube import YouTube


def descargar_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Descarga completa.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")


# Crear la ventana principal
root = tk.Tk()
root.title("Descargar Video de YouTube")

# Crear etiqueta y campo de entrada para la URL
url_label = tk.Label(root, text="URL del video de YouTube:")
url_label.pack()
url_entry = tk.Entry(root, width=40)
url_entry.pack()

# Botón para iniciar la descarga
download_button = tk.Button(root, text="Descargar", command=descargar_video)
download_button.pack()

# Etiqueta para mostrar el estado de la descarga
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
