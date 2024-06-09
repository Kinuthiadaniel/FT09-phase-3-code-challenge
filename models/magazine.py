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
        



