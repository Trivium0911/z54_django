from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path, include
from task4.views import info


def hello_world(request: HttpRequest):
    x = str(request.headers)
    return HttpResponse(x)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', hello_world),
    path('task4/', include("task4.urls")),
    path ("blog/", include ("blog.urls")),
]


