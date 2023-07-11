valorPedido = int(input())

def verificar_brinde_especial(valorPedido):
    if valorPedido >= 50.00:
        mensagem = "Parabéns, você ganhou uma sobremesa grátis!"
    else:
        mensagem = "Que pena, você não ganhou nenhum brinde especial."
    
    return mensagem

# Exemplo de uso
#valorPedido = 60.00

mensagem_brinde = verificar_brinde_especial(valorPedido)
print(f"{mensagem_brinde}")