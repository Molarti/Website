from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name = "main_index"),
    path('text/',views.text_1),
    path('about/',views.about, name = "main_about"),
    path('info/',views.info,name = "main_info"),
    path('create/',views.create,name = "main_create"),

]