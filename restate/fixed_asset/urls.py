from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name="login_url"),
    path('logout/', views.logout_view, name="logout_url"),

    # session urls
    path('my-app/', views.home, name="dashboard"),
    path('my-app/upload/', views.upload_file, name="upload_file"),

]
