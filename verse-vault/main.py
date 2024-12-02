from colorama import Fore, Style
from utils.display import browse_authors, browse_genres, browse_titles, display_logo, display_menu, display_browse_menu, add_text, ornament, show_favourites
from utils.fetcher import fetch_by_author, fetch_by_genre, fetch_by_title, fetch_random, fetch_favourites
from utils.utils import clear_screen

def main():
    while True:
        clear_screen()
        display_logo()
        choice = display_menu()
        if choice == '1':
            browse_choice = display_browse_menu()
            if browse_choice == '1':
                clear_screen()
                browse_authors()
            elif browse_choice == '2':
                clear_screen()
                browse_genres()
            elif browse_choice == '3':    
                clear_screen()    
                browse_titles()
        elif choice == '2':
            result = fetch_random('Poem')
            if result:
                title, content = result
                clear_screen()
                print(Fore.LIGHTMAGENTA_EX + f"Title: {title}\n\n{content}\n" + Style.RESET_ALL)
                input("Press Enter to continue...")
            else:
                print(Fore.RED + "No poems found in the library." + Style.RESET_ALL)
                input("Press Enter to continue...")
        elif choice == '3':
            result = fetch_random('Other')
            if result:
                title, content = result
                clear_screen()
                print(Fore.LIGHTMAGENTA_EX + f"Title: {title}\n\n{content}\n" + Style.RESET_ALL)
                input("Press Enter to continue...")

            else:
                print(Fore.RED + "No excerpts found in the library." + Style.RESET_ALL)
                input("Press Enter to continue...")
        elif choice == '4':
            add_text()
        elif choice == '5':
            show_favourites()
        elif choice == '6':
            clear_screen()
            print(Fore.LIGHTWHITE_EX + "Be sure to come back. I will be waiting here..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()
