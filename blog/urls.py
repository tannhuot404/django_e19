from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("blog/", views.welcome_view, name='welcome'),
    path("search/", views.search),
    path("blog/<int:id>/", views.post_detail),
    path('payment', views.payment)
]
