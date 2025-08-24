# Christopher Rhyan Poole
# CIS 261
# Movie Guide Part 2

import os

FILENAME = "movies.txt"
SEED_TITLES = [
    "Cat on a Hot Tin Roof",
    "On the Waterfront",
    "Monty Python and the Holy Grail",
]

def ensure_movies_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            for t in SEED_TITLES:
                f.write(t + "\n")

def show_menu():
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def load_movies():
    movies = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            title = line.strip()
            if title:
                movies.append(title)
    return movies

def list_movies(movies):
    if not movies:
        print("No movies found.\n")
        return
    for i, title in enumerate(movies, start=1):
        print(f"{i}. {title}")
    print()

def add_movie(movies):
    title = input("Movie: ").strip()
    if not title:
        print("No title entered. \n")
        return
    movies.append(title)
    save_movies(movies)
    print(f"{title} was added. \n")

def delete_movie(movies):
    try:
        num = int(input("Number: ").strip())
        if 1 <= num <= len(movies):
            removed = movies.pop(num - 1)
            save_movies(movies)
            print(f"{removed} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for t in movies:
            f.write(t + "\n")

def main():
    ensure_movies_file()
    show_menu()
    movies = load_movies()

    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            print("Press any key to continue . . .")
            break
        else:
            print("Not a valid command. Try again.\n")

if __name__ == "__main__":
    main()


