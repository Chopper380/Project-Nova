from cryptography.fernet import Fernet
import in_main
import cryptography
import os
import sys
import shutil
import sqlite3
import pyminizip
import pyzipper
import zipfile
import tkinter
from tkinter import messagebox, Listbox, StringVar, filedialog
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
k = os.getenv('K')
kk = os.getenv('KK')

kfernet = Fernet(k)


with open('11.zip', 'rb') as f:
    data = f.read()

decr = kfernet.decrypt(data)

with open('11.zip', 'wb') as f:
    f.write(decr)