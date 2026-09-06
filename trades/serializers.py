from rest_framework import serializers

from .models import StrategyRule, Trade, TradeNote


class TradeNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeNote
        fields = "__all__"


class TradeSerializer(serializers.ModelSerializer):
    notes = TradeNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Trade
        fields = "__all__"


class StrategyRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyRule
        fields = "__all__"
