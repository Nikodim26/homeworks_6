from django.urls import path
from django.views.generic import RedirectView

from blog.apps import BlogConfig
from blog.views import EntrysView, EntryDetail

app_name = BlogConfig.name

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='blog:entrys', permanent=False), name='root'),
    path('entrys/', EntrysView.as_view(), name='entrys'),
    path('entry/<int:pk>/', EntryDetail.as_view(), name='entry'),

]

