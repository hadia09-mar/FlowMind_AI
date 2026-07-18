from app.services.database import db


class HRService:

    @staticmethod
    def save_report(candidate_name, ats_score):

        db.execute(
            """
            INSERT INTO hr_reports(
                candidate_name,
                ats_score
            )
            VALUES(?,?)
            """,
            (
                candidate_name,
                ats_score
            )
        )

    @staticmethod
    def get_reports():

        db.execute("""
        SELECT
            id,
            candidate_name,
            ats_score,
            created_at
        FROM hr_reports
        ORDER BY id DESC
        """)

        return db.fetchall()