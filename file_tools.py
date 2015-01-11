import os
import win32api


def get_file_comparison_table(directories):
    file_table = {}
    for directory in directories:
        fill_file_info_dictionary(file_table, directory)
    return file_table


def get_version(file_path):
    try:
        info = win32api.GetFileVersionInfo(file_path, "\\")
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]
        version = "%d.%d.%d.%d" % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    except:
        version = "0.0.0.0"
    return version


def fill_file_info_dictionary(dictionary, path):
    filelist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in filelist:
        filename = os.path.join(path, file)
        if file not in dictionary:
            dictionary[file] = []
        info_tuple = (path, get_version(filename))
        dictionary[file] = sorted(dictionary[file] + [info_tuple], key=lambda item: item[1])


path1 = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop\\VSTPlugins 64 bit")
path2 = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop\\VSTPlugins")
paths = [path1, path2]
table = get_file_comparison_table(paths)
print(table)





