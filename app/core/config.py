from pathlib import Path
from dotenv import load_dotenv
import os

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()

class Settings:
    """Central configuration for FlowMind AI."""

    PROJECT_NAME = "FlowMind AI"
    VERSION = "1.0.0"

    BASE_DIR = Path(__file__).resolve().parents[2]

    APP_DIR = BASE_DIR / "app"
    DATA_DIR = BASE_DIR / "data"
    LOG_DIR = BASE_DIR / "logs"

    UPLOAD_DIR = DATA_DIR / "uploads"
    VECTOR_DB_DIR = DATA_DIR / "vector_db"
    SQLITE_DIR = DATA_DIR / "sqlite"

    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    @classmethod
    def create_directories(cls):
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        cls.VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
        cls.SQLITE_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)


settings = Settings()

settings.create_directories()