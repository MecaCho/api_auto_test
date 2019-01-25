#-*- coding=UTF-8 -*-
# import sys
import os
import json
import sqlite3
import time
from functools import wraps
import unittest
import logging
import logging.config
import ConfigParser
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s -- %(message)s")
LOG = logging.getLogger(__name__)


def method_decorator(func):
    def wrapper(self, *args):
        LOG.info("Add wrapper..")
        return func(self, *args)
    return wrapper


def return_api_resp(*args, **kwargs):
    to_type = kwargs.get("to_type", None)

    def catch_api_error(func):
        def wrapper(*args, **kwargs):
            resp = None
            try:
                LOG.debug("Func name : {2} , args: {0}, kwargs : {1}".format(args, json.dumps(kwargs), func.__name__))
                time_satrt = time.time()
                resp = func(*args, **kwargs)
                time_end = time.time()
                cost_time = time_end - time_satrt
		if kwargs.get("headers"):
			if kwargs.get("headers").get("X-Auth-Token"):
				kwargs["headers"].pop("X-Auth-Token")
				
                LOG.info("Func name : {2} , args: {0}, kwargs : {1}".format(args, json.dumps(kwargs), func.__name__))
	#	LOG.info(resp)
                LOG.info("Cost time : {0}s, start at :{1}".format(cost_time, time.ctime(time_satrt)))
            except Exception as e:
                LOG.error("Failed to %s ,ret : %s,  %s: " % (func.__name__, str(resp), str(e)))
            return resp
        return wrapper
    return catch_api_error


def createlog(name=__name__,log_file_name='test.log', debug=[], info=[], warn=[], error=[], fetal=[]):
    try:
        if os.path.getsize(log_file_name) > 1000000:
            os.remove(log_file_name)
    except BaseException:
        LOG.error('txt can not be deleted')
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
    if info: logger.info(info)
    if debug: logger.debug(debug)
    if warn: logger.warning(warn)
    if error: logger.error(error)
    if fetal: logger.fatal(fetal)


def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0]+'/fx.conf'
    config.read(path)
    try:
        return config.get(section,key)
    except BaseException as errorMessage:
        createlog('__dbconnect_getConfig__', debug=[errorMessage])
        return


@return_api_resp()
def test_fun():
    i = 0
    sum = 0
    while i < 1000:
        sum += i
        i += 1
    return sum

if __name__ == '__main__':
    test_fun()
