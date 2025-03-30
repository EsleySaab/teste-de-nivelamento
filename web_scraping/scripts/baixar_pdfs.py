import os
import requests
from bs4 import BeautifulSoup # type: ignore

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

PASTA_DOWNLOADS = "web_scraping/downloads"

def criar_pasta():
  if not os.path.exists(PASTA_DOWNLOADS):
    os.makedirs(PASTA_DOWNLOADS)

def obter_links_pdfs():
  resposta = requests.get(URL)
  if resposta.status_code != 200:
    print("Erro ao acessar a página")
    return []
  
  soup = BeautifulSoup(resposta.text, "html.parser")
  links = soup.find_all("a", href=True)

  pdf_links = [link["href"] for link in links if link["href"].endswith(".pdf")]
  return pdf_links

def baixar_pdfs():
  criar_pasta()
  pdf_links = obter_links_pdfs()

  if not pdf_links:
    print("Nenhum PDF encontrado.")
    return
  
  for url in pdf_links:
    nome_arquivo = url.split("/")[-1]
    caminho_arquivo = os.path.join(PASTA_DOWNLOADS, nome_arquivo)

    print(f"Baixando: {nome_arquivo}")
    resposta = requests.get(url)

    with open(caminho_arquivo, "wb") as arquivo:
      arquivo.write(resposta.content)
      
  print("Download concluído!")

if __name__ == "__main__":
  baixar_pdfs()
