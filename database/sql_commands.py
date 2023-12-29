import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("hw3bot  .sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.commit()

    def sql_select_user(self, tg_id):
        query = "SELECT * FROM telegram_users WHERE telegram_id = ?"
        self.cursor.execute(query, (tg_id,))
        user = self.cursor.fetchone()
        return user

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name)
        )
        self.connection.commit()

    def sql_insert_profile(self, tg_id, nickname, bio, age, gender, phone_number, married, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, bio, age, gender, phone_number, married, photo)
        )
        self.connection.commit()

    def sql_select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "gender": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "gender": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_update_profile(self, nickname, bio, age, gender, photo, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_PROFILE_QUERY,
            (nickname, bio, age, gender, photo, tg_id,)
        )
        self.connection.commit()

    def sql_delete_profile(self, tg_id):
        self.cursor.execute(
            sql_queries.DELETE_PROFILE_QUERY,
            (tg_id,)
        )
        self.connection.commit()



