from django.urls import path
from blog.views import AllPostsView, SinglePostsView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [

    path ("", AllPostsView.as_view(), name = "all posts"),
    path("<int:pk>/", SinglePostsView.as_view()),
    path("new/", CreatePostView.as_view()),
    path("<int:pk>/update/", UpdatePostView.as_view()),
    path("<int:pk>/delete/", DeletePostView.as_view()),

]
