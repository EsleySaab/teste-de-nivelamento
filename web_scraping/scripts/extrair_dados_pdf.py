import pdfplumber
import csv

CAMINHO_PDF = "web_scraping/downloads/anexo_1.pdf"

CAMINHO_CSV = "web_scraping/dados_extraidos.csv"

def extrair_dados_pdf():
    with pdfplumber.open(CAMINHO_PDF) as pdf:
        with open(CAMINHO_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Código", "Procedimento", "Descrição", "Categoria", "Valor"])  
            
            for pagina in pdf.pages:
                tabela = pagina.extract_table()
                
                if tabela:
                    for linha in tabela[1:]:  
                        writer.writerow(linha)
            
    print(f"Dados extraídos com sucesso para {CAMINHO_CSV}")

if __name__ == "__main__":
    extrair_dados_pdf()