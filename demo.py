# below code is to check the logging config
# from us_visa.logger import logging

# logging.info("This is to test the logging config")


# below code is to check the exception config
from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys) from e