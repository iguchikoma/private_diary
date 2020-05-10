from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
]