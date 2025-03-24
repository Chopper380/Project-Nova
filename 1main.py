from cryptography.fernet import Fernet
import in_main
import cryptography
import re
import os
import sys
import shutil
import sqlite3
from subprocess import Popen
import pyminizip
import pyzipper
import zipfile
import tkinter
from tkinter import messagebox, Listbox, StringVar, filedialog
from dotenv import load_dotenv, find_dotenv


root1 = tkinter.Tk()
root1['bg'] = 'gray6'
root1.title('Проект Нова')
root1.wm_attributes('-alpha', 1)
root1.geometry('600x600')

root1.resizable (False, False)

frame = tkinter.Frame(root1, bg = 'gray6')
frame.place(relwidth = 1, relheight = 1)

title2 = tkinter.Label(frame, text = 'Введите свой Логин и Пароль', bg = 'gray8', font = 100, fg = 'white')
title2.place(relx = 0, rely = 0.1)

fon = tkinter.Label(frame,bg = 'gray8', pady=130, padx=180)
fon.place(relx = 0, rely = 0.15)

user_login1 = tkinter.Label(frame, text = 'Логин', bg = 'gray8', font = 100, fg = 'dark violet')
user_login1.place(relx = 0, rely = 0.2)

user_login2 = tkinter.Entry (frame, bg = 'gray11', foreground = 'white', font = 100)
user_login2.place(relx = 0.001, rely = 0.25, relwidth = 0.45)

user_password1 = tkinter.Label(frame, text = 'Пароль', bg = 'gray8', font = 40, fg = 'dark violet')
user_password1.place(relx = 0, rely = 0.35)

user_password2 = tkinter.Entry (frame, bg = 'gray11', foreground = 'white', font = 100, show= "*")
user_password2.place(relx = 0.001, rely = 0.4, relwidth = 0.45)

if_pannel0 = tkinter.Label(frame, bg = 'gray8',pady=23, padx=130)
if_pannel0.place(relx = 0, rely = 0.67)

if_pannel1 = tkinter.Label(frame, text = 'Если у вас отсутствует аккаунт, то', bg = 'gray8', font = 100, fg = 'white')
if_pannel1.place(relx = 0, rely = 0.67)


