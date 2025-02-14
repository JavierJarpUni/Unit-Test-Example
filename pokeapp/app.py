import requests

def obtener_info_pokemon(nombre):
    """
    Consulta la información de un Pokémon en la PokeAPI.
    Retorna un diccionario con la información si el Pokémon existe, o lanza una excepción si no se encuentra.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return {
            "name": datos["name"],
            "height": datos["height"],
            "weight": datos["weight"]
        }
    else:
        raise Exception("Pokémon no encontrado")

def formatear_datos(datos):
    """
    Formatea los datos de un Pokémon en una cadena para su visualización.
    """
    return f"Nombre: {datos['name']} | Altura: {datos['height']} | Peso: {datos['weight']}"

if __name__ == "__main__":
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
    try:
        info_pokemon = obtener_info_pokemon(nombre_pokemon)
        print(formatear_datos(info_pokemon))
    except Exception as e:
        print(e)
