import logging

logging.basicConfig(filename='myLogs.log', level=logging.DEBUG)

logging.warning("Method is not implemented")
logging.info("Code works correctly")
logging.error("Unexpected error")
logging.critical("Program is broken")


# adding traceback to the logging file
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.exception("Dividing the number by zero")
    else:
        return result


division(10, 0)