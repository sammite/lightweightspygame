import random
import os
from dataclasses import dataclass
import pyfiglet


@dataclass(frozen=True)
class TextColor:
    GREEN: str = "\033[92m"
    RED: str = "\033[91m"
    YELLOW: str = "\033[93m"
    BLUE: str = "\033[94m"
    MAGENTA: str = "\033[95m"
    CYAN: str = "\033[96m"
    WHITE: str = "\033[97m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"
    RESET: str = "\033[0m"

# Instance to use for dot access
COLOR = TextColor()

def color_print(text, color=COLOR.GREEN):
    print(f"{color}{text}{COLOR.RESET}")



def get_random_city_place():
    city_places = [
        "Coffee shop",
        "Library",
        "Train station",
        "Museum",
        "Airport",
        "Park",
        "Farmer's market",
        "Skyscraper rooftop",
        "Underground metro",
        "Street food stall"
    ]
    vacation_places = [
    "Private island escape",
    "Luxury yacht cruise",
    "5-star beach resort",
    "Ski chalet in the Alps",
    "Gourmet food and wine tour",
    "Luxury African safari",
    "Overwater bungalow retreat",
    "Designer shopping trip in a world capital",
    "Wellness spa in the Swiss mountains"
]   
    places = vacation_places

    return random.choice(places)


def print_spy_banner():
    banner = pyfiglet.figlet_format("Cool Spy Game")
    COLOR = "\033[96m"  # Cyan
    RESET = "\033[0m"
    print(f"{COLOR}{banner}{RESET}")


rando_place = get_random_city_place()


def spy_game(location, num_players):
    print_spy_banner()
    roles = [location] * num_players
    spy_index = random.randint(0, num_players - 1)
    roles[spy_index] = "You are the spy"

    color_print("Pass the device around. Press Enter when you're ready for each player's role.", COLOR.RED)
    for i in range(num_players):
        color_print(f"\nPlayer {i+1}, press Enter to see your role...", COLOR.BLUE)
        input("> ")
        color_print(roles[i])
        color_print("Press Enter to hide your role and pass to the next player.", COLOR.BLUE)
        input("> ")
        print("\n" + "-"*40)
        os.system("clear")



os.system("clear")
spy_game(get_random_city_place(), 4)