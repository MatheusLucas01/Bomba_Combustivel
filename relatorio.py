import pandas as pd
import os

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
    """Salva ou atualiza os relatórios em um arquivo Excel e adiciona o total do dia."""
    if not relatorios:
        print("Nenhum dado para salvar!")
        return
    
    # Se o arquivo já existe, carrega o conteúdo existente
    if os.path.exists(nome_arquivo):
        df = pd.read_excel(nome_arquivo, engine='openpyxl')
    else:
        df = pd.DataFrame()  # Caso contrário, cria um novo DataFrame vazio
    
    # Criação do DataFrame a partir da lista de dicionários
    novos_dados = pd.DataFrame(relatorios)
    
    # Adiciona os novos dados ao DataFrame existente
    df = pd.concat([df, novos_dados], ignore_index=True)
    
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
    
    # Salvando o DataFrame no arquivo Excel
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    print(f"Relatório salvo em {nome_arquivo}")
