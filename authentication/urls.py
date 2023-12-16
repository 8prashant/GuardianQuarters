from django.contrib import admin
from django.urls import path ,include
from . import views

from django.conf import settings #profile pic
from django.conf.urls.static import static #profile pic
from .views import create_property, property_list #property
from .views import my_properties   #my propertys
from .views import delete_property  #delete my properyts

#contact seller
from django.urls import path
from .views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),#contact seller

    path('property/<int:property_id>/delete/', delete_property, name='delete_property'),#delete that property
    path('my-properties/', my_properties, name='my_properties'),  #my propertys
    path('change_username/', views.change_username, name='change_username'),#update first and last name
    path('change_password/', views.change_password, name='change_password'),#update password

    path('property/<int:property_id>/', views.single_property, name='single_property'), #single property

    path('upload/', create_property, name='create_property'),#all propery
    path('property_list', property_list, name='property_list'),#all propery
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),#profile pic
    path('home',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('',views.adm,name="adm"),
    path('pro',views.pro,name="pro"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

