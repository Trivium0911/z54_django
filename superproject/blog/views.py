from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post


class AllPostsView(ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(hidden=False)

class SinglePostsView(DetailView):
    model = Post

class CreatePostView(CreateView):
    fields = "__all__"
    model = Post

class UpdatePostView(UpdateView):
    fields = "__all__"
    model = Post

class DeletePostView(DeleteView):
    fields = "__all__"
    model = Post
    success_url = "/blog/"



