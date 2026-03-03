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
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(e)
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()
            return HttpResponse('OK!')
        

######################################################################################################################

def insert_data2(request):
    row = ["The Phantom Menace", 1, "George Lucas", "Rick McCallum", datetime.date(1999, 5, 19)]
    row2 = ["Attack of the Clones", 2, "George Lucas", "Rick McCallum", datetime.date(2002, 5, 16)]
    row3 = ["Revenge of the Sith", 3, "George Lucas", "Rick McCallum", datetime.date(2002, 5, 19)]
    row4 = ["A New Hope", 4, "George Lucas", "Gary Kurtz, Rick McCallum", datetime.date(1977, 5, 25)]
    row5 = ["The Empire Strikes Back", 5, "Irvin Kershner", "Gary Kurtz, Rick McCallum", datetime.date(1980, 5, 17)]
    row6 = ["Return of the Jedi", 6, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", datetime.date(1983, 5, 25)]
    row7 = ["The Force Awakens", 7, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", datetime.date(2015, 12, 11)]
    rows = [row, row2, row3, row4, row5, row6, row7]
    try:
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        for row in rows:
            cursor.execute("""INSERT INTO ex02_movies ( title, episode_nb, director, producer, release_date ) \
                            VALUES (%s, %s, %s, %s, %s)""", (
                                row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4]
                            ))
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(e)
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()
            return HttpResponse('OK!')
        

def display_data(request):
    try:
        html = ""
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM ex02_movies;")
        rows = cursor.fetchall()
        print(rows[0])

        html += """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL TABLE</title>
</head>
<body>
    <table>
        <tr>
          <th>title</th>
          <th>episode_nb</th>
          <th>director</th>
          <th>producer</th>
          <th>release_date</th>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table> 
</body>
</html>

"""
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(e)
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()
            return HttpResponse(html)