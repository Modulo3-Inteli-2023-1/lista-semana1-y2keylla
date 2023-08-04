#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista):
    soma = 0
    for sublist in lista:
        for numero in sublist:
            soma += numero
    return soma

lista_de_listas = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, -1000]]

resultado = soma_dos_aninhados(lista_de_listas)
print(resultado)







# Teste a sua função aqui (caso ache necessário)











