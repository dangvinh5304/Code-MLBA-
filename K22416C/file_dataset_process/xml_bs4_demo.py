from bs4 import BeautifulSoup

# Reading the data inside the XML file into a variable
with open('../dataset/SalesTransactions.xml', 'r') as f:
    data = f.read()

# Passing the stored data into the BeautifulSoup parser
bs_data = BeautifulSoup(data, 'xml')

# Finding all instances of a specific tag
UelSample = bs_data.find_all('UelSample')

# Printing the extracted data
print(UelSample)