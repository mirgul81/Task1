from django.urls import path, include
from .views import (
    indexView,
    newsView,
    studentView,
    aboutView,
)

app_name = 'main'

urlpatterns = [
    path('index/', indexView, name='index'),
    path('news/<int:pk>/', newsView, name='news'),
    path('student/<int:pk>/', studentView, name='student'),
    path('about/<int:pk>/', aboutView, name='about')



]