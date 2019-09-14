import pandas as pd
from pandas import DataFrame
import requests
import simplejson as json
from datetime import datetime, date, timedelta


def get_data(ticker):
    url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'

    params = {'ticker':ticker, 'qopts.columns':'date'+','+'close', 'api_key':'q6i6KJAszzGMXgEihbj7'}
    
    end_date = date(2018, 2, 28)
    start_date = date(2018, 2, 1)
    date_list = [end_date - timedelta(days=x) for x in range((end_date-start_date).days+1)]
    
    resp = requests.get(url,params)
    json = resp.json()
    datatable = json['datatable']
    data = datatable['data']
    df = DataFrame(data)
    try:
        df = df.set_index(0)
        df.index = pd.to_datetime(df.index)
        df.columns = ['closing']
        df = df.reindex(date_list)
        df = df.dropna()
        return df
    except Exception as e:
        df = []
        return df

