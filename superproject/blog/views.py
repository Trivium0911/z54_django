from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post



class BlogMixin:
    fields = ["title", "content", "hidden"]
    model = Post
    success_url = reverse_lazy("blog:all")

class AllPostsView(BlogMixin, ListView):
    def get_queryset(self):
        return super().get_queryset().filter(hidden=False)

    def get_queryset(self):
        return self.model.objects.filter(hidden=False)

class SinglePostsView(LoginRequiredMixin,BlogMixin,DetailView):
    pass

class CreatePostView(LoginRequiredMixin,BlogMixin, CreateView):
    fields = ["title", "content", "hidden"]

    def form_valid(self, form):

        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin,BlogMixin,UpdateView):
    pass

class DeletePostView(LoginRequiredMixin,BlogMixin,DeleteView):
    pass


