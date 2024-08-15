import pytube
import streamlit as st


class YoutubeDownloader:
    def __init__(self, url):
        self.url = url
        # self.youtube = pytube.YouTube(self.url)
        self.youtube = pytube.YouTube(
            self.url, on_progress_callback=self.onProgress)
        self.stream = None

    def showTitle(self):
        st.write(f"**Titulo: ** {self.youtube.title}")
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
        # return self.stream.filesize

    def getPermissionToCOntinue(self, file_size):
        st.write(f"**Titulo: ** {self.youtube.title}")
        st.write(f"**Autor: ** {self.youtube.author}")
        st.write(f"**Tamaño del archivo: ** {file_size:.2f} MB")
        st.write(f"**Resolución: ** {self.stream.resolution or 'N/A'}")
        st.write(f"**FPS: ** {getattr(self.stream, 'fps', 'N/A')}")

        if st.button("Descargar"):
            self.download()

    def download(self):
        self.stream.download()
        st.succes("Descarga completada")

    @staticmethod
    def onProgress(stream=None, chunk=None, remaining=None):
        file_size = stream.filesize / 1000000
        file_downloaded = file_size - (remaining / 1000000)
        # percentage = (file_downloaded / file_size) * 100
        st.progress(file_downloaded / file_size)


if __name__ == "__main__":
    st.title("Youtube Downloader")
    url = st.text_input("Ingrese la URL del video")
    if url:
        downloader = YoutubeDownloader(url)
        downloader.showTitle()
        if downloader.stream:
            file_size = downloader.getFilesize()
            downloader.getPermissionToCOntinue(file_size)
