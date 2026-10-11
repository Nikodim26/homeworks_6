from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogEntry


class EntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'entry.html'
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class EntriesListView(ListView):
    model = BlogEntry
    template_name = "entries.html"
    context_object_name = "entries"

    def get_queryset(self):
        return BlogEntry.objects.filter(publication=True)

# CUD

class EntryCreateView(CreateView):
    model = BlogEntry
    fields = ['name', 'content', 'preview', 'created_at', 'publication']
    template_name = 'create_form.html'
    success_url = reverse_lazy("blog:entries")


class EntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['name', 'content', 'preview', 'created_at']
    template_name = 'create_form.html'
    success_url = reverse_lazy("blog:entries")

    def get_success_url(self):
        return self.object.get_absolute_url()


class EntryDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'delete_form.html'
    success_url = reverse_lazy("blog:entries")
