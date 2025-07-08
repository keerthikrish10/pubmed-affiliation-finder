# utils.py

import logging

def get_logger(name: str = "pubmed_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def setup_logging(debug: bool = False):
    level = logging.DEBUG if debug else logging.WARNING
    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
