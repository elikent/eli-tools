import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def report(
    msg: str,
    log_level: str = "info",
    *,
    verbose: bool = False,
    logger: logging.Logger | None = None) -> None:
    '''Purpose: Set log level and optionally print

    Args:
        msg: Message to log
        log_level: log_level. options are v
        verbose: if True, print msg to console
        logger:

    Steps:
        1. create _map of log_level string to logging.level
        2. get log_fn by mapping log_level var to logging.level via _map
        3. log message
        4. print msg to console if verbose or log_level != "info"
    '''

    # Map string to logging level
    _map = {
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error,
        "critical": logging.critical,
        "debug": logging.debug,
    }
    # Get specified logging level. Raise error if log_level typed in wrong
    if not log_level.lower() in _map.keys():
        raise ValueError(f'Invalid log_level: {log_level}. Options are [k for k in _maps.keys()]')
    else:
        log_fn = _map.get(log_level.lower(), logging.info)
        log_fn(msg)
        if verbose or log_level != "info":
            print(msg)

def logging_config(
        level: int = logging.INFO,
        fmt: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        log_file: Optional[Path] = None,
        max_bytes: int = 5_000_000, # ~5 MB per file
        backup_count: int = 5,
        console: bool = True,
        force: bool = True
        ) -> None:

    '''Configure global logging for the application.

    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG)
        fmt: Format string for log messages. Defauylt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        log_file: Path object for log file.
        max_bytes: Max size per log file before rotation (default = ~5MB).
        backup_count: Number of rotates log files to keep.
        console: If True, log to console.
        force: If True, recopngireu even if logging was already set up.
    '''

    # Declare empty list of handlers. Possible handlers = StreamHandler (console) and RotatingFileHandler (file)
    handlers = []

    # File handler if requested
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
        )
        file_handler.setFormatter(logging.Formatter(fmt))
        handlers.append(file_handler)

    # Console handler if not surpressed
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(fmt))
        handlers.append(console_handler)

    logging.basicConfig(
        level=level,
        handlers=handlers,
        force=force
    )
