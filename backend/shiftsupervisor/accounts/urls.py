
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path("api/v2/", include("djoser.urls.jwt")),
    # path("api/v2/", include("djoser.urls")),
]