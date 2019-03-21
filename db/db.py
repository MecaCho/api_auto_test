# -*- coding=UTF-8 -*-
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

dbpath = getConfig('database', 'dbpath')
cx = sqlite3.connect(dbpath)
cu = cx.cursor()
cx.text_factory = str
now = time.strftime("%Y-%m-%d-%H:%M:%S")


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        starttime = time.time()
        functionResult = function(*args, **kwargs)
        endtime = time.time()
        lostTime = functionResult[-1]
        testTime = round(endtime - starttime, 3) - float(str(lostTime))
        testTime = str(testTime) + 's'
        FunctionTestInfo = function.func_name + ' totalTime: ' + testTime + ' function lost Time: ' + str(lostTime)
        createlog(log_file_name='test.log', info=[function.func_name, functionResult, testTime])
        insertResult('GUIFunctionTest', [function.func_name, '', '', '', testTime])
        # createlog(log_file_name='time.log',info=[function.func_name,testTime])
        fp = open('log.txt', 'a+')
        now = time.strftime('%Y-%m-%d--%H:%M:%S')
        fp.writelines(now + " ## ")
        fp.writelines(FunctionTestInfo)
        fp.write('\n')
        return testTime

    return function_timer


def deleteDB(DBtable):
    #######删除数据库表格
    cu.execute('drop table if exists ' + DBtable + ';')
    createlog(name='__dbconnect__', warn=['Warning##drop a database Table :', DBtable])


def createDB(DBtable, *dbinfo):
    #######创建数据库结果表格
    print dbinfo
    temp = str(dbinfo)
    try:
        cu.execute('Create table if not exists ' + DBtable + ' ' + temp + ';')
    except sqlite3.OperationalError as errorMessage:
        cu.execute("INSERT INTO " + DBtable + " VALUES('This','is','a','New','Test','null')")
        createlog(name='__createDB__', error=[errorMessage])
        createlog(name='__createDB__', info=['create a DB successfully: ', DBtable])


def insertResult(DBtable, info):
    try:
        now = time.strftime("%Y-%m-%d-%H:%M:%S")
        info.append(now)
        n = len(info) - 1
        dbinfo = '(' + '?' + ',?' * n + ')'
        cmd1 = "INSERT into %s VALUES %s" % (DBtable, dbinfo)
        #########################windows系统下,如果不是读取文件，则注释掉以下两句################################################
        # print chardet.detect(info[0])['encoding']
        print type(info[0])
        if isinstance(info[0], str):
            info[0] = info[0].decode('gbk')
            info[1] = info[1].decode('gbk')
        cu.execute(cmd1, info)
        print 'DB info 中文 : ', info[0]
        cx.commit()
        # cx.close()
    except Exception as error_Message:
        createlog(name='__insertResult__', error=['databaseError', error_Message])


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """

    def __init__(self, methodName='runTest', filename='', filepath=''):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.filename = filename
        self.filepath = filepath
        print "Parametrize_init_"

    @staticmethod
    def parametrize(testcase_klass, filename='', filepath=''):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, filename=filename, filepath=filepath))
        return suite


if __name__ == "__main__":
    createHtml('中文', '中文测试.html', '1', '2', '3')
