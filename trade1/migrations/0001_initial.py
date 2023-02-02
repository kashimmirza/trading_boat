# Generated by Django 4.1.5 on 2023-01-31 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OptionData",
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
                ("symbol", models.CharField(max_length=10)),
                (
                    "option_type",
                    models.CharField(
                        choices=[("call", "Call"), ("put", "Put")], max_length=4
                    ),
                ),
                (
                    "breakeven_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "bought_at_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("expiration_date", models.DateField()),
                (
                    "stop_loss_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("limit_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("current_price", models.FloatField()),
                ("difference", models.FloatField()),
                ("next_target_price", models.FloatField()),
                ("time_hit_target_price", models.IntegerField()),
                ("time_hit_average_price", models.IntegerField()),
                ("time_hit_median_price", models.IntegerField()),
                ("lowest_price", models.FloatField()),
                ("average_price", models.FloatField()),
                ("median_price", models.FloatField()),
                ("difference_high_low", models.FloatField()),
                ("highest_price", models.FloatField()),
                ("option_suggestion", models.CharField(max_length=50)),
                ("volume", models.FloatField()),
                ("option_price_suggested_target", models.FloatField()),
                ("option_price_suggested_average", models.FloatField()),
                ("option_price_median", models.FloatField()),
                ("next_earning_date", models.DateField()),
                ("next_earning_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="EarningsHistory",
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
                ("earning_date", models.DateField()),
                ("earning_time", models.TimeField()),
                ("analysis_confidence", models.FloatField()),
                ("eps_estimate", models.FloatField()),
                ("mkt_cap", models.FloatField()),
                ("reported_eps", models.FloatField()),
                ("surprise", models.FloatField()),
                ("surprise_percentage", models.FloatField()),
                ("revenue_forecast", models.FloatField()),
                ("revenue_actual", models.FloatField()),
                ("stock_price_before_earning", models.FloatField()),
                ("stock_price_after_earning", models.FloatField()),
                ("implied_volatility", models.FloatField()),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="earnings_history",
                        to="trade1.stock",
                    ),
                ),
            ],
        ),
    ]