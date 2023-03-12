import pandas as pd

data = pd.read_csv('california_housing_train.csv')
min_population = data.population.min()
max_households = data[(data['population'] == min_population)].households.max()
print('Максимальная households: %s в зоне минимального значения population: %s' % (max_households, min_population))
