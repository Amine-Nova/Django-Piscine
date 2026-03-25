from django.shortcuts import render, redirect
from .models import Movies
from django.http import HttpResponse
import datetime


# Create your views here.
def insert_data7(request):
    try:
        Movies.objects.bulk_create({
            Movies(title='The Phantom Menace', episode_nb=1, director='George Lucas', producer='Rick McCallum', release_date=datetime.date(1999, 5, 19)),
            Movies(title='Attack of the Clones', episode_nb=2, director='George Lucas', producer='Rick McCallum', release_date=datetime.date(2002, 5, 16)),
            Movies(title='Revenge of the Sith', episode_nb=3, director='George Lucas', producer='Rick McCallum', release_date=datetime.date(2002, 5, 19)),
            Movies(title='A New Hope', episode_nb=4, director='George Lucas', producer='Gary Kurtz, Rick McCallum', release_date=datetime.date(1977, 5, 25)),
            Movies(title='The Empire Strikes Back', episode_nb=5, director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date=datetime.date(1980, 5, 17)),
            Movies(title='Return of the Jedi', episode_nb=6, director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date=datetime.date(1983, 5, 25)),
            Movies(title='The Force Awakens', episode_nb=7, director='J. J. Abrams', producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date=datetime.date(2015, 12, 11)),
        }, ignore_conflicts=True)
        return HttpResponse('OK!')
    except ( Exception ) as e:
        return HttpResponse(str(e))
    

def display_data7(request):
    try:
        html = ""
        rows = Movies.objects.all().values()
        if (len(rows) == 0):
            raise Exception("No data available")
        html += f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL TABLE</title>
    <style>th,
td {{
  border: 1px solid rgb(160 160 160);
  padding: 8px 10px;
}}</style>
</head>
<body>
    <table>
        <tr>
          <th>title</th>
          <th>episode_nb</th>
          <th>opening_crawl</th>
          <th>director</th>
          <th>producer</th>
          <th>release_date</th>
          <th>created</th>
          <th>updated</th>
        </tr>
        <tr>
           """

        for row in rows:
            html += ""f"<td>{row['title']}</td> \n\
           <td>{row['episode_nb']}</td> \n\
           <td>{row['opening_crawl']}</td> \n\
           <td>{row['director']}</td> \n\
           <td>{row['producer']}</td> \n\
           <td>{row['release_date']}</td> \n\
           <td>{row['created']}</td> \n\
           <td>{row['updated']}</td> \n\
        </tr> \n\
        <tr> \n           """
        html += """</table> 
</body>
</html>"""
          

        return HttpResponse(html)
    except ( Exception ) as e:
        return HttpResponse(str(e))
    

def get_data2up7(request):
    try:
        data = Movies.objects.all().values()
        if (len(data) == 0):
            raise Exception("No data available")
        return render(request, "ex07/index.html", { "data": data })
    except ( Exception ) as e:
        return HttpResponse(str(e))


def update_data7(request):
    try:
        if request.method == "POST":
            opening_crawl = request.POST.get("opening_crawl")
            id = request.POST.get("movie")
            if id and opening_crawl:
                movie = Movies.objects.get(pk=id)
                movie.opening_crawl = opening_crawl
                movie.save()
                return redirect("/ex07/update")
            else:
                return HttpResponse("No Data Received!")
        else:
            return HttpResponse("ERROR!")
    except ( Exception ) as e:
        return HttpResponse(str(e))