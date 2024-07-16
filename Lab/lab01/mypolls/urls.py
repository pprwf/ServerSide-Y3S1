from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("<int:id>/", views.detail, name = "detail"),
    path("<int:id>/results/", views.results, name = "results"),
    path("<int:id>/vote/", views.vote, name = "vote")
]
