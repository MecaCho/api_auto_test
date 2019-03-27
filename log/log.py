# -*- coding=UTF-8 -*-
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

# logging.basicConfig(level=logging.INFO,filename="report.html", format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
logging.basicConfig(level=logging.INFO, filename="report.html", format='%(message)s')
# logging.basicConfig(level=logging.INFO,filename="report.html", format='<tr bordercolor="Blue" align="left">%(message)s</tr>')
LOG = logging.getLogger(__name__)


def method_decorator(func):
    def wrapper(self, *args):
        LOG.info("Add wrapper..")
        return func(self, *args)

    return wrapper


def assert_resp(*args, **kwargs):
    expection_code = kwargs.get("expection_code", None)
    partion = args[0] if args[0] else None
    comment = kwargs.get("comment")

    def catch_resp(func):
        def wrapper(*args, **kwargs):
            resp = func(*args, **kwargs)
            code = ""
            ret = ""
            try:
                if not partion:
                    code = resp.status_code
                    assert code == expection_code
                else:
                    code, _ = resp
                    assert code == expection_code
                ret = "Success"
            except Exception as err:
                ret = "Failed"
                LOG.error("Check test result failed : {}".format(str(err)))
            if comment:
                LOG.info('<td colspan="7">{}</td>'.format(comment))
            # LOG.info("Expection response code : {}, Real response code :{}, Test Result:{}".format(
            #        expection_code, code, ret
            # ))
            return resp

        return wrapper

    return catch_resp


def return_api_resp(*args, **kwargs):
    to_type = kwargs.get("to_type", None)

    def catch_api_error(func):
        def wrapper(*args, **kwargs):
            resp = None
            try:
                # LOG.debug("Func name : {2} , args: {0}, kwargs : {1}".format(args, json.dumps(kwargs), func.__name__))
                time_satrt = time.time()
                resp = func(*args, **kwargs)
                # LOG.info(resp)
                time_end = time.time()
                cost_time = time_end - time_satrt
                time.sleep(0.5)
                if kwargs.get("headers"):
                    if kwargs.get("headers").get("X-Auth-Token"):
                        kwargs["headers"].pop("X-Auth-Token")
                        #       LOG.info(
                        #               "Func name : {2} , args: {0}, kwargs : {1}".format(args,
                        #                                                                  json.dumps(kwargs),
                        #                                                                  func.__name__))
                try:
                    path = kwargs.get("path").split("/v2/")[1]
                except Exception as err:
                    path = "error"
                    # LOG.error("Get request path error : {}".format(str(err)))
                log_dict = {"method" : kwargs.get("method"), "path": path, "body": str(kwargs.get("body")),
                            "cost"   : cost_time,
                            "st_time": time.ctime(time_satrt)}
                #                import pdb
                #               pdb.set_trace()
                if kwargs.get("portion"):
                    log_dict["resp_code"], _ = resp
                else:
                    try:
                        log_dict["resp_code"] = str(resp.status_code)
                    except Exception:
                        log_dict["resp_code"] = resp
                # LOG.info(
                #        "Request method: {method}, path :{path}, resp: {resp_code}, body: {body}, "
                #        "cost time : {cost}s, start at :{st_time}".format(
                #                **log_dict))
                log_dict["expect_code"] = log_dict["resp_code"]
                log_dict["result"] = "success"
                msg = '<td>{method}</td><td>{path}</td><td>{cost}</td><td>{resp_code}</td><td>{expect_code}</td><td>{result}</td><td>{body}</td>'.format(
                        **log_dict)
                LOG.info('<tr bordercolor="Blue" align="left">{}</tr>'.format(msg))
                # logging.basicConfig(level=logging.INFO, filename="report.html", format="%(message)s")
                # log = logging.getLogger("test result")
                # log.info(msg)
            except Exception as e:
                # LOG.error("Failed to %s ,ret : %s,  %s: " % (func.__name__, str(resp), str(e)))
                raise e
            return resp

        return wrapper

    return catch_api_error


def createlog(name=__name__, log_file_name='report.html', debug=[], info=[], warn=[], error=[], fetal=[]):
    try:
        if os.path.getsize(log_file_name) > 1000000:
            os.remove(log_file_name)
    except BaseException:
        pass
        # LOG.error('txt can not be deleted')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # create a file handler
        handler = logging.FileHandler(log_file_name)
        handler.setLevel(logging.DEBUG)
        # create a logging format
        formatter = logging.Formatter('%(message)s')
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
    path = os.path.split(os.path.realpath(__file__))[0] + '/fx.conf'
    config.read(path)
    try:
        return config.get(section, key)
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
