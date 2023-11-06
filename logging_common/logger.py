import logging
import time

from pathlib import Path


class Logger:
    def __init__(
        self, verbosity: str = "DEBUG", log_to_file: bool = True, log_file_path: str = "", logger_name: str = None
    ) -> None:
        """
        Initializes the logger with the specified settings.

        Args:
            verbosity (str, optional): The verbosity level of the logger. Defaults to "DEBUG".
            log_to_file (bool, optional): Whether to log to a file. Defaults to True.
            log_file_path (str, optional): The path to the log file. Defaults to "".
            logger_name (str, optional): The name of the logger. Defaults to None.

        Raises:
            AssertionError: If logger_name is not provided.

        Returns:
            None
        """
        assert logger_name is not None, "Must Provide Name For Logger."
        self.logger_name = logger_name

        self.verbosity = self.__get_verbosity(verbosity)

        self.logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(self.verbosity)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(module)s:%(lineno)s - %(funcName)s() - %(levelname)s - %(message)s"
        )

        self.logger.addHandler(self.__create_stream_handler(formatter, logger_name))

        if log_to_file:
            self.logger.addHandler(self.__create_file_handler(formatter, logger_name, log_file_path))

    def __get_verbosity(self, verbosity: str) -> int:
        """
        Get the corresponding logging level for a given verbosity level.

        Parameters:
            verbosity (str): The verbosity level to be converted.

        Returns:
            int: The corresponding logging level.

        Raises:
            ValueError: If the verbosity level is invalid.
        """
        match verbosity.upper():
            case "DEBUG":
                return logging.DEBUG
            case "INFO":
                return logging.INFO
            case "WARNING":
                return logging.WARNING
            case "ERROR":
                return logging.ERROR
            case "CRITICAL":
                return logging.CRITICAL
            case _:
                raise ValueError("Invalid Verbosity Level.")


    def __create_stream_handler(self, format: logging.Formatter, name: str) -> logging.StreamHandler:
        """
        Create a stream handler for the logger.

        Args:
            format (logging.Formatter): The formatter to use for the stream handler.
            name (str): The name of the stream handler.

        Returns:
            logging.StreamHandler: The created stream handler.
        """
        stream_handler_name = f"{name}_StreamHandler"
        existing_streamhandlers = [stream_handler_name in x.name for x in self.logger.manager.loggerDict.get(stream_handler_name).handlers]
        if len(existing_streamhandlers) == 0:
            stream_handler = logging.StreamHandler()
            stream_handler.set_name(stream_handler_name)
            stream_handler.setLevel(self.verbosity)
            stream_handler.setFormatter(format)
            return stream_handler

    def __create_file_handler(self, format: logging.Formatter, name: str, file_location: str) -> logging.FileHandler:
        """
        Create a file handler for logging.

        Args:
            format (logging.Formatter): The formatter to use for the handler.
            name (str): The name of the file handler.
            file_location (str): The location where the log file will be saved.

        Returns:
            logging.FileHandler: The created file handler.

        Raises:
            AssertionError: If the file_location is empty.
        """
        assert file_location != "", "Must Provide Location For Log File."

        file_date = time.strftime("%Y%m%d-%H%M%S")
        file_handler_name = f"{name}_FileHandler"
        log_location = Path(file_location).joinpath(f"{file_handler_name}_{file_date}.log")
        existing_file_handlers = [file_handler_name in x.name for x in self.logger.manager.loggerDict.get(file_handler_name).handlers]

        if len(existing_file_handlers) == 0:
            file_handler = logging.FileHandler(filename=log_location)
            file_handler.set_name(file_handler_name)
            file_handler.setLevel(self.verbosity)
            file_handler.setFormatter(format)
            return file_handler

    def info(self, message) -> None:
        self.logger.info(message, stacklevel=2)

    def debug(self, message) -> None:
        self.logger.debug(message, stacklevel=2)

    def warning(self, message) -> None:
        self.logger.warning(message, stacklevel=2)

    def error(self, message) -> None:
        self.logger.error(message, stacklevel=2)

    def critical(self, message) -> None:
        self.logger.critical(message, stacklevel=2)