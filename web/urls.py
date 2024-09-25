
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from ap.views import home, myproduct, edit, detail, about, contact, category, search, signup, login,Logout, create_product, create_category, adding_image_product, delate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('myproducts/', myproduct, name='myproduct'),
    path('myproducts/', myproduct, name='myproduct'),
    path('detail|<int:id>/', detail, name='detail'),
    path('delate/<int:id>/', delate, name='delate'),  
    path('edit|<int:id>/', edit, name='edit'),  
    path('about/',  about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('search/', search, name='search'), 
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', Logout, name='logout'),
    path('create/product/', create_product, name='create_product'),
    path('create/category/', create_category, name='create_category'),
    path('add/image/<int:id>/', adding_image_product, name='add_image'),    

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
