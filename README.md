# **Verse Vault**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey?style=flat-square)](#)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)](CONTRIBUTING.md)
[![GitHub issues](https://img.shields.io/github/issues/bxavaby/vault?style=flat-square)](https://github.com/bxavaby/vault/issues)
[![GitHub forks](https://img.shields.io/github/forks/bxavaby/vault?style=flat-square)](https://github.com/bxavaby/vault/network)
[![GitHub stars](https://img.shields.io/github/stars/bxavaby/vault?style=flat-square)](https://github.com/bxavaby/vault/stargazers)


A private library for storing and exploring a collection of short texts, poems, apophthegms, and other literary pieces. This program provides a simple and interactive way to browse, fetch, and manage your library of texts.

---

## **Table of Contents**
- [Demo](#demo)
- [Features](#features)
- [Exemplary Screenshots](#exemplary-screenshots)
- [Current Status](#current-status)
- [Development Tools](#development-tools)
- [Domain Driven Design (DDD)](#domain-driven-design)
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

# **Domain-Driven Design (DDD)**

## 🔎 **A) Event-Storming: Discovering Domains**
To define the functional areas of **Verse Vault**, I conducted **Event-Storming**, ensuring the project remains modular and extensible. The primary objective of this tool is to **help users store, explore, and manage a literary collection interactively**.

## 📖 **Identified Domains**
| **Domain**                     | **Description**                                         | **Type** |
|---------------------------------|---------------------------------------------------------|----------|
| **Vault & Content Management**  | Stores and organizes short texts, poems, and quotes   | **Core** |
| **Discovery & Retrieval**       | Allows users to search, fetch, and randomize entries  | **Core** |
| **User Customization**          | Enables users to modify the database, add/edit texts  | Supporting |
| **Styling & Display**           | Formats terminal output for readability               | Supporting |
| **CLI & Interactive Commands**  | Handles user interactions via command-line interface  | **Core** |
| **Favorites & Personalization** | Lets users mark preferred texts for quick access     | Supporting |


## 📌 **B) Core Domain Chart**
Based on an event-storming process, the ![chart](media/core_domain_chart.odg) found in ![media](media/) highlights **core** and **supporting** domains, illustrating how they interact.

- **CLI & Interactive Input** serves as the main user interface.
- **Vault & Management** handles text storage and retrieval.
- **Discovery & Fetch** helps users explore the content.
- **Styling & Display** ensure readable output.
- **Personalization & Customization** enhance the user experience.

# 📊 **Metrics & Code Quality**

To ensure **high performance, maintainability, and code quality**, Verse Vault was analyzed using **SonarQube and additional metrics**.

## 1️⃣ **SonarQube Code Quality Metrics**
I ran a **SonarQube analysis**, focusing on:
- **Cyclomatic Complexity**: Measures code paths and branching. A **low complexity score** ensures maintainable code.
- **Code Smells**: Identifies non-critical issues that could lead to technical debt.

## 2️⃣ **Code Coverage Metric**
**Test coverage** was evaluated to ensure the codebase is well-tested.

## 📝 **Findings**:
- **Low cyclomatic complexity**, ensuring easy readability.
- A few minor **code smells** (e.g., redundant imports), which have been addressed.
- **Areas for improvement**: Need better test coverage for error-handling and edge cases.

# ✅ **Conclusion**
- **Defined core domains** through **DDD event-storming**, ensuring clear structure.
- **Mapped inter-domain relationships** in a structured diagram.
- **Implemented code quality metrics** with **SonarQube & test coverage**.

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

- **Deleting unwanted entries (manually)** in the `library/` directory >> select the JSON file >> delete any or all entries manually.
- **Adding new enties (manually)** in the `library/` directory >> select the JSON file >> add new entries manually.
- **Adding new entries (automatically)** run the program >> select option 4 ("Fill up your vault!") >> add the content interactively >> the program appends the new entry to the selected JSON automatically.

### **3. Change Display Colors**

- **Customizing the terminal colors** modify the COLOR_SCHEMES across all files using them (not optimal, will update in the future).

### **3. Customize Favorites**

- **Picking your preferred titles (manually)** in the `library/` directory >> select the JSON file >> edit the value directly (yes/no).
- **Picking your preferred titles (automatically)** when adding a new entry (option 4), the program requests a boolean value (yes/no).


---

## **Acknowledgments**
This project is inspired by a deep appreciation for literature, philosophy and the desire to create a personal, private library of short-form texts.
