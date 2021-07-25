from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse


class Muscle(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', default='')

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', default='')
    description = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='workout_pics',
                              default='default.jpg', blank=True)
    video = models.CharField(max_length=500, default='', blank=True)
    sets = models.CharField(max_length=100, default='', blank=True)
    rep_range = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100, default='', blank=True)
    target = models.ForeignKey(Muscle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('detail', kwargs={
            'slug': self.slug,
        }
        )
