from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def executar_scraping(url, classe_tabela, indice_tabela, caminho_saida):
    """
    Faz o scraping da tabela e salva diretamente como CSV.
    """
    print("Iniciando scraping...")
    driver = None
    try:
        # Configura o driver
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)

        # Captura a tabela
        tables = driver.find_elements(By.CLASS_NAME, classe_tabela)
        if len(tables) > indice_tabela:
            table_html = tables[indice_tabela].get_attribute("outerHTML")

            # Converte a tabela HTML para DataFrame
            df = pd.read_html(table_html)[0]

            # Salva o DataFrame diretamente como CSV
            df.to_csv(caminho_saida, index=False, encoding="utf-8")
            print(f"Tabela capturada e salva como CSV em {caminho_saida}.")
        else:
            raise IndexError("Tabela não encontrada no índice fornecido.")
    except Exception as e:
        print(f"Erro no scraping: {e}")
        raise
    finally:
        if driver:
            driver.quit()
            print("Driver encerrado.")
