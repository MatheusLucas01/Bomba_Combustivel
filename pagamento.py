def realizar_pagamento(valor_total):
    print(f"\nValor total a pagar: R${valor_total:.2f}")
    while True:
        pagamento = input("Escolha o método de pagamento (1 - Dinheiro, 2 - Cartão): ")
        if pagamento == '1':
            print("Pagamento realizado em dinheiro.")
            break
        elif pagamento == '2':
            print("Pagamento realizado com cartão.")
            break
        else:
            print("Método de pagamento inválido.")
