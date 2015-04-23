
def tmb_homem(peso,altura,idade):
	tmb = 88.36 + (13.4*float(peso)) + (4.8*float(altura)) - (5.7*float(idade))
	return tmb #Funcao que recebe peso, altura e idade e retorna o TMB de um homem.
def tmb_mulher(peso,altura,idade):
	tmb = 447.6 + (9.2*float(peso)) + (3.1*float(altura)) - (4.3*float(idade))
	return tmb #Funcao que recebe peso, altura e idade e retorna o TMB de uma mulher
def necessidade_calorica(tmb,grau):
	if grau == "minimo":
		nec_calorica = 1.2*tmb
	if grau == "baixo":
		nec_calorica = 1.375*tmb
	if grau == "medio":
		nec_calorica = 1.55*tmb
	if grau == "alto":
		nec_calorica = 1.725*tmb
	if grau == "muito alto":
		nec_calorica = 1.9*tmb
	return nec_calorica #Funcao que recebe o TMB do individuo e seu grau de exercicio e retorna a necessidade calórica dele
def imc(peso,altura):
	imc = 1.3*float(peso)/(float(altura)**2.5)
	return imc#Funcao para calcular o IMC do individuof = open ('alimentos.csv') # Abrindo o arquivo com alimentos
arquivo = f.readlines()
alimentos = [[0 for x in range(6)] for y in range(len(arquivo)-1)]  
for i in range (1,len(arquivo)): #Transformando o arquivo de alimentos em uma matriz chamada "alimentos"
	k = i - 1
	linha_aux = arquivo[i].split(',')
	for j in range (6):
		alimentos[k][j] = linha_aux[j].replace(";","")
g = open ('usuario.csv') #Abrindo o arquivo do usuario
arquivo2 = g.readlines()
informacoes = arquivo2[1].split(',') #Criando funcoes para as informacoes basicas do individuo a partir do arquivo usuarios . + 5 linhas
idade = informacoes[1]
peso = informacoes[2]
sexo = informacoes[3]
altura = informacoes[4]
grau = informacoes[5].strip()
if sexo == "M": #Funcao SE para que faça uma medida de TMB diferente para cada sexo
	calorias = necessidade_calorica(tmb_homem(peso,altura,idade),grau)
if sexo == "F":
	calorias = necessidade_calorica(tmb_mulher(peso,altura,idade),grau)