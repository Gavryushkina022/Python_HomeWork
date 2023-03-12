import pandas as pd

data = pd.read_csv('california_housing_train.csv')
median = data[(data['population'] > 0) & (data['population'] < 500)].median_house_value.mean().round(2)

print('Средняя стоимость дома: %s, где кол-во людей от 0 до 500' % median)
