import sys
import re


def ret_value(text):
    data = {}
    f = open("settings.py").read().split("\n")
    for l in f:
        if not l or l.startswith("#"):
            continue
        if "=" in l:
            k, v = l.strip().split("=", 1)
            v = v.split("#")[0].strip()
            k = k.strip(" ")
            v = v.strip('"' + " ")
            data[k] = v
    if text in data:
        return data[text]


def get_title(file):
    index = file.find("<title>")
    end = file.find("</title>")
    if index != -1 or end != -1:
        return (index + 7, end)
    return None


def render():
    if len(sys.argv) == 2:
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
"""
        file = open(sys.argv[1], "r").read()
        data = re.findall("{[a-z]+}", file)
        for i in data:
            text = str(i.strip("{}"))
            value = ret_value(text)
            if i in file and value:
                file = file.replace(i, value)
        filehtml = open("myCv.html", "w+")
        start, end = get_title(file)
        if start != None and end != None:
            title = f"<title>{file[start:end]}</title>"
            title = title.strip("\n")
        file = file.replace(title, "").strip("\n")
        html += f"""\t\t{title}
</head>
  <body>
    {file}
  </body>
</html>
"""
        filehtml.write(html)


if __name__ == "__main__":
    render()
