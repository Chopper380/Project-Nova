#import pathlib
from pathlib import Path
import os
import shutil
import pyminizip
#import zipfile
import pyzipper
#from zipfile import ZipFile
import sqlite3
import tkinter
from tkinter import messagebox



root1 = tkinter.Tk()

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

    fon1 = tkinter.Label(frame1,bg = 'gray8', pady=138, padx=165)
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
        log = user_login21.get()
        pas = user_password21.get()
        repas = repassword2.get()

        if repas != pas:
            messagebox.showinfo(title='Регистрация', message='Ой. Вы не правильно повторили пароль.')
            return

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
            messagebox.showinfo(title='Регистрация',message='Ой. Учётная запись с таким логином уже существует, попробуйте другой.')
            db.close()

        db.commit()

        #cursor.execute("DROP TABLE users")

        db.close()

        pyminizip.compress('1test.TXT', None, log + '.zip', pas, 5)

        messagebox.showinfo(title='Регистрация', message='Учётная запись успешно добавленна.')

    logging1 = tkinter.Button(frame1, text='Добавить учётную запись', command=register, fg = 'dark violet', bg = 'gray11', font = 90)
    logging1.place(relx=0, rely=0.66)

    registration.mainloop()

root1['bg'] = 'gray6'
root1.title('Проект Нова')
root1.wm_attributes('-alpha', 1)
root1.geometry('725x600')

root1.resizable (False, False)

frame = tkinter.Frame(root1, bg = 'gray6')
frame.place(relwidth = 1, relheight = 1)

#greeting = tkinter.Label(frame, text = 'Добро пожаловать', bg = 'gray6', font = '200', fg = 'dark violet')
#greeting.place(relx = 0, rely = 0.05)

title2 = tkinter.Label(frame, text = 'Введите свой Логин и Пароль', bg = 'gray8', font = 100, fg = 'white')
title2.place(relx = 0, rely = 0.1)

fon = tkinter.Label(frame,bg = 'gray8', pady=100, padx=165)
fon.place(relx = 0, rely = 0.15)

user_login1 = tkinter.Label(frame, text = 'Логин', bg = 'gray8', font = 100, fg = 'dark violet')
user_login1.place(relx = 0, rely = 0.2)

user_login2 = tkinter.Entry (frame, bg = 'gray11', foreground = 'white', font = 100)
user_login2.place(relx = 0.001, rely = 0.25, relwidth = 0.3)

user_password1 = tkinter.Label(frame, text = 'Пароль', bg = 'gray8', font = 40, fg = 'dark violet')
user_password1.place(relx = 0, rely = 0.35)

user_password2 = tkinter.Entry (frame, bg = 'gray11', foreground = 'white', font = 100, show= "*")
user_password2.place(relx = 0.001, rely = 0.4, relwidth = 0.3)

if_pannel0 = tkinter.Label(frame, bg = 'gray8',pady=23, padx=130)
if_pannel0.place(relx = 0, rely = 0.57)

if_pannel1 = tkinter.Label(frame, text = 'Если у вас отсутствует аккаунт, то', bg = 'gray8', font = 100, fg = 'white')
if_pannel1.place(relx = 0, rely = 0.57)

def main_window():
    log = user_login2.get()
    pas = user_password2.get()
    log2 = "'" + log + "'"
    pas2 = "'" + pas + "'"


    db = sqlite3.connect('1not_user.db')

    cursor = db.cursor()

    request = bool(cursor.execute(f'SELECT * FROM users WHERE col2 = {log2} AND col3 = {pas2}').fetchall())

    if  not request:
        messagebox.showinfo(title='Авторизация',message='Ой. Неправильно введён Логин или Пароль.')
        return

    db.close()

    parent_dir = "./Temp"
    parent_dir1 = parent_dir + "/"
    parent_dir2 = parent_dir1 + log
    path = os.path.join(parent_dir, log)

    if not os.path.exists(parent_dir2):
        os.mkdir(path)

    zipl = log + ".zip"

    with pyzipper.AESZipFile(zipl) as zf:
        #with zf.open("1test(dont delete).TXT","r", pwd= pas3):
        zf.extractall(path = parent_dir2, pwd = bytes(pas, 'utf-8'))



    main = tkinter.Tk()

    root1.destroy()

    main.grid_columnconfigure(1, weight=1)
    main.grid_rowconfigure(1, weight=1)

    main['bg'] = 'gray6'
    main.title('Проект Нова')
    main.wm_attributes('-alpha', 1)
    main.geometry("1200x800")
    main.resizable(False, False)

    messagebox.showinfo(title='Предупреждение', message='К сожалению, в данной версии отсутствует поддержка папок и русских букв, если хотите, можете использовать их на свой страх и риск.')

    #btn = tkinter.Button(main, text = "test", command= print).grid(row = 0, column = 12)

    pas3 = bytes(pas2,"utf-8")
    pas4 = bytes(pas, "utf-8")
    parent_dir3 = "./Temp" +"/" + log
    t = os.getcwd()
    t0 = os.path.join(t, "Temp", log)
    t1= os.walk(t0)
    t2 = str(t1)
    files = list(t2)

    def closing(event):
        os.remove("./" + zipl)

        #os.chdir("./Temp" )

        #zipa = zipfile.ZipFile(zipl, "w")
        #for root, dirs, files in os.walk(parent_dir3):
            #for file in files:
                #zipa.write(file)
        #zipa.close()

        def walk (path:Path):
            all_files = []
            for x in path.iterdir():
                if x.is_dir:
                    all_files.extend(walk(x))
                else:
                    all_files.append(x)
            return all_files



        pyminizip.compress_multiple(files,[], zipl, pas, 5)

        shutil.rmtree(parent_dir3)


    main.bind('<Destroy>', closing)

    main.mainloop()

loggingInSys = tkinter.Button (frame, text = 'Авторизация', command= main_window, fg = 'dark violet', bg = 'gray11', font = 90)
loggingInSys.place (relx = 0.001, rely = 0.45)

logging = tkinter.Button (frame, text = 'создайте учётную запись', command= registration_window, fg = 'dark violet', bg = 'gray11', font = 90)
logging.place (relx = 0.001, rely = 0.62)

root1.mainloop()