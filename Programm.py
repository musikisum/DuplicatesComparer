__author__ = 'Ulrich Kaiser'

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


def get_html_firts_part(folders):
    return """<!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title>Duplicates Comparer</title>
             <style>
                table, tr, td {
                    border: 1px solid black;
                    padding: 1em;
                    margin-left: 5%;
                 }
                 body {
                    background-color: gray;
                 }
                 h1 {
                    color:maroon;
                    font-size: 3em;
                 }
                 h2 {
                    color:maroon;
                    font-size: 1.5em;
                 }
                 #container{
                    width: 60%;
                    margin-left: auto;
                    margin-right: auto;
                    background-color: white;
                    padding: 1em 2em;"
                 }
                 #info {
                    padding-left: 20%;
                    background-color:white;
                    padding: 1em;
                 }
                 #folderinfo {
                    padding-left: 5%;
                 }
            </style>
        </head>
        <body>
            <div id="container">
                <div id="info">
                    <h1>File Information Tool</h1>
                    <div id="folderinfo">
                        <h2>compared folders</h2>""" + format_folders(folders) + """</div></div>"""


def format_folders(folders):
    snippet = "<p>"
    for folder in folders:
        snippet += folder
        snippet += "<br/>"
    snippet += "</p>"
    return snippet


def get_html_table(dic):
    str_arr = ["""<table><tr><th>filename</th><th>version / installation path</th></tr>"""]
    keys = sorted(dic.keys())
    for key in keys:
        str_arr.append("""<tr>""")
        str_arr.append("""<td>""")
        str_arr.append(key)
        str_arr.append("""</td>""")
        str_arr.append("""<td>""")
        valuelist = dic[key]
        index = 0
        oldValue = ""
        for value in valuelist:
            if index == 0 or oldValue == value[1]:
                str_arr.append("""<span style="color: green; font-weight:bold;">""")
            else:
                str_arr.append("""<span style="color: red; font-weight:bold;">""")
            str_arr.append(value[1] + " - " + value[0])
            str_arr.append("""</span>""")
            str_arr.append("""<br/>""")
            index += 1
            oldValue = value[1]
        str_arr.append("""</td>""")
        str_arr.append("""</tr>""")
    str_arr.append("""</table>""")
    return "".join(str_arr)


def get_html_last_part():
    return """</div></body></html>"""


def main():
    dic = get_file_comparison_table(read_folders_from_file())
    html_file = open("result.html", "w", encoding="UTF-8-sig")
    html_file.write(get_html_firts_part(read_folders_from_file())
                    + get_html_table(dic)
                    + get_html_last_part())
    html_file.close()

if __name__ == "__main__":
    main()