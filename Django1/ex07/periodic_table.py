import sys

def cssopen():
    fcss = open("styles.css", 'w')
    css = """.main {
  display: flex;
  flex-direction: column;
  width: 1735px;
}
.main2 {
  display: flex;
  justify-content: space-between;
  width: 100%;
  display: flex;
  justify-content: space-between;
  width: 100%;
}
h4 {
  margin: 0;
  text-align: center;
}
.wrapper {
  border: 1px solid black;
  width: 95px;
  display: flex;
  flex-direction: column;
  margin: 0;
}
.p1 {
  font-size: 15px;
  align-items: flex-start;
  margin: 2px;
}
.p2 {
  text-align: center;
  font-size: 30px;
  margin: 10px;
}"""
    fcss.write(css)

def get_item(data, delimiter, num):
    var = data.split(delimiter)
    return var[num]



def file():
    number, name, sign = [], [], []
    f = open("amine.html", 'w')
    cssopen()
    f2 = open("periodic_table.txt")
    for line in f2:
        line = line.strip()
        part = line.split(',')
        name.append(get_item(part[0], "=", 0))
        number.append(get_item(part[1], ":", 1))
        sign.append(get_item(part[2], ":", 1))

    print(len(sign))
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
"""
    html += """ <div class="main">
    <div style="display: flex; justify-content: space-between; width: 100%">""" 
    i = 0
    while i < 2:
        html += f"""<div class="wrapper">
          <p class="p1">{number[i]}</p>
          <p class="p2">{sign[i]}</p>
          <h4>{name[i]}</h4>
        </div>""" 
        i += 1
    html += """</div>
    <div class="main2">
    <div style="display: flex">"""
    while i < 4:
        html += f"""<div class="wrapper">
          <p class="p1">{number[i]}</p>
          <p class="p2">{sign[i]}</p>
          <h4>{name[i]}</h4>
        </div>""" 
        i += 1
    html += """</div>
    <div style="display: flex">"""
    while i < 10:
        html += f"""<div class="wrapper">
          <p class="p1">{number[i]}</p>
          <p class="p2">{sign[i]}</p>
          <h4>{name[i]}</h4>
        </div>""" 
        i += 1
    html += """</div>"""
    f.write(html)

if __name__ == "__main__":
    file()
