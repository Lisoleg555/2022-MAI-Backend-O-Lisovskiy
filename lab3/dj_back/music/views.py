from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    
    context ={
        "data":"test string",
    }
    return render(request, "index.html", context)

@csrf_exempt # разрешаем делать POST запрос без куки
def music(request):
    if request.method == "GET":
        id = request.GET.get("id", 0)
        name = request.GET.get("name", "Sandstorm")
        year = request.GET.get("year", 1993)
        return JsonResponse({"id": id, "name": name, "year": year})
    elif request.method == "POST":
        id = request.GET.get("id", 0)
        name = request.GET.get("name", "Sandstorm")
        year = request.GET.get("year", 1993)
        # TODO: Занести в базу данных
        return JsonResponse({"id": id, "name": name, "year": year})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")