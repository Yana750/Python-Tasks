import pandas as pd

# предполагая, что у вас есть следующие два фрейма данных
df1 = pd.DataFrame({
    'full_name': ['John Doe', 'Jane Smith'],
    'address': ['123 Main St', '456 Elm St'],
    'dob': ['1980-01-01', '1990-01-01'],
    'car_number': ['ABC123', 'DEF456']
})

df2 = pd.DataFrame({
    'car_number': ['ABC123', 'DEF456'],
    'make': ['Toyota', 'Honda'],
    'model': ['Corolla', 'Civic'],
    'year': [2015, 2018],
    'mileage': [30000, 20000],
    'engine_capacity': [1.8, 1.5]
})

# объедините фреймы данных в столбце 'car_number'
df = pd.merge(df1, df2, on='car_number')

# Выводится объединенные дата фреймы
print(df)