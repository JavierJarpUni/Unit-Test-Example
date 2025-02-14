# test_app.py

import pytest
from pokeapp.app import obtener_info_pokemon, formatear_datos

# Caso de Uso 1: Consulta de Información de un Pokémon

def test_obtener_info_pokemon_existente(monkeypatch):
    """
    Prueba que simula la respuesta exitosa de la API para un Pokémon existente.
    Se verifica que la función 'obtener_info_pokemon' retorne datos correctos.
    """
    class DummyResponse:
        def __init__(self, json_data, status_code=200):
            self._json_data = json_data
            self.status_code = status_code

        def json(self):
            return self._json_data

    def dummy_get(url):
        # Simula una respuesta positiva cuando se consulta "pikachu"
        if "pikachu" in url:
            return DummyResponse({"name": "pikachu", "height": 4, "weight": 60})
        return DummyResponse({}, status_code=404)

    # Se reemplaza el método requests.get por la función dummy_get
    monkeypatch.setattr("pokeapp.app.requests.get", dummy_get)

    # Ejecución de la prueba
    info = obtener_info_pokemon("pikachu")
    assert info["name"] == "pikachu"
    assert info["height"] == 4
    assert info["weight"] == 60

def test_obtener_info_pokemon_inexistente(monkeypatch):
    """
    Prueba que simula la respuesta de la API para un Pokémon inexistente.
    Se espera que 'obtener_info_pokemon' lance una excepción o maneje el error.
    """
    class DummyResponse:
        def __init__(self, json_data, status_code=404):
            self._json_data = json_data
            self.status_code = status_code

        def json(self):
            return self._json_data

    def dummy_get(url):
        # Siempre retorna una respuesta de error (404) para simular un Pokémon no encontrado
        return DummyResponse({"error": "Not found"}, status_code=404)

    monkeypatch.setattr("pokeapp.app.requests.get", dummy_get)

    with pytest.raises(Exception):
        obtener_info_pokemon("pokemon_inexistente")

# Caso de Uso 2: Visualización de la Información en la Interfaz

def test_formatear_datos():
    """
    Prueba que verifica el formateo correcto de los datos del Pokémon para su visualización.
    Se valida que la función 'formatear_datos' genere una cadena con la información esperada.
    """
    datos = {"name": "pikachu", "height": 4, "weight": 60}
    resultado = formatear_datos(datos)
    
    # Ejemplo de formato esperado: "Nombre: pikachu | Altura: 4 | Peso: 60"
    assert "pikachu" in resultado
    assert "4" in resultado
    assert "60" in resultado
