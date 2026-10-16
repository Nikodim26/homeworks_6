from django.urls import path
from django.views.generic import RedirectView

from blog.apps import BlogConfig
from blog.views import EntryDetailView, EntriesListView, EntryCreateView, EntryUpdateView, EntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='blog:entries', permanent=False), name='root'),
    path('entries/', EntriesListView.as_view(), name='entries'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry'),

    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),

]

