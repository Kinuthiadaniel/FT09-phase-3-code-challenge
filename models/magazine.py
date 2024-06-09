from database.connection import get_db_connection
class Magazine:
    def __init__(self,name, category): #intialize differently
        self._id = None
        self._name = name
        self._category = category

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?,?)", (self._name, self._category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()


    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and len(name):
            raise ValueError("Name must be a string")
        self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str) and len(category):
            raise ValueError("Category must be a string")
        self._category = category

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id =?", (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return articles  

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id =?""", (self._id,))
        authors = [row for row in cursor.fetchall()]
        conn.close()
        return authors
    
    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id =?", (self._id,))
        titles = [row["title"] for row in cursor.fetchall()]
        if not titles:
            titles = None
        conn.close()
        return titles
    
    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.*, COUNT(articles.id) as article_count FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
            """, (self._id,))
        authors = cursor.fetchall()
        if not authors:
            authors = None
        conn.close()
        return authors
      



