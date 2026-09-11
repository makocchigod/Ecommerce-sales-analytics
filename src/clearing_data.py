from download_csv import *

def customers_cleared():
    c = download_customers()
    c['age'] = c['age'].astype('Int64')
    c = c.drop_duplicates().reset_index(drop=True)
    return c

def orders_cleared():
    o = download_orders()
    o['quantity'] = o['quantity'].astype('Int64')
    o = o.drop_duplicates().dropna().reset_index(drop=True)
    o['order_date'] = pd.to_datetime(o['order_date'], format='mixed')
    return o

def products_cleared():
    p = download_products()
    p = p.drop_duplicates().reset_index(drop=True)
    p['category'] = p['product_name'].str.split().str[0] + "s"
    return p
