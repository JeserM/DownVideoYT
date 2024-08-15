
""" 
Pytube no esta funcionando, de ahi el usar pytubefix
Se debe instalar pytubefix con pip install pytubefix
Info: 
    - https://pytubefix.readthedocs.io/en/latest/api.html
    - https://pypi.org/project/pytubefix/
    - https://www.youtube.com/watch?v=51pjGysr7ws&t=116s

Para ejecutar este script se debe hacer lo siguiente:
    - streamlit run appOK.py
    """
import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
# from pytubefix.cli import on_progress
import streamlit as st


class YoutubeDownloader:
    def __init__(self, url):
        self.url = url
        # self.youtube = pytube.YouTube(self.url)
        # self.youtube = YouTube(
        #     self.url, on_progress_callback=on_progress)
# ! no use "on_progress_callback=on_progress" muestra una barra pero en la consola. con este adornador muestra la barra en la web

        self.youtube = YouTube(
            self.url, on_progress_callback=self.onProgress)
        self.stream = None

    def showTitle(self):
        st.write(f"Titulo:   {self.youtube.title}")
        self.showStreams()

    def showStreams(self):
        streams = self.youtube.streams
        stream_options = [
            f"Resolution: {stream.resolution or 'N/A'} / FPS: {
                getattr(stream, 'fps', 'N/A')}/Tipo: {stream.mime_type})"
            for stream in streams
        ]
        choice = st.selectbox("Elija una opción de stream", stream_options)
        self.stream = streams[stream_options.index(choice)]

    def getFilesize(self):
        file_size = self.stream.filesize / 1000000
        return file_size

    def getPermissionToCOntinue(self, file_size):
        st.write(f"Titulo:  {self.youtube.title}")
        st.write(f"Autor:  {self.youtube.author}")
        st.write(f"Tamaño del archivo:  {file_size:.2f} MB")
        st.write(f"Resolución:  {self.stream.resolution or 'N/A'}")
        st.write(f"FPS:  {getattr(self.stream, 'fps', 'N/A')}")
        if st.button("Descargar"):
            self.download()

    def download(self):
        # if st.button("Seleccionar carpeta de descarga"):
        #     # Inicializar tkinter
        #     root = tk.Tk()
        #     root.withdraw()
        #     download_path = filedialog.askdirectory()
        #     root.destroy()
        #     st.text_input("Ruta de descarga seleccionada", value=download_path)
        #     if st.button("Descargar"):
        #         self.download(download_path)
        # download_path = filedialog.askdirectory()
        # self.download(download_path)
        self.stream.download()
        st.success("Descarga completada")

    # @staticmethod
    # def onProgress(stream=None, chunk=None, remaining=None):
        # file_size = stream.filesize / 1000000
        # file_downloaded = file_size - (remaining / 1000000)
        # st.progress(file_downloaded / file_size)

    # @staticmethod
    # def onProgress(stream, chunk, remaining):
    #     file_size = stream.filesize / 1000000
    #     file_downloaded = (file_size - (remaining / 1000000))
    #     progress_percentage = file_downloaded / file_size
    #     # my_bar = st.progress(progress_percentage, text=f"Descargando... {
    #     #     progress_percentage:.2%}")
    #     # for progreso in range(100):
    #     #     my_bar.progress(progreso + 1, text=f"Descargando... {
    #     #         progress_percentage:.2%}")
    #     my_bar = st.progress(0)
    #     for i in range(1, 101):
    #         my_bar.progress(i, text=f"Descargando... {
    #                         progress_percentage:.2%}")
    #     time.sleep(0.1)

    # @staticmethod
    # def onProgress(stream=None, chunk=None, remaining=None):
    #     file_size = stream.filesize / 1000000
    #     file_downloaded = (file_size - (remaining / 1000000))
    #     # progress_percentage = file_downloaded / file_size
    #     st.progress(file_downloaded / file_size,
    #                 text=f"Descargando... {file_downloaded / file_size:.2%}")

    @staticmethod
    def onProgress(stream=None, chunk=None, remaining=None):
        file_size = stream.filesize / 1000000
        file_downloaded = (file_size - (remaining / 1000000))
        # progress_percentage = file_downloaded / file_size
        st.progress(file_downloaded / file_size,
                    text=f"Descargando... {file_downloaded / file_size:.2%}")


#   st.button("Rerun")
if __name__ == "__main__":
    st.title("Youtube Downloader")
    url = st.text_input("Ingrese la URL del video")
    if url:
        downloader = YoutubeDownloader(url)
        downloader.showTitle()
        if downloader.stream:
            file_size = downloader.getFilesize()
            downloader.getPermissionToCOntinue(file_size)
