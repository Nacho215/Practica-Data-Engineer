# main.py
import logging
import os
import functions

# Filename
file_name = os.path.basename(__file__).split('.')[0]
# Get logger
logger = logging.getLogger(file_name)


# Main function
def main():
    # Configure loggers
    functions.configure_logging('log_conf_file.conf')
    # Try to read cuento.txt file
    try:
        logger.info("...Leyendo el archivo...")
        functions.read_text_file('cuento.txt')
        logger.info("...Archivo procesado...")
    # If can't, log error
    except OSError:
        logger.error("No se pudo abrir el archivo")


# If this script is run directly, go main
if __name__ == "__main__":
    main()
