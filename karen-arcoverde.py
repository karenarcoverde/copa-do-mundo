# Programa karen-arcoverde.py
# Autora: Karen dos Anjos Arcoverde
# Data: 13/06/2018
#
# Programa que contem um banco de dados da Copa do Mundo
#

########################## Funcoes ###################################

def criar_selecao(selecao):
	selecoes = open('selecoes.txt','r+')
	conteudo_selecoes = selecoes.readlines()
	
	# Tira o '\n' que esta presente na lista em cada elemento
	for indice in range (len(conteudo_selecoes)):	
		conteudo_selecoes[indice] = conteudo_selecoes[indice][:-1]

	# Verifica se a selecao digitada pelo usuario ja existe
	for linha in conteudo_selecoes:
		while (linha == selecao):
			print("Essa selecao ja esta cadastrada!!!!")
			print("Digite uma selecao valida")
			print('Selecoes existentes:')
			for indice in range(len(conteudo_selecoes)):
				print(conteudo_selecoes[indice])
			print()
			selecao = input('Informe OUTRA selecao: ')
	
	selecoes.write(selecao +'\n')
	selecao = open(selecao + '.txt', 'w+')
	
	selecoes.close()
	selecao.close()
	


def acrescentar_jogador(selecao,jogador_nome):

	selecao	= open(selecao +'.txt', 'r+')
	conteudo_selecao = selecao.readlines()
	
	jogador_idade = input('Informe a idade: ')
	jogador_posicao = input('Informe a posicao: ')
	jogador_time = input('Informe o time que atua: ')
	jogador_gols = input('Informe o numero de gols: ')
	selecao.write(jogador_nome + ';' + jogador_idade + ';' + jogador_posicao + ';' + jogador_time + ';' + jogador_gols + '\n')
	
	selecao.close()



def apagar_jogador(selecao,jogador_nome):
	conteudoNew = []
	selecao1 = selecao
	selecao2 = selecao

	selecao1 = open(selecao1 +'.txt', 'r+')
	conteudoOld = selecao1.readlines()
			
	for linha in conteudoOld:
		if not (jogador_nome in linha):
			conteudoNew += [linha]

        
	selecao1.close()

	selecao2 = open(selecao2+'.txt', 'w+')
	for linha in conteudoNew:
		selecao2.write(linha)

	selecao2.close()
        


def atualizar_gols(jogador_nome,selecao,jogador_gols):
	conteudoNew = []
	quantidade = 0
	selecao1 = selecao
	selecao2 = selecao
	selecao3 = selecao

	selecao1 = open(selecao1 + '.txt', 'r+')
	conteudoOld = selecao1.readlines()

	# Transforma cada elemento de uma linha do arquivo em uma lista
	for linha in conteudoOld:
		lista = [0,0,0,0,0]
		inicio = 0
		contador = 0
		while (linha[contador] != ";"):
    			contador += 1
		lista[0] = linha[inicio:contador]
		contador += 1
		inicio = contador
		while (linha[contador] != ";"):
    			contador += 1
		lista[1] = linha[inicio:contador]
		contador += 1
		inicio = contador
		while (linha[contador] != ";"):
    			contador += 1
		lista[2] = linha[inicio:contador]
		contador += 1
		inicio = contador
		while (linha[contador] != ";"):
    			contador += 1
		lista[3] = linha[inicio:contador]
		contador += 1
		inicio = contador
		while (linha[contador] != "\n"):
    			contador += 1
		lista[4] = linha[inicio:contador]
		
		quantidade += 1

		if (lista[0] == jogador_nome):
			lista[4] = jogador_gols
		
		conteudoNew += [lista]
	
	selecao2 = open(selecao2 + '.txt', 'w+')

	selecao1.close()
	selecao2.close()
	
	selecao3 = open(selecao3 + '.txt', 'r+')
	for i in range (quantidade):
		selecao3.write(conteudoNew[i][0] + ';' + conteudoNew[i][1] + ';' + conteudoNew[i][2] + ';' + conteudoNew[i][3] + ';' + conteudoNew[i][4] +'\n')
		
	selecao3.close()



