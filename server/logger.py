import logging


def setup_logger(name: str = "Medical Assistant"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger


logger = setup_logger()

logger.info("RAG Process started !")
logger.debug("Debugging !")
logger.error("Failed to load !")
logger.critical("Critical Message !")
