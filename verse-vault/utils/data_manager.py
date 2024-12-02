import json
import os

def load_all_libraries():
    all_entries = []
    for text_type in ['Poem', 'Short Story', 'Apophthegm', 'Other']:
        entries = load_library(text_type)
        print(f"Loaded {len(entries)} entries for type '{text_type}'")
        all_entries.extend(entries)
    print(f"Total loaded entries: {len(all_entries)}")
    return all_entries

def load_library(text_type):
    file_map = {
        'Poem': 'library/poems.json',
        'Short Story': 'library/short_stories.json',
        'Apophthegm': 'library/apophthegm.json',
        'Other': 'library/other_texts.json'
    }
    filename = file_map.get(text_type, 'library/other_texts.json')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_library(library, text_type):
    file_map = {
        'Poem': 'library/poems.json',
        'Short Story': 'library/short_stories.json',
        'Apophthegm': 'library/apophthegm.json',
        'Other': 'library/other_texts.json'
    }
    filename = file_map.get(text_type, 'library/other_texts.json')
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(library, file, ensure_ascii=False, indent=4)

