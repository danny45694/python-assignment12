import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.data as pldata


#try:
with sqlite3.connect('db/lesson.db') as conn:
    cursor = conn.cursor()

sql_query = """
SELECT o.order_id, li.quantity * p.price AS total_price   
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p ON li.product_id = p.product_id
GROUP BY o.order_id
"""
df = pd.read_sql(sql_query, conn)
def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)
df['cumulative'] = df['total_price'].cumsum()

df.plot(kind='line',
        title = 'cumulative revenue vs. order_id',
        xlabel='order_id',
        ylabel='cumulative revenue',
        figsize=(10,6))
#plt.show()
#except sqlite3.Error as e:
#   print(f"Error connecting to SQLite DB: {e}")


#Task3
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

#Code below is not extracting - and + symbols. Will need to test with regex d next.
df['strength'] = df['strength'].str.replace(r"\-", "", regex=True)
df['strength'] = df['strength'].str.replace(r"\+", "", regex=True)
df['strength'] = df['strength'].astype(float)