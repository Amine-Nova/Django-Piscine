import psycopg2
from django.http import HttpResponse
import datetime
# Create your views here.
def create_table2(request):
    try:
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ex02_movies( title VARCHAR(64) NOT NULL UNIQUE, \
                        episode_nb INTEGER PRIMARY KEY, \
                        opening_crawl TEXT, \
                        director VARCHAR(32) NOT NULL, \
                        producer VARCHAR(128) NOT NULL, \
                        release_date DATE NOT NULL );")
        return HttpResponse('OK!')
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()

        

######################################################################################################################

def insert_data2(request):
    try:
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        cursor.execute(""f"INSERT INTO ex02_movies ( title, episode_nb, director, producer, release_date ) \
                        VALUES \
                            ('The Phantom Menace', {1}, 'George Lucas', 'Rick McCallum', '{datetime.date(1999, 5, 19)}'), \
                            ('Attack of the Clones', {2}, 'George Lucas', 'Rick McCallum', '{datetime.date(2002, 5, 16)}'), \
                            ('Revenge of the Sith', {3}, 'George Lucas', 'Rick McCallum', '{datetime.date(2002, 5, 19)}'), \
                            ('A New Hope', {4}, 'George Lucas', 'Gary Kurtz, Rick McCallum', '{datetime.date(1977, 5, 25)}'), \
                            ('The Empire Strikes Back', {5}, 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '{datetime.date(1980, 5, 17)}'), \
                            ('Return of the Jedi', {6}, 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '{datetime.date(1983, 5, 25)}'), \
                            ('The Force Awakens', {7}, 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '{datetime.date(2015, 12, 11)}')""")
        return HttpResponse('OK!')
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()
        

######################################################################################################################


def display_data(request):
    try:
        html = ""
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM ex02_movies;")
        rows = cursor.fetchall()
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
        </tr>
        <tr>
           """

        for row in rows:
            html += ""f"<td>{row[0]}</td> \n\
           <td>{row[1]}</td> \n\
           <td>{row[2]}</td> \n\
           <td>{row[3]}</td> \n\
           <td>{row[4]}</td> \n\
           <td>{row[5]}</td> \n\
        </tr> \n\
        <tr> \n           """
        html += """</table> 
</body>
</html>"""
          

        return HttpResponse(html)
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()