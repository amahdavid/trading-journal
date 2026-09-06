from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ticker", models.CharField(max_length=10)),
                (
                    "strategy_type",
                    models.CharField(
                        choices=[
                            ("credit_spread", "Credit Spread"),
                            ("wheel", "Wheel Strategy"),
                        ],
                        max_length=20,
                    ),
                ),
                ("entry_date", models.DateField()),
                ("expiry_date", models.DateField()),
                (
                    "short_strike",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "long_strike",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "credit_received",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("closed", "Closed"),
                            ("rolled", "Rolled"),
                            ("assigned", "Assigned"),
                        ],
                        default="open",
                        max_length=20,
                    ),
                ),
                (
                    "realized_pnl",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="StrategyRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "strategy_type",
                    models.CharField(
                        choices=[
                            ("credit_spread", "Credit Spread"),
                            ("wheel", "Wheel Strategy"),
                        ],
                        max_length=20,
                    ),
                ),
                ("rule_name", models.CharField(max_length=100)),
                ("rule_description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="TradeNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("ai_generated", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "trade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="trades.trade",
                    ),
                ),
            ],
        ),
    ]
