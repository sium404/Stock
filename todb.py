# A file to store the excel tickr file as a database

import pandas as pd
import sqlite3 as sq
tkr = pd.read_excel('/Users/sium/Desktop/Stock-Price-Prediction-App/Yahoo\ Ticker\ Symbols.xlsx')
db = sq.connect('stocks.db')
tkr.to_sql("tkrinfo",db)
db.close()
