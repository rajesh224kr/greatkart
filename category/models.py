from django.urls import reverse
from django.db import models

# Create your models here.
class Category(models.Model):
         category_name = models.CharField(max_length=50, unique=True)
         slug = models.SlugField(max_length=50, unique=True)
         description = models.TextField()
         category_image = models.ImageField(upload_to = 'photos/categories', blank =True)
         
         class Meta:
                  verbose_name = 'category'
                  verbose_name_plural = 'categories'

         def get_url(self):
                  return reverse('products_by_category', args = [self.slug])
         def __str__(self):
                  return self.category_name