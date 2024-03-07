from wrapper import PokeAPI

def main():
    print("Welcome to the Pokemon API!")
    while True:
        name = input("Enter the name of a Pokemon or Quit:\n").lower()
        poke = PokeAPI()
        pokemon = poke.get_pokemon(name)
        if name.lower() == "quit":
            print("Goodbye!")
            break
        elif pokemon:
            print(pokemon)
        else:
            print(f"Pokemon {name} not found")

if __name__ == "__main__":
    main()
