#Lọc dữ liệu bị thiếu
from numpy import nan as NA
import pandas as pd
data = pd.DataFrame([[1., 6.5, 3.],
                    [1., NA, NA],
                    [NA, NA, NA],
                    [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned = data.dropna()
print(cleaned)
cleaned2 = data.dropna(how='all')
print(cleaned2)

#Điền dữ liệu còn thiếu
from numpy import nan as NA
import pandas as pd
data = pd.DataFrame([[1., 6.5, 3.],
                    [1., NA, NA],
                    [NA, NA, NA],
                    [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned = data.fillna(data.mean())
print(cleaned)

