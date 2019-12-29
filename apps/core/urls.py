from django.urls import path
from apps.core import views

apps_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
