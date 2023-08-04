#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
lista = [1, 2, 3, 4, 5]

def cumulativa(lista):
    lista_cumulativa = []
    soma = 0

    for i in lista:
        soma += i
        lista_cumulativa.append(soma)

    return lista_cumulativa

resultado = cumulativa(lista)
print(f"A lista de entrada é {lista} e a lista de somas cumulativas é: {resultado}")







# Teste a sua função aqui (caso ache necessário)











