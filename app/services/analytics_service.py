from app.services.database import db


class AnalyticsService:

    @staticmethod
    def get_stats():

        stats = {}

        db.execute("SELECT COUNT(*) FROM hr_reports")
        stats["reports"] = db.fetchone()[0]

        db.execute("SELECT COUNT(*) FROM activity_logs")
        stats["activities"] = db.fetchone()[0]

        db.execute("SELECT COUNT(*) FROM automation_workflows")
        stats["workflows"] = db.fetchone()[0]

        db.execute("SELECT COUNT(*) FROM documents")
        stats["documents"] = db.fetchone()[0]

        stats["agents"] = 8
        stats["database"] = "Connected"

        return stats