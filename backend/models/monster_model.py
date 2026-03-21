from database.db import get_connection

class MonsterModel:

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM monsters")
        rows = cur.fetchall()
        conn.close()
        return [
            {"id": r[0], "name": r[1], "hp_dice": r[2], "initiative_dice":r[3]}
            for r in rows
        ]

    @staticmethod
    def get_by_id(monster_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM monsters WHERE id=?",
            (monster_id)
        )
        row = cur.fetchone()
        conn.close()
        if not row:
            return None
        return {"id": row[0], "name": row[1], "hp_dice": row[2], "initiative_dice": row[3]}

    @staticmethod
    def create(name, hp_dice, initiative_dice):
        if name is not None and name.strip() == "":
            raise ValueError("Name cannot be empty")
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO monsters (name, hp_dice, initiative_dice) VALUES (?, ?, ?)",
            (name, hp_dice, initiative_dice)
        )
        conn.commit()
        monster_id = cur.lastrowid
        conn.close()
        return monster_id

    @staticmethod
    def update(monster_id, name=None, hp_dice=None, initiative_dice=None):
        conn = get_connection()
        cur = conn.cursor()
        updates = []
        values = []
        if name is not None:
            updates.append("name=?")
            values.append(name)
        if hp_dice is not None:
            updates.append("hp_dice=?")
            values.append(hp_dice)
        if initiative_dice is not None:
            updates.append("initiative_dice=?")
            values.append(initiative_dice)
        if not updates:
            conn.close()
            return False
        query = f"UPDATE monsters SET {', '.join(updates)} WHERE id=?"
        values.append(monster_id)
        cur.execute(query, values)
        conn.commit()
        success = cur.rowcount > 0
        conn.close()
        return success

    @staticmethod
    def delete(monster_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM monsters WHERE id=?",
            (monster_id,)
        )
        conn.commit()
        success = cur.rowcount > 0
        conn.close()
        return success