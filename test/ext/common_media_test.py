# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  cognitive項目-翻译检查  =======================

class CommonMediaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/common/media']

    # ext-i18n/common/media/No empty value
    def test_ext_i18n_cognitive_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/common/media/No new or missing items
    def test_ext_i18n_common_media_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 8)

if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CommonMediaTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

