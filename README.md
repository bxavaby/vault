# **Verse Vault**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey?style=flat-square)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/bxavaby/verse-vault?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/bxavaby/verse-vault?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/bxavaby/verse-vault?style=flat-square)


A private library for storing and exploring a collection of short texts, poems, apophthegms, and other literary pieces. This program provides a simple and interactive way to browse, fetch, and manage your library of texts.

---

## **Table of Contents**
- [Demo](#demo)
- [Features](#features)
- [Exemplary Screenshots](#exemplary-screenshots)
- [Current Status](#current-status)
- [Development Tools](#development-tools)
- [Project Structure](#project-structure)
- [Installation and Usage](#installation-and-usage)
- [Customization Guide](#customization-guide)
- [Acknowledgments](#acknowledgments)

---

## **Demo**
![Verse Vault Demo](media/verse.gif)  
*Above: A brief walkthrough of the core features.*

---

## **Features**
- **Browse**: Navigate through your library by category (poems, apophthegms, short stories, others, favorited).
- **Fetch**: Fetch random entries or search by author/genre/title.
- **Customizable**: Easily add new texts or modify the existing content.
- **Minimalist Design**: Simple and clean display focused on readability.

---

## **Exemplary Screenshots**

### **Add Entry Menu**
![Entry Menu Screenshot](media/addnew.png)  
*Above: Sub-menu with types of entry.*

### **Browsing**
![Browsing Texts Screenshot](media/browse.png)  
*Above: Sub-menu with types of search.*

### **Favourites List**
![Favourites Screenshot](media/favs.png)  
*Above: List of preferred titles.*

---

## **Current Status**
### December 2, 2024:
- Basic functionality is implemented, including:
  - Text browsing and randomization features.
  - Modular utilities for managing data, display, and fetching.
  
- The database is structured using JSON files stored in the `library/` directory.

- Git is used for version control with the following commands:
  - `git init`, `git clone`, `git add`, `git commit`, `git push`, `git pull`, `git status`, `git log`.

- PyCache files have been ignored using `.gitignore`.

---

## **Development Tools**
- **Code Editors**:

  - **Micro**:
    - `Ctrl+S` → Save file
    - `Ctrl+Q` → Quit editor
    - `Ctrl+E` → Command mode
  - **Neovim**:
    - `:w` → Save file
    - `:q` → Quit editor
    - `dd` → Delete line
    - `Shift + :` → Command mode
  - **VS Code**:
    - `Ctrl+F` → Find text
    - `Ctrl+Shift+P` → Command Palette
    - `Alt+Shift+F` → Format document
    
- **Git**:
  - All project updates are tracked and committed using Git.
  
- **AI Integration**:
  - Copilot is set up inside VS Code for prompt code assistance and debugging.
  - [Fabric Framework](https://github.com/danielmiessler/fabric):  
      Utilized for its sleek and simple solution to leverage LLMs directly from the command line, enhancing workflow efficiency and allowing for swift experimentation.

---

## **Project Structure**
```plaintext
.
├── README.md
└── verse-vault
    ├── assets
    │   └── logo.txt
    ├── library
    │   ├── apophthegm.json     # apophthegms
    │   ├── other_texts.json    # miscellaneous
    │   ├── poems.json          # poems
    │   └── short_stories.json  # short stories
    ├── main.py                 # entry point
    ├── requirements.txt        # dependencies
    └── utils
        ├── data_manager.py     # handles loading and saving JSON files
        ├── display.py          # handles terminal display and styling
        ├── fetcher.py          # internal fetcher
        └── __init__.py         # module initializer
```

---

## **Installation and Usage**

#### **Prerequisites**
- Python 3.8 or later
- Virtual environment (recommended)

#### **Steps to Run**
1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bxavaby/verse-vault.git
   cd verse-vault
   ```
   
2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the Program**:

   ```bash
   python main.py
   ```
   
---

## **Customization Guide**

### **1. Update the Logo**
Personalize the ASCII art logo displayed on startup.

- **Create Your Logo**:
  Use [Text to ASCII](https://patorjk.com/software/taag/) to create a custom logo.
- **Replace the Logo File**:
  Update the `logo.txt` in the `assets/` directory.
- **Preview**:
  Run the program to see your new logo.

### **2. Add New Categories**
Tweak your library by:

- **Deleting unwanted entries (manually)** in the `library/` directory ->  select the JSON file -> delete any or all entries manually.
- **Adding new enties (manually)** in the `library/` directory ->  select the JSON file -> add new entries manually.
- **Adding new entries (automatically)** run the program -> select option 4 ("Fill up your vault!") -> add the content interactively -> the program appends the new entry to the selected JSON automatically.

### **3. Change Display Colors**

- **Customizing the terminal colors** modify the COLOR_SCHEMES across all files using them (not optimal, will update in the future).

### **3. Customize Favorites**

- **Picking your preferred titles (manually)** in the `library/` directory ->  select the JSON file -> edit the value directly (yes/no).
- **Picking your preferred titles (automatically)** when adding a new entry (option 4), the program requests a boolean value (yes/no).


---

## **Acknowledgments**
This project is inspired by a deep appreciation for literature, philosophy and the desire to create a personal, private library of short-form texts.
