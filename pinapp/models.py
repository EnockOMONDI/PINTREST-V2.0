from django.db import models

# Create your models here.
'''
class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)
    image_name = models.CharField(max_length=25)
    image_description = models.TextField(max_length='140')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    '''
