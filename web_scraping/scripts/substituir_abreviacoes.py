import csv

abreviacoes_para_descricoes = {
    "OD": "Óptico-Dentário", 
    "AMB": "Ambulatório",  
}

def substituir_abreviacoes(caminho_csv_original, caminho_csv_modificado):
    with open(caminho_csv_original, mode="r", encoding="utf-8") as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        with open(caminho_csv_modificado, mode="w", newline="", encoding="utf-8") as novo_csv:
            writer = csv.writer(novo_csv)
            
            for i, linha in enumerate(reader):
                if i == 0:
                    writer.writerow(linha)
                else:
                    linha_modificada = [abreviacoes_para_descricoes.get(celula, celula) for celula in linha]
                    writer.writerow(linha_modificada)

    print(f"Arquivo CSV com abreviações substituídas gerado em {caminho_csv_modificado}")

CAMINHO_CSV_ORIGINAL = "web_scraping/dados_extraidos.csv"
CAMINHO_CSV_MODIFICADO = "web_scraping/dados_extraidos_modificado.csv"

substituir_abreviacoes(CAMINHO_CSV_ORIGINAL, CAMINHO_CSV_MODIFICADO)