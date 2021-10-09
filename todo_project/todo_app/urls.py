from django.urls import path
from . import views

'''
    migrationsdaki pk olan id yi kullanarak seçilen todo satırını sileriz
'''
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<Todos_id>', views.delete, name="delete")
]
