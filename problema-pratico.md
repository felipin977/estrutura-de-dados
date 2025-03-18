### Desafio Prático: Gestão de Chamados de Suporte Técnico
# Descrição do Desafio
Em um departamento de suporte técnico, os pedidos de assistência dos clientes precisam ser atendidos de acordo com a sequência de chegada, garantindo um processo justo e eficiente. Para isso, é fundamental um sistema que registre os pedidos e os processe de maneira organizada, respeitando a ordem de chegada.

### Solução com Filas
A estrutura de fila (Queue) é a mais indicada, pois segue o princípio FIFO (First In, First Out), ou seja, o primeiro pedido registrado será o primeiro a ser atendido.

### Como Funciona:
1. Chamados novos são inseridos no final da fila.
2. O atendimento é feito removendo o pedido do início da fila.
3. O sistema pode mostrar a fila atual para monitoramento.
