import logging
import os


class Logger:

    @staticmethod
    def get_logger(name="AutomationFramework"):

        log_directory = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "logs"
        )

        os.makedirs(log_directory, exist_ok=True)

        log_file = os.path.join(
            log_directory,
            "automation.log"
        )

        logger = logging.getLogger(name)

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            console_handler = logging.StreamHandler()

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger