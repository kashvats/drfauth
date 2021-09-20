from django.urls import path
from .views import *

urlpatterns = [
    path('', listapi.as_view(),name='list'),
    path('detail/<int:pk>', detailapi.as_view(),name='detail'),
    path('update/<int:pk>', updateapi.as_view(),name='update'),
    path('delete/<int:pk>', deleteapi.as_view(),name='delete'),
    path('create/', createapi.as_view(),name='create'),
    path('register/', reg.as_view(),name='register'),

]