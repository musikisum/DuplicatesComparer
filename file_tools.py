import os
import win32api


def read_folders_from_file():
    lines = open("paths.txt", "r", encoding="UTF-8-sig").readlines()
    return [line.rstrip() for line in lines]


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
        dictionary[file] = order_by_version(dictionary[file] + [info_tuple])


def order_by_version(tuples):
    tuples = sorted(tuples, key=lambda item: get_version_part(item[-1], 3), reverse=True)
    tuples = sorted(tuples, key=lambda item: get_version_part(item[-1], 2), reverse=True)
    tuples = sorted(tuples, key=lambda item: get_version_part(item[-1], 1), reverse=True)
    tuples = sorted(tuples, key=lambda item: get_version_part(item[-1], 0), reverse=True)
    return tuples


def get_version_part(version, index):
    parts = version.split('.')
    return int(parts[index]) if (0 <= index < len(parts)) else None




def main():
    table = get_file_comparison_table(read_folders_from_file())
    print(table)

if __name__ == "__main__":
    main()







