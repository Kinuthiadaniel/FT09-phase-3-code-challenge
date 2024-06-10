from __init__ import CURSOR, CONN

class Magazine:
    all = {}

    def __init__(self, id, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category
        self.save()

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self._id = value
        else:
            raise TypeError("id must be of type int")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def save(self):
        sql = """
            INSERT INTO magazines (name, category)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.category,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        if hasattr(self, '_id'):
            sql = """
                UPDATE magazines
                SET name = ?, category = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.category, self.id))
            CONN.commit()

    @classmethod
    def create(cls,id, name, category):
        magazine = cls(id = id, name=name, category=category)
        magazine.save()
        return magazine

    def articles(self):
        from models.article import Article  
        sql = """
            SELECT articles.id, articles.title, articles.content, articles.author_id, articles.magazine_id
            FROM articles
            INNER JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        """
        CURSOR.execute(sql, (self.id,))
        articles = CURSOR.fetchall()
        return [Article(*row) for row in articles]

    def contributors(self):
        from models.author import Author  
        sql = """
            SELECT authors.id, authors.name
            FROM articles
            INNER JOIN authors ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
        """
        CURSOR.execute(sql, (self.id,))
        contributors = CURSOR.fetchall()
        return [Author(*row) for row in contributors]

    def article_titles(self):
        sql = """
            SELECT title
            FROM articles
            WHERE magazine_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        titles = CURSOR.fetchall()
        return [title[0] for title in titles] if titles else None

    def contributing_authors(self):
        from models.author import Author  
        sql = """
            SELECT authors.id, authors.name
            FROM articles
            INNER JOIN authors ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(*) > 2
        """
        CURSOR.execute(sql, (self.id,))
        contributors_data = CURSOR.fetchall()
        return [Author(*row) for row in contributors_data] if contributors_data else None