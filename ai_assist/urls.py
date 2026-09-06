from django.urls import path

from .views import TradeSummaryView

urlpatterns = [
    path("summary/", TradeSummaryView.as_view(), name="trade-summary"),
]
