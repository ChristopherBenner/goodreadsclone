from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    categories = models.ManyToManyField(Category, related_name='books')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # cover = models.ImageField(upload_to='item_images', blank=True, null=True)
    # Author shouldn't be a foreign key as it limits the authors of books to only
    # Those who are site users -> still good to use foreign key for recipes (probably)
    author = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
    