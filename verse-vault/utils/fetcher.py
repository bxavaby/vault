import random
from .data_manager import load_all_libraries, load_library


def fetch_by_author(author):
    library = load_all_libraries()
    return [entry for entry in library if entry['author'] == author]

def fetch_by_genre(genre, text_type):
    library = load_all_libraries()
    return [entry for entry in library if entry['genre'] == genre and entry['type'] == text_type]

def fetch_by_title(title, text_type):
    library = load_all_libraries()
    for entry in library:
        if entry['title'] == title:
            return entry
    return None

def fetch_random(text_type):
    all_entries = load_library(text_type)
    if not all_entries:
        return None
    entry = random.choice(all_entries)
    return entry['title'], entry['content']


def fetch_favourites():
    all_entries = load_all_libraries()
    favourites = [entry for entry in all_entries if entry.get('favourite', '').lower() == 'yes']
    return favourites
