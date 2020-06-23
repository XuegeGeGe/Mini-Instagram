from annoying.decorators import ajax_request
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.forms import InstaUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Insta.models import InstaUser, Post, Like


class HelloWorld(TemplateView):
    template_name = 'HelloWorld.html'


class PostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "index.html"
    login_url = 'login'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    login_url = "login"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ['title', 'image']
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']
    login_url = "login"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('posts')
    login_url = "login"


class SignUpView(CreateView):
    form_class = InstaUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = InstaUser
    template_name = "user_detail.html"
    login_url = "login"


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
