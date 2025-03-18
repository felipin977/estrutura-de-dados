# Criando uma lista de tamanho fixo (alocação estática)
tamanho_fixo = 3
array_estatico = [0] * tamanho_fixo  # Lista com 3 elementos, todos zero

print("Array de tamanho fixo:", array_estatico)

# Modificando um valor dentro do array (isso é permitido)
array_estatico[1] = 42

print("Array após modificação:", array_estatico)
