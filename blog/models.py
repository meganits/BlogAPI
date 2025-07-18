from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=20,
                            choices=[('draft','Draft'),('published','Published')],default='draft')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True, max_length=200)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title