#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
a = 10
b = 12

def multiplas_operacoes(a, b):
    # Soma
    soma = a + b

    # Subtração
    subtracao = a - b

    # Multiplicação
    multiplicacao = a * b

    # Divisão com tratamento de divisão por zero
    if b != 0:
        divisao = a / b
    else:
        divisao = 0

    return soma, subtracao, multiplicacao, divisao

resultado = multiplas_operacoes(a, b)
print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])







# Teste a sua função aqui (caso ache necessário)











