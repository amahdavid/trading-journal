from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import generate_trade_summary


class TradeSummaryView(APIView):
    def post(self, request):
        trade_data = request.data.get("trade")
        model = request.data.get("model", "llama3")

        if not isinstance(trade_data, dict):
            return Response(
                {"detail": "'trade' must be a JSON object."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            summary = generate_trade_summary(trade_data, model=model)
        except Exception as exc:
            return Response(
                {"detail": f"Unable to generate trade summary: {exc}"},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        return Response({"summary": summary})
