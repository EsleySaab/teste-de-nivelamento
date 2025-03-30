import zipfile
import os

def compactar_csv_em_zip(caminho_csv, caminho_zip):
  with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(caminho_csv, os.path.basename(caminho_csv))
  print(f"Arquivo compactado com sucesso em {caminho_zip}")

CAMINHO_CSV = "web_scraping/dados_extraidos.csv"
CAMINHO_ZIP = "web_scraping/dados_extraidos.zip"

compactar_csv_em_zip(CAMINHO_CSV, CAMINHO_ZIP)
