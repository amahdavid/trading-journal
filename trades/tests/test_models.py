from datetime import date
from decimal import Decimal

from django.test import TestCase

from trades.models import StrategyRule, Trade, TradeNote


class TradeModelTests(TestCase):
    def test_trade_string_representation(self):
        trade = Trade.objects.create(
            ticker="AAPL",
            strategy_type="credit_spread",
            entry_date=date(2026, 9, 1),
            expiry_date=date(2026, 9, 18),
            short_strike=Decimal("220.00"),
            long_strike=Decimal("215.00"),
            credit_received=Decimal("1.50"),
        )

        self.assertEqual(str(trade), "AAPL credit_spread (open)")

    def test_trade_note_belongs_to_trade(self):
        trade = Trade.objects.create(
            ticker="MSFT",
            strategy_type="wheel",
            entry_date=date(2026, 9, 1),
            expiry_date=date(2026, 9, 18),
            short_strike=Decimal("500.00"),
            credit_received=Decimal("2.25"),
        )
        note = TradeNote.objects.create(trade=trade, content="Good entry.")

        self.assertEqual(trade.notes.count(), 1)
        self.assertEqual(note.trade, trade)
        self.assertFalse(note.ai_generated)

    def test_strategy_rule_is_active_by_default(self):
        rule = StrategyRule.objects.create(
            strategy_type="credit_spread",
            rule_name="Minimum credit",
            rule_description="Require a minimum credit before entering.",
        )

        self.assertTrue(rule.is_active)
