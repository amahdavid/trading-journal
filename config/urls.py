from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("trades.urls")),
    path("api/ai/", include("ai_assist.urls")),
]