# Funcao que transforma cada elemento de uma linha do arquivo em uma lista	
def passagem_arquivo_lista(linha,conteudo_selecao):
	lista = [0,0,0,0,0]
	inicio = 0
	contador = 0
	while (linha[contador] != ";"):
    		contador += 1
	lista[0] = linha[inicio:contador]
	contador += 1
	inicio = contador
	while (linha[contador] != ";"):
    		contador += 1
	lista[1] = linha[inicio:contador]
	contador += 1
	inicio = contador
	while (linha[contador] != ";"):
    		contador += 1
	lista[2] = linha[inicio:contador]
	contador += 1
	inicio = contador
	while (linha[contador] != ";"):
    		contador += 1
	lista[3] = linha[inicio:contador]
	contador += 1
	inicio = contador
	while (linha[contador] != "\n"):
    		contador += 1
	lista[4] = linha[inicio:contador]

	return lista 



# Funcao que mostra os nomes e posicoes dos jogadores de uma determinada selecao ordenados 
# pela categoria de posicoes (goleiro - zagueiro - lateral - meio-campo - atacante),
# em que os jogadores de mesma posicao sao ordenados em ordem alfabetica
def consulta_jogadores_selecao():
	lista_goleiros = []
	lista_zagueiros = []
	lista_laterais = []
	lista_meiocampos = []
	lista_atacantes = []
	lista_selecao = []
	
	selecoes = open('selecoes.txt','r')
	conteudo_selecoes = selecoes.readlines()
	
	print('Selecoes existentes:')
	for indice in range(len(conteudo_selecoes)):
		print(conteudo_selecoes[indice],end='')
	print()

	selecao = input('Informe a selecao existente: ')
	print()
	
	selecao = open(selecao + '.txt','r')
	conteudo_selecao = selecao.readlines()

	for linha in conteudo_selecao:
		lista = passagem_arquivo_lista(linha,conteudo_selecao)
		
		# Transforma cada elemento de uma linha em uma lista de registros
		jogador = {'Nome': ' ','Posicao': ' '}
		jogador['Nome'] = lista[0]
		jogador['Posicao'] = lista[2]
		lista_selecao += [jogador]
	
	
	# Ordena os nomes dos jogadores em ordem alfabetica
	Trocou = True
	n = 1 
	while (Trocou):
		Trocou = False
		for indice in range (len(lista_selecao)-n):
			if(lista_selecao[indice]['Nome'] > lista_selecao[indice+1]['Nome']):
				temp = lista_selecao[indice+1]
				lista_selecao[indice+1] = lista_selecao[indice]
				lista_selecao[indice] = temp
				Trocou = True
		n += 1
	
	# Ordenando a posicao por goleiro - zagueiro - lateral - meio-campo - atacante
	for indice in range (len(lista_selecao)):
		if (lista_selecao[indice]['Posicao'] == 'goleiro'):
			lista_goleiros += [lista_selecao[indice]]
		
		elif (lista_selecao[indice]['Posicao'] == 'zagueiro'):
			lista_zagueiros += [lista_selecao[indice]]

		elif (lista_selecao[indice]['Posicao'] == 'lateral'):
			lista_laterais += [lista_selecao[indice]]

		elif (lista_selecao[indice]['Posicao'] == 'meio-campo'):
			lista_meiocampos += [lista_selecao[indice]]

		elif (lista_selecao[indice]['Posicao'] == 'atacante'):
			lista_atacantes += [lista_selecao[indice]]


	lista_selecao_final = lista_goleiros + lista_zagueiros + lista_laterais + lista_meiocampos + lista_atacantes
	
	# Imprime em forma de tabela
	print("{:<25}{}".format('NOME','POSICAO'))
	for indice in range(len(lista_selecao_final)):
		print("{:<25}{}".format(lista_selecao_final[indice]['Nome'],lista_selecao_final[indice]['Posicao']))
	

	selecao.close()
	selecoes.close()



