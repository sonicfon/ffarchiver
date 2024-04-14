import zipfile

from watchdog.observers import Observer
import pathlib
from pathlib import Path
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import os
import time

i = -1
class Sort(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folger_unfiltered):
            ext = filename.split(".")
            if len(ext) > 1 and (ext[i].lower() == 'jpg' or ext[i].lower() == 'png' or ext[i].lower() == 'svg' or ext[i].lower() == 'jpeg' or ext[i].lower() == 'gif'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_images + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'mp4' or ext[i].lower() == 'webm' or ext[i].lower() == 'avi' or ext[i].lower() == 'mkv' or ext[i].lower() == 'mp4'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_video + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'mp3' or ext[i].lower() == 'opus' or ext[i].lower() == 'ogg' or ext[i].lower() == 'm4a' or ext[i].lower() == 'wav' or ext[i].lower() == 'flac' or ext[i].lower() == 'dsf' or ext[i].lower() == 'dff'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_audio + "/" + filename
                os.rename(file, new_path)
            elif len(ext) > 1 and (
                    ext[i].lower() == 'doc' or ext[i].lower() == 'docx' or ext[i].lower() == 'pdf' or ext[i].lower() == 'odt'):
                file = folger_unfiltered + "/" + filename
                new_path = folger_doc + "/" + filename
                os.rename(file, new_path)
            else:
                file = folger_unfiltered + "/" + filename
                new_path = folger_misc + "/" + filename
                os.rename(file, new_path)

BASE_DIR = Path(__file__).resolve().parent.parent
folger_unfiltered = 'C:/Users/Flyers3/Desktop/ls/sorttest/unfiltered'
folger_images = 'C:/Users/Flyers3/Desktop/ls/sorttest/images'
folger_video = 'C:/Users/Flyers3/Desktop/ls/sorttest/video'
folger_audio = 'C:/Users/Flyers3/Desktop/ls/sorttest/audio'
folger_doc = 'C:/Users/Flyers3/Desktop/ls/sorttest/doc'
folger_misc = 'C:/Users/Flyers3/Desktop/ls/sorttest/misc'
#folger_images = f'{pathlib.Path().resolve()}'
#folger_audio = f'{pathlib.Path().resolve()}'
#folger_video = f'{pathlib.Path().resolve()}'
#folger_doc = f'{pathlib.Path().resolve()}'
#folger_misc = f'{pathlib.Path().resolve()}'
#folger_unfiltered = BASE_DIR
print("1 - Отслеживание папки")
print("2 - Архивирование папки")
mode = int(input("Режим: "))
if mode == 1:
    sort = Sort()
    observer = Observer()
    observer.schedule(sort, folger_unfiltered, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
elif mode == 2:
    name = str(input("Имя файла: "))
    zip_file = zipfile.ZipFile(name + ".zip", "w")
    print("Создание архива в " + f'{Path(__file__).resolve().parent.parent}')
    for root, dirs, files in os.walk('sorttest'):
            for file in files:
                zip_file.write(os.path.join(root , file))
    zip_file.close()
    print("Архив готов")
else:
    print("Ошибка ввода режима.")
    exit(0)
print("Удалить файлы после архивации? 1-Да/любая цифра-Нет")
delfile = int(input(":"))
#if delfile == 1:
   # for filename in os.listdir(folger_doc, folger_misc, folger_audio ,folger_video,folger_images,folger_unfiltered):
    #    os.remove(folger_images,folger_unfiltered,folger_doc,folger_misc,folger_audio,folger_video)
if delfile ==2:
    print("Exit")
    exit(0)
