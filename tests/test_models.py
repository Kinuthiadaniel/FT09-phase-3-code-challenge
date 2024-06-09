import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from database.setup import create_tables

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_name_change(self):
        author = Author(1, "John Doe")
        with self.assertRaises(AttributeError):
            author.name = "Jane Doe"

    def test_author_name_type(self):
        with self.assertRaises(TypeError):
            author = Author(1, 123)

    def test_author_name_length(self):
        with self.assertRaises(ValueError):
            author = Author(1, "")

    def test_author_magazines(self):
        author = Author(1, "John Doe")
        magazines = author.magazines()
        self.assertEqual(len(magazines), 0)  

    def test_article_title_length(self):
        with self.assertRaises(ValueError):
            article = Article(1, "", "Test Content", 1, 1)

    def test_magazine_name_length(self):
        with self.assertRaises(ValueError):
            magazine = Magazine(1, "", "Technology")

    def test_magazine_articles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        articles = magazine.articles()
        self.assertEqual(len(articles), 0)  

    def test_magazine_contributors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 0)  

    def test_magazine_article_titles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        titles = magazine.article_titles()
        self.assertIsNone(titles)  

    def test_magazine_contributing_authors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        contributing_authors = magazine.contributing_authors()
        self.assertIsNone(contributing_authors)  
    

if __name__ == '__main__':
    unittest.main()