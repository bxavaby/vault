import shutil
import random
from colorama import init, Fore, Style

from utils.fetcher import fetch_by_author, fetch_by_genre, fetch_by_title, fetch_favourites
from .data_manager import load_all_libraries, load_library, save_library
from .utils import clear_screen

init(autoreset=True)

def display_logo():
    color_map = {
        '{RED}': Fore.RED,
        '{LIGHTBLACK_EX}': Fore.LIGHTBLACK_EX,
        '{RESET}': Fore.RESET
    }
    
    with open('assets/logo.txt', 'r', encoding='utf-8') as file:
        logo = file.read()

    for placeholder, color in color_map.items():
        logo = logo.replace(placeholder, color)

    print(logo)

def ornament():
    orn = f"""
{Fore.LIGHTBLACK_EX}                                                                   
                                                                                          
_/_/_/_/_/  _/_/_/_/_/  _/_/_/_/_/  _/_/_/_/_/  _/_/_/_/_/ 
                   
{Style.RESET_ALL}
    """
    print(orn)

def display_menu():
    menu_items = [
        "1. Browse your vault",
        "2. Random poem",
        "3. Random excerpt",
        "4. Fill up your vault!",
        "5. Show favourites <3",
        "6. Exit..."
    ]
    menu_items.sort()

    print("\n")
    for item in menu_items:
        print(Fore.RED + item + "\n")
    ornament()
    choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Choose an option: " + Style.RESET_ALL)
    return choice

def display_browse_menu():
    clear_screen()
    ornament()
    print(Fore.RED + "Browse:")
    browse_items = [
        "1. Authors",
        "2. Genres",
        "3. Titles",
        "4. Return to previous menu"
    ]
    browse_items.sort()

    for item in browse_items:
        print("\n" + Fore.RED + item)
    print(Fore.LIGHTBLACK_EX + "═════════════════════════════" + Style.RESET_ALL)
    choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT +  "Choose an option: " + Style.RESET_ALL)
    return choice

def browse_authors():
    all_entries = load_all_libraries()
    authors = sorted(set(entry['author'] for entry in all_entries))
    author = list_and_choose_from_options(authors, "Choose an author: ")
    if author:
        titles = sorted([entry['title'] for entry in all_entries if entry['author'] == author])
        action = list_and_choose_from_options(["Random text", "List all titles"], "Choose an action: ")
        if action == "Random text":
            results = fetch_by_author(author)
            if results:
                entry = random.choice(results)
                clear_screen()
                print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                input("Press Enter to continue...")
        elif action == "List all titles":
            title = list_and_choose_from_options(titles, "Choose a title: ")
            if title:
                text_type = next((entry['type'] for entry in all_entries if entry['title'] == title and entry['author'] == author), None)
                if text_type:
                    entry = fetch_by_title(title, text_type)
                    if entry:
                        clear_screen()
                        print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                        input("Press Enter to continue...")

def browse_genres():
    all_entries = load_all_libraries()
    genres = sorted(set(entry['genre'] for entry in all_entries if entry['genre'] is not None))
    genre = list_and_choose_from_options(genres, "Choose a genre: ")
    if genre:
        titles = sorted([entry['title'] for entry in all_entries if entry['genre'] == genre])
        action = list_and_choose_from_options(["Random text", "List all titles"], "Choose an action: ")
        if action == "Random text":
            text_type = next((entry['type'] for entry in all_entries if entry['genre'] == genre), None)
            if text_type:
                results = fetch_by_genre(genre, text_type)
                if results:
                    entry = random.choice(results)
                    clear_screen()
                    print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                    input("Press Enter to continue...")
        elif action == "List all titles":
            title = list_and_choose_from_options(titles, "Choose a title: ")
            if title:
                text_type = next((entry['type'] for entry in all_entries if entry['title'] == title and entry['genre'] == genre), None)
                if text_type:
                    entry = fetch_by_title(title, text_type)
                    if entry:
                        clear_screen()
                        print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                        input("Press Enter to continue...")
                        
