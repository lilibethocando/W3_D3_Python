import requests

base_url = 'https://pokeapi.co/api/v2/pokemon/'

class Pokemon:
    def __init__(self, name, height, weight, ability, artwork_url):
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.ability = ability
        self.artwork_url = artwork_url
        
    def __str__(self):
        return f"Name: {self.name}\nHeight: {self.height}\nWeight: {self.weight}\nAbility: {self.ability}\nArtwork: {self.artwork_url}"
    
    def __repr__(self):
        return f"<Pokemon|{self.name}>"
    
class PokeAPI:
    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    def __get(self, pokemon):
        request_url= f"{self.base_url}{pokemon}"
        response = requests.get(url=request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None

        
    def get_pokemon(self, pokemon):
        data = self.__get(pokemon)
        if data:
            artwork_url = data['sprites']['other']['official-artwork']['front_default']
            return Pokemon(data['name'], data['height'], data['weight'], data['abilities'][0]['ability']['name'], artwork_url)
        else:
            return None
        
