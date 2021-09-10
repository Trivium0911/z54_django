
from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path


def hello_world(request: HttpRequest):
    x = str(request.headers)
    return HttpResponse(x)


urlpatterns = [
    path('admin/', admin.site.urls),
path('hw/', hello_world),
]
####