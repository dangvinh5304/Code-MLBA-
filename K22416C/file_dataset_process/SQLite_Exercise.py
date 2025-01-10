import sqlite3
import pandas as pd
def get_customers_with_invoices(database_path, min_invoices):
    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect(database_path)
        cursor = sqliteConnection.cursor()
        print('DB Init')
        # Write a query to find customers with >= N invoices and execute it
        query = f'''
        SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, COUNT(Invoice.InvoiceId) AS InvoiceCount
        FROM Customer
        INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        HAVING InvoiceCount >= {min_invoices};
        '''
        cursor.execute(query)
        # Fetch and output result as a DataFrame
        df = pd.DataFrame(cursor.fetchall(), columns=['CustomerId', 'FirstName', 'LastName', 'InvoiceCount'])
        print(df)
        # Close the cursor
        cursor.close()
        return df
    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None
    finally:
        # Close DB Connection irrespective of success or failure
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

# Example usage
database_path = '../databases/Chinook_Sqlite.sqlite'
min_invoices = 5
result = get_customers_with_invoices(database_path, min_invoices)
print(result)