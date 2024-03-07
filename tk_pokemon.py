import requests
import tkinter as tk
from PIL import Image, ImageTk
import io


base_url = 'https://pokeapi.co/api/v2/pokemon/'

class Pokemon:
    def __init__(self, name, height, weight, ability, artwork_url):
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.ability = ability
        self.artwork_url = artwork_url
        
    def __str__(self):
        return f"Name: {self.name}\nHeight: {self.height}\nWeight: {self.weight}\nAbility: {self.ability}\nArtwork URL: {self.artwork_url}"
    
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

def fetch_and_display_pokemon():
    pokemon_name = entry.get().lower()
    pokemon = poke.get_pokemon(pokemon_name)
    if pokemon:
        text_info.config(text=str(pokemon))
        load_and_display_image(pokemon.artwork_url)
    else:
        text_info.config(text="Pokémon not found!")

def load_and_display_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        img = Image.open(io.BytesIO(image_data))
        img.thumbnail((200, 200)) 
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    else:
        print("Failed to fetch image")

#main window
root = tk.Tk()
root.title("Pokemon Viewer")
root.geometry("500x500")

#entry field for entering the pokemon
entry = tk.Entry(root)
entry.pack()

#button to get the pokemon
fetch_button = tk.Button(root, text="Get Pokemon", command=fetch_and_display_pokemon)
fetch_button.pack()

#display details
text_info = tk.Label(root, wraplength=400, justify="left")
text_info.pack()

#display image
image_label = tk.Label(root)
image_label.pack()

#create the PokeAPI instance
poke = PokeAPI()

# Run Tkinter
root.mainloop()
