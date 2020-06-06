"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.*
"""


#Cria inteiro que gerará, através da função range, uma lista de números de 1-1000
nums = range(1,1000)	

#Inteiro de valor zero para gerar contagem a partir do zero
soma_dos_numeros = 0

#Para cada inteiro contido em nums
for i in nums:

#SE forem divisíveis por 3 ou 5
	if i % 3 == 0 or i % 5 == 0:

		#O resultado será a somatória, desde o número zero, dos resultados do for e do if
		soma_dos_numeors = i + soma_dos_numeros

print(soma_dos_numeros)