from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.pull_feed)
]

