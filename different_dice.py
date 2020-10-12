
from die import Die

import pygal

# Cria um D6 e um D10
die_1 = Die()
die_2 = Die(10) # 10 lados


# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
	
# Analiza os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value) # contamos quantas vezes cada numero aparece em results
	frequencies.append(frequency) # Adiciona esse valor a lista frequencies


# Visualiza os resultados
hist = pygal.Bar()


hist.title = 'Results of rolling a D6 and a D10 50,000 times'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12',
	'13','14','15','16',]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'


hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')









