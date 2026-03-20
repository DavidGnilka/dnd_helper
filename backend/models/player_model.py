from database.db import get_connection

class PlayerModel:

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM players")
        rows = cur.fetchall()
        conn.close()
        return [
            {"id": r[0], "name": r[1], "hp": r[2]}
            for r in rows
        ]

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
        if not row:
            return None
        return {"id": row[0], "name": row[1], "hp": row[2]}

    @staticmethod
    def create(name, hp):
        if name is not None and name.strip() == "":
            raise ValueError("Name cannot be empty")
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO players (name,hp) VALUES (?,?)",
            (name,hp)
        )
        conn.commit()
        player_id = cur.lastrowid
        conn.close()
        return player_id

    @staticmethod
    def update(player_id, name=None, hp=None):
        conn = get_connection()
        cur = conn.cursor()
        updates = []
        values = []
        if hp is not None:
            updates.append("hp=?")
            values.append(hp)
        if name is not None:
            updates.append("name=?")
            values.append(name)
        if not updates:
            conn.close()
            return False
        query = f"UPDATE players SET {', '.join(updates)} WHERE id=?"
        values.append(player_id)
        cur.execute(query, values)
        conn.commit()
        success = cur.rowcount > 0
        conn.close()
        return success

    @staticmethod
    def delete(player_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM players WHERE id=?",
            (player_id,)
        )
        conn.commit()
        success = cur.rowcount > 0
        conn.close()
        return success
