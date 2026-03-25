from django.http import HttpResponse
from django.shortcuts import render
from .models import People, Planets

# Create your views here.
def display_data9(requets):
    try:
        html = ""
        people_data = People.objects.all().order_by('name')
        if len(people_data) == 0:
            html = "<p>No data available, please use the following command line before use:\
            <span style='color:red; font-weight: bold'>\"python3 manage.py load_data ex09/fixtures/ex09_initial_data.json\"\
            </span></p>"
            return HttpResponse(html)
        html += f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ORM TABLE</title>
    <style>th,
td {{
  border: 2px solid orange;
  padding: 8px 10px;
  background-color: #FFFFFF;
}}</style>
</head>
<body style="background-color: #909090;">
    <table style="border: 3px solid red; background-color: #ffff17;">
        <tr>
          <th style="color:red;">People Name</th>
          <th style="color:green;">HomeWorld</th>
          <th style="color:blue;">Climate</th>
        </tr>
        <tr>
           """
        for data in people_data:
            html += ""f"<td>{data.name}</td> \n           """
            if data.homeworld:
                html += ""f"<td>{data.homeworld}</td> \n\
           <td>{data.homeworld.climate}</td> \n\
        </tr> \n\
        <tr> \n           """
            else:
                html += ""f"<td>{None}</td> \n\
           <td>{None}</td> \n\
        </tr> \n\
        <tr> \n           """
        html += """</table> 
</body>
</html>"""
        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(str(e))