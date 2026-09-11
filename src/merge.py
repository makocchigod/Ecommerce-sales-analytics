from clearing_data import *

def merge_all():
    o = orders_cleared()
    p = products_cleared()
    c = customers_cleared()
    df = (o.merge(c, how='outer', on='customer_id')).merge(p, how='outer', on='product_id')
    return df