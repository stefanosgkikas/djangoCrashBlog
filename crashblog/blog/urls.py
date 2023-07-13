
from django.urls import path

from . import views

# δίνουμε το όνομα post_detail στην view που θα καλείται στο slug κάθε post - για πρώτη σελίδα
urlpatterns = [
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category,  name='category_detail'),
]