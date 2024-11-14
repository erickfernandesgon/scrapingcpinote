import pandas as pd
def executar_etl(caminho_csv, caminho_excel):
    """
    Processa os dados do CSV e salva como Excel.
    """
    print("Iniciando ETL...")
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv)

        # Realiza transformações (exemplo de tratamento básico)
        df.columns = df.columns.str.strip()  # Remove espaços dos nomes das colunas
        df = df.dropna(how="all")  # Remove linhas completamente vazias
        df = df.fillna(0)  # Substitui valores ausentes por zero

        # Salva o DataFrame processado como Excel
        df.to_excel(caminho_excel, index=False)  # Remove o argumento 'encoding'
        print(f"ETL concluído. Dados salvos como Excel em {caminho_excel}.")
    except Exception as e:
        print(f"Erro no ETL: {e}")
        raise
