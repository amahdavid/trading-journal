from rest_framework import viewsets

from .models import StrategyRule, Trade
from .serializers import StrategyRuleSerializer, TradeSerializer


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all().order_by("-entry_date")
    serializer_class = TradeSerializer


class StrategyRuleViewSet(viewsets.ModelViewSet):
    queryset = StrategyRule.objects.all()
    serializer_class = StrategyRuleSerializer
