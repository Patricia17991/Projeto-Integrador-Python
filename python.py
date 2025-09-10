# Lista para armazenar os números inseridos pelo usuário
numeros = []

# Laço 'while' para coletar a entrada do usuário
while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")
    
    # Condição de parada do laço 'while'
    if entrada.lower() == 'sair':
        break
    
    try:
        # Tenta converter a entrada para um número inteiro
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        # Se a entrada não for um número válido, exibe uma mensagem de erro
        print("Entrada inválida. Por favor, digite um número.")

# ---

# Verifica se a lista de números não está vazia
if numeros:
    # Variável para armazenar a soma dos números
    soma = 0
    
    # Laço 'for' para somar todos os números na lista
    for num in numeros:
        soma += num
        
    # Calcula a média
    media = soma / len(numeros)
    
    # Exibe os resultados
    print("\n--- Resultados ---")
    print(f"Você inseriu os seguintes números: {numeros}")
    print(f"A soma total é: {soma}")
    print(f"A média é: {media:.2f}") # O .2f formata a média com duas casas decimais
else:
    print("\nNenhum número foi inserido.")
    
    
#COMO O CÓDIGO FUNCIONA
#while True:: Este é o laço while. Ele cria um ciclo infinito que só para quando a condição break é ativada.

#entrada = input(...): Pede ao usuário para digitar algo.

#if entrada.lower() == 'sair':: Se o usuário digitar "sair" (não importa se é com letras maiúsculas ou minúsculas), o comando break é executado, e o laço while é interrompido.

#try...except: Essa estrutura é usada para lidar com possíveis erros. Se o usuário digitar algo que não é um número, a parte except ValueError exibe uma mensagem de erro em vez de travar o programa.

#for num in numeros:: Depois que o laço while termina, este laço for percorre cada item (chamado de num) na lista de numeros e adiciona-o à variável soma.

#soma += num: É o mesmo que soma = soma + num. É uma forma mais curta de escrever.

#print(f"..."): Isso usa uma f-string para incluir variáveis diretamente dentro de uma string.



#######################################################################################################3


#O Laço while (Enquanto)

#O laço while repete um bloco de código enquanto uma condição for verdadeira. Pense nele como uma verificação contínua: ele executa a ação, volta e verifica a condição de novo. Se a condição ainda for verdadeira, ele executa de novo, e assim por diante. Se a condição se tornar falsa em algum momento, o laço para.

#Como funciona:

   # O Python verifica a condição.

    #Se a condição for verdadeira, o código dentro do laço é executado.

    #Após a execução, o Python volta ao início e verifica a condição novamente.

    #Se a condição for falsa, o laço é encerrado, e o programa continua a partir do código que está depois do while.