from django.shortcuts import render
from .models import People, Planets, Movies
from django.http import HttpResponse

# Create your views here.
def form_fields(request):
    if request.method == "POST":
        gender = request.POST.get('genders')
        min = request.POST.get('minimum')
        max = request.POST.get('maximum')
        diameter = request.POST.get('diameter')
        if gender and min and max and diameter:
            names = []
            to_rem = []
            movies = []
            diameters = []
            final = []
            g = People.objects.filter(gender=gender)
            for people in g.values_list():
                names.append([people[1], people[8], people[3]])
            for name in names:
                movie = Movies.objects.filter(characters__name=name[0], release_date__range=(min, max))
                dia = Planets.objects.filter(name=name[1], diameter__gt=diameter)
                title = list(movie.values_list('title', flat=True))
                if len(title) > 0 and len(dia) > 0:
                    movies.append(list(movie.values_list('title', flat=True)))
                    print(movies)
                    diameters.append(list(dia.values_list('diameter', flat=True))[0])
                else:
                    to_rem.append(name)
            names = [x for x in names if x not in to_rem]

            for name, mov, diam in zip(names, movies, diameters):
                final.append([name[0], name[1], name[2], " | ".join(mov), diam])
            return render(request, "display.html", {"data": final})
        else:
            return HttpResponse("No Data Available!")
    else:
        data = People.objects.all().values_list('gender').distinct()
        if len(data) == 0:
            return HttpResponse("No Data Available!")
        genders = []
        for d in data:
            genders.append(d)
        return render(request, "index.html", { 'genders': genders })
