import pandas as pd
import requests

# Указываем ссылку на скачивание файла
link = "https://drive.google.com/uc?id=1l0My0ZcrEF5_kpEWajQULEqgF7Suvz_l"

# Скачивание и сохранение файла Excel в данном каталоге
response = requests.get(link)
open("data2.xlsx", "wb").write(response.content)

# Чтение загруженного файла Excel 
df = pd.read_excel("data2.xlsx")

# Calculate the mean and variance for each row (excluding the first column)
mean_col = df.iloc[:, 1:].mean(axis=1)
variance_col = df.iloc[:, 1:].var(axis=1)

# Add the mean and variance columns to the DataFrame
df['mean'] = mean_col
df['variance'] = variance_col

# Print only the first column and the new columns
print(df[['Unnamed: 0', 'mean', 'variance']])