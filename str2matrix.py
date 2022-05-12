import pandas as pd
import numpy as np

StrRates = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"
column_names =[]
row_names =[]
final_matrix =[]
columns = StrRates.split(';')
columns.pop()
print(columns)
row_names_chk = False
for column in columns:
    column_names.append((column.split(':')[-1]).split('L')[-1])
    column_items = (column.split(':')[0]).split(',')
    print(column_items)
    column_data = []
    for i in range(0, len(column_items), 2):
        print(i)
        column_data.append(column_items[i+1])
        if row_names_chk ==False:
            row_names.append(column_items[i])
    row_names_chk=True
    final_matrix.append(column_data)
final_matrix = np.array(final_matrix).transpose()
df = pd.DataFrame(final_matrix, index = row_names, columns=column_names)

html_content = df.to_html()

with open('table.html', 'w') as file:
    file.write(html_content)
        