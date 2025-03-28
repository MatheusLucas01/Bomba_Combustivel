import abastecimento
import pagamento
import relatorio

def abastecer_combustivel(tipo_combustivel, relatorios):
    # Preços fixos para gasolina e álcool
    precos = {'gasolina': 2.5, 'alcool': 1.9}
    
    if tipo_combustivel not in precos:
        print("Combustível inválido!")
        return
    
    preco = precos[tipo_combustivel]
    print(f"Preço por litro de {tipo_combustivel}: R${preco:.2f}")
    
    # Solicita o número de litros
    try:
        litros = float(input(f"Quantos litros de {tipo_combustivel} você deseja abastecer? "))
        if litros <= 0:
            raise ValueError("A quantidade de litros deve ser positiva.")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    # Limita a quantidade máxima de combustível
    capacidade_tanque = 50  # Limite de 50 litros
    if litros > capacidade_tanque:
        print(f"O tanque não comporta mais de {capacidade_tanque} litros!")
        return
    
    # Calcula o valor total com desconto
    try:
        valor_total, desconto = abastecimento.calcular_valor(preco, litros)
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    # Realiza o pagamento
    pagamento.realizar_pagamento(valor_total)
    
    # Gera o relatório e adiciona à lista
    relatorio_data = relatorio.gerar_relatorio(tipo_combustivel, litros, valor_total, desconto)
    relatorios.append(relatorio_data)

def main():
    relatorios = []  # Lista para armazenar os relatórios
    while True:
        print("\nEscolha uma opção:")
        print("1 - Abastecer Gasolina")
        print("2 - Abastecer Álcool")
        print("3 - Exibir relatório completo do dia")
        print("4 - Salvar relatório em Excel")
        print("5 - Sair")
        
        try:
            escolha = int(input("Escolha uma opção (1, 2, 3, 4 ou 5): "))
            
            if escolha == 1:
                abastecer_combustivel('gasolina', relatorios)
            elif escolha == 2:
                abastecer_combustivel('alcool', relatorios)
            elif escolha == 3:
                relatorio.exibir_relatorios(relatorios)
            elif escolha == 4:
                relatorio.salvar_relatorio_excel(relatorios)
            elif escolha == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida! Escolha 1, 2, 3, 4 ou 5.")
        except ValueError:
            print("Digite um número válido!")

if __name__ == "__main__":
    main()
