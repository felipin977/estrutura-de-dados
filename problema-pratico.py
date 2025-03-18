from collections import deque

class SuporteTecnico:
    def __init__(self):
        # Inicializa a fila de chamados
        self.fila = deque()

    def adicionar_chamado(self, chamado):
        """Adiciona um chamado ao final da fila."""
        self.fila.append(chamado)
        print(f"Chamado '{chamado}' adicionado à fila.")
    
    def atender_chamado(self):
        """Atende o chamado no início da fila."""
        if self.fila:
            chamado_atendido = self.fila.popleft()
            print(f"Chamado '{chamado_atendido}' atendido e removido da fila.")
        else:
            print("Não há chamados na fila para atender.")
    
    def exibir_fila(self):
        """Exibe os chamados na fila atual."""
        if self.fila:
            print("Fila de Chamados: ", list(self.fila))
        else:
            print("A fila está vazia.")
            

# Exemplo de uso do sistema de suporte técnico
suporte = SuporteTecnico()

# Adicionando chamados
suporte.adicionar_chamado("Problema de conexão")
suporte.adicionar_chamado("Erro no login")
suporte.adicionar_chamado("Falha na impressão")

# Exibindo a fila
suporte.exibir_fila()

# Atendendo chamados
suporte.atender_chamado()
suporte.atender_chamado()

# Exibindo a fila novamente
suporte.exibir_fila()

# Atendendo o restante dos chamados
suporte.atender_chamado()
suporte.atender_chamado()
