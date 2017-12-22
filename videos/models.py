from django.core.urlresolvers import reverse
from django.db import models


class Videos(models.Model):
    video_name = models.CharField(max_length=250)
    video_desc = models.CharField(max_length=250)
    video_file = models.FileField()

    # redirect
    def get_absolute_url(self):
        return reverse('gala:video', kwargs={'pk': self.pk})

