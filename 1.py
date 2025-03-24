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

    with open('test2.zip', 'rb') as f:
        data = f.read()

    encr = kfernet.encrypt(data)

    with open('test2.zip', 'wb') as f:
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


temp_or_temp = filedialog.askopenfilename(title="Выберете Изображение, в которое вы хотите добавить Архив")
a = os.path.basename(temp_or_temp)
print(a)
