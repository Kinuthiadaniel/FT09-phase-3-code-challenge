from __init__ import CURSOR, CONN

class Author:
    all = {}

    def __init__(self, id=None, name=None):
        if id is not None:
            self.id = id
        self.name = name
        self.save()

    def __repr__(self):
        return f'<Author {self.name}>'

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
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed after the person is instantiated")
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def save(self):
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        author = cls(name=name)
        author.save()
        return author

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(id=row[0])
            author.id= row[1]
            cls.all[author.id] = author
        return author

    
    def articles(self):
        from models.article import Article 
        sql = """
            SELECT articles.id, articles.title, articles.content, articles.author_id, articles.magazine_id
            FROM articles
            INNER JOIN authors ON articles.author_id = authors.id
            WHERE authors.id =?
        """
        CURSOR.execute(sql, (self.id,))
        articles = CURSOR.fetchall()
        return [Article.instance_from_db(row) for row in articles]

    def magazines(self):
        from models.magazine import Magazine 
        sql = """
            SELECT magazines.id, magazines.name, magazines.category
            FROM articles
            LEFT JOIN magazines ON articles.magazine_id = magazines.id
            INNER JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
            GROUP BY magazines.id
        """
        CURSOR.execute(sql, (self.id,))
        magazines = CURSOR.fetchall()
        return [Magazine(*data) for data in magazines]