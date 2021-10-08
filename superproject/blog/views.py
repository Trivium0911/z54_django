from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post


PAGE_SIZE = 50


class OwnerMixin:
    def get_queryset(self):
        k = super().get_queryset().filter(author=self.request.user)
        return k

class BlogMixin:
    fields = ["title", "content", "hidden"]
    model = Post
    success_url = reverse_lazy("blog:all")



class AllPostsView(BlogMixin, ListView):
    def get_queryset(self):
        return super().get_queryset().filter(hidden=False).order_by("pk")[:PAGE_SIZE]



class SinglePostsView(LoginRequiredMixin,BlogMixin,DetailView):
    pass

class CreatePostView(LoginRequiredMixin,BlogMixin, CreateView):
    fields = ["title", "content", "hidden"]

    def form_valid(self, form):

        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin,BlogMixin,OwnerMixin,UpdateView):
    pass

class DeletePostView(LoginRequiredMixin,BlogMixin,OwnerMixin,DeleteView):
    pass


