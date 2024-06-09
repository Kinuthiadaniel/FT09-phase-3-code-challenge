from database.connection import get_db_connection
class Author:
    def __init__(self,name):
        self._id = None
        self._name = name
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
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
        if not isinstance(name, str) or len(name):
            raise ValueError("Name must be a string")
        self._name = name

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id =?", (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?""", (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines







    
        
    

