from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.detail),
    path('<int:id>/results', views.result),
    path('<int:id>/vote', views.voting),

]