from app.core.logger import logger


def log_exception(error: Exception):
    """
    Log unexpected exceptions.
    """

    logger.exception(f"Unexpected Error: {error}")