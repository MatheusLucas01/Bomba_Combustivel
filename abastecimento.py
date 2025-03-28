# abastecimento.py

def calcular_valor(preco, litros):
    if litros <= 0:
        raise ValueError("A quantidade de litros deve ser positiva.")
    
    if preco <= 0:
        raise ValueError("O preço do combustível deve ser positivo.")
    
    # Aplica desconto dependendo da quantidade de litros
    if litros <= 20:
        desconto = litros * preco * 0.03  # 3% de desconto
    else:
        desconto = litros * preco * 0.05  # 5% de desconto
    
    valor_total = (litros * preco) - desconto
    return valor_total, desconto
