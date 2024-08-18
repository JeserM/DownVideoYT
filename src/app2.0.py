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
        """
        Get permission to continue the download.

        Args:
            file_size (float): The size of the file in MB.
        """
        st.write(f"Titulo:  {self.youtube.title}")
        st.write(f"Autor:  {self.youtube.author}")
        st.write(f"Tamaño del archivo:  {file_size:.2f} MB")
        st.write(f"Resolución:  {self.stream.resolution or 'N/A'}")
        st.write(f"FPS:  {getattr(self.stream, 'fps', 'N/A')}")

        if st.button("Descargar"):
            self.download()

    def download(self):
        """
        Download the video.
        """
        print("Downloading...")
        download_path = self.select_download_path()
        # Specify the download path
        st.write(f"Descargando en:  {download_path}")
        self.stream.download(download_path)
        print(download_path)
        st.success("Descarga completada")

    def select_download_path(self):
        print("Selecciona carpeta, puede que este en segundo plano...")
        download_path = filedialog.askdirectory()
        # download_path = st.download_button(
        #     label="Selecciona carpeta destino", data=filedialog.askdirectory())
        print(download_path)
        return download_path

    # def download(self):
    #     self.download_path()
    #     self.stream.download()
    #     st.success("Descarga completada")

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
