from django.db import models
from django.forms import ModelForm

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField()
    category_slug = models.CharField(max_length=200,default=1)
    category_image = models.FileField(default='media/Screenshot_from_2020-06-13_19-49-07.png')


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Paint(models.Model):
    paint_name=models.CharField (max_length=30)
    description=models.CharField (max_length=50)
    category=models.ForeignKey(Category,default=1,verbose_name='Category',on_delete=models.SET_DEFAULT)
    paint_image=models.FileField()
    published = models.DateTimeField("Date Published")

    def __str__(self):
        return self.paint_name


class User(models.Model):
    userName = models.CharField(max_length=30)
    userDescription = models.TextField()
    userImage = models.FileField()

    def __str__(self):
        return self.userName


