from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path
from task4.views import view
from task4.views import task4
def hello_world(request: HttpRequest):
    x = str(request.headers)
    return HttpResponse(x)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', hello_world),
    path('task', view),
    path('task4/', task4)

]
