from scrapper import executar_scraping
from etl import executar_etl

def executar_processo_completo():
    """
    Orquestra o scraping e o ETL.
    """
    # Configurações
    URL = "https://www.bls.gov/news.release/cpi.htm"
    CLASSE_TABELA = "regular"
    INDICE_TABELA = 1  # Índice da tabela desejada
    CAMINHO_CSV = "data/raw/tabela_2.csv"
    CAMINHO_EXCEL = "data/processed/tabela_2_processada.xlsx"

    try:
        # Etapa 1: Scraping (salva como CSV)
        executar_scraping(URL, CLASSE_TABELA, INDICE_TABELA, CAMINHO_CSV)

        # Etapa 2: ETL (converte CSV para Excel)
        executar_etl(CAMINHO_CSV, CAMINHO_EXCEL)

        print("Processo completo finalizado.")
    except Exception as e:
        print(f"Erro no processo completo: {e}")

if __name__ == "__main__":
    executar_processo_completo()
