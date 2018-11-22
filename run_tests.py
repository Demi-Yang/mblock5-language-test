# coding=utf-8
import time, sys, os
sys.path.append('./')
from HTMLTestRunner import HTMLTestRunner
import unittest

"""fix:UnicodeDecodeError"""
reload(sys)
sys.setdefaultencoding('utf-8')


test_dir = './test/mscratch/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
lang = sys.argv[1]

if __name__ == '__main__':
    if lang =='all':
        filename = './report/'+lang+'_'+'last_result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='Passport3 System Inteface Test Report', description="Implementation Example with:")
        runner.run(discover)
        fp.close()
    elif os.access('./FORMAT_RESULT/'+lang+'.json', os.F_OK):
        filename = './report/'+lang+'_'+'last_result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='Passport3 System Inteface Test Report', description="Implementation Example with:")
        runner.run(discover)
        fp.close()
    else:
        print('There is no such file named '+ lang + '.json ' + 'in the <./FORMAT_RESULT/> directory. ')
    # filename = './report/'+lang+'_'+'last_result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='Passport3 System Inteface Test Report', description="Implementation Example with:")
    # # print(discover)
    # runner.run(discover)
    # fp.close()