# Funcao em que imprime as idades menores do que a idade pedida pelo usuario 
# dos jogaores junto com seus paises e idades ordenados pela idade	
def consulta_idades_menores(idade):
	lista_selecao_nome_pais_idade = []
	lista_idades_menores = []
	
	selecoes = open('selecoes.txt','r')
	conteudo_selecoes = selecoes.readlines()

	# Tira o '\n' que esta presente na lista em cada elemento
	for indice in range (len(conteudo_selecoes)):	
		conteudo_selecoes[indice] = conteudo_selecoes[indice][:-1]
		
	for indice in range (len(conteudo_selecoes)):
		selecao = open(conteudo_selecoes[indice] +'.txt','r')
		conteudo_selecao = selecao.readlines()
		
		for linha in conteudo_selecao:
			lista = passagem_arquivo_lista(linha,conteudo_selecao)
			
			# Transforma cada elemento de uma linha em uma lista de registros		
			jogador = {'Nome': ' ','Posicao': ' '}
			jogador['Nome'] = lista[0]
			jogador['Idade'] = lista[1]
			jogador['Pais'] = conteudo_selecoes[indice]
			lista_selecao_nome_pais_idade += [jogador]

	
	# Ordena os jogadores pela idade em ordem decrescente
	Trocou = True
	n = 1 
	while (Trocou):
		Trocou = False
		for indice in range (len(lista_selecao_nome_pais_idade)-n):
			if(lista_selecao_nome_pais_idade[indice]['Idade'] < lista_selecao_nome_pais_idade[indice+1]['Idade']):
				temp = lista_selecao_nome_pais_idade[indice+1]
				lista_selecao_nome_pais_idade[indice+1] = lista_selecao_nome_pais_idade[indice]
				lista_selecao_nome_pais_idade[indice] = temp
				Trocou = True
		n += 1
	
	# Faz uma lista com jogadores com idades menores do que a pedida pelo usuario
	for indice in range(len(lista_selecao_nome_pais_idade)):
		if (lista_selecao_nome_pais_idade[indice]['Idade'] < idade):
			lista_idades_menores += [lista_selecao_nome_pais_idade[indice]]


	
	
	# Imprime em forma de tabela
	print("{:<20}{:<20}{}".format('NOME','IDADE','PAIS'))
	for indice in range(len(lista_idades_menores)):
		print("{:<20}{:<20}{}".format(lista_idades_menores[indice]['Nome'],lista_idades_menores[indice]['Idade'],lista_idades_menores[indice]['Pais']))
	
	selecoes.close()
	selecao.close()