def browse_titles():
    all_entries = load_all_libraries()
    titles = sorted(set(entry['title'] for entry in all_entries))
    title = list_and_choose_from_options(titles, "Choose a title: ")
    if title:
        text_type = next((entry['type'] for entry in all_entries if entry['title'] == title), None)
        if text_type:
            entry = fetch_by_title(title, text_type)
            if entry:
                clear_screen()
                print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                input("Press Enter to continue...")

def add_text():
    clear_screen()
    print(Fore.LIGHTWHITE_EX + "Got a new gem, huh? What kind?" + "\n")
    text_types = {
        '1': 'Apophthegm',
        '2': 'Poem',
        '3': 'Short Story',
        '4': 'Other',
        '5': 'Return to previous menu'
    }
    for key, value in text_types.items():
        print(f"\n{Fore.RED}{key}. {value}")
    print(Fore.LIGHTBLACK_EX + "═════════════════════════════" + Style.RESET_ALL)

    text_type_choice = input(Fore.LIGHTCYAN_EX + "Choose a type: " + Style.RESET_ALL)
    text_type = text_types.get(text_type_choice)

    if not text_type:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Returning to main menu..." + Style.RESET_ALL)
            return

    if text_type == 'Return to previous menu':
       return

    clear_screen()
    print(Fore.LIGHTWHITE_EX + "Let me help you with that:)" + Style.RESET_ALL + "\n")

    title = input(Fore.RED + "1. Title: " + Style.RESET_ALL)
    author = input(Fore.RED + "2. Author: " + Style.RESET_ALL)
    language = input(Fore.RED + "3. Language: " + Style.RESET_ALL)
    genre = input(Fore.RED + "4. Genre: " + Style.RESET_ALL)
    favourite = input(Fore.RED + "5. Favourite (yes/no): " + Style.RESET_ALL)

    clear_screen()
    print("\n" + Fore.LIGHTWHITE_EX + "Well, now I am intrigued… Spit it out!")

    content = []
    prev_line_empty = False
    while True:
        line = input()
        if line == "" and prev_line_empty:
            break
        elif line == "":
            prev_line_empty = True
        else:
            prev_line_empty = False
        content.append(line)
    content = "\n".join(content)

    library = load_library(text_type)
    library.append({
        'title': title,
        'author': author,
        'language': language,
        'genre': genre,
        'type': text_type,
        'content': content,
        'favourite': favourite
    })
    save_library(library, text_type)
    input("Press Enter to continue...")

    print("\n" + Fore.LIGHTWHITE_EX + f"I will be taking a look into your {text_type} while you’re gone, don’t mind me. {author} is a great entertainer of the dead. See you later, fellow bibliophile." + Style.RESET_ALL)

def show_favourites():
    favourites = fetch_favourites()
    if not favourites:
        print(Fore.RED + "No favourites found." + Style.RESET_ALL)
        input("Press Enter to continue...")
        return

    while True:
        clear_screen()
        print(Fore.LIGHTCYAN_EX + "Favourite Titles:" + Style.RESET_ALL)
        for i, entry in enumerate(favourites):
            print(Fore.RED + f"{i + 1}. {entry['title']}" + Style.RESET_ALL)
        print(Fore.RED + f"{len(favourites) + 1}. Back to main menu" + Style.RESET_ALL)
        
        choice = input(Fore.LIGHTCYAN_EX + "Choose a title to view or go back: " + Style.RESET_ALL)
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(favourites):
                entry = favourites[choice - 1]
                clear_screen()
                print(Fore.LIGHTMAGENTA_EX + f"Title: {entry['title']}\n\n{entry['content']}" + Style.RESET_ALL)
                input("Press Enter to continue...")
            elif choice == len(favourites) + 1:
                break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


def list_and_choose_from_options(options, prompt):
    for i, option in enumerate(options):
        print(Fore.RED + f"{i + 1}. {option}" + Style.RESET_ALL)
    print(Fore.RED + f"{len(options) + 1}. Back to previous menu" + Style.RESET_ALL)
    
    choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + prompt + Style.RESET_ALL)
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(options):
            return options[choice - 1]
    return None