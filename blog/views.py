from django.views.generic import ListView, DetailView

from blog.models import BlogEntry


class EntryDetail(DetailView):
    model = BlogEntry
    template_name = 'entry.html'
    context_object_name = 'entry'

class EntrysView(ListView):
    model = BlogEntry
    template_name = 'entrys.html'
    context_object_name = 'entrys'

# CRUD