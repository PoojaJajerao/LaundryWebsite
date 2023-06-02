import logging
import sys
import traceback

# Constants
DATABASE = 'database'
FILENAME = 'filename'
RETRIEVE = 'retrieve'
LIMIT = 'limit'
ERROR = 'error'
MESSAGE = 'message'
ERROR_CODE = 'error_code'
RESULTS = 'results'
SUCCESSFUL = 'successful'
ERR_MSG = f"module={{module_name}}, error={{error_msg}}"


# Functions
def log_err_message(module_name, error_message):
    """
    Logs error message to the console and raises an exception.

    :param module_name: str, the name of the module where the error occurred
    :param error_message: str, the error message to log and raise
    :raises Exception: The error message passed to the function
    """
    err_str = ERR_MSG.format(module_name=module_name, error_msg=error_message)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb_msg = traceback.format_exc()
    logging.error("Exception occurred\nType: {}\nName:{}\nTraceback:{}".format(exc_type, exc_obj, tb_msg))
    raise Exception(error_message)