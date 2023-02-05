import matplotlib.pyplot as plt
from django.shortcuts import render
# views.py
import requests
import json
from django.shortcuts import render
from yahoo_fin import options as op

import yfinance as yf
from django.http.response import HttpResponse

from .models import Stock
from django.http import JsonResponse
"""
def get_stock_data(request):
    symbol = request.GET.get('symbol')
    if symbol:
        data = get_stock_data(symbol)
        save_stock_data(data)
        plot_stock_data(symbol)
        return JsonResponse(data)
"""


'''
def get_stock_data(symbol):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data
'''

"""
def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'trade1/stockpicker.html', {'stockpicker': stock_picker})

"""
"""
def get_NAME(request):
    s = request.post()
    print(s)
"""


def get_stock_data(request, symbol):
    stock = yf.Ticker(symbol)
    data = stock.info
    print(data)

    return render(request, 'trade1/display_stock_data.html', {'data': data})


def save_stock_data(data):
    # retrieve relevant data from the API response
    symbol = data['01. symbol']
    current_price = data['05. price']
    volume = data['06. volume']
    latest_trading_day = data['07. latest trading day']
    latest_update = data['08. latest update']
    # create a new Stock object and save it to the database
    stock = Stock(symbol=symbol, current_price=current_price, volume=volume,
                  latest_trading_day=latest_trading_day, latest_update=latest_update)
    stock.save()


def stock_data(request):
    symbol = request.GET.get('symbol')
    if symbol:
        data = get_stock_data(request, symbol)
        save_stock_data(data)
    stocks = Stock.objects.all()
    return render(request, 'stock_data.html', {'stocks': stocks})


def view_stock_data(request):
    # retrieve all stock data from the database
    stocks = Stock.objects.all()
    # pass the data to the template
    return render(request, 'view_stock_data.html', {'stocks': stocks})


def analyze_stock_data(request):
    # retrieve all stock data from the database
    stocks = Stock.objects.all()
    # perform the analysis for each stock
    for stock in stocks:
        stock.average_price = calculate_average_price(stock)
        stock.median_price = calculate_median_price(stock)
        stock.difference = calculate_difference(stock)
        stock.save()
    return render(request, 'trade1/analyze_stock_data.html', {'stocks': stocks})


def display_stock_data(request, symbol):
    stocks = Stock.objects.all()
    return render(request, 'trade1/display_stock_data.html', {'stocks': stocks})

# views.py


"""
def get_stock_data(symbol):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data
"""


def save_stock_data(data):
    # retrieve relevant data from the API response
    symbol = data['01. symbol']
    current_price = data['05. price']
    volume = data['06. volume']
    latest_trading_day = data['07. latest trading day']
    latest_update = data['08. latest update']
    # create a new Stock object and save it to the database
    stock = Stock(symbol=symbol, current_price=current_price, volume=volume,
                  latest_trading_day=latest_trading_day, latest_update=latest_update)
    stock.save()


def stock_data(request):
    symbol = request.GET.get('symbol')
    if symbol:
        data = get_stock_data(symbol)
        save_stock_data(data)
    stocks = Stock.objects.all()
    return render(request, 'trade1/stock_data.html', {'stocks': stocks})

# views.py


def plot_stock_data(symbol):
    stock_data = Stock.objects.filter(symbol=symbol).order_by('latest_update')
    dates = [data.latest_update for data in stock_data]
    prices = [data.current_price for data in stock_data]
    plt.plot(dates, prices)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{symbol} Stock Price')
    plt.show()


def stock_data(request):
    symbol = request.GET.get('symbol')
    if symbol:
        data = get_stock_data(symbol)
        save_stock_data(data)
        plot_stock_data(symbol)
    stocks = Stock.objects.all()
    return render(request, 'trade1/stock_data.html', {'stocks': stocks})


def upcoming_earnings(request):
    stocks = Stock.objects.filter(
        earning_date__gte=datetime.today()).order_by('earning_date')
    return render(request, 'trade1/upcoming_earnings.html', {'stocks': stocks})


def stock_detail(request, symbol):
    stock = get_object_or_404(Stock, symbol=symbol)
    earnings_history = stock.earnings_history.all()
    return render(request, 'trade1/stock_detail.html', {'stock': stock, 'earnings_history': earnings_history})


# Create your views here.


def stock_analysis(request, symbol):
    stock = Stock.objects.get(symbol=symbol)
    return render(request, 'trade1/stock_analysis.html', {'stock': stock})


def get_option_data(symbol, option_type):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=OPTION_PRICE&symbol={symbol}&apikey={API_KEY}&option_type={option_type}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data
