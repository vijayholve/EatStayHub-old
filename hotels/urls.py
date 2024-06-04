
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("base.urls")),
    path("profile/<str:pk>/",include("accounts.urls")),
    path("api/",include("api.urls")),
]
