import requests


def get_pokemon_info(pokemon_name: str) -> None:
    """Fetch and print basic Pokemon data from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as exc:
        print(f"Network error: {exc}")
        return

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print(f"Weight: {data['weight']}")
        print(f"Primary Type: {data['types'][0]['type']['name']}")
    elif response.status_code == 404:
        print("Error: Pokemon not found.")
    else:
        print(f"Error: Request failed (status code {response.status_code}).")


if __name__ == "__main__":
    get_pokemon_info("ditto")
