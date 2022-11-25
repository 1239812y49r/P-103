import sys
import time
import random
import os
import shutil
import logging
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 

from_dir = "C:\Users\52558\OneDrive\Documents"

class FileEventHandler (FileSystemEventHandler):
    def on_created(self,event):
        print("Se ha creado el archivo")

    def on_modified(self,event):
        print("se ha modificado el archivo")

    def on_moved(self,event):
        print("Se ha movido el archivo")

    def on_deleted(self,event):
        print("Se ha eliminado el archivo")

m = FileEventHandler()

observer = Observer()
observer.schedule(m,from_dir,recursive = True)
observer.start()

try:
    while True:
        print("Corriendo...")
        time.sleep(2)
except KeyboardInterrupt: 
    print("Detubido")
    observer.stop()  