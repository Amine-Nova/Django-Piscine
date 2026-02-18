from django.shortcuts import render

# Create your views here.


def colors_shade(color):
    hexabase = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hex = '04'
    ff = 'ff'
    increment = 4
    steps = 50

    i = 0
    colors = []
    while(i < steps):
        indice = (hexabase.index(hex[1]) + increment)
        if (indice >= 16 and hex[0] != 'f'):
            hex = hexabase[hexabase.index(hex[0]) + 1] + hex[:1]
        hex = hex[:1] + hexabase[indice % 16]
        if (color == 'R'):
            colors.append("#" + ff + hex + hex)
        elif (color == 'G'):
            colors.append("#" + hex + ff + hex)
        elif (color == 'B'):
            colors.append("#" + hex + hex + ff)
        else:
            colors.append("#" + hex + hex + hex)
        i += 1
    return colors


def renderTemplate(request):
    red = colors_shade('R')
    green = colors_shade('G')
    blue = colors_shade('B')
    black = colors_shade('black')

    colors = zip(red, green, blue, black)
    return render(request, 'index.html', {"colors": colors})