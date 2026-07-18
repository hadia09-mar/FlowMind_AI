from app.services.database import db


class ActivityService:

    @staticmethod
    def log(module, activity):

        db.execute(
            """
            INSERT INTO activity_logs(
                module,
                activity
            )
            VALUES(?,?)
            """,
            (
                module,
                activity
            )
        )

    @staticmethod
    def get_logs():

        db.execute(
            """
            SELECT
                module,
                activity,
                created_at
            FROM activity_logs
            ORDER BY id DESC
            LIMIT 20
            """
        )

        return db.fetchall()