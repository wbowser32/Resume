import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

p = 'C:\\Users\\BowDa001\\Desktop\\Kount_Analysis_Worksheet.xlsm'
ws = 'Kount_Analysis_Worksheet'

df = pd.read_excel(p, sheet_name= ws)
print("Column Headings:")
for col in df.columns:
    print(col)
