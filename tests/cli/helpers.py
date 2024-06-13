from models.author import Author
from models.magazine import Magazine
from models.article import Article

def exit_program():
    print("Goodbye!")
    exit()

def list_articles():
    author_id = int(input("Enter author id: "))
    author = Author.find_by_id(author_id)
    articles = author.articles()
    for article in articles:
        print(article)

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
    author_id = int(input("Enter author id: "))
    magazine_id = int(input("Enter magazine id: "))
    try:
        article = Article.create(title, content, author_id, magazine_id)
        print(f"Article created: ID ={article}")
    except Exception as e:
        print(f"Error creating Article: ",e)

def author_of_the_article():
    article_id = int(input("Enter article id: "))
    article = Article.find_by_id(article_id)
    try:
        author = article.author()
        print(f"Author of the article: {author}")
    except Exception as e:
        print(f"Error finding author of the article: ",e)

def contributor():
    magazine_id = int(input("Enter magazine id: "))
    try:
        magazine = Magazine.find_by_id(magazine_id)
        print(type(magazine_id))
        contributors = magazine.contributors()
        print(contributors)
        for contributor in contributors:
            print(contributor)
    except Exception as e:
        print(f"Error finding contributors: ",e)

def magazines_by_author():
    author_id = int(input("Enter author id: "))
    author = Author.find_by_id(author_id)
    try:
        magazines = author.magazines()
        for magazine in magazines:
            print(magazine)
    except Exception as e:
        print(f"Error finding magazines: ",e)



