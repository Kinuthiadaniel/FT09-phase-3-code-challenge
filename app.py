from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    try:
        create_tables()
        print("Tables created")

        author = Author("John")
        print(f"Author created: ID ={author.id}, Name ={author.name}")

        magazine = Magazine("Tech Weekly", "Technology News")
        print(f"Magazine created: ID ={magazine.id}, Name ={magazine.name}")

        article = Article("Python", "Python and Web Applications", author=author, magazine= magazine)
        print(f"Article created: ID ={article.id}, Title ={article.title}, Content ={article.content}, Author={article.author.name}, Magazine={article.magazine.name}")

    
    # Initialize the database and create tables


    # Display results
        print("Author's Articles:", author.articles())
        print("Author's Magazines:", author.magazines())
        print("Magazine's Articles:", magazine.articles())
        print("Magazine's Contributors:", magazine.contributors())
        print("Magazine's Article Titles:", magazine.article_titles())
        print("Magazine's Contributing Authors:", magazine.contributing_authors())
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
