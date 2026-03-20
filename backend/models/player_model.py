from database.db import get_connection

class PlayerModel:

    @staticmethod
    def get_all():

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM players")

        rows = cur.fetchall()
        conn.close()

        return rows

    @staticmethod
    def get_by_id(player_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM players WHERE id=?",
            (player_id,)
        )

        row = cur.fetchone()
        conn.close()

        return row

    @staticmethod
    def create(name, hp):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO players (name,hp) VALUES (?,?)",
            (name,hp)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def update_hp(player_id, hp):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE players SET hp=? WHERE id=?",
            (hp,player_id)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete(player_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM players WHERE id=?",
            (player_id,)
        )

        conn.commit()
        conn.close()
