# DownVideoYT

Aplicación para hacer pruebas y obtener info de los videos de Youtube. Basado en las guias de [@codigoespinoza](https://www.youtube.com/@CodigoEspinoza), y su canal.
He añadido/cambiado un par de funcionalidades como:
- cambiado la libreria de pytube, que ya no funciona, por pytubefix.
- posibilidad de seleccionar la ruta de descarga con una ventana de selección.
  
Ahora mismo entre las pruebas que se puede realizar, en el caso de descarga de archivos de video solo en el caso de resolución de 360P se descarga auduo y video en un solo fichero. Para mayarores resoluciones hay que bajar audio por un lado y video por otro, para luego juntarlos. Se puede hacer por ejemplo con VLC.


### Librerias
---

```py
    import tkinter as tk
    from tkinter import filedialog
    from pytubefix import YouTube
    # from pytubefix.cli import on_progress ==> se puede usar y quitar el metodo estatico "onProgress", si se usa se pierde la barra de descarga y solo la muestra en consola.
    import streamlit as st
```

Pytube no esta funcionando, de ahi el usar pytubefix. Se debe instalar pytubefix con:
- pip install pytubefix
- pip install streamlit

  
Mas Info sobre pytube
- https://pytubefix.readthedocs.io/en/latest/api.html
- https://pypi.org/project/pytubefix/
- https://www.youtube.com/watch?v=51pjGysr7ws&t=116s

Para ejecutar los archivos \*.py con librerias de Streamlit de debe ejecutar: - "streamlit run name.py"

### Para poner en focus o top la ventana de descarga:
---
    - https://github.com/python-eel/Eel/issues/395

En mi caso he empleado:

```py
    def select_Folder(self)
        root = tk.Tk()
        # Prueba para foco root.lift()
        root.withdraw()
==>     root.wm_attributes("-topmost", True)
        folder_path = filedialog.askdirectory(
            parent=root, title="Elige una carpeta de descarga")
        root.destroy()
        return folder_path
```
## Generar un archivo ejecutable al hacer uso de streamlit (no funcionara el exe generado con pyinstaller sin estos pasos)
---
Siguiendo la guia de "Neelasha Sen" en su [articulo](https://ploomber.io/blog/streamlit_exe/), para poder crear un ejecutable con pyinstaller, se puede crear el "run.exe".
En el archivo "run.py" tambien hay que añadir las librerias que se usan en archivo que contiene el codigo fuente de la app:
```py
import os
import sys
import streamlit as st
import streamlit.web.cli as stcli
import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
# from pytubefix.cli import on_progress


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app3.0.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
```

tan solo seguir el resto del articulo.
Hay que poner los archivos py de la aplicacion en la misma ubicación que el exe.


### Ejecución:
---

Hacen falta en la misma carpeta el archivo "run.exe" y el app**.py. El exe hara de lanzador.
Para usar solo el py, hay que ejecutarlo con "streamlit run app**.py"


## DownLoad

- [V.3.0](https://github.com/JeserM/DownVideoYT/releases/tag/V.3.0](https://github.com/JeserM/DownVideoYT/releases)


___ FIN ___
