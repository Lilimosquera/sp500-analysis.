# -*- coding: utf-8 -*-
"""Clase6.ipynb

Automatically generated by Colab.

Elaborado por Liliana Mosquera, Melisa Ruiz, Edgar Ramos
"""

import yfinance as yf
import pandas as pd
import os
import logging
import requests
from bs4 import BeautifulSoup


log_dir = './logs'
data_dir = './data'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

log_filename = os.path.join(log_dir, 'etl_process.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

url = "https://es.wikipedia.org/wiki/Anexo:Compa%C3%B1%C3%ADas_del_S%26P_500"
req = requests.get(url)
soup = BeautifulSoup(req.text, features="lxml")
data = soup.find_all("table")[0]
df_p_and_s = pd.read_html(str(data))[0]
print (df_p_and_s)

def extract_data():
    try:
        logging.info('Extrayendo datos')
        data = df_p_and_s
        logging.info('Datos extraídos exitosamente')
        return data
    except Exception as e:
        logging.error(f'Error extrayendo datos {e}')
        return None

def load_data(df, data_dir="data"):
    try:
        data_dir = os.path.abspath(data_dir)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        filename = os.path.join(data_dir, 'df_p_and_s_processed.csv')
        logging.info(f'Guardando datos transformados en {filename}')
        df.to_csv(filename, index=False)
        logging.info('Datos guardados exitosamente')
    except Exception as e:
        logging.error(f'Error guardando datos: {e}')
    
data = extract_data ()

if data is not None:
    load_data(data)


def extract_data():
    try:
        logging.info('Extrayendo datos')
        data = df_p_and_s
        logging.info('Datos extraídos exitosamente')
        return data
    except Exception as e:
        logging.error(f'Error extrayendo datos {e}')
        return None

def load_data(df, data_dir="data"):
    try:
        data_dir = os.path.abspath(data_dir)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        filename = os.path.join(data_dir, 'combined_data.csv')
        logging.info(f'Guardando datos transformados en {filename}')
        df.to_csv(filename, index=False, mode='a', header=not os.path.exists(filename ))
        logging.info('Datos guardados exitosamente')
    except Exception as e:
        logging.error(f'Error guardando datos: {e}')
    
def transform_data(data):
    try:
        logging.info('Transformando datos')
        df = pd.DataFrame()
        for ticker in data["Símbolo"]:
            ticker_data = yf.download(ticker, start=start_date, end=end_date)
            ticker_data['Ticker'] = ticker
            ticker_data.reset_index(inplace=True)
            df = pd.concat([df, ticker_data], ignore_index=True)
        df.rename(columns={'Date': 'ds', 'Adj Close': 'y'}, inplace=True)
        logging.info('Datos transformados exitosamente')
        return df
    except Exception as e:
        logging.error(f'Error transformando datos: {e}')
        return None

def etl_process(ticker, start_date, end_date):
    data = extract_data()
    if data is not None:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            load_data(transformed_data)
            return transformed_data
    return None

tickers = df_p_and_s ["Símbolo"].tolist()
start_date = '2024-01-01'
end_date = '2024-03-31'
combined_data = etl_process(tickers, start_date, end_date)
