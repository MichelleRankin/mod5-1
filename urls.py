
from django.contrib import admin
from django.urls import path
from app.views import root
import app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hey/", root),
]
