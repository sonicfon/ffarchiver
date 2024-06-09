import zipfile
from tkinter import *
from watchdog.observers import Observer
import pathlib
from pathlib import Path
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import os
import time
mode = 0
root = Tk()
folger_unfiltered = 'C:/Users/Flyers3/Desktop/ls/sorttest/unfiltered'
folger_images = 'C:/Users/Flyers3/Desktop/ls/sorttest/images'
folger_video = 'C:/Users/Flyers3/Desktop/ls/sorttest/video'
folger_audio = 'C:/Users/Flyers3/Desktop/ls/sorttest/audio'
folger_doc = 'C:/Users/Flyers3/Desktop/ls/sorttest/doc'
folger_misc = 'C:/Users/Flyers3/Desktop/ls/sorttest/misc'
e = Entry(root)
e.grid(row = 4, column = 0)
myLabel = Label(root, text="1 - Отслеживание папки")
myLabel2 = Label(root, text="2 - Архивирование папки")

myLabel.grid(row=0, column=0, padx=50, pady=100)
myLabel2.grid(row=1, column=0, padx=50, pady=100)
def myClick():
    myLabel1 = Label(root, text="Выбран режим отслеживания")
    global mode
    mode = 1
    MyLabel2 = Label(root, text="Отслеживание началось")
    myLabel1.grid(row=0, column=0, padx=50, pady=100)
    MyLabel2.grid(row=1, column=0, padx=50, pady=100)
    myLabel3 = Label(root, text="путь:"+e.get())
    myLabel3.grid(row=5, column=0, padx=50, pady=100)
myButton = Button(root, text="Отслеживание папки", command=myClick)
myButton2 = Button(root, text="Архивирование папки")
myButton.grid(row=2, column=0)
myButton2.grid(row=3, column=0)

root.mainloop()
i = -1


class Sort(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folger_unfiltered):
            ext = filename.split(".")
            if len(ext) > 1 and (ext[i].lower() == 'jpg' or ext[i].lower() == 'png' or ext[i].lower() == 'svg' or ext[
                i].lower() == 'jpeg' or ext[i].lower() == 'gif'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_images + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'mp4' or ext[i].lower() == 'webm' or ext[i].lower() == 'avi' or ext[
                i].lower() == 'mkv' or ext[i].lower() == 'mp4'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_video + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'mp3' or ext[i].lower() == 'opus' or ext[i].lower() == 'ogg' or ext[
                i].lower() == 'm4a' or ext[i].lower() == 'wav' or ext[i].lower() == 'flac' or ext[i].lower() == 'dsf' or
                    ext[i].lower() == 'dff'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_audio + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'doc' or ext[i].lower() == 'docx' or ext[i].lower() == 'pdf' or ext[
                i].lower() == 'odt'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_doc + "/" + filename
                os.rename(file, new_path)
            else:
                file = folger_unfiltered + "/" + filename
                new_path = folger_misc + "/" + filename
                os.rename(file, new_path)


BASE_DIR = Path(__file__).resolve().parent.parent

# folger_images = f'{pathlib.Path().resolve()}'
# folger_audio = f'{pathlib.Path().resolve()}'
# folger_video = f'{pathlib.Path().resolve()}'
# folger_doc = f'{pathlib.Path().resolve()}'
# folger_misc = f'{pathlib.Path().resolve()}'
# folger_unfiltered = BASE_DIR
print("1 - Отслеживание папки")
print("2 - Архивирование папки")
if mode == 1:
    sort = Sort()
    observer = Observer()
    observer.schedule(sort, folger_unfiltered, recursive=True)
    observer.start()
    print("Отслеживание началось. ")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        print("Отслеживание закончилось")
elif mode == 2:
    name = str(input("Имя файла: "))
    zip_file = zipfile.ZipFile(name + ".zip", "w")
    print("Создание архива в " + f'{Path(__file__).resolve().parent.parent}')
    for root, dirs, files in os.walk('sorttest'):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()
    print("Архив готов")
else:
    print("Ошибка ввода режима.")
    exit(0)
print("Удалить файлы после архивации? 1-Да/любая цифра-Нет")
delfile = int(input(":"))
# if delfile == 1:
# for filename in os.listdir(folger_doc, folger_misc, folger_audio ,folger_video,folger_images,folger_unfiltered):
#    os.remove(folger_images,folger_unfiltered,folger_doc,folger_misc,folger_audio,folger_video)
if delfile == 2:
    print("Exit")
    exit(0)
