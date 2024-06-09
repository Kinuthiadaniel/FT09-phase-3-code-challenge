from database.connection import get_db_connection

class Article:
    def __init__(self, title, content, author, magazine):
        self._id = None
        self._title = title
        self._content = content
        self._author = author
        self._magazine = magazine

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?,?,?,?)", (self._title, self._content, self._author.id, self._magazine.id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) and len(title):
            raise ValueError("Title must be a string")
        self._title = title
    
    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
