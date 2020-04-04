from django.urls import path
from .views import home,update,delete, create

app_name="notepad"
urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('update/<int:id>', update, name="update"),
    path('delete/<id>', delete, name="delete"),
]
