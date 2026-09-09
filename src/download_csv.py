import pandas as pd

def download_customers():
    customers = pd.read_csv('../data/customers.csv')
    return customers

def download_employees():
    employees = pd.read_csv('../data/employees.csv')
    return employees

def download_orders():
    orders = pd.read_csv('../data/orders.csv')
    return orders

def download_products():
    products = pd.read_csv('../data/products.csv')
    return products