# -*- coding: UTF-8 -*-

# [^ ] - não tem espaço
# * - tudo
# [^ ]* - tudo que não tenha espaço
# [r|R] - Tenha uma letra R no meio(maiúscula ou minúscula)
# [^|\.] - Não tenha espaço ou . no final(descape \.)


import re



## ---- search, este método pesquisa e retorna primeira instancia encontrada usando expressões regex
frase = "O rato roeu a roupa do rei de roma."

busca = re.search("[^ ]*[r|R][^ |\.]*", frase)

if busca:
	print("Primeira palavra da busca acima com search: ",busca.group())
	

	

## ---- findAll, retorna uma lista com todos os resultados encontrados através da expressão regular
busca = re.findall("[^ ]*[r|R][^ |\.]*", frase)

if busca:
	print("Todas as palavras da busca acima com findall: ",busca)
	
	
	
	
## ---- Split, retorna lista criada através do caracter de corte na frase
busca = re.split(" ", frase)

if busca:
	print("split: ",busca)
	
	
	
	
## ---- Procurar email na frase
busca = re.findall("[A-Za-z0-9]*[@][^ ]*[^ \)]", "Meu email é lipe2018@gmail.com e sempre olho a caixa de mensagem!(lipe2016@gmail)")

if busca:
	print("pesquisar email(s) em frase: ",busca)
