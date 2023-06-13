import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


def browse_button():
    # Abre un diálogo para seleccionar la ubicación de guardado del video
    download_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(tk.END, download_path)


def download_video():
    video_url = url_entry.get()
    download_path = path_entry.get()

    try:
        # Descarga el video utilizando pytube
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download(download_path)
        status_label.config(text="Descarga completada!")
    except Exception as e:
        status_label.config(text="Error al descargar el video")


# Configuración de la ventana principal
window = tk.Tk()
window.title("Descargador de Videos")
window.geometry("400x200")

# Etiqueta y campo de entrada para la URL del video
url_label = tk.Label(window, text="URL del Video:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Etiqueta y campo de entrada para la ubicación de descarga
path_label = tk.Label(window, text="Ubicación de Descarga:")
path_label.pack()
path_entry = tk.Entry(window, width=50)
path_entry.pack()

# Botón para seleccionar la ubicación de descarga
browse_button = tk.Button(window, text="Buscar", command=browse_button)
browse_button.pack()

# Botón para iniciar la descarga
download_button = tk.Button(window, text="Descargar", command=download_video)
download_button.pack()

# Etiqueta de estado de descarga
status_label = tk.Label(window, text="")
status_label.pack()

# Inicia el bucle principal de la ventana
window.mainloop()
