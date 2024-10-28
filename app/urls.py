from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('check_id/', views.check_id, name='check_id'),
]
