from .models import Videos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'video/index.html'
    context_object_name = 'all_video'

    def get_queryset(self):
        return Videos.objects.all()
