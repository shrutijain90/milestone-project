import pandas as pd
from pandas import DataFrame
import requests
import simplejson as json
from datetime import datetime, date, timedelta


def get_data(ticker):
    url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'

    params = {'ticker':ticker, 'qopts.columns':'date'+','+'close', 'api_key':'q6i6KJAszzGMXgEihbj7'}
    
    today = date(2018, 3, 1)
    start_date = today.replace(year=today.year if today.month > 1 else today.year - 1, month=today.month - 1 if today.month >1 else 12)
    date_list = [today - timedelta(days=x) for x in range((today-start_date).days+1)]
    
    resp = requests.get(url,params)
    json = resp.json()
    datatable = json['datatable']
    data = datatable['data']
    df = DataFrame(data)
    try:
        df = df.set_index(0)
        df.index = pd.to_datetime(df.index)
        df.columns = ['closing']
        return df.loc[date_list]
    except Exception as e:
        df = []
        return df

