"""
Para poner en focus o top la ventana de descarga:
    -https://github.com/python-eel/Eel/issues/395
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
        # TODO: no use "on_progress_callback=on_progress" muestra una barra pero en la consola. con este adornador muestra la barra en la web
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

        if st.button("Seleccionar carpeta de descarga"):
            rutaDescarga = self.select_Folder()
            st.warning(f"Destino:   {rutaDescarga}")
            # st.session_state.folder_path = selected_folder_path
            if rutaDescarga:
                self.download(rutaDescarga)

    def select_Folder(self):

        root = tk.Tk()
        # Prueba para foco root.lift()
        root.withdraw()
        root.wm_attributes("-topmost", True)
        folder_path = filedialog.askdirectory(
            parent=root, title="Elige una carpeta de descarga")
        root.destroy()
        return folder_path

    def download(self, ruta):

        print("Descargando, para verlo en consola...")
        self.stream.download(output_path=ruta)
        st.success("Descarga completada")
        print("Descarga completada, para verlo en consola...")

    @staticmethod
    def onProgress(stream=None, chunks=None, remaining=None):

        file_size = stream.filesize / 1000000
        file_downloaded = file_size - (remaining / 1000000)
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
            pesoArchivo = downloader.getFilesize()
            downloader.getPermissionToCOntinue(pesoArchivo)
