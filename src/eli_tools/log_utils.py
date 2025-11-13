import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

DEFAULT_FMT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
DEFAULT_DATE_FMT = "%Y-%m-%d %H:%M:%S"

def make_formatter(
        fmt: str,
        date_fmt: str,
        ) -> logging.Formatter:
    """
    Return a logging formatter object.
    """
    return logging.Formatter(
        fmt,
        datefmt= date_fmt,
    )

def attach_console_handler(
        logger: logging.Logger,
        formatter: logging.Formatter,
        level: int,
        ):
    """
    Attach a stream handler to logger.
    Default level is NOTSET.
     - Currently inherits level from app_level in setup_logging()
     - setup_logging() does not allow for customization of console_level. Can be added later.
    """
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def attach_file_handler(
        logger: logging.Logger,
        file_name: str | Path,
        formatter: logging.Formatter,
        level: int,
        rotate: bool,
        file_mode: str
        ):
    """
    Attach a file handler logger.
    Inherits all from setup_logging().
    Default behavior: attaches a RotatingFileHandler to logger.
    Optional behavior: attach a FileHandler to logger.
    """
    # Make directory if doesn't exist
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)

    # if rotate, create a RotatingFileHandler object
    if rotate:
        fh = RotatingFileHandler(
            filename=file_name,
            maxBytes=5_000_000,
            backupCount=5,
            encoding='utf-8'
        )
    # else, create a FileHandler object
    else:
        fh = logging.FileHandler(file_name, mode=file_mode, encoding='utf-8')
    # set FileHandler object level and format
    fh.setLevel(level)
    fh.setFormatter(formatter)
    # attach FileHandler to logger
    logger.addHandler(fh)

def clear_handlers(logger: logging.Logger):
    """Clear all handlers from specific logger"""
    for h in list(logger.handlers):
        logger.removeHandler(h)
        h.close()

def setup_logging(
        name: str,
        file_name: str | Path,
        app_level: int = logging.INFO,
        console_level: int = logging.NOTSET,
        file_level: int = logging.WARNING,
        log_fmt: str = DEFAULT_FMT,
        date_fmt: str = DEFAULT_DATE_FMT,
        rotate: bool = True,
        file_mode: str = 'a'
        ) -> logging.Logger:

    """
    Returns an app-level logging object with a Console Handler and a File Handler, and sets propagate = False.

    Usage:
    from eli_tools.log_utils import setup_logging
    log = setup_logging(name="my_app", file_name="logs/my_app.log")
    log.info("Job started")
    log.warning("Something fishy")
    log.error("Something failed)

    Required args:
    - app-level log name
    - file name or path for file log

    By default:
    - logging object level set to INFO
    - console level not set
    - file level set to WARNING
    - log format set to "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    - date format set to "%Y-%m-%d %H:%M:%S"
    - file is a rotating file with max 5_000_000 bytes and 5 backups

    Options:
    - set app-level, console level and file level
    - customize log format and date format locally
    - create a FileHandler rather than a RotatingFileHandler and set filemode (default is 'a')

    Future features:
    - add ability to create and customize child logs
    - add ability to set propagate = True
    """

    app = logging.getLogger(name)
    app.setLevel(app_level)
    app.propagate = False

    formatter = make_formatter(log_fmt, date_fmt)
    attach_console_handler(app, formatter, console_level)
    attach_file_handler(app, file_name, formatter,file_level, rotate, file_mode)

    return app
