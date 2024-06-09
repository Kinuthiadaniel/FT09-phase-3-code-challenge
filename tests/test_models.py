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
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsNotNone(author.id)

    def test_article_creation(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsNotNone(magazine.id)

    def test_author_name_immutable(self):
        author = Author("John")
        with self.assertRaises(ValueError):
            author.name = "Jane Doe"

    def test_author_magazines(self):
        author = Author("John")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(len(author.magazines()), 1)

    def test_magazine_articles(self):
        author = Author("John")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(len(magazine.articles()), 1)

    def test_magazine_contributors(self):
        author = Author("John")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(len(magazine.contributors()), 1)


    

if __name__ == '__main__':
    unittest.main()