from django.db import models


class Trade(models.Model):
    STRATEGY_CHOICES = [
        ("credit_spread", "Credit Spread"),
        ("wheel", "Wheel Strategy"),
    ]
    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
        ("rolled", "Rolled"),
        ("assigned", "Assigned"),
    ]

    ticker = models.CharField(max_length=10)
    strategy_type = models.CharField(max_length=20, choices=STRATEGY_CHOICES)
    entry_date = models.DateField()
    expiry_date = models.DateField()
    short_strike = models.DecimalField(max_digits=10, decimal_places=2)
    long_strike = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit_received = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    realized_pnl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticker} {self.strategy_type} ({self.status})"


class TradeNote(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField()
    ai_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        source = "AI" if self.ai_generated else "Manual"
        return f"Note on {self.trade} ({source})"


class StrategyRule(models.Model):
    strategy_type = models.CharField(max_length=20, choices=Trade.STRATEGY_CHOICES)
    rule_name = models.CharField(max_length=100)
    rule_description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.strategy_type}: {self.rule_name}"
