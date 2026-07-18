from app.services.database import db


class DashboardService:

    @staticmethod
    def get_counts():

        data = {}

        db.execute("SELECT COUNT(*) FROM hr_reports")
        data["reports"] = db.fetchone()[0]

        db.execute("SELECT COUNT(*) FROM activity_logs")
        data["activities"] = db.fetchone()[0]

        return data