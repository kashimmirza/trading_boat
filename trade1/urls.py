from django.urls import path
from . import views


urlpatterns = [
    path('get_stock_data/<str:symbol>/',
         views.get_stock_data, name='get_stock_data'),

    path('save_stock_data/', views.save_stock_data, name='save_stock_data'),
    path('stock_data/', views.stock_data, name='stock_data'),
    path('view_stock_data/', views.view_stock_data, name='view_stock_data'),
    path('analyze_stock_data/', views.analyze_stock_data,
         name='analyze_stock_data'),
    path('display_stock_data/<str:symbol>/', views.display_stock_data,
         name='display_stock_data'),
    path('get_stock_data/', views.display_stock_data, name='get_stock_data'),
    path('save_stock_data/', views.save_stock_data, name='save_stock_data'),
    path('stock_data/', views.stock_data, name='stock_data'),
    path('plot_stock_data/', views.plot_stock_data, name='plot_stock_data'),
    path('stock_detail/', views.stock_detail, name='stock_detail'),
    path('get_option_data/', views.get_option_data, name='get_option_data'),
    # path('<str:symbol>/', views.detail, name='detail'),
    # path('', views.stockPicker, name='stockpicker')
    # path('stocktracker/', views.stockTracker, name='stocktracker'),

]
