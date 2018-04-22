from django.http import HttpResponse


def index(request):
    return HttpResponse("This is my new Home page.")


def hello(resquest, name):
    return HttpResponse(f"Hello {name}")
