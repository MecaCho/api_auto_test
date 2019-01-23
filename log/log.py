#-*- coding=UTF-8 -*-
import sys
import os
import sqlite3
import time
from functools import wraps
import unittest
import logging
import logging.config
import ConfigParser
import sqlite3
import chardet
from pyh import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def createlog(name=__name__,log_file_name = 'test.log',debug=[],info=[],warn= [],error= [],fetal=[]):
    try:
        if os.path.getsize(log_file_name) > 1000000:
            os.remove(log_file_name)
    except BaseException:
        print 'txt can not be deleted'
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # create a file handler
        handler = logging.FileHandler(log_file_name)
        handler.setLevel(logging.DEBUG)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        ########################解决日志重复的问题logger.removeHandler(handler)
    if info:logger.info(info)
    if debug:logger.debug(debug)
    if warn:logger.warning(warn)
    if error:logger.error(error)
    if fetal:logger.fatal(fetal)
def getConfig(section,key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0]+'/fx.conf'
    config.read(path)
    try:
        return config.get(section,key)
    except BaseException as errorMessage:
        createlog('__dbconnect_getConfig__',debug=[errorMessage])
        return