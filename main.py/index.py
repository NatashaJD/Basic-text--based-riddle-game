

def show_intro():
    print("Welcome to 'The Hijacked Money Truck Mystery'!")
    print("A truck full of money was hijacked while supplying cash to banks.")
    print("As a top detective, it's your job to gather clues, track down the hijackers, and recover the money.")
    print("Navigate through various locations, interact with characters, solve riddles, and unravel the mystery.")
    print("Good luck, detective!")

def main_menu():
    print("\nMain Menu")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def show_instructions():
    print("\nInstructions:")
    print("1. Solve riddles to gather clues about the next location.")
    print("2. Use commands like 'solve riddle' to interact with the game.")
    print("3. Type 'inventory' to check your items and clues.")
    print("4. Type 'hint' to get a hint for the current riddle.")
    print("5. Type 'quit' to exit the game.")

def start_game():
    game_state = {
        "current_location": "crime_scene",
        "inventory": [],
        "clues_found": []
    }

    locations = {
        "crime_scene": {
            "description": "You are at the crime scene. The truck is missing, and there are clues around.",
            "riddle": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?",
            "answer": "map",
            "next_location": "warehouse",
            "clue": "Your next destination is where keys make music.",
            "hint": "It's something you often use to find your way."
        },
        "warehouse": {
            "description": "You are at an abandoned warehouse. It looks like someone has been here recently.",
            "riddle": "What has keys but can't open locks?",
            "answer": "piano",
            "next_location": "docks",
            "clue": "Look for a place where the sea meets the land.",
            "hint": "It produces music and often has many keys."
        },
        "docks": {
            "description": "You are at the docks. There are several boats and crates lying around.",
            "riddle": "What can travel around the world while staying in a corner?",
            "answer": "stamp",
            "next_location": "abandoned_factory",
            "clue": "Head to a place where things are made, now left to decay.",
            "hint": "It's something you place on a letter."
        },
        "abandoned_factory": {
            "description": "You are at an abandoned factory. It's quiet, but you sense that you're getting closer.",
            "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "answer": "echo",
            "next_location": "final_hideout",
            "clue": "Find the echo of the crime at the hideout.",
            "hint": "Think about something that reflects sound."
        },
        "final_hideout": {
            "description": "You have reached the hijackers' hideout. Solve the final riddle to catch them and recover the money.",
            "riddle": "The more you take, the more you leave behind. What am I?",
            "answer": "footsteps",
            "next_location": "solved",
            "clue": "You've found the trail to the final showdown.",
            "hint": "It's something you make when you walk."
        },
        "solved": {
            "description": "Congratulations! You have caught the hijackers and recovered the money truck!",
            "riddle": None,
            "answer": None,
            "next_location": None,
            "clue": None
        }
    }

    def get_hint(location_data):
        if "hint" in location_data:
            return location_data["hint"]
        return "No hints available."

    while True:
        current_location = game_state["current_location"]
        location_data = locations[current_location]
        print(f"\n{location_data['description']}")

        if location_data['riddle']:
            print(f"Riddle: {location_data['riddle']}")
            action = input("Enter your answer or type 'hint' for a hint: ").lower()
            if action == location_data['answer']:
                print("Correct! Here is your clue to the next location:")
                print(f"Clue: {location_data['clue']}")
                game_state["current_location"] = location_data["next_location"]
            elif action == "hint":
                print(f"Hint: {get_hint(location_data)}")
            else:
                print("Incorrect. Try again.")
        else:
            print(location_data['description'])
            print("You win! The mystery is solved!")
            break
        
        if action == "inventory":
            print(f"Inventory: {game_state['inventory']}")
        elif action == "quit":
            break
        else:
            print("Next level")

if __name__ == "__main__":
    show_intro()
    while True:
        choice = main_menu()
        if choice == "1":
            start_game()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
 