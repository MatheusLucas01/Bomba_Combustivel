import pandas as pd

def gerar_relatorio(tipo_combustivel, litros, valor_total, desconto):
    """Cria um dicionário com os dados do abastecimento."""
    return {
        "Combustível": tipo_combustivel.capitalize(),
        "Litros abastecidos": litros,
        "Desconto aplicado": desconto,
        "Valor total": valor_total
    }

def exibir_relatorios(relatorios):
    """Exibe os relatórios no terminal."""
    if not relatorios:
        print("\nNenhum abastecimento registrado hoje.")
        return
    
    print("\n--- Relatório Completo do Dia ---")
    for i, relatorio in enumerate(relatorios, 1):
        print(f"\nAbastecimento {i}:")
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")
    print("-----------------------------")

def salvar_relatorio_excel(relatorios, nome_arquivo="relatorio_abastecimentos.xlsx"):
    """Salva os relatórios em um arquivo Excel e adiciona o total do dia."""
    if not relatorios:
        print("Nenhum dado para salvar!")
        return
    
    # Criação do DataFrame a partir da lista de dicionários
    df = pd.DataFrame(relatorios)
    
    # Calcular o valor total de todos os abastecimentos no dia
    total_dia = df['Valor total'].sum()
    
    # Adicionar a linha com o total do dia
    total_row = pd.DataFrame({
        "Combustível": ["Total"],
        "Litros abastecidos": [""],
        "Desconto aplicado": [""],
        "Valor total": [total_dia]
    })
    
    # Adiciona a linha de total ao DataFrame
    df = pd.concat([df, total_row], ignore_index=True)
    
    # Salvando o DataFrame em um arquivo Excel
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    print(f"Relatório salvo em {nome_arquivo}")