# Funcao em que dado um time pedido pelo usuario
# imprime os nomes dos jogadores com seus respectivos paises e posicoes desse time
# ordenados pelas categorias de posicoes(goleiro - zagueiro - lateral - meio-campo - atacante) 	
def consulta_time(time):
	lista_selecao_nome_posicao_pais = []
	lista_selecao_nome_posicao_pais_time = []
	lista_goleiros = []
	lista_zagueiros = []
	lista_laterais = []
	lista_meiocampos = []
	lista_atacantes = []
	
	selecoes = open('selecoes.txt','r')
	conteudo_selecoes = selecoes.readlines()

	# Tira o '\n' que esta presente na lista em cada elemento
	for indice in range (len(conteudo_selecoes)):	
		conteudo_selecoes[indice] = conteudo_selecoes[indice][:-1]

	for indice in range (len(conteudo_selecoes)):
		selecao = open(conteudo_selecoes[indice] +'.txt','r')
		conteudo_selecao = selecao.readlines()
	
		for linha in conteudo_selecao:
		
			lista = passagem_arquivo_lista(linha,conteudo_selecao)

			# Transforma cada elemento de uma linha em uma lista de registros
			jogador = {'Nome': ' ','Posicao': ' ','Pais': ' ','Time': ' '}
			jogador['Nome'] = lista[0]
			jogador['Posicao'] = lista[2]
			jogador['Pais'] = conteudo_selecoes[indice]
			jogador['Time'] = lista[3]
			
			lista_selecao_nome_posicao_pais_time += [jogador]

	# Ordenando a posicao por goleiro - zagueiro - lateral - meio-campo - atacante
	for indice in range (len(lista_selecao_nome_posicao_pais_time)):
		if (lista_selecao_nome_posicao_pais_time[indice]['Posicao'] == 'goleiro'):
			lista_goleiros += [lista_selecao_nome_posicao_pais_time[indice]]
		
		elif (lista_selecao_nome_posicao_pais_time[indice]['Posicao'] == 'zagueiro'):
			lista_zagueiros += [lista_selecao_nome_posicao_pais_time[indice]]

		elif (lista_selecao_nome_posicao_pais_time[indice]['Posicao'] == 'lateral'):
			lista_laterais += [lista_selecao_nome_posicao_pais_time[indice]]

		elif (lista_selecao_nome_posicao_pais_time[indice]['Posicao'] == 'meio-campo'):
			lista_meiocampos += [lista_selecao_nome_posicao_pais_time[indice]]

		elif (lista_selecao_nome_posicao_pais_time[indice]['Posicao'] == 'atacante'):
			lista_atacantes += [lista_selecao_nome_posicao_pais_time[indice]]


	lista_selecao_final = lista_goleiros + lista_zagueiros + lista_laterais + lista_meiocampos + lista_atacantes
	
	# Coloca em uma lista somente os jogadores do time pedido pelo usuario
	for indice in range (len(lista_selecao_final)):
		if (lista_selecao_final[indice]['Time'] == time):
			lista_selecao_nome_posicao_pais += [lista_selecao_final[indice]]

	# Imprime em forma de tabela
	print("{:<20}{:<20}{}".format('NOME','POSICAO','PAIS'))
	for indice in range(len(lista_selecao_nome_posicao_pais)):
		print("{:<20}{:<20}{}".format(lista_selecao_nome_posicao_pais[indice]['Nome'],lista_selecao_nome_posicao_pais[indice]['Posicao'],lista_selecao_nome_posicao_pais[indice]['Pais']))

	selecao.close()
	selecoes.close()


	
# Funcao que mostra os 5 primeiros artilheiros com seus respectivos nomes,
# paises e numero de gols, ordenados pelos numeros de gols
def consulta_artilheiros():
	lista_atacantes = []
	lista_selecoes = []
	lista_selecao_nome_posicao_pais_gols = []

	selecoes = open('selecoes.txt','r')
	conteudo_selecoes = selecoes.readlines()
	
	# Tira o '\n' que esta presente na lista em cada elemento
	for indice in range (len(conteudo_selecoes)):	
		conteudo_selecoes[indice] = conteudo_selecoes[indice][:-1]

		
		
	for indice in range (len(conteudo_selecoes)):
		selecao = open(conteudo_selecoes[indice] +'.txt','r')
		conteudo_selecao = selecao.readlines()
	

		
		for linha in conteudo_selecao:
			lista = passagem_arquivo_lista(linha,conteudo_selecao)
			
			# Transforma cada elemento de uma linha em uma lista de registros
			jogador = {'Nome':' ','Posicao':' ','Pais':' ','Gols': -1}
			jogador['Nome'] = lista[0]
			jogador['Posicao'] = lista[2]
			jogador['Pais']	= conteudo_selecoes[indice]
			jogador['Gols'] = int(lista[4])
			lista_selecao_nome_posicao_pais_gols += [jogador]
	
	# Ordena os numeros de gols dos jogadores em ordem decrescente
	Trocou = True
	n = 1 
	while (Trocou):
		Trocou = False
		for indice in range (len(lista_selecao_nome_posicao_pais_gols)-n):
			if(lista_selecao_nome_posicao_pais_gols[indice]['Gols'] < lista_selecao_nome_posicao_pais_gols[indice+1]['Gols']):
					temp = lista_selecao_nome_posicao_pais_gols[indice+1]
					lista_selecao_nome_posicao_pais_gols[indice+1] = lista_selecao_nome_posicao_pais_gols[indice]
					lista_selecao_nome_posicao_pais_gols[indice] = temp
					Trocou = True
		n += 1
	
	# Imprime em forma de tabela
	print("{:<20}{:<20}{}".format('NOME','PAIS','GOLS'))
	for indice in range (len(lista_selecao_nome_posicao_pais_gols)):
		if (indice <= 4):
			print("{:<20}{:<20}{}".format(lista_selecao_nome_posicao_pais_gols[indice]['Nome'],lista_selecao_nome_posicao_pais_gols[indice]['Pais'],lista_selecao_nome_posicao_pais_gols[indice]['Gols']))

	selecao.close()
	selecoes.close()
		

