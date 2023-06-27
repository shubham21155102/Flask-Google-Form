import sqlite3
class FormData:
    def __init__(self, name, email, roll, branch, year, dob):
        self.name = name
        self.email = email
        self.roll = roll
        self.branch = branch
        self.year = year
        self.dob = dob
    def save(self):
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO formdata (name, email, roll, branch, year, dob) VALUES (?, ?, ?, ?, ?, ?)",
                      (self.name, self.email, self.roll, self.branch, self.year, self.dob))
            conn.commit()

    @staticmethod
    def get_all():
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM formdata")
            rows = c.fetchall()

            data = []
            for row in rows:
                form_data = FormData(*row)
                data.append(form_data)

        return data

    @staticmethod
    def is_email_unique(email):
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM formdata WHERE email=?", (email,))
            count = c.fetchone()[0]
            return count == 0
