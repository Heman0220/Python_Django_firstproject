from django.conf import Settings, settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name="about")  
]
