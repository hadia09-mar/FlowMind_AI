from app.core.config import settings
from app.core.logger import logger


class StartupManager:
    """Handles application startup."""

    def initialize(self):

        logger.info("=" * 60)
        logger.info("Initializing FlowMind AI...")
        logger.info(f"Project     : {settings.PROJECT_NAME}")
        logger.info(f"Version     : {settings.VERSION}")
        logger.info(f"Environment : {settings.APP_ENV}")
        logger.info("Startup completed successfully.")
        logger.info("=" * 60)