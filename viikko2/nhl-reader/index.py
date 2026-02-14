import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("Players from FIN:")
    #print(response)
    
    # I have removed players = [] because the list is giant
    for player_dict in response:
        player = Player(player_dict)
        
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()