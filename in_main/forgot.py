import tkinter
from tkinter import  messagebox
import sqlite3
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv
import os
import re
import pyzipper
import sys
import zipfile
import shutil

def new_password():
    psw_win = tkinter.Tk()
    psw_win['bg'] = 'gray6'
    psw_win.wm_attributes('-alpha', 1)
    psw_win.title("Смена Пароля")
    psw_win.geometry("525x375")
    psw_win.resizable(False, False)

    fon3 = tkinter.Label(psw_win, bg='gray8', pady=150, padx=245)
    fon3.place(relx=0, rely=0.07)

    user_login31 = tkinter.Label(psw_win, text='Введите свой Логин', bg='gray8', font=100, fg='dark violet')
    user_login31.place(relx=0, rely=0.12)

    user_login32 = tkinter.Entry(psw_win, bg='gray11', foreground='white', font=100)
    user_login32.place(relx=0.001, rely=0.2, relwidth=0.75)

    user_password31 = tkinter.Label(psw_win, text='Введите старый Пароль', bg='gray8', font=100, fg='dark violet')
    user_password31.place(relx=0, rely=0.34)

    user_password32 = tkinter.Entry(psw_win, bg='gray11', foreground='white', font=100, show="*")
    user_password32.place(relx=0.001, rely=0.42, relwidth=0.75)

    user_newpassword31 = tkinter.Label(psw_win, text='Придумайте новый Пароль', bg='gray8', font=100, fg='dark violet')
    user_newpassword31.place(relx=0, rely=0.62)

    user_newpassword32 = tkinter.Entry(psw_win, bg='gray11', foreground='white', font=100, show="*")
    user_newpassword32.place(relx=0.001, rely=0.7, relwidth=0.75)

    def enc():
        load_dotenv(find_dotenv())
        k = os.getenv('K')
        kfernet = Fernet(k)

        with open('1not_user.db', 'rb') as f:
            data = f.read()

        encr = kfernet.encrypt(data)

        with open('1not_user.db', 'wb') as f:
            f.write(encr)

    def dec():
        load_dotenv(find_dotenv())
        k = os.getenv('K')
        kfernet = Fernet(k)

        with open('1not_user.db', 'rb') as f:
            data = f.read()

        decr = kfernet.decrypt(data)

        with open('1not_user.db', 'wb') as f:
            f.write(decr)

    def deleted1():
        psw_win.destroy()

    def repswd():
        loog = "'" + user_login32.get() + "'"
        paas = "'" + user_password32.get() + "'"
        newpaas = "'" + user_newpassword32.get() + "'"

        dec()

        db = sqlite3.connect('1not_user.db')

        cursor = db.cursor()

        request = bool(cursor.execute(f'''SELECT * 
            FROM users
            WHERE col2 = {loog} 
            AND col3 = {paas} 
            ''').fetchall())
        if not request:
            messagebox.showerror(title='Смена пароля', message='Ой. Неправильно введён Логин и/или Пароль.')

            enc()

            db.commit()
            db.close()
            return

        if len(newpaas) < 8:
            messagebox.showwarning(title='Смена пароля', message='Новый Пароль должен содержать от 8 символов.')
            enc()
            return
        if not re.search("[a-z]", newpaas):
            messagebox.showwarning("Смена пароля", "Новый Пароль должен содержать хотя бы 1 прописную латинскую букву.")
            enc()
            return
        if not re.search("[A-Z]", newpaas):
            messagebox.showwarning("Смена пароля", "Новый Пароль должен содержать хотя бы 1 строчную латинскую букву.")
            enc()
            return
        if not re.search("[0-9]", newpaas):
            messagebox.showwarning("Смена пароля", "Новый Пароль должен содержать хотя бы 1 цифру.")
            enc()
            return


        log = user_login32.get()
        pas = user_password32.get()
        newpas = user_newpassword32.get()

        pd = "./Changing/"
        pd0 = pd + log


        zipl = log + ".zip"
        cur_wor_dir = os.getcwd()

        load_dotenv(find_dotenv())
        kk = os.getenv('KK')
        kkfernet = Fernet(kk)


        with open(zipl, 'rb') as f:
            data = f.read()

        decr = kkfernet.decrypt(data)

        with open(zipl, 'wb') as f:
            f.write(decr)


        if not os.path.exists(pd):
            os.mkdir(pd)

        if not os.path.exists(pd0):
            os.mkdir(pd0)


        with pyzipper.AESZipFile(zipl) as zf:
            zf.extractall(path=pd0, pwd=bytes(pas, 'utf-8'))


        def zip_folder_pyzipper(folder_path, output_path):
            parent_folder = os.path.dirname(folder_path)
            contents = os.walk(folder_path)
            try:
                zip_file = pyzipper.AESZipFile(zipl, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES)
                zip_file.pwd = bytes(newpas, 'utf-8')
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

        os.mkdir("./" + log)
        os.remove("./" + zipl)
        te_di = os.path.join(os.getcwd(), log)

        if not os.path.exists(pd0):
            for dir_name in os.listdir(pd0):
                if os.path.isdir(os.path.join(pd0, dir_name)):
                    shutil.move("./" + dir_name, te_di)

            for file_name in os.listdir(pd0):
                if os.path.isfile(os.path.join(pd0, file_name)):
                    shutil.move("./" + file_name, te_di)

        else:
            os.chdir(pd)
            os.chdir("./" + log)

            for dir_name in os.listdir(os.getcwd()):
                if os.path.isdir(os.path.join(os.getcwd(), dir_name)):
                    shutil.move("./" + dir_name, te_di)

            for file_name in os.listdir(os.getcwd()):
                if os.path.isfile(os.path.join(os.getcwd(), file_name)):
                    shutil.move("./" + file_name, te_di)

            os.chdir(cur_wor_dir)
            shutil.rmtree("./Changing/" + log)


        os.chdir(cur_wor_dir)

        se_di = os.path.join(te_di, log)

        zip_folder_pyzipper(folder_path=se_di, output_path=cur_wor_dir)
        shutil.rmtree(te_di)

        with open(zipl, 'rb') as f1:
            data1 = f1.read()

        encr1 = kkfernet.encrypt(data1)

        with open(zipl, 'wb') as f1:
            f1.write(encr1)


        cursor.execute(f'UPDATE users SET col3={newpaas} WHERE col2={loog}')

        db.commit()

        enc()

        db.commit()
        db.close()

        messagebox.showinfo(title='Смена пароля', message='Пароль был успешно сменён.')

        deleted1()

    b_t_n = tkinter.Button(psw_win, text="Потвердить", font=100, fg='dark violet', bg='gray11', command=repswd)
    b_t_n.place(relx=0.001, rely=0.82)

    b_t_n1 = tkinter.Button(psw_win, text="Отменить", font=100, fg='dark violet', bg='gray11', command=deleted1)
    b_t_n1.place(relx=0.25, rely=0.82)

    psw_win.mainloop()

