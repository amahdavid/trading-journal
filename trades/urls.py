from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StrategyRuleViewSet, TradeViewSet

router = DefaultRouter()
router.register(r"trades", TradeViewSet, basename="trade")
router.register(r"strategy-rules", StrategyRuleViewSet, basename="strategy-rule")

urlpatterns = [
    path("", include(router.urls)),
]
