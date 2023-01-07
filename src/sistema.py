import random

class system:
	def comprobarUnico(nuevo, lista):
		unico = True
		for x in range(len(lista)):
			if nuevo == lista[x]:
				unico = False
				break

		return unico

	def dividirResultado(lista):
		i = 0
		recorte = []
		sub = []
		while i<len(lista):
			sub.append(lista[i])
			i += 1
			if i % 4 == 0:
				recorte.append(sub)
				sub = []
			

		return recorte

	@classmethod
	def iniciarNumeros(self, dividir=bool()):
		lista = []
		i = 0

		while i<96:
			num = random.randint(1,96)
			if self.comprobarUnico(num, lista):
				lista.append(num)
				i+=1

		if dividir == True:
			return self.dividirResultado(lista)
		else:
			return lista