import logging

# set logging level
logging.basicConfig(level=logging.DEBUG)

logging.debug('This is the debug message')
logging.info('This is the info message')
logging.warning("This is the warning message")
logging.error("This is the error message")
logging.critical("This is the critical message")

print("\n")

# change the format of displayed messages
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This is the debug message 2')
