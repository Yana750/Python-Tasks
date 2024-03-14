# импортируем нужные библиотеки для работы
import requests
import pandas as pd

# Указываем ссылку на скачивание файла
link = "https://drive.google.com/uc?id=1l0My0ZcrEF5_kpEWajQULEqgF7Suvz_l"

# Скачивание и сохранение файла Excel в данном каталоге
response = requests.get(link)
open("data.xlsx", "wb").write(response.content)

# Чтение загруженного файла Excel 
df = pd.read_excel("data.xlsx")

# Вычисление матрицы коэффициентов корреляции функцией corr()
# в загруженном файле
corr_matrix = df.iloc[:, 1:].corr()

# Вывод матрицы 
print(corr_matrix)