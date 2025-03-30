import pytest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../backend')))

from app import app  

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_search_empty_query(client):
    """Testa a busca com uma query vazia."""
    response = client.get('/search?query=')
    assert response.status_code == 200  
    data = json.loads(response.data)
    assert isinstance(data, list)  

def test_search_with_query(client):
    """Testa a busca com uma query válida."""
    query = 'unimed'  
    response = client.get(f'/search?query={query}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  
    assert len(data) > 0 

def test_search_no_results(client):
    """Testa a busca que não retorna resultados."""
    query = 'operadora_inexistente'  
    response = client.get(f'/search?query={query}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 0


def test_search_long_query(client):
    """Testa a busca com uma query excessivamente longa."""
    long_query = "a" * 256
    response = client.get(f'/search?query={long_query}')
    assert response.status_code == 400  
    data = json.loads(response.data)
    assert "error" in data