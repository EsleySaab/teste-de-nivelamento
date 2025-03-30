import zipfile
import os

CAMINHO_CSV_MODIFICADO = "web_scraping/dados_extraidos_modificado.csv"

CAMINHO_ZIP = "web_scraping/dados_extraidos_modificado.zip"

def compactar_csv_em_zip(caminho_csv, caminho_zip):
    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv, os.path.basename(caminho_csv))
    print(f"Arquivo ZIP gerado em {caminho_zip}")

compactar_csv_em_zip(CAMINHO_CSV_MODIFICADO, CAMINHO_ZIP)