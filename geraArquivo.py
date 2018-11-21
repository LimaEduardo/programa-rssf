import math

def distancia(i,j):
	coluna_i = i%15
	linha_i = i//15
	
	coluna_j = j%15
	linha_j = j//15
	
	a = math.pow(coluna_j - coluna_i, 2)
	b = math.pow(linha_j - linha_i, 2)
	distancia = math.sqrt(a + b)
	return distancia * 20

def atenuacao(i,j):
	distanciaIJ = distancia(i,j)
	return -45 - (20 * math.log(distanciaIJ, 10))
	
def escreveArquivo(mat):
	arquivo = open("arquivo.txt","w")
	for linha in mat:
		arquivo.write(str(linha))
		arquivo.write("\n")

mat = []

for	i in range(255):
	for j in range(225):
		if i != j:
			mat.append([i,j,atenuacao(i,j)])

escreveArquivo(mat)
