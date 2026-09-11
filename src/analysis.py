from merge import merge_all
import matplotlib.pyplot as plt

def revenue():
    df = merge_all()
    df['revenue'] = df['quantity'] * df['price']
    df['month'] = df['order_date'].dt.to_period('M')
    print(df['month'].unique())
    result = df.groupby(['product_name','month']).agg(revenue=('revenue', 'sum'))
    return result

def monthly_revenue():
    df = revenue()
    result = df.groupby('month').agg(revenue=('revenue', 'sum'))
    print(result)
    result['revenue'].plot(kind='line', ylabel='revenue', xlabel='month')
    plt.show()
monthly_revenue()