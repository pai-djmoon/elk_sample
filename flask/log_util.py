import logging
import datetime
import pathlib


def create_logger():
    logger = logging.getLogger()
    today_str = datetime.datetime.today().strftime("%Y-%m-%d")
    base_dir = pathlib.Path("./logs")

    if not base_dir.exists():
        base_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(message)s]")
    file_name = pathlib.Path(base_dir, today_str + ".log")
    fh = logging.FileHandler(file_name)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return logger
