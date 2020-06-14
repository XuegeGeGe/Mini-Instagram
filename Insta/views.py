from django.views.generic import TemplateView, ListView
from Insta.models import Post


class HelloWorld(TemplateView):
    template_name = 'HelloWorld.html'


class PostsView(ListView):
    model = Post
    template_name = "index.html"
