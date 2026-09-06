from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from trades.views import StrategyRuleViewSet, TradeViewSet

router = DefaultRouter()
router.register(r"trades", TradeViewSet, basename="trade")
router.register(r"strategy-rules", StrategyRuleViewSet, basename="strategy-rule")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/ai/", include("ai_assist.urls")),
]
