import pandas as pd

df = pd.read_csv(r'C:\Users\User\OneDrive\Desktop\Finance\Asset_Management\hw1\spy_ticker.txt',header=None)
df.columns = ['ticker']

tickers = "'" + "', '".join(df.ticker) + "'"


# import wrds
# db = wrds.Connection(wrds_username='bgreen41')
# db.raw_sql("""select * from comp.secd where tic IN('AAPL', 'MSFT')""")