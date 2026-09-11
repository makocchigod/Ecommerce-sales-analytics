import pandas as pd

def download_customers():
    customers = pd.read_csv('../data/customers.csv')
    return customers

def download_orders():
    orders = pd.read_csv('../data/orders.csv')
    return orders

def download_products():
    products = pd.read_csv('../data/products.csv')
    return products