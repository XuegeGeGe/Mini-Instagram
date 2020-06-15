from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from Insta.models import Post


class HelloWorld(TemplateView):
    template_name = 'HelloWorld.html'


class PostsView(ListView):
    model = Post
    template_name = "index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"
