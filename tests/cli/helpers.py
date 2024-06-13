from models.author import Author
from models.magazine import Magazine
from models.article import Article

def exit_program():
    print("Goodbye!")
    exit()

def list_articles():
    article = input("Enter article: ")
    authors = Author.articles(article)
    for author in authors:
        print(author)

def create_author():
    name = input("Enter author name: ")
    try:
        author = Author.create(name)
        print(f"Author created: ID ={author}")
    except Exception as e:
        print(f"Error creating Author: ",e)

def create_magazine():
    name = input("Enter magazine name: ")
    category = input ("Enter category: ")
    try:
        magazine = Magazine.create(name, category)
        print(f"Magazine created: ID ={magazine}")
    except Exception as e:
        print(f"Error creating Magazine: ",e)

def create_article():
    title = input("Enter article title: ")
    content = input("Enter article content: ")
    author_id = input("Enter author id: ")
    magazine_id = input("Enter magazine id: ")
    try:
        article = Article.create(title, content, author_id, magazine_id)
        print(f"Article created: ID ={article}")
    except Exception as e:
        print(f"Error creating Article: ",e)

def author_of_the_article():
    article_id = input("Enter article id: ")
    try:
        author = Article.author(article_id)
        print(f"Author of the article: {author}")
    except Exception as e:
        print(f"Error finding author of the article: ",e)


