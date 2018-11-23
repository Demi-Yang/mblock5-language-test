# coding=utf-8
import time, sys, os
sys.path.append('./')
from HTMLTestRunner import HTMLTestRunner
import unittest

"""fix:UnicodeDecodeError"""
reload(sys)
sys.setdefaultencoding('utf-8')


test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
lang = sys.argv[-1]

if __name__ == '__main__':
    if os.access('./FORMAT_RESULT/'+lang+'.json', os.F_OK):
        filename = './report/'+lang+'_'+'last_result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='Passport3 System Inteface Test Report', description="Implementation Example with:")
        runner.run(discover)
        fp.close()
    elif lang == 'all':
        os.system("python run_tests.py de")
        os.system("python run_tests.py en")
        os.system("python run_tests.py es")
        os.system("python run_tests.py fi")
        os.system("python run_tests.py fr")
        os.system("python run_tests.py hr")
        os.system("python run_tests.py id")
        os.system("python run_tests.py it")
        os.system("python run_tests.py ja")
        os.system("python run_tests.py ko")
        os.system("python run_tests.py nl")
        os.system("python run_tests.py pl")
        os.system("python run_tests.py pt")
        os.system("python run_tests.py ru")
        os.system("python run_tests.py uk")
        os.system("python run_tests.py zh-hant")
        os.system("python run_tests.py zh")
    else:
        print('\n\nThe last parameter "'+ lang + '" you entered is neither the file name existing under <./FORMAT_RESULT/> directory nor the "all".  \n\nIf you want to test a language individually, enter:  < python run_tests.py en[or de/zh...] >  \nIf you want to test all languages, please enter:  < python run_tests.py all> \n\n')


