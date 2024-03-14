# Импортируем библиотеки
import pandas as pd

# Для начала работы перейдите по ссылке https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
# Как перейдете нажмите на кнопку Download, скачается архив, поместите файл master.csv в виртуальное окружение, где пишите код
data = pd.read_csv('master.csv')

# Очищаем данные
data = data.dropna(subset=['suicides_no', 'population', 'country', 'year', 'age'])

# Сгруппируется данные по стране, полу и возрасту
grouped_data = data.groupby(['country', 'sex', 'age'])['suicides_no'].mean().reset_index()

# Рассчитайте среднее число самоубийств для каждой группы
average_suicides = grouped_data.groupby(['country', 'sex', 'age'])['suicides_no'].mean().reset_index()

#Вывод кода
print(average_suicides)