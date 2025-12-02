import pandas as pd
import matplotlib.pyplot as plt
import re

def ext_date(orders_df, ts = "timestamp", orders_dt = "date"):
    orders_df[orders_dt] = orders_df[ts].dt.date
    return orders_df

def any_price_to_dollar(orders_df, orders_unit_price_norm = "unit_price_norm", num_price="unit_price_num", cur_price = "unit_price_currency"):
    # for i in orders_df:
    #     unit_price_str = str(i[orders_unit_price_norm])
    #     currency = unit_price_str[0]
    #     m = re.search(r"\d+(\.\d+)?", unit_price_str)
    #     num_price = float(m.group(0))
    prices = orders_df[orders_unit_price_norm].astype(str).str.strip()
    # orders_df[num_price] = prices.str.extract(r"\d+(\.\d+)?", expand = False).astype(float).round(2)
    
    orders_df[order]
