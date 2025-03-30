import os
import zipfile

PASTA_DOWNLOADS = "web_scraping/downloads"
ARQUIVO_ZIP = "web_scraping/anexos.zip"

def compactar_pdfs():
    with zipfile.ZipFile(ARQUIVO_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(PASTA_DOWNLOADS):
            if arquivo.endswith(".pdf"):
                caminho_arquivo = os.path.join(PASTA_DOWNLOADS, arquivo)
                print(f"Adicionando {arquivo} ao arquivo ZIP...")
                zipf.write(caminho_arquivo, arcname=arquivo) 

    print(f"Arquivos compactados com sucesso em {ARQUIVO_ZIP}")

if __name__ == "__main__":
    compactar_pdfs()