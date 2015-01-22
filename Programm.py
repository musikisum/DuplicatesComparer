__author__ = 'Ulrich Kaiser'

import file_tools
import html_tools

def main():
    table = file_tools.get_file_comparison_table(file_tools.read_folders_from_file())
    html_file = open("result.html", "w", encoding="UTF-8-sig")
    html_file.write(html_tools.get_html_firts_part(file_tools.read_folders_from_file()) + html_tools.get_html_table() + html_tools.get_html_last_part())
    html_file.close()

if __name__ == "__main__":
    main()