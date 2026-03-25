from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def create_table8(request):
    try:
        success = False
        connect = psycopg2.connect(dbname="djangotraining", user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        success = True
        cursor.execute("CREATE TABLE ex08_planets ( id SERIAL PRIMARY KEY, \
                        name VARCHAR(64) NOT NULL UNIQUE, \
                        climate VARCHAR, \
                        diameter INT, \
                        orbital_period INT, \
                        population BIGINT, \
                        rotation_period INT, \
                        surface_water REAL, \
                        terrain VARCHAR(128)); \
                        CREATE TABLE ex08_people ( id SERIAL PRIMARY KEY, \
                        name VARCHAR(64) NOT NULL UNIQUE, \
                        birth_year VARCHAR(32), \
                        gender VARCHAR(32),\
                        eye_color VARCHAR(32), \
                        hair_color VARCHAR(32), \
                        height INT, \
                        mass REAL, \
                        homeworld VARCHAR(64),\
                        FOREIGN KEY (homeworld) REFERENCES ex08_planets(name));")
        return HttpResponse('OK!')
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if success:
            connect.commit()
            cursor.close()
            connect.close()


def copy_data8(request):
    try:
        success = False
        connect = psycopg2.connect(dbname="djangotraining", user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        success = True
        cursor.execute("COPY ex08_planets ( name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain ) FROM '/home/planets.csv' DELIMITER '	'  NULL 'NULL';")
        cursor.execute("COPY ex08_people ( name, birth_year, gender, eye_color, hair_color, height, mass, homeworld ) FROM '/home/people.csv' DELIMITER '	' NULL 'NULL';")
        return HttpResponse('OK!')
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if success:
            connect.commit()
            cursor.close()
            connect.close()

# for tomorrow try to access to planet data from the id fk maybe u will use SELECT climate FROM ex08_planets WICH id=the one from people u need

def display_data8(request):
    try:
        climate = []
        html = ""
        success = False
        connect = psycopg2.connect(dbname="djangotraining", user="djangouser", password="secret", host="localhost", port="5432")
        cursor = connect.cursor()
        success = True
        cursor.execute("SELECT name, homeworld FROM ex08_people;")
        people_data = list(cursor)
        if (len(people_data) == 0):
            raise Exception("No data available")
        people_data = sorted(people_data)
        for row in people_data:
            cursor.execute(f"SELECT climate FROM ex08_planets where name='{row[1]}';")
            data = cursor.fetchall()
            if data:
                climate.append(data[0][0])
            else:
                climate.append(None)
        if (len(climate) == 0):
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
  background-color: #FFFFFF;
}}</style>
</head>
<body style="background-color: #85ffe7;">
    <table>
        <tr>
          <th style="color:red;">People Name</th>
          <th style="color:green;">Homeworld</th>
          <th style="color:blue;">Climate</th>
        </tr>
        <tr>
           """

        for people, cli in zip(people_data, climate):
            html += ""f"<td>{people[0]}</td> \n\
           <td>{people[1]}</td> \n\
           <td>{cli}</td> \n\
        </tr> \n\
        <tr> \n           """
        html += """</table> 
</body>
</html>"""

        return HttpResponse(html)
    except ( Exception, psycopg2.OperationalError ) as e:
        return HttpResponse(str(e))
    finally:
        if success:
            connect.commit()
            cursor.close()
            connect.close()
