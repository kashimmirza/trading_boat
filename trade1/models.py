from django_cron import CronJobBase, Schedule
from django.db import models
from django.db import models


class Stock(models.Model):
    current_price = models.FloatField()
    difference = models.FloatField()
    next_target_price = models.FloatField()
    time_hit_target_price = models.IntegerField()
    time_hit_average_price = models.IntegerField()
    time_hit_median_price = models.IntegerField()
    lowest_price = models.FloatField()
    average_price = models.FloatField()
    median_price = models.FloatField()
    difference_high_low = models.FloatField()
    highest_price = models.FloatField()
    option_suggestion = models.CharField(max_length=50)
    volume = models.FloatField()
    option_price_suggested_target = models.FloatField()
    option_price_suggested_average = models.FloatField()
    option_price_median = models.FloatField()
    next_earning_date = models.DateField()
    next_earning_time = models.TimeField()


class EarningsHistory(models.Model):
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='earnings_history')
    earning_date = models.DateField()
    earning_time = models.TimeField()
    analysis_confidence = models.FloatField()
    eps_estimate = models.FloatField()
    mkt_cap = models.FloatField()
    reported_eps = models.FloatField()
    surprise = models.FloatField()
    surprise_percentage = models.FloatField()
    revenue_forecast = models.FloatField()
    revenue_actual = models.FloatField()
    stock_price_before_earning = models.FloatField()
    stock_price_after_earning = models.FloatField()
    implied_volatility = models.FloatField()


class OptionData(models.Model):
    symbol = models.CharField(max_length=10)
    option_type = models.CharField(
        max_length=4, choices=(("call", "Call"), ("put", "Put")))
    breakeven_price = models.DecimalField(max_digits=10, decimal_places=2)
    bought_at_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    stop_loss_price = models.DecimalField(max_digits=10, decimal_places=2)
    limit_price = models.DecimalField(max_digits=10, decimal_places=2)


class UpdateStockData(CronJobBase):
    RUN_EVERY_MINS = 1440  # run once per day
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.update_stock_data'

    def do(self):
        # retrieve the list of all stock symbols
        symbols = Stock.objects.values_list('symbol', flat=True).distinct()
        # update the data for each symbol
        for symbol in symbols:
            data = get_stock_data(symbol)
            save_stock_data(data)
