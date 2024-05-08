import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Task(
            id Integer Primary Key,
            title text,
            description text,
            deadline text,
            priority text,
            completed boolean
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, title, description, deadline, completed, priority):
        self.cur.execute("insert into Task values (NULL,?,?,?,?,?)",
                         (title, description, deadline, completed, priority))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from Task")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from Task where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
def update(self, id, title, description, deadline, completed, priority):
    self.cur.execute(
        "UPDATE Task SET title=?, description=?, deadline=?, completed=?, priority=? WHERE id=?",
        (title, description, deadline, completed, priority, id))
    self.con.commit()