def main_window():
    log = user_login2.get()
    pas = user_password2.get()
    log2 = "'" + log + "'"
    pas2 = "'" + pas + "'"

    load_dotenv(find_dotenv())
    k = os.getenv('K')
    kk = os.getenv('KK')

    kfernet = Fernet(k)
    kkfernet = Fernet(kk)

    with open('1not_user.db', 'rb') as f:
        data = f.read()

    decr = kfernet.decrypt(data)

    with open('1not_user.db', 'wb') as f:
        f.write(decr)

    db = sqlite3.connect('1not_user.db')

    cursor = db.cursor()

    request = bool(cursor.execute(f'SELECT * FROM users WHERE col2 = {log2} AND col3 = {pas2}').fetchall())

    if not request:
        messagebox.showerror(title='Авторизация',message='Ой. Неправильно введён Логин и/или Пароль.')
        with open('1not_user.db', 'rb') as f:
            data = f.read()

        encr = kfernet.encrypt(data)

        with open('1not_user.db', 'wb') as f:
            f.write(encr)

        db.commit()
        db.close()
        return



    with open('1not_user.db', 'rb') as f:
        data = f.read()

    encr = kfernet.encrypt(data)

    with open('1not_user.db', 'wb') as f:
        f.write(encr)

    db.commit()

    db.close()

    parent_dir = "./Temp"
    parent_dir1 = parent_dir + "/"
    parent_dir2 = parent_dir1 + log
    pd = "./Check"
    pd1 ="./" + log

    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    if not os.path.exists(pd):
        os.mkdir(pd)

    zipl = log + ".zip"
    cur_wor_dir = os.getcwd()

    with open(zipl, 'rb') as f:
        data = f.read()

    decr = kkfernet.decrypt(data)

    with open(zipl, 'wb') as f:
        f.write(decr)

    with pyzipper.AESZipFile(zipl) as zf:
        zf.extractall(path = pd, pwd = bytes(pas, 'utf-8'))

    os.chdir("./Temp")
    temp_wor_dir = os.getcwd()

    main_cur_dir = os.path.join(temp_wor_dir, log)

    os.chdir(cur_wor_dir)

    os.chdir("./Check")
    last_wor_dir = os.getcwd()

    if os.path.exists(pd1):

        os.chdir(cur_wor_dir)
        os.mkdir(parent_dir2)
        os.chdir(last_wor_dir)

        os.chdir("./" + log)
        for dir_name in os.listdir(os.getcwd()):
            if os.path.isdir(os.path.join(os.getcwd(), dir_name)):
                shutil.move("./" + dir_name, temp_wor_dir + '/' + log)

        for file_name in os.listdir(os.getcwd()):
            if os.path.isfile(os.path.join(os.getcwd(), file_name)):
                shutil.move("./" + file_name, temp_wor_dir + '/' + log)

        os.chdir(last_wor_dir)
        shutil.rmtree("./" + log)
    else:
        os.chdir(cur_wor_dir)
        if not os.path.exists(parent_dir2):
            os.mkdir(parent_dir2)
        os.chdir(last_wor_dir)

        for dir_name in os.listdir(last_wor_dir):
            if os.path.isdir(os.path.join(last_wor_dir, dir_name)):
                shutil.move("./" + dir_name, temp_wor_dir + '/' + log)

        for file_name in os.listdir(last_wor_dir):
            if os.path.isfile(os.path.join(last_wor_dir, file_name)):
                shutil.move("./" + file_name, temp_wor_dir + '/' + log)

        os.chdir(cur_wor_dir)

    os.chdir(main_cur_dir)



    main = tkinter.Tk()

    root1.destroy()

    main['bg'] = 'gray6'
    main.title('Проект Нова')
    main.wm_attributes('-alpha', 1)
    main.geometry("1200x800")
    main.resizable(False, False)

    fon1 = tkinter.Label(main, bg='gray8', pady=296, padx=556)
    fon1.place(relx=0, rely=0.07)

    list1 = Listbox(main, font=100, fg='white', bg='gray11', highlightcolor="white", selectbackground="dark violet")
    list1.place(relx=0.13, rely=0.165, relwidth=0.8, relheight=0.67)



    def path_change(*event):
        list1.delete(0, 'end')
        os.getcwd()

        for file in os.listdir(os.getcwd()):
            list1.insert(0,file)


    def change_path_by_click(event):
        selection = list1.get(list1.curselection()[0])
        path = os.path.join(os.getcwd(), selection)

        if os.path.isfile(path):
            os.startfile(path)

        if os.path.isdir(path):
            os.chdir(path)
            current_path.set(path)


    def dir_creation():
        os.mkdir(os.path.join(os.getcwd(), "Папка"), dir_fd= None)
        path_change()


    def add_file():
        file_p = filedialog.askopenfilename(title='Выберете Файл, который хотите добавить')
        shutil.copy(file_p, os.getcwd())
        path_change()


    def add_dir():
        dir_p = filedialog.askdirectory(title='Выберете Папку, которую хотите добавить')
        shutil.copytree(dir_p, os.path.join(os.getcwd(), os.path.basename(os.path.normpath(dir_p))))
        path_change()


    def extr_data():
        dir_pp = filedialog.askdirectory(title='Выберете Папку, в которую хотите извлечь Файл или Папку')
        shutil.move(os.path.join( os.getcwd(), list1.get(list1.curselection()[0])), dir_pp)
        path_change()


    def rename():
        rename_window = tkinter.Toplevel(main)
        rename_window['bg'] = 'gray6'
        rename_window.wm_attributes('-alpha', 1)
        rename_window.title("Переименование")
        rename_window.geometry("600x200")
        rename_window.resizable(False, False)

        fon11 = tkinter.Label(rename_window, bg='gray8', pady=75, padx=290)
        fon11.place(relx=0, rely=0.07)

        name = tkinter.Label(rename_window, text='Ведите новое имя файла и его расширение', bg='gray8', font=100,
                                 fg='white')
        name.place(relx=0.001, rely=0.15)

        new_name = tkinter.Entry(rename_window, bg='gray11', foreground='white', font=100)
        new_name.place(relx=0.007, rely=0.28, relwidth=0.8, relheight=0.2)

        def re_n():
            os.rename(list1.get(list1.curselection()[0]), new_name.get())
            path_change()
            rename_window.destroy()

        bt_n = tkinter.Button(rename_window, text="Потвердить", font=100, fg='dark violet', bg='gray11',
                                  command=re_n)
        bt_n.place(relx=0.007, rely=0.55)

        def destroying():
            rename_window.destroy()

        bt_n = tkinter.Button(rename_window, text="Отменить", font=100, fg='dark violet', bg='gray11',
                                  command=destroying)
        bt_n.place(relx=0.2, rely=0.55)

        rename_window.mainloop()


    def move_data():
        move_win = tkinter.Toplevel(main)
        move_win['bg'] = 'gray6'
        move_win.wm_attributes('-alpha', 1)
        move_win.title("Перемещение")
        move_win.geometry("600x400")
        move_win.resizable(False, False)

        fon111 = tkinter.Label(move_win, bg='gray8', pady=160, padx=285)
        fon111.place(relx=0, rely=0.07)

        name11 = tkinter.Label(move_win, text='Переместить в архив выше', bg='gray8', font=100, fg='white')
        name11.place(relx=0.001, rely=0.15)

        up_dir = tkinter.Listbox(move_win, font=100, fg='white', bg='gray11', highlightcolor="white",
                                 selectbackground="dark violet", exportselection=0)
        up_dir.place(relx=0.001, rely=0.21, relwidth=0.8, relheight=0.2)

        name22 = tkinter.Label(move_win, text='Переместить в архив ниже', bg='gray8', font=100, fg='white')
        name22.place(relx=0.001, rely=0.48)

        down_dir = tkinter.Listbox(move_win, font=100, fg='white', bg='gray11', highlightcolor="white",
                                   selectbackground="dark violet", exportselection=0)
        down_dir.place(relx=0.001, rely=0.54, relwidth=0.8, relheight=0.2)

        def deleted():
            move_win.destroy()

        def checking():
            up_dir.delete(0, 'end')
            par = os.path.dirname(os.getcwd())
            if par != temp_wor_dir:
                parent = os.path.basename(os.path.normpath(os.path.dirname(os.getcwd())))
                up_dir.insert(0, parent)
            else:
                up_dir.insert(0, '')

            down_dir.delete(0, 'end')
            for directory in os.listdir(os.getcwd()):
                if os.path.isdir(os.path.join(os.getcwd(), directory)):
                    down_dir.insert(0, directory)

        con = list1.get(list1.curselection()[0])

        def start_updir(event):
            if not event.widget.curselection():
                return
            else:
                shutil.move(con, os.path.dirname(os.getcwd()))
                path_change()
                deleted()

        def start_downdir(event):
            if not event.widget.curselection():
                return
            else:
                shutil.move(con, os.path.join(os.getcwd(), down_dir.get(down_dir.curselection()[0])))
                path_change()
                deleted()

        checking()

        del_btn = tkinter.Button(move_win, text="Отменить", font=100, fg='dark violet', bg='gray11', command=deleted)
        del_btn.place(relx=0.005, rely=0.81)

        up_dir.bind("<<ListboxSelect>>", start_updir)
        down_dir.bind("<<ListboxSelect>>", start_downdir)

        move_win.mainloop()


    def deleting():
        con = list1.get(list1.curselection()[0])
        if os.path.isfile(con):
            os.remove(con)
        else:
            shutil.rmtree(con)
        path_change()


    def arc_crt():
        arc_win = tkinter.Toplevel(main)
        arc_win['bg'] = 'gray6'
        arc_win.wm_attributes('-alpha', 1)
        arc_win.title("Создание архива")
        arc_win.geometry("600x300")
        arc_win.resizable(False, False)

        fon111 = tkinter.Label(arc_win, bg='gray8', pady=120, padx=285)
        fon111.place(relx=0, rely=0.07)

        name = tkinter.Label(arc_win, text='Введите имя для архива (без расширения)', bg='gray8', font=100,
                                 fg='white')
        name.place(relx=0.001, rely=0.17)

        arc_name = tkinter.Entry(arc_win, bg='gray11', foreground='white', font=100)
        arc_name.place(relx=0.007, rely=0.28, relwidth=0.8, relheight=0.12)

        password = tkinter.Label(arc_win, text='Введите пароль для архива', bg='gray8', font=100, fg='white')
        password.place(relx=0.001, rely=0.52)

        arc_password = tkinter.Entry(arc_win, bg='gray11', foreground='white', font=100, show="*")
        arc_password.place(relx=0.007, rely=0.63, relwidth=0.8, relheight=0.12)


        def destroying1():
            arc_win.destroy()


        def arc_creation():
            arc_log = arc_name.get()
            arc_pas = arc_password.get()

            pyminizip.compress(os.path.join(cur_wor_dir, '1test.TXT'), None, arc_log + '.zip', arc_pas, 5)
            path_change()
            destroying1()

        bt_n = tkinter.Button(arc_win, text="Потвердить", font=100, fg='dark violet', bg='gray11',
                                  command=arc_creation)
        bt_n.place(relx=0.007, rely=0.8)

        bt_n = tkinter.Button(arc_win, text="Отменить", font=100, fg='dark violet', bg='gray11',
                                  command=destroying1)
        bt_n.place(relx=0.2, rely=0.8)

        arc_win.mainloop()


    def special_win():
        in_main.specl_win()



    def go_back():
        parent = os.path.dirname(os.getcwd())
        if parent != temp_wor_dir:
            current_path.set(parent)
            os.chdir(parent)
            path_change()
        else:
            return



    current_path = StringVar(main, name='current_path', value=main_cur_dir)

    current_path.trace('w', path_change)

    greting0 = tkinter.Label(main, text='Кнопоки', bg='gray8', font=100, fg='white')
    greting0.place(relx=0.001, rely=0.02)

    slesh1 = tkinter.Label(main, text='|', bg='gray8', font=100, fg='white')
    slesh1.place(relx=0.127, rely=0.13)

    slesh2 = tkinter.Label(main, text='|', bg='gray8', font=100, fg='white')
    slesh2.place(relx=0.127, rely=0.1)

    slesh3 = tkinter.Label(main, text='|', bg='gray8', font=100, fg='white')
    slesh3.place(relx=0.127, rely=0.07)

    slesh1 = tkinter.Label(main, text='|', bg='gray8', font=100, fg='white')
    slesh1.place(relx=0.127, rely=0.13)

    greting01 = tkinter.Label(main, text='Путь и меню', bg='gray8', font=100, fg='white')
    greting01.place(relx=0.135, rely=0.02)

    greting = tkinter.Label(main, text='Основные кнопки', bg='gray8', font=100, fg='white')
    greting.place(relx=0.001, rely=0.08)

    greting1 = tkinter.Label(main, text='(также на ПКМ)', bg='gray8', font=100, fg='white')
    #greting1.place(relx=0.001, rely=0.11)

    separator1 = tkinter.Label(main, bg='gray8', text = "_______________", font=100, fg='white')
    separator1.place(relx=0.005, rely=0.14)

    btn1 = tkinter.Button(main, text="Создать папку", font=100, fg='dark violet', bg = 'gray11', command=dir_creation)
    btn1.place(relx=0.001, rely=0.19)

    btn2 = tkinter.Button(main, text="Добавить файл", font=100, fg='dark violet', bg = 'gray11', command=add_file)
    btn2.place(relx=0.001, rely=0.24)

    btn9 = tkinter.Button(main, text="Добавить папку", font=100, fg='dark violet', bg='gray11', command=add_dir)
    btn9.place(relx=0.001, rely=0.29)

    btn10 = tkinter.Button(main, text="Извлечь", font=100, fg='dark violet', bg='gray11', command=extr_data)
    btn10.place(relx=0.001, rely=0.34)

    btn3 = tkinter.Button(main, text="Переименовать", font=100, fg='dark violet', bg = 'gray11', command=rename)
    btn3.place(relx=0.001, rely=0.39)

    btn4 = tkinter.Button(main, text="Переместить", font=100, fg='dark violet', bg = 'gray11', command=move_data)
    btn4.place(relx=0.001, rely=0.44)

    btn5 = tkinter.Button(main, text="Удалить файл", font=100, fg='dark violet', bg = 'gray11', command=deleting)
    btn5.place(relx=0.001, rely=0.49)

    btn7 = tkinter.Button(main, text="Сохдать архив", font=100, fg='dark violet', bg='gray11', command=arc_crt)
    btn7.place(relx=0.001, rely=0.6)

    separator2 = tkinter.Label(main, bg='gray8', text="_______________", font=100, fg='dark violet')
    separator2.place(relx=0.005, rely=0.64)

    btn8 = tkinter.Button(main, text="Специальне кнопки", font=100, fg='dark violet', bg='gray11',
                          command=special_win)
    btn8.place(relx=0.001, rely=0.686)

    btn6 = tkinter.Button(main, text="Назад", font=100, fg='dark violet', bg='gray11', command=go_back)
    btn6.place(relx=0.145, rely=0.123)

    path_en = tkinter.Entry(main,textvariable= current_path, bg = 'gray11', foreground = 'white', font = 100)
    path_en.place(relx=0.145, rely=0.078, relwidth = 0.77, relheight= 0.04)

    current_path.trace('w', path_change())



    def zip_folder_pyzipper(folder_path, output_path):
        parent_folder = os.path.dirname(folder_path)
        contents = os.walk(folder_path)
        try:
            zip_file = pyzipper.AESZipFile(zipl, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES)
            zip_file.pwd = bytes(pas, 'utf-8')
            for root, folders, files in contents:
                for folder_name in folders:
                    absolute_path = os.path.join(root, folder_name)
                    relative_path = absolute_path.replace(parent_folder + '\\',
                                                          '')
                    print("Adding '%s' to archive." % absolute_path)
                    zip_file.write(absolute_path, relative_path)
                for file_name1 in files:
                    absolute_path = os.path.join(root, file_name1)
                    relative_path = absolute_path.replace(parent_folder + '\\',
                                                          '')
                    print("Adding '%s' to archive." % absolute_path)
                    zip_file.write(absolute_path, relative_path)

            print("'%s' created successfully." % output_path)

        except IOError as message:
            print(message)
            sys.exit(1)
        except OSError as message:
            print(message)
            sys.exit(1)
        except zipfile.BadZipfile as message:
            print(message)
            sys.exit(1)
        finally:
            zip_file.close()

    parent_dir3 = "./Temp" + "/" + log

    def if_exit(event):
        if event.widget != main:
            return

        os.chdir(cur_wor_dir)
        os.remove("./" + zipl)

        os.chdir("./Temp/")
        zip_folder_pyzipper(folder_path= "./" + log, output_path= cur_wor_dir)
        os.chdir(cur_wor_dir)

        shutil.move("./Temp/" + zipl, cur_wor_dir)

        shutil.rmtree(parent_dir3)

        with open(zipl, 'rb') as f1:
            data1 = f1.read()

        encr1 = kkfernet.encrypt(data1)

        with open(zipl, 'wb') as f1:
            f1.write(encr1)


    main.bind('<Double-1>', change_path_by_click)

    main.bind('<Destroy>', if_exit)

    path_change('')
    main.mainloop()

loggingInSys = tkinter.Button (frame, text = 'Авторизация', command= main_window, fg = 'dark violet', bg = 'gray11',
                               font = 90)
loggingInSys.place (relx = 0.001, rely = 0.45)

forg_pas = tkinter.Button (frame, text = 'Сменить пароль', command= in_main.new_password, fg = 'dark violet', bg = 'gray11', font = 90)
forg_pas.place (relx = 0.001, rely = 0.55)

logging = tkinter.Button (frame, text = 'создайте учётную запись', command= in_main.registration_window,
                          fg = 'dark violet', bg = 'gray11', font = 90)
logging.place (relx = 0.001, rely = 0.72)

root1.mainloop()