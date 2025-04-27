from src.repositories.interfaces.repository import Repository
import sqlite3

class SQLUserRepository(Repository):
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def create(self, user):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', 
                       (user.id, user.name, user.email))
        self.conn.commit()

    def read(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, email FROM users WHERE id=?', (user_id,))
        row = cursor.fetchone()
        if row:
            from src.entities.user import User  # Import here to avoid circular imports
            return User(id=row[0], name=row[1], email=row[2], roles=[])
        return None

    def update(self, user):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE users SET name=?, email=? WHERE id=?', 
                       (user.name, user.email, user.id))
        self.conn.commit()

    def delete(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, email FROM users')
        rows = cursor.fetchall()
        from src.entities.user import User
        return [User(id=row[0], name=row[1], email=row[2], roles=[]) for row in rows]
