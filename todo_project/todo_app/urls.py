from django.urls import path
from . import views

'''
    migrationsdaki pk olan id yi kullanarak seçilen todo satırını sileriz
'''
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<Todos_id>', views.delete, name="delete"),
    path('done/<Todos_id>', views.done, name="done"),
    path('undone/<Todos_id>', views.undone, name="undone"),
    path('update/<Todos_id>', views.update, name="update")
]
