import pandas as pd

def find_orders_within_range(df, minValue, maxValue, SortType):
    # tổng giá trị từng đơn hàng
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    # lọc đơn hàng trong range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
    # tạo danh sách các hóa đơn với mã đơn hàng và tổng giá trị
    order_details = orders_within_range.reset_index(name='TotalValue')
    # sắp xếp nếu SortType là True (tăng dần), False (giảm dần)
    if SortType:
        order_details = order_details.sort_values(by='TotalValue', ascending=True)
    else:
        order_details = order_details.sort_values(by='TotalValue', ascending=False)

    return order_details

df = pd.read_csv('../dataset/SalesTransactions.csv')

minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
SortType = input("Sắp xếp (True/False): ").lower() == 'true'
result = find_orders_within_range(df, minValue, maxValue, SortType)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:', result)
