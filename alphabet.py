# Desafio
# Dada a letra N do alfabeto, nos diga qual a sua posição.

# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.

letter = input()

position = ord(letter) - ord('A') + 1
print(position)


# DICA SOBRE PYTHON:
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
#or

# letter = input()
# position = ord(letter) - ord('A') + 1
# print(f"The position of '{letter}' in the alphabet is {position}")