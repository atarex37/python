import pandas as pd

file_name = "test.xlsx" # File name
sheet_name = 0 # 4th sheet
header = 0 # The header is the 2nd row
df = pd.read_excel('test.xlsx', sheet_name = sheet_name, header = header)
print(df.head(3)) # Prints first 5 rows from the top along with the header
# print(df.tail(2)) # Prints first 5 rows from the bottom along with the header