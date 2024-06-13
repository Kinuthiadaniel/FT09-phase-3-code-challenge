from database.setup import create_tables,drop_table
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from tests.cli.helpers import( exit_program, 
list_articles,
create_author,
create_article,
create_magazine,
author_of_the_article,
contributor,
magazines_by_author
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_author
        elif choice == "2":
            create_article()
        elif choice == "3":
            create_magazine()
        elif choice == "4":
            author_of_the_article()
        elif choice == "5":
            list_articles()
        elif choice == "6":
            contributor()
        elif choice =="7":
            magazines_by_author()

        else:
            print("Invalid choice")

        

    
def menu():
        print("Please select an option")
        print("0. Exit program")
        print("1. Create authors")
        print("2. Create articles")
        print("3. Create magazines")
        print("4. Author of the article")
        print("5. List of articles")
        print("6. List of Contributors")
        print("7. Magazines by author")

        
   

if __name__ == "__main__":
    main()
