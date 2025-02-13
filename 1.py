import shutil
from operator import truediv

from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv
import os
from in_main import *

def enc():
    load_dotenv(find_dotenv())
    k = os.getenv('KK')
    kfernet = Fernet(k)

    with open('1not_user.db', 'rb') as f:
        data = f.read()

    encr = kfernet.encrypt(data)

    with open('1not_user.db', 'wb') as f:
        f.write(encr)

def dec():
    load_dotenv(find_dotenv())
    k = os.getenv('KK')
    kfernet = Fernet(k)

    with open('as.zip', 'rb') as f:
        data = f.read()

    decr = kfernet.decrypt(data)

    with open('as.zip', 'wb') as f:
        f.write(decr)



os.chdir(r"C:\Users\Chopper\PycharmProjects\Project Nova")