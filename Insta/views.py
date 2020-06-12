from django.views.generic import TemplateView

class HelloWorld(TemplateView):
    template_name = 'HelloWorld.html'