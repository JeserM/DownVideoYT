# DownVideoYT

---

Descargar videos de Youtube

### Librerias

---

```py
    import tkinter as tk
    from tkinter import filedialog
    from pytubefix import YouTube
    # from pytubefix.cli import on_progress
    import streamlit as st
```

Pytube no esta funcionando, de ahi el usar pytubefix
Se debe instalar pytubefix con pip install pytubefix
Mas Info: - https://pytubefix.readthedocs.io/en/latest/api.html - https://pypi.org/project/pytubefix/ - https://www.youtube.com/watch?v=51pjGysr7ws&t=116s

Para ejecutar los archivos \*.py con librerias de Streamlit de debe ejecutar: - "streamlit run name.py"

### Para poner en focus o top la ventana de descarga:

---

    -https://github.com/python-eel/Eel/issues/395
    - En mi caso:
        ~~~py
            def select_Folder(self):

                root = tk.Tk()
                # Prueba para foco root.lift()
                root.withdraw()
                root.wm_attributes("-topmost", True)
                folder_path = filedialog.askdirectory(
                    parent=root, title="Elige una carpeta de descarga")
                root.destroy()
                return folder_path
        ~~~

### Para convertir a EXE

---

https://ploomber.io/blog/streamlit_exe/

Hay que poner los archivos py de la aplicacion en la misma ubicación que el exe.

### Ejecución:

---

En la misma carpeta estará el exe junto con el archivo de código de python. El exe hara de lanzador.
