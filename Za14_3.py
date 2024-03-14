import pandas as pd
from scipy import stats

# Чтение файла Excel
data1 = pd.read_excel('Group1.xlsx')
data2 = pd.read_excel('Group2.xlsx')

# Предварительно обработайте данные
# В этом примере я предполагаю, что академическая успеваемость хранится в столбце под названием "Оценка"
group1_scores = data1['Оценка']
group2_scores = data2['Оценка']

# Выполните t-тест
t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)

# Определите, следует ли отклонять нулевую гипотезу
alpha = 0.05
if p_value < alpha:
    print('Отвергаем нулевую гипотезу. Существует существенная разница между двумя группами.', p_value, t_stat)
else:
    print('Не удается отвергнуть нулевую гипотезу. Существенной разницы между двумя группами нет.', p_value, t_stat)