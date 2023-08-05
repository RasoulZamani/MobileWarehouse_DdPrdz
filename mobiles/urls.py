from django.urls import path
from . import views

app_name='mobiles'
urlpatterns= [
    path('',views.search_in_mobiles, name='mobiles'),
]