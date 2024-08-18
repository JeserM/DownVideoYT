import streamlit


import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
# from pytubefix.cli import on_progress
import streamlit as st
import streamlit.web.cli as stcli
import os
import sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app3.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
