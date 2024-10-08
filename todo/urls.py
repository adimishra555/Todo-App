from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('remove_all/', views.remove_all, name='remove_all')
]