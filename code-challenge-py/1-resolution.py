nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

def informar_tempo_entrega(nomeRestaurante, tempoEstimadoEntrega):
    mensagem = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
    return mensagem

mensagem_entrega = informar_tempo_entrega(nomeRestaurante, tempoEstimadoEntrega)
print(mensagem_entrega)
