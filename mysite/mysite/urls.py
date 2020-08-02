from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('regist',views.regist),
    path('sign_up',views.sign_up),
    path('sign_in',views.sign_in),
    path('home',views.home),
    path('logout',views.logout),
    path('makeboard',views.make_board),
    path('createboard',views.create_board),
    path('myboard',views.myboard),
    path('deleteboard',views.delete_board),
]
