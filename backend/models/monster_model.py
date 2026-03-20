from database.db import get_connection

class MonsterModel:

    @staticmethod
    def get_all():

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM monsters")

        rows = cur.fetchall()
        conn.close()

        return rows

    @staticmethod
    def create(name, hp_dice, initiative_dice):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO monsters (name, hp_dice, initiative_dice) VALUES (?, ?, ?)",
            (name, hp_dice, initiative_dice)
        )

        conn.commit()
        conn.close()