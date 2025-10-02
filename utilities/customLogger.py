import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Correct path to the Logs folder
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
        log_file = os.path.join(log_dir, "automation.log")

        # Create Logs folder if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
        if not logger.handlers:
            fileHandler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger




# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fhandler.setFormatter(formatter)
#         logger.addHandler(fhandler)
#         logger.setLevel(logging.INFO)
#         return logger