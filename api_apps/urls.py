from django.urls import path
from . import views

urlpatterns = [
    path('', views.advices, name = "advices"),
    path('facts/', views.facts, name = "facts"),
    path('jokes/', views.jokes, name = "jokes"),
    path('quotes/', views.quotes, name = "quotes"),
]
