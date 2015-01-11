import os


def fill_file_info_dictionary(dictionary, path):
    filelist = os.listdir(path)
    for file in filelist:
        filename = os.path.join(path, file)
        props = os.stat(filename)
        if file not in dictionary:
            dictionary[file] = []
        dictionary[file] += [(filename, props)]



dict = {}
dllPath = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop\\VSTPlugins 64 bit")
fill_file_info_dictionary(dict, dllPath)
print(dict)





