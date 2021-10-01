from django.urls import path
from blog.views import AllPostsView, SinglePostsView, CreatePostView, UpdatePostView, DeletePostView

app_name = "blog"

urlpatterns = [

    path ("", AllPostsView.as_view(), name="all"),
    path("<int:pk>/", SinglePostsView.as_view(), name="single"),
    path("new/", CreatePostView.as_view(), name="new"),
    path("<int:pk>/update/", UpdatePostView.as_view(), name="update"),
    path("<int:pk>/delete/", DeletePostView.as_view(), name="delete"),

]
