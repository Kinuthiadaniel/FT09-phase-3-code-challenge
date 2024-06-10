from database.setup import create_tables,drop_table
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    try:
        drop_table()
        create_tables()
        print("Tables created")
        # author_name = input("Enter author's name: ")
        # magazine_name = input("Enter magazine name: ")
        # magazine_category = input("Enter magazine category: ")
        # article_title = input("Enter article title: ")
        # article_content = input("Enter article content: ")


        author = Author(1, "John")
        print(f"Author created: ID ={author.id}, Name ={author.name}")

        magazine = Magazine(1,"Tech Weekly", "Technology News")
        print(f"Magazine created: ID ={magazine.id}, Name ={magazine.name}, Category = {magazine.category}" )

        article = Article(1,"Python", "Python and Web Applications", 1,1)
        print(f"Article created: ID ={article.id}, Title ={article.title}, Content ={article.content}, Author={article.author_id}, Magazine={article.magazine_id}")
        

        author1 = Author.create( "John")
        print(f"Author created: ID ={author1.id}, Name ={author1.name}")

        magazine1 = Magazine.create(1,"name","Tech_Weekly" )
        print(f"Magazine created: ID ={magazine1.id}, Name ={magazine1.name}, Category = {magazine1.category}" )

        article1 = Article.create(1, "Python", "Python and Web Applications,", 1, 1)
        print(f"Article created: ID ={article1.id}, Title ={article1.title}, Content ={article1.content}, Author={author1}, Magazine={author1}")

    
    # Initialize the database and create tables


    # Display results
        print("Author's Articles:", author.articles())
        print("Author's Magazines:", author.magazines())
        print("Magazine's Articles:", magazine.articles())
        print("Magazine's Contributors:", magazine.contributors())
        print("Magazine's Article Titles:", magazine.article_titles())
        print("Magazine's Contributing Authors:", magazine.contributing_authors())
        print("Article's Authors:", article.author())
        print("Article's Magazine:", article.magazine())
 

        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
