from flask import Flask, render_template
from sistema import system

app = Flask(__name__)

def dividirLista(lista):

	length = len(lista)

	middle_index = length // 2

	first_half = lista[:middle_index]
	second_half = lista[middle_index:]

	print(len(first_half))
	i = 1
	indice1 = []
	indice2 = []
	while i<=len(first_half):
		indice1.append(i)
		indice2.append(i+12)
		i+=1

	first_half = dict(zip(indice1,first_half))
	second_half = dict(zip(indice2,second_half))
	return first_half, second_half

@app.route("/")
def index():
	valores, valores2 = dividirLista(system.iniciarNumeros(dividir=True))
	return render_template("index.html", lista = valores, lista2 = valores2, funcion=system.iniciarNumeros)

if __name__ == "__main__":
	app.run(debug=False)
