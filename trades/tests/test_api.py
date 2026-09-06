from datetime import date
from decimal import Decimal

from rest_framework.test import APITestCase

from trades.models import Trade


class TradeAPITests(APITestCase):
    def setUp(self):
        self.trade = Trade.objects.create(
            ticker="AAPL",
            strategy_type="credit_spread",
            entry_date=date(2026, 9, 1),
            expiry_date=date(2026, 9, 18),
            short_strike=Decimal("220.00"),
            long_strike=Decimal("215.00"),
            credit_received=Decimal("1.50"),
        )

    def test_list_trades(self):
        response = self.client.get("/api/trades/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["ticker"], "AAPL")

    def test_create_trade(self):
        payload = {
            "ticker": "MSFT",
            "strategy_type": "wheel",
            "entry_date": "2026-09-05",
            "expiry_date": "2026-09-25",
            "short_strike": "500.00",
            "credit_received": "2.25",
            "status": "open",
        }

        response = self.client.post("/api/trades/", payload, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["ticker"], "MSFT")
        self.assertEqual(Trade.objects.count(), 2)
