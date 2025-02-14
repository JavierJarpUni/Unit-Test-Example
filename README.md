# Unit-Test-Example
Unit tests for a Pokemon Extraction App built in python using PokeAPI.

# Video
[![Explanation](https://img.youtube.com/vi/QqKp_a3uj2g/0.jpg)](https://youtu.be/1RqX6lD-8dI)

## Explanation

### 1. **Test: `test_obtener_info_pokemon_existente`**
   - **Purpose:** 
     This test simulates a successful response from the API when querying for an existing Pokémon (e.g., "pikachu").
   - **How it works:**
     - A mock API response is created using a `DummyResponse` class.
     - The `dummy_get` function simulates a successful response for a "pikachu" query with the appropriate JSON data: 
       ```json
       {"name": "pikachu", "height": 4, "weight": 60}
       ```
     - The `requests.get` method is replaced with `dummy_get` using the `monkeypatch` method to simulate this behavior during the test.
   - **Assertions:**
     - Verifies that the returned data contains the correct Pokémon name, height, and weight.
     ```python
     assert info["name"] == "pikachu"
     assert info["height"] == 4
     assert info["weight"] == 60
     ```

### 2. **Test: `test_obtener_info_pokemon_inexistente`**
   - **Purpose:**
     This test simulates a failed API response when querying for a non-existent Pokémon.
   - **How it works:**
     - The `DummyResponse` class simulates a 404 error response with the following JSON error message:
       ```json
       {"error": "Not found"}
       ```
     - The test verifies that the `obtener_info_pokemon` function raises an exception when a non-existent Pokémon is queried.
   - **Assertions:**
     - The test expects an exception to be raised when querying for a non-existent Pokémon:
     ```python
     with pytest.raises(Exception):
         obtener_info_pokemon("pokemon_inexistente")
     ```

### 3. **Test: `test_formatear_datos`**
   - **Purpose:**
     This test verifies that the `formatear_datos` function correctly formats the Pokémon data into a string for display.
   - **How it works:**
     - A sample Pokémon dictionary is provided as input:
       ```python
       {"name": "pikachu", "height": 4, "weight": 60}
       ```
     - The `formatear_datos` function is expected to return a string formatted as:
       ```
       Nombre: pikachu | Altura: 4 | Peso: 60
       ```
   - **Assertions:**
     - The test checks that the formatted string contains the expected values:
     ```python
     assert "pikachu" in resultado
     assert "4" in resultado
     assert "60" in resultado
     ```

## Requirements
- Python 3.11+
- pytest library for running tests

## Running the Tests
To run the tests, you need to create your own virtual environment.
### Steps
1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**
   MacOS/Linux
   ```bash
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
### Run the tests
```bash
pytest -v tests/
```


