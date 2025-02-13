import pyminizip
import sqlite3
import os
import tkinter
from tkinter import messagebox
from dotenv import load_dotenv, find_dotenv
import cryptography
from cryptography.fernet import Fernet
import re

def registration_window():

    registration = tkinter.Tk()

    registration['bg'] = 'gray6'
    registration.title('Регистрация')
    registration.wm_attributes('-alpha', 1)
    registration.geometry('350x500')

    registration.resizable(False, False)

    frame1 = tkinter.Frame(registration, bg='gray6')
    frame1.place(relwidth=1, relheight=1)

    title21 = tkinter.Label(frame1, text='Придумайте свой Логин и Пароль', bg='gray6', font=100, fg='white')
    title21.place(relx=0, rely=0.03)

    fon1 = tkinter.Label(frame1,bg = 'gray8', pady=138, padx=150)
    fon1.place(relx = 0, rely = 0.15)

    user_login11 = tkinter.Label(frame1, text='Логин', bg='gray8', font=100, fg='dark violet')
    user_login11.place(relx=0, rely=0.18)

    user_login21 = tkinter.Entry(frame1,bg = 'gray11', foreground = 'white', font = 100)
    user_login21.place(relx=0.001, rely=0.24, relwidth=0.7)

    user_password11 = tkinter.Label(frame1, text='Пароль', bg='gray8', font=100, fg='dark violet')
    user_password11.place(relx=0, rely=0.36)

    user_password21 = tkinter.Entry(frame1, bg = 'gray11', foreground = 'white', font = 100, show= "*")
    user_password21.place(relx=0.001, rely=0.42, relwidth=0.7)

    repassword1 = tkinter.Label(frame1, text = 'Повторите пароль', bg='gray8', font=100, fg='dark violet')
    repassword1.place(relx = 0, rely = 0.54)

    repassword2 = tkinter.Entry(frame1, bg = 'gray11', foreground = 'white', font = 100, show= "*")
    repassword2.place(relx = 0.001, rely = 0.6, relwidth=0.7)


    def register():
        load_dotenv(find_dotenv())
        k = os.getenv('K')
        kk = os.getenv('KK')

        kfernet = Fernet(k)
        kkfernet = Fernet(kk)

        log = user_login21.get()
        pas = user_password21.get()
        repas = repassword2.get()

        if len(pas) < 8:
            messagebox.showwarning(title='Регистрация', message='Пароль должен содержать от 8 символов.')
            return
        if not re.search("[a-z]", pas):
            messagebox.showwarning("Регистрация", "Пароль должен содержать хотя бы 1 прописную латинскую букву.")
            return
        if not re.search("[A-Z]", pas):
            messagebox.showwarning("Регистрация", "Пароль должен содержать хотя бы 1 строчную латинскую букву.")
            return
        if not re.search("[0-9]", pas):
            messagebox.showwarning("Регистрация", "Пароль должен содержать хотя бы 1 цифру.")
            return

        if repas != pas:
            messagebox.showinfo(title='Регистрация', message='Ой. Вы не правильно повторили пароль.')
            return


        if os.path.exists('1not_user.db'):
            with open('1not_user.db', 'rb') as f:
                data = f.read()

            decr = kfernet.decrypt(data)

            with open('1not_user.db', 'wb') as f:
                f.write(decr)


        db = sqlite3.connect('1not_user.db')

        cursor = db.cursor()

        col2, col3 = (log, pas)

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            col2 TEXT,
            col3 TEXT
        )''')

        cursor.execute('INSERT INTO users (col2, col3) VALUES (?, ?)',
                       (col2, col3))

        cursor.execute("SELECT * FROM users;")

        co = cursor.execute("SELECT col2 FROM users GROUP BY col2 HAVING COUNT(*) > 1").fetchall()

        log_log = "[('" + log + "',)]"
        log_list = [log_log]
        b = str(co)
        result = [b]

        if result == log_list:
            messagebox.showwarning(title='Регистрация',
                                message='Ой. Учётная запись с таким логином уже существует, попробуйте другой.')

            db.close()

            sqlite3.connect('1not_user.db')

            with open('1not_user.db', 'rb') as f:
                data = f.read()

            encr = kfernet.encrypt(data)

            with open('1not_user.db', 'wb') as f:
                f.write(encr)

            db.commit()

            db.close()



        db.commit()

        with open('1not_user.db', 'rb') as f:
            data = f.read()

        encr = kfernet.encrypt(data)

        with open('1not_user.db', 'wb') as f:
            f.write(encr)

        db.commit()

        db.close()

        pyminizip.compress('1test.TXT', None, log + '.zip', pas, 5)

        with open(log + '.zip', 'rb') as f:
            data = f.read()

        encr = kkfernet.encrypt(data)

        with open(log + '.zip', 'wb') as f:
            f.write(encr)

        messagebox.showinfo(title='Регистрация', message='Учётная запись успешно добавленна.')

    logging1 = tkinter.Button(frame1, text='Добавить учётную запись', command=register, fg = 'dark violet', bg = 'gray11', font = 90)
    logging1.place(relx=0, rely=0.66)

    registration.mainloop()
