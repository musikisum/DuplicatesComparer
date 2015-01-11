__author__ = 'Ulrich Kaiser'

import os
import datetime


def writeinfos(path):

    filelist = os.listdir(path)
    print("Dateien im Verzeichnis:", path)
    print("-----------------------------")
    print("\n".join(filelist))
    print("")
    print("====================================================================")
    print("")
    print("")
    for file in filelist:
        filename = os.path.join(path, file)
        props = os.stat(filename)
        print(file)
        print("-----------------------------")
        print("Protection Bits:", props[0])
        print("Inode-Nummer:", props[1])
        print("Anzahl der Hardlinks:", props[3])
        print("Größe des Objekts in Bytes:", props[6])
        print("Zeitstempel des letzten Zugriffs auf das Objekt (atime):", adate(filename))
        print("Zeitstempel der letzten Änderung des Objekts (mtime):", mdate(filename))
        print("Zeitstempel der letzten Änderung der Metadaten des Objekts (ctime):", cdate(filename))
        print("")
        print("====================================================================")
        print("")


def adate(filename):
    t = os.path.getatime(filename)
    return datetime.datetime.fromtimestamp(t).strftime("%d.%m.%y - %H:%M")

def mdate(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).strftime("%d.%m.%y - %H:%M")

def cdate(filename):
    t = os.path.getctime(filename)
    return datetime.datetime.fromtimestamp(t).strftime("%d.%m.%y - %H:%M")


