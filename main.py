# Passo 1: Solicita 5 números inteiros do usuário e armazena em uma lista
numeros = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

# Passo 2: Calcula o maior, o menor e a soma dos elementos da lista
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Passo 3: Imprime os resultados
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma de todos os números:", soma)1