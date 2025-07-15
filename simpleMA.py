import pymysql
import pandas as pd
import mplfinance as mpf

conn = pymysql.connect(
    host='localhost',
    user='aaa',
    password='aaa',
    database='aaa',
    charset='utf8'
)


sql = """
SELECT date, open, high, low, close, volume FROM daily WHERE scode = '2498' and DATE >= '2025-07-01' ORDER BY DATE
"""

df = pd.read_sql(sql, conn)
conn.close()

#將日期欄位轉換成datetime，並設為index (mplfinance要求)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


'''
#計算5日均線(收盤價的移動平均)
df['MA5'] = df['close'].rolling(window=5).mean()

#用mplfinance繪圖
#將MA5放入addplot，以畫出均線
addplots = [mpf.make_addplot(df['MA5'], color='orange')]
'''

mpf.plot(
    df,
    type='candle',
    style='yahoo',
    mav=(2, 5, ),
    volume=True,
    savefig='ma.png'
)
