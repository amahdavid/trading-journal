from django.contrib import admin

from .models import StrategyRule, Trade, TradeNote


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "ticker",
        "strategy_type",
        "entry_date",
        "expiry_date",
        "status",
        "credit_received",
        "realized_pnl",
    )
    list_filter = ("strategy_type", "status")
    search_fields = ("ticker",)
    ordering = ("-entry_date",)


@admin.register(TradeNote)
class TradeNoteAdmin(admin.ModelAdmin):
    list_display = ("trade", "ai_generated", "created_at")
    list_filter = ("ai_generated",)
    search_fields = ("trade__ticker", "content")
    ordering = ("-created_at",)


@admin.register(StrategyRule)
class StrategyRuleAdmin(admin.ModelAdmin):
    list_display = ("strategy_type", "rule_name", "is_active")
    list_filter = ("strategy_type", "is_active")
    search_fields = ("rule_name", "rule_description")
