from django.urls import path

from task4.views import view,  InfoView
from task4.views import ShowNumbersView


urlpatterns = [
    path('task/', view),
    path("shogun/", ShowNumbersView.as_view()),
    path ('info/' , InfoView.as_view()),
]
