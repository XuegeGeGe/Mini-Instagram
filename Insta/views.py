from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Insta.models import Post


class HelloWorld(TemplateView):
    template_name = 'HelloWorld.html'


class PostsView(ListView, LoginRequiredMixin):
    model = Post
    template_name = "index.html"


class PostDetailView(DetailView, LoginRequiredMixin):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = "post_update.html"
    fields = ['title']


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('posts')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')
