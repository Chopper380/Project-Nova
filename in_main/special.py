import in_main
#import pathlib
#from pathlib import Path
import os
import sys
import shutil
import pyminizip
import zipfile
import pyzipper
#from zipfile import ZipFile
import sqlite3
import tkinter
from tkinter import messagebox, Listbox, StringVar, Variable, filedialog

import tkinter
from tkinter import Listbox


def specl_win():
    spcl_win = tkinter.Tk()
    spcl_win['bg'] = 'gray6'
    spcl_win.wm_attributes('-alpha', 1)
    spcl_win.title("Дополнительные способы скрытия файлов")
    spcl_win.geometry("900x600")
    spcl_win.resizable(False, False)

    fon111 = tkinter.Label(spcl_win, bg='gray8', pady=260, padx=430)
    fon111.place(relx=0, rely=0.05)

    name = tkinter.Label(spcl_win, text='Функции', bg='gray8', font=100, fg='white')
    name.place(relx=0.001, rely=0.06)

    razdelitel = tkinter.Label(spcl_win, text='____________', bg='gray8', font=100, fg='white')
    razdelitel.place(relx=0.001, rely=0.095)

    slesh11 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh11.place(relx=0.128, rely=0.05)
    slesh12 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh12.place(relx=0.128, rely=0.09)
    slesh13 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh13.place(relx=0.128, rely=0.13)
    slesh14 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh14.place(relx=0.128, rely=0.17)
    slesh15 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh15.place(relx=0.128, rely=0.21)
    slesh16 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh16.place(relx=0.128, rely=0.25)
    slesh17 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh17.place(relx=0.128, rely=0.29)
    slesh18 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh18.place(relx=0.128, rely=0.33)
    slesh19 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh19.place(relx=0.128, rely=0.37)
    slesh121 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh121.place(relx=0.128, rely=0.41)
    slesh122 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh122.place(relx=0.128, rely=0.45)
    slesh123 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh123.place(relx=0.128, rely=0.49)
    slesh124 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh124.place(relx=0.128, rely=0.53)
    slesh125 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh125.place(relx=0.128, rely=0.57)
    slesh126 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh126.place(relx=0.128, rely=0.61)
    slesh127 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh127.place(relx=0.128, rely=0.65)
    slesh128 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh128.place(relx=0.128, rely=0.69)
    slesh129 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh129.place(relx=0.128, rely=0.73)
    slesh131 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh131.place(relx=0.128, rely=0.77)
    slesh132 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh132.place(relx=0.128, rely=0.81)
    slesh133 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh133.place(relx=0.128, rely=0.85)
    slesh134 = tkinter.Label(spcl_win, text='|', bg='gray8', font=100, fg='white')
    slesh134.place(relx=0.128, rely=0.89)

    text = tkinter.Text(spcl_win, height=27, width=80, bg='gray11', font=100, fg='white')
    text.place(relx=0.14, rely=0.06)

    aaaa = os.getcwd()

    def cancel():
        os.chdir(aaaa)
        spcl_win.destroy()

    def invsb_frm():
        text.delete('1.0', 'end')
        opis1 = """Название: Полностью невидемая папка

        Краткое описание: 
        Даннная папка работает как обычная, однако, найти её случайному пользователю будет 
        крайне трудно.

        Как создать самому: 
        Откройте свойства папки. В разделе 'Общее' поставте галочку напротив пункта 'Скрытый'. 
        А в разделе 'Настройки' выбрать 'Сменить значок'  и в открывшемся окне найти и выбрать 
        любой значок без картинки (если не сработает, попробуйте другой).
        Закройте окно. Выберете фкнкцию 'Переименовать', удалите имя, зажмите клавишу 'Alt' и с
        цифровой панели клавиаутуры (если её нет использу те встроенну цифровую панель) введите
        комбинацию 0160. Нажмите 'Enter'.
        Переместите папку в нужный каталог. В настройках каталога 'Тип' выключите отображение
        типа файла, размера файла и дату изменения.
        """
        text.insert('1.0', opis1)


        def path_finder():
            path = os.getcwd()
            a = 0
            while a == 0:
                path = os.path.abspath(path)
                if os.path.exists(os.path.join(path, os.path.join("./Addition", "\xa0"))):
                    path = os.path.join(path, os.path.join("./Addition", "\xa0"))
                    a += 1
                    return path
                else:
                    continue

        #path_path = path_finder()
        #print(path_path)

        def ok():
            cho_nor_dir = filedialog.askdirectory(title="Выберете Папку, в которую вы хотите добавить Скрытую папку")
            shutil.copytree(os.path.join("./Addition", "\xa0"),
                            cho_nor_dir, dirs_exist_ok=True)

            messagebox.showinfo(title="Скрытая папка", message='Скрытая папка была успешно добавлена. Для '
                                                               'дополнитнльного скрытия этой папки вы можете октлючить в'
                                                               ' настройках каталога отображение типа файла, размера '
                                                               'файла и дату изменения.')

        os.chdir(aaaa)
        btn_.config(command=ok)

    def coding():
        pass

    bt_n = tkinter.Button(spcl_win, text="Нев. папка", font=100, fg='dark violet', bg='gray11', command=invsb_frm)
    bt_n.place(relx=0.001, rely=0.15)

    bt_n1 = tkinter.Button(spcl_win, text="Скрыть файл", font=100, fg='dark violet', bg='gray11', command=coding)
    bt_n1.place(relx=0.001, rely=0.21)

    btn_ = tkinter.Button(spcl_win, text="Потвердить", font=100, fg='dark violet', bg='gray11')
    btn_.place(relx=0.14, rely=0.89)

    btn_1 = tkinter.Button(spcl_win, text="Отмена", font=100, fg='dark violet', bg='gray11', command=cancel)
    btn_1.place(relx=0.27, rely=0.89)

    spcl_win.mainloop()


