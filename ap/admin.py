from django.contrib import admin
from .models import Category, Product, ProductImages, MyUser, Comment


admin.site.register(MyUser)
admin.site.register(ProductImages)
admin.site.register(Product)
admin.site.register(Comment)
# Register your models here.
