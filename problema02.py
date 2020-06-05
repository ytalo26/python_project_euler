import logging
logging.basicConfig(level=logging.DEBUG)


# gerar sequencia fibonacci  
fibNumeros = [1, 2] 

while fibNumeros[-1] < 4000000:
	fibNumeros.append(fibNumeros[-1] + fibNumeros[-2])

logging.debug(fibNumeros) 


# encontrar todos os numeros pares
fibNumeros_pares = []
for fibNumero in fibNumeros:
	if fibNumero % 2 == 0:
		fibNumeros_pares.append(fibNumero)

logging.debug(fibNumeros_pares)


# somar todos os números pares
soma_total = 0
for numero in fibNumeros_pares:
	soma_total += numero

print(soma_total)