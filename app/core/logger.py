import logging

from app.core.config import settings

# Create log directory if it doesn't exist
settings.LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = settings.LOG_DIR / "flowmind.log"

logger = logging.getLogger("FlowMindAI")
logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)