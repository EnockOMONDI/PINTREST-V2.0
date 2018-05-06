from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=70)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)
    image_name = models.CharField(max_length=25)
    image_description = models.TextField(max_length='140')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
