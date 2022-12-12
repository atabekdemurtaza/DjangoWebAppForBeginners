from django.urls import path
from .views import listing_list
from .views import listing_retrieve
from .views import listing_create
from .views import listing_update
from .views import listing_delete

urlpatterns = [
    path('', listing_list, name='listing_list'),
    path('<int:pk>/', listing_retrieve, name='listing_retrieve'),
    path('<int:pk>/edit/', listing_update, name='listing_update'),
    path('<int:pk>/delete/', listing_delete, name='listing_delete'),
    path('create/', listing_create, name='listing_create'),
]
