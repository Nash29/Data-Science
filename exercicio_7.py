
from die import Die
import pygal


# Cria dois dados
die_1 = Die(8)
die_2 = Die(8)


# Faz alguns lançamentos e armazena os resultados em um lista
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
	
# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value) # contamos quantas vezes cada numero aparece em results
	frequencies.append(frequency) # Adiciona esse valor a lista frequencies
	

# Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Results of rolling two D8 dice 1000 times'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12', 
	'13','14','15','16',]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('exercicio7.svg')
