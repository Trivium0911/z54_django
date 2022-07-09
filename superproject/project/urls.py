from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpRequest
from django.urls import path, include

from project.views import SignUpView
from task4.views import info


def hello_world(request: HttpRequest):
    x = str(request.headers)
    return HttpResponse(x)


urlpatterns = [
        path('admin/', admin.site.urls),
        path('hw/', hello_world),
        path('task4/', include("task4.urls")),
        path("blog/", include ("blog.urls")),
        path("signup/", SignUpView.as_view(), name='signup'),
        path("login/", LoginView.as_view(), name='login'),
        path("logout/", LogoutView.as_view(), name='logout')
]


