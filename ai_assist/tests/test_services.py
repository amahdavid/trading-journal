from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from ai_assist.services import generate_trade_summary


class GenerateTradeSummaryTests(SimpleTestCase):
    @patch("ai_assist.services.requests.post")
    def test_generate_trade_summary_returns_model_response(self, mock_post):
        response = Mock()
        response.json.return_value = {"response": "A concise trade summary."}
        mock_post.return_value = response

        result = generate_trade_summary({"ticker": "AAPL"})

        self.assertEqual(result, "A concise trade summary.")
        response.raise_for_status.assert_called_once()
        mock_post.assert_called_once()

    @patch("ai_assist.services.requests.post")
    def test_generate_trade_summary_uses_requested_model(self, mock_post):
        response = Mock()
        response.json.return_value = {"response": "Summary"}
        mock_post.return_value = response

        generate_trade_summary({"ticker": "MSFT"}, model="mistral")

        request_kwargs = mock_post.call_args.kwargs
        self.assertEqual(request_kwargs["json"]["model"], "mistral")
        self.assertFalse(request_kwargs["json"]["stream"])
