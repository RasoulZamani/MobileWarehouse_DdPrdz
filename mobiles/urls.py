from django.urls import path
from . import views

app_name='mobiles'
urlpatterns= [
    path('search_mobiles/',views.search_mobiles, name='search_mobiles'),
    path('search_results/',views.search_results, name='search_results'),
]