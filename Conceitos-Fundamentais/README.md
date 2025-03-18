
# 📌 Alocação Estática

A **alocação estática** ocorre quando a quantidade de memória necessária para armazenar uma estrutura de dados é determinada em tempo de compilação. Ou seja, o tamanho do espaço de memória a ser utilizado é fixo e não pode ser alterado durante a execução do programa. Um exemplo clássico de alocação estática são os arrays em linguagens como C e C++.

## Características da Alocação Estática:
- O tamanho da estrutura de dados é conhecido em tempo de compilação.
- A memória é alocada uma vez e não pode ser alterada.
- Não há sobrecarga para gerenciar a memória durante a execução.
- Pode resultar em desperdício de memória se a alocação for maior que a necessária.

## Exemplos de Alocação Estática:

Em **Python**, o exemplo mais próximo de alocação estática seria uma lista de tamanho fixo, embora Python seja tipicamente uma linguagem de alocação dinâmica.

### Exemplo de Alocação Estática em Python:

```python
# Exemplo de alocação estática
# Uma lista com tamanho fixo de 5 elementos

tamanho_fixo = 5
array = [0] * tamanho_fixo  # Inicializando um array com 5 elementos, todos 0

print(array)  # [0, 0, 0, 0, 0]

# Não podemos redimensionar o array diretamente em Python, mas podemos simular alocação estática
