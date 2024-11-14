
# Web Scraping e ETL para Tabelas do BLS

Este projeto realiza **web scraping** de tabelas do site do Bureau of Labor Statistics (BLS), transforma os dados capturados (ETL) e salva os resultados processados como arquivos Excel. O processo é modularizado em três partes: scraping, ETL e orquestração.

## Estrutura do Projeto

```plaintext
.
├── scrapper.py         # Captura os dados da web e salva como CSV
├── etl.py              # Processa o CSV e converte para Excel
├── orquestrador.py     # Orquestra o fluxo de scraping e ETL
├── data/
│   ├── raw/            # Armazena os arquivos CSV brutos
│   ├── processed/      # Armazena os arquivos Excel processados
└── README.md           # Documentação do projeto
```

---

## Fluxo do Projeto

1. **Scraper (`scrapper.py`)**:
   - Captura uma tabela específica do site do BLS.
   - Converte a tabela HTML capturada em um arquivo CSV.
   - Salva o arquivo na pasta `data/raw/`.

2. **ETL (`etl.py`)**:
   - Lê o CSV gerado pelo scraper.
   - Realiza transformações básicas nos dados:
     - Remove linhas vazias.
     - Substitui valores ausentes por zero.
   - Salva os dados processados como Excel na pasta `data/processed/`.

3. **Orquestrador (`orquestrador.py`)**:
   - Coordena as etapas de scraping e ETL.
   - Garante que o fluxo seja executado na ordem correta.

---

## Como Usar

### Pré-requisitos

1. **Instale as dependências**:
   Certifique-se de que você possui o `Python` instalado. Use o seguinte comando para instalar as dependências:

   ```bash
   pip install selenium pandas
   ```

2. **Estrutura de pastas**:
   - Certifique-se de que as pastas `data/raw/` e `data/processed/` existem. Se não, crie-as manualmente ou o script fará isso automaticamente.

### Executando o Script

1. **Rodar o Orquestrador**:
   O `orquestrador.py` é o ponto de entrada do projeto. Ele chamará as funções necessárias para realizar o scraping e o ETL.

   ```bash
   python orquestrador.py
   ```

2. **Arquivos Gerados**:
   - O **CSV bruto** será salvo em: `data/raw/tabela_2.csv`.
   - O **Excel processado** será salvo em: `data/processed/tabela_2_processada.xlsx`.

---

## Explicação do Código

### 1. Scraper (`scrapper.py`)

- **Função Principal**: `executar_scraping(url, classe_tabela, indice_tabela, caminho_saida)`
  - Faz o scraping da tabela HTML com base na URL e salva como CSV.
  - Parâmetros:
    - `url`: URL do site a ser acessado.
    - `classe_tabela`: Classe CSS usada para localizar as tabelas.
    - `indice_tabela`: Índice da tabela desejada.
    - `caminho_saida`: Caminho para salvar o CSV.

### 2. ETL (`etl.py`)

- **Função Principal**: `executar_etl(caminho_csv, caminho_excel)`
  - Processa os dados do CSV e salva como Excel.
  - Parâmetros:
    - `caminho_csv`: Caminho do CSV bruto.
    - `caminho_excel`: Caminho para salvar o Excel processado.

### 3. Orquestrador (`orquestrador.py`)

- **Função Principal**: `executar_processo_completo()`
  - Chama o `executar_scraping` para capturar os dados e o `executar_etl` para processá-los.
  - Configurações:
    - URL do site.
    - Classe CSS da tabela.
    - Índices e caminhos para salvar os arquivos.

---

## Próximos Passos

- Adicionar suporte a múltiplas tabelas.
- Implementar logs detalhados para cada etapa.
- Criar testes automatizados para garantir a confiabilidade do código.

---

Qualquer dúvida ou sugestão, é só chamar! 🚀
