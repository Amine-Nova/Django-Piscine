def cssopen():
    fcss = open("periodic_table.css", 'w')
    css = """   .main {
        display: flex;
        width: 2160px;
        flex-direction: row;
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
        width: 120px;
        display: flex;
        flex-direction: column;
        margin: 0;
      }
      .wrapper2 {
        border: 1px solid rgba(0, 0, 0, 0);
        width: 120px;
        display: flex;
        flex-direction: column;
        margin: 0;
      }
      .p1 {
        font-size: 15px;
        align-items: flex-start;
        margin: 2px;
      }
      .molar {
        text-align: center;
        margin: 0;
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
    number, name, sign, molar = [], [], [], []
    f = open("periodic_table.html", 'w')
    cssopen()
    f2 = open("periodic_table.txt")
    for line in f2:
        line = line.strip()
        part = line.split(',')
        name.append(get_item(part[0], "=", 0))
        number.append(get_item(part[1], ":", 1))
        sign.append(get_item(part[2], ":", 1))
        molar.append(get_item(part[3], ":", 1))

    line1 = [number[0]] + [""] * 16 + [number[1]]
    line2 = number[2:4] + [""] * 10 + number[4:10] 
    line3 = number[10:12] + [""] * 10 + number[12:18] 
    line4 = number[18:36]
    line5 = number[36:54]
    line6 = number[54:56] + [""] + number[56:71]
    line7 = number[71:73] + [""] + number[73:88]
    lines = [line1, line2, line3, line4, line5, line6, line7]
    red_numbers = {1,2,3,4,11,12,19,20,37,38,55,56,87,88}
    blue_ranges = [(21,30), (39,48), (71,80), (103,112)]
    html = """<!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Periodic Table</title>
     <link rel="stylesheet" href="periodic_table.css">
 </head>
 <body>
 """
    for l in lines:
        html += """\t<div class="main">\n"""
        for i in l:
            if int(number[0]) in red_numbers:
                color = "#f57171"
            elif any(start <= int(number[0]) <= end for start, end in blue_ranges):
                color = "#7199f5"
            else:
                color = "#f5f571"
            if i == "":
                html += """\t<div class="wrapper2"></div>\n"""
            else:
                html += f"""\t<div class="wrapper" style="background-color: {color};">
          <p class="p1">{number[0]}</p>
          <p class="p2">{sign[0]}</p>
          <h4>{name[0]}</h4>
          <p class="molar">{molar[0]}</p>
        </div>\n"""
                del number[0]
                del sign[0]
                del name[0]
                del molar[0]

        html += """\t</div>\n"""
    html+= """</body>\n </html>"""
    f.write(html)

if __name__ == "__main__":
    file()
# please remember tomorrow to set the data to not use soo much html