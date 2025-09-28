import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

try:
    with sqlite3.connect('db/lesson.db') as conn:
        cursor = conn.cursor()

    sql_query = """
    SELECT o.order_id, li.quantity * p.price AS total_price   
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
    """
    df = pd.dataFrame(sql_query)
    def cumulative(row):
        totals_above = df['total_price'][0:row.name+1]
        return totals_above.sum()
    
    df['cumulative'] = df.apply(cumulative, axis=1)
    df['cumulative'] = df['total_price'].cumsum()

    

except sqlite3.Error as e:
    print(f"Error connecting to SQLite DB: {e}")