
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


def get_html_table():
    return """ <table>
          <tr>
            <th>filename</th>
            <th>version / last modification date</th>
          </tr>
          <tr>
            <td>Miljöh</td>
            <td>Kiez</td>
          </tr>
          <tr>
            <td>Buletten</td>
            <td>Frikadellen</td>
          </tr>
        </table>"""


def get_html_last_part():
    return """</div></body></html>"""
