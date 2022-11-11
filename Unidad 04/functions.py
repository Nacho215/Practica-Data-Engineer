# functions.py
import logging
import logging.config
import os

# Filename
file_name = os.path.basename(__file__).split('.')[0]
# Get logger
logger = logging.getLogger(file_name)


def configure_logging(config_file):
    """
    Set up loggers, handlers and formatters, based on a given configuration file.

    Args:
        config_file (str): Path of the configuration file.
    """
    # Configure logging
    logging.config.fileConfig(fname=config_file, disable_existing_loggers=False)


def read_text_file(filepath):
    """
    Read a text file located in a given path, logging info about its lines and words.

    Args:
        filepath (str): Path of the text file.
    """
    # Open the file in read mode
    with open(filepath, 'r') as f:
        # Read data
        file_data = f.read()
        # Get line count and logs it
        lines = file_data.split('\n')
        line_count = len(lines)
        logger.info("%s - Cantidad de renglones: %d", f.name, line_count)
        # Iterate through each line
        for idx, line in enumerate(lines):
            # Get word count and logs it
            word_count = len(line.split(' '))
            logger.info("Renglón %d: %d palabras", idx, word_count)
