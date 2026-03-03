from django.http import HttpResponse
# Create your views here.
import psycopg2

def create_table0(request):
    try:
        connect = psycopg2.connect(dbname='djangotraining', user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ex00_movies( title VARCHAR(64) NOT NULL UNIQUE, \
                        episode_nb INTEGER PRIMARY KEY, \
                        opening_crawl TEXT, \
                        director VARCHAR(32) NOT NULL, \
                        producer VARCHAR(128) NOT NULL, \
                        release_date DATE NOT NULL );")
    except (Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(e)
    finally:
        if connect:
            connect.commit()
            cursor.close()
            connect.close()
            return HttpResponse('OK!')


