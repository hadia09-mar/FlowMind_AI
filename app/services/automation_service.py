from app.services.database import db


class AutomationService:

    @staticmethod
    def save_workflow(trigger, action):

        db.execute(
            """
            INSERT INTO automation_workflows(
                trigger_name,
                action_name
            )
            VALUES(?,?)
            """,
            (
                trigger,
                action
            )
        )

    @staticmethod
    def get_workflows():

        db.execute(
            """
            SELECT
                trigger_name,
                action_name,
                created_at
            FROM automation_workflows
            ORDER BY id DESC
            """
        )

        return db.fetchall()