from django.urls import path, include

from . import views
from .views import dashboard

urlpatterns = [
    # Urls go in here
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),

]
