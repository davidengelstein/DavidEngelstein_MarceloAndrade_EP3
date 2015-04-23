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