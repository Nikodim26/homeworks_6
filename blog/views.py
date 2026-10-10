from django.views.generic import TemplateView, ListView

from blog.models import BlogEntry


# class EntrysView(TemplateView):
#
#     template_name = 'entrys.html'

class EntrysView(ListView):
    model = BlogEntry
    template_name = 'entrys.html'
    context_object_name = 'entrys'