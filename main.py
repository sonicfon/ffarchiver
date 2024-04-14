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
sort = Sort()
observer = Observer()
observer.schedule(sort, folger_unfiltered, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()