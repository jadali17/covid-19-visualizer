import logging
import os
from sys import platform
import datetime


logger = logging
cwd = os.getcwd()
if platform == "win32":
    logger.basicConfig(
        filename=cwd+'\logs\datapy.log',
        level=logging.INFO,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
elif platform == "linux" or platform == "linux2":
    logger.basicConfig(
        filename=cwd+'/logs/datapy.log',
        level=logging.INFO,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
