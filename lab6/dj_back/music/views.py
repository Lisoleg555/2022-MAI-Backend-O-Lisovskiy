from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from music import models

# Create your views here.

def index(request):
    
    context ={
        "data":"test string",
    }
    return render(request, "index.html", context)

@csrf_exempt # разрешаем делать POST запрос без куки
def music(request):
    if request.method == "GET":
        id = request.GET.get("id", -1)
        
        try:
            if(id == -1):
                print('as')
                musics = models.Music.objects.all()
                return JsonResponse([{"id": music.id, "name": music.name,  "date of post": music.year} for music in musics],safe=False)
            music = models.Music.objects.get(id=id)
            return JsonResponse({"id": music.id, "name": music.name, "date of post": music.year})
        except models.Music.DoesNotExist:
            return JsonResponse({})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Field error"})
    elif request.method == "POST":
        name = request.GET.get("name", None)
        year = request.GET.get("year", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})
        try:

            music = models.Music()
            music.name = name
            music.year = year
            print(name,year)
            try:
                _ = models.Music.objects.get(name=name)
            except models.Music.DoesNotExist:
                music.save()
                return JsonResponse({"status": "OK"})
            except models.Music.MultipleObjectsReturned:
                pass
            return JsonResponse({"status": "Already exists"})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

@csrf_exempt # разрешаем делать POST запрос без куки
def author(request):
    if request.method == "GET":
        id = request.GET.get("id", -1)
        
        try:
            if(id == -1):
                print('as')
                authors = models.Author.objects.all()
                return JsonResponse([{"id": author.id, "name": author.name, "date of birth": author.year} for author in authors],safe=False)
            author = models.Author.objects.get(id=id)
            return JsonResponse({"id": author.id, "name": author.name, "date of birth": author.year})
        except models.Author.DoesNotExist:
            return JsonResponse({})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Field error"})
    elif request.method == "POST":
        name = request.GET.get("name", None)
        year = request.GET.get("year", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})
        try:

            author = models.Author()
            author.name = name
            author.year = year
            print(name,year)
            try:
                _ = models.Author.objects.get(name=name,year=year)
            except models.Author.DoesNotExist:
                author.save()
                return JsonResponse({"status": "OK"})
            except models.Author.MultipleObjectsReturned:
                pass
            return JsonResponse({"status": "Already exists"})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")