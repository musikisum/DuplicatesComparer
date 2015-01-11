import os
import time


def get_file_comparison_table(directories):
    file_table = {}
    for directory in directories:
        fill_file_info_dictionary(file_table, directory)
    return file_table


def fill_file_info_dictionary(dictionary, path):
    filelist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in filelist:
        filename = os.path.join(path, file)
        props = os.stat(filename)
        if file not in dictionary:
            dictionary[file] = []
        dictionary[file] += [(path, time.ctime(props.st_ctime))]


path1 = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop\\VSTPlugins 64 bit")
path2 = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop\\VSTPlugins")
paths = [path1, path2]
table = get_file_comparison_table(paths)
print(table)