########################## Programa Principal ###################################

def menu():
	# Inicializacao de valores
	
	operacao = 0
	
	while (operacao != 6):
		print('##################### MENU PRINCIPAL ########################')
		print('1. Criar uma selecao')
		print('2. Acrescentar um jogador em uma selecao')
		print('3. Apagar um jogador em uma selecao')
		print('4. Atualizar o numero de gols de um jogador')
		print('5. Consultar')
		print('6. Sair')
		print('#############################################################')
		
		print('ATENCAO: DIGITE A SELECAO E A POSICAO EM MINUSCULO, NOME DO JOGADOR E TIME SOMENTE A PRIMEIRA LETRA MAIUSCULA')
		operacao = int(input())

	
		if (operacao == 1):
			print()
			selecao = input('Informe a selecao: ')
			criar_selecao(selecao)
			print()

		elif (operacao == 2):
			print()
			selecao = input('Informe a selecao: ')
			jogador_nome = input('Informe um nome: ')
			acrescentar_jogador(selecao,jogador_nome)
			print()

		elif (operacao == 3):
			print()
			selecao = input('Informe a selecao: ')
			jogador_nome = input('Informe um nome: ')
			apagar_jogador(selecao,jogador_nome)
			print()

		elif (operacao == 4):
			print()
			jogador_nome = input('Informe o nome: ')
			selecao = input('Informe a selecao: ')
			jogador_gols = input('Informe o NOVO numero de gols: ')
			atualizar_gols(jogador_nome,selecao,jogador_gols)
			print()
	
		elif (operacao == 5):
			print()
			print('##################### MENU CONSULTAR ########################')
			print ('1. Nomes e posicoes dos jogadores de uma selecao')
			print ('2. Nomes, idades e selecao dos jogadores abaixo de uma determinada idade') 
			print ('3. Nomes, posicoes e selecao dos jogadores de um time')
			print ('4. Nomes, selecao, numero de gols dos artilheiros')
			print('5. VOLTAR AO MENU PRINCIPAL')
			print('#############################################################')
			
			operacao_consulta = int(input())
			
			if (operacao_consulta == 1):
				print()
				consulta_jogadores_selecao()
				print()

			elif (operacao_consulta == 2):
				print()
				idade = input('Informe uma idade superior a 10: ')
				consulta_idades_menores(idade)
				print()
				
			elif (operacao_consulta == 3):
				print()
				time = input('Informe um time: ')
				consulta_time(time)
				print()

			elif (operacao_consulta == 4):
				print()
				consulta_artilheiros()
				print()
	
			elif (operacao_consulta == 5):
				menu()
######## Chamada ao menu
menu()

