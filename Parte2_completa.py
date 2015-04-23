
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
datas = [[0 for x in range(3)] for y in range(len(arquivo2)-3)] #Criacao de uma matriz para as informacoes de comida diarias do usuario
for i in range (3,len(arquivo2)):
	k = i - 3
	linha_aux = arquivo2[i].split(',')
	for j in range (3):
		datas[k][j] = linha_aux[j].replace(";","").strip()
num_dias_aux = []
for i in range (len(arquivo2)-3): #Contagem de dias que foram usados "num_dias" e quais sao esses dias "num_dias_aux" + 6 linhas
	for j in range (len(arquivo2)-3):
		if datas[i][0] not in num_dias_aux and datas[i][0] != 0:
			num_dias_aux.append(datas[i][0])
		if i != j:
			if datas[j][0] == datas[i][0] and datas[i][0] != 0:
				datas[j][0] = 0
datas = [[0 for x in range(3)] for y in range(len(arquivo2)-3)] #Por conta de um erro que dava, novamente a criação da mesma matriz com informacoes de comida diarias
for i in range (3,len(arquivo2)):
	k = i - 3
	linha_aux = arquivo2[i].split(',')
	for j in range (3):
		datas[k][j] = linha_aux[j].replace(";","").strip()
num_dias = len(num_dias_aux)
tempo = [1]*num_dias #Criacao de uma lista de tempo que o usuario utilizou para o gráfico.
for i in range (1,num_dias):
	tempo[i] = tempo [i-1] + 1
lista_nec_calorica = [calorias]*num_dias
data_calorias = [0]*(num_dias)#Criacao de listas para armazenamento de informacoes das comidas para os gráficos.
data_proteinas = [0]*(num_dias)
data_carboidratos = [0]*(num_dias)
data_gorduras = [0]*(num_dias)
for i in range (2): #Funcao para comparar o que o usuario ingeriu e a quantidade, por dia, com as informacoes contidas no arquivo dos alimentos, para saber no final qual a quantidade de cada substancia ingerida. +10 linhas
	for j in range (len(arquivo2)-3):
		if datas[j][0] == num_dias_aux[i]:
			for k in range (len(arquivo)-1):
				if datas[j][1] == alimentos[k][0]:
					data_calorias[i] += (float(datas[j][2])/float(alimentos[k][1]))*float(alimentos[k][2])
					data_proteinas[i] += (float(datas[j][2])/float(alimentos[k][1]))*float(alimentos[k][3])
					data_carboidratos[i] += (float(datas[j][2])/float(alimentos[k][1]))*float(alimentos[k][4])
					data_gorduras[i] += (float(datas[j][2])/float(alimentos[k][1]))*float(alimentos[k][5])
if imc(peso,altura)<18.5:#Funcao para verificar se a pessoa está magra ou acima do peso pelo imc
	peso_final = "magro"
if imc(peso,altura)>18.5 and imc(peso,altura)<25:
	peso_final = "normal"
if imc(peso,altura)>25 and imc(peso,altura)<30:
	peso_final = "acima do peso"
if imc(peso,altura)>30:
	peso_final = "obeso"
f = open('resultado_imc', 'w')#Aqui é criado um arquivo chamado resultado_imc, onde é escrito o valor final do IMC e a condição do usuario(magro, acima do peso...)
f.write('IMC final é %d\n'%imc(peso,altura))
f.write('Com esse valor, o usuário está %s\n'%peso_final)
for i in range (num_dias):
	f.write('Quantidade de calorias consumida no dia %s = %d\n'%(num_dias_aux[i],data_calorias[i]))