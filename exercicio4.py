#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
entrada = [1,2,3,4,5,5]

def tem_duplicados(lista):
    tamanho_lista = len(lista)
    saida = False
    for numero in range(tamanho_lista):
        
        for outro_numero in range(numero + 1, tamanho_lista):
            if lista[numero] == lista[outro_numero]:
                saida = True
    return saida        

print(tem_duplicados(entrada))







# Teste a sua função aqui (caso ache necessário)











