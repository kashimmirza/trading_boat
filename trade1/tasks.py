from celery import task


@task
def check_option_data():
    options = OptionData.objects.all()
    for option in options:
        live_data = get_option_data(option.symbol, option.option_type)
        if live_data['current_price'] >= option.breakeven_price:
            # in profit
            send_alert("In profit", option)
        elif live_data['current_price'] <= option.stop_loss_price:
            # stop loss hit
            send_alert("Stop loss hit", option)
        elif live_data['expiration_date'] <= datetime.now().date():
            # about to expire
            send_alert("About to expire", option)
        elif live_data['current_price'] <= option.stop_loss_price - 5:
            # about to hit stop loss
            send_alert("About to hit stop loss", option)
        else:
            # in loss
            send_alert("In loss", option)


def send_alert(message, option):
    # send an email or SMS to the customer with the message and option data
    pass


def get_stock_data(symbol):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data
