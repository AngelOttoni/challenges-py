valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())



#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

#TODO: Imprimir a saída no formato especificado neste desafio.

def calcular_preco_final_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago):
    totalHamburguer = valorHamburguer * quantidadeHamburguer
    totalBebida = valorBebida * quantidadeBebida
    precoTotal = totalHamburguer + totalBebida
    troco = valorPago - precoTotal
    
    mensagem = f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}."
    return mensagem

mensagem_pedido = calcular_preco_final_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago)
print(mensagem_pedido)

