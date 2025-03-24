import time

import in_main
#import pathlib
#from pathlib import Path
import os
import sys
import shutil
import subprocess
from subprocess import Popen
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
            a = 0
            path = os.getcwd()
            while a == 0:
                path = os.path.abspath(os.path.join(path, os.pardir))
                if os.path.exists(os.path.join(path, os.path.join("./Addition", "\xa0"))):
                    path = os.path.join(path, "./Addition")
                    a += 1
                    return path
                else:
                    continue



        def ok():
            path = path_finder()
            cho_nor_dir = filedialog.askdirectory(title="Выберете Папку, в которую вы хотите добавить Скрытую папку")
            shutil.copytree(path, cho_nor_dir, dirs_exist_ok=True)

            messagebox.showinfo(title="Скрытая папка", message='Скрытая папка была успешно добавлена. Для '
                                                               'дополнитнльного скрытия этой папки вы можете октлючить в'
                                                               ' настройках каталога отображение типа файла, размера '
                                                               'файла и дату изменения.')

        os.chdir(aaaa)
        btn_.config(command=ok)

    def coding():
        text.delete('1.0', 'end')
        opis1 = """Название: Стенография изображения

                Краткое описание: 
                Создаёт архив, в котром вы храните свои файлы, и прячет его в изображении. Для 
                доступа к архиву, нужно открыть с помощью стороннего приложения (по типу WinRAR).
                
                Как создать самому: 
                Создайте архив, в который нужно поместить нужные файлы. Поместите архив и 
                выбранноеизображение в одну директорию. Здесь же создайте текстовый файл со 
                следующим текстом: copy /b [имя изображения] + [имя архива] [имя нового 
                изображения]. Измените формат текстового файла на 'bat'. Активируйте его.
                """
        text.insert('1.0', opis1)



        def ok():
            temp_temp = filedialog.askdirectory(title="Выберете Папку, в которую вы хотите добавить Архив")


            def path_finder():
                a = 0
                path1 = os.getcwd()
                while a == 0:
                    path1 = os.path.abspath(os.path.join(path1, os.pardir))
                    if os.path.exists(os.path.join(path1, os.path.join("./Addition_2", "Put_your_files_here.zip"))):
                        path1 = os.path.join(os.path.join(path1, "./Addition_2"), "Put_your_files_here.zip")
                        a += 1
                        return path1
                    else:
                        continue


            path = path_finder()
            shutil.copy(path, temp_temp)
            messagebox.showinfo(title="Стенография", message='Добавьте нужные файлы в Архив (не переименуйте его)')
            messagebox.showinfo(title="Стенография", message='При выборе Изображения, убедитесь, что в его имени '
                                                             'отсутствуют пробелы')

            temp_or_temp = filedialog.askopenfilename(title="Выберете Изображение, в которое вы хотите добавить Архив")
            shutil.copy(temp_or_temp, temp_temp)


            def path_finder1():
                a = 0
                path2 = os.getcwd()
                while a == 0:
                    path2 = os.path.abspath(os.path.join(path2, os.pardir))
                    if os.path.exists(os.path.join(path2, os.path.join("./Addition_2", "File_to_turn_into_bat.TXT"))):
                        path2 = os.path.join(os.path.join(path2, "./Addition_2"), "File_to_turn_into_bat.TXT")
                        a += 1
                        return path2
                    else:
                        continue


            path3 = path_finder1()
            shutil.copy(path3, temp_temp)

            f = open(os.path.join(temp_temp, "File_to_turn_into_bat.TXT"), "w")
            file_name = os.path.basename(temp_or_temp)

            f.write("copy /b " + file_name + " + Put_your_files_here.zip Your_new_image.jpg")
            f.close()
            os.rename(os.path.join(temp_temp, "File_to_turn_into_bat.TXT"), os.path.join(temp_temp,
                                                                                         "File_to_turn_into_bat.bat"))

            #time.sleep(3)
            cmd = os.path.join(temp_temp, "File_to_turn_into_bat.bat")
            os.system(cmd)


            messagebox.showinfo(title="Стенография", message="Откройте ранее выбранную папку и активируйте "
                                                             "'File_to_turn_into_bat.bat' и ТОЛЬКО после этого жмите "
                                                             "'Ок'")
            os.remove(os.path.join(temp_temp, "File_to_turn_into_bat.bat"))
            os.remove(os.path.join(temp_temp, "Put_your_files_here.zip"))
            os.remove(os.path.join(temp_temp, file_name))

            messagebox.showinfo(title="Стенография", message='Скрытие архива было успешно завершенно')

        os.chdir(aaaa)
        btn_.config(command=ok)

    bt_n = tkinter.Button(spcl_win, text="Нев. папка", font=100, fg='dark violet', bg='gray11', command=invsb_frm)
    bt_n.place(relx=0.001, rely=0.15)

    bt_n1 = tkinter.Button(spcl_win, text="Скрыть файл", font=100, fg='dark violet', bg='gray11', command=coding)
    bt_n1.place(relx=0.001, rely=0.21)

    btn_ = tkinter.Button(spcl_win, text="Потвердить", font=100, fg='dark violet', bg='gray11')
    btn_.place(relx=0.14, rely=0.89)

    btn_1 = tkinter.Button(spcl_win, text="Отмена", font=100, fg='dark violet', bg='gray11', command=cancel)
    btn_1.place(relx=0.27, rely=0.89)

    spcl_win.mainloop()


