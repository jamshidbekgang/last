from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User
from taggit.managers import TaggableManager



class Product(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='user/', default='33.png')
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, related_name='products')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    rasm = models.ImageField(default='no_image.webp')

    def __str__(self) -> str:
        return self.name


class Meta:
    verbose_name = 'Mahsulot'
    verbose_name_plural = 'mahsulotlar'

class ProductImages(models.Model):
    image = models.ImageField(upload_to='productImages/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')    

   
class Meta:
    verbose_name = 'Mahsulot rasmi'
    verbose_name_plural = 'mahsulotlar rasmlari' 

 
class Comment(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comments")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)

    def __str__(self) -> str:
        return self.comment

