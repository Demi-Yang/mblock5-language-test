# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  tm項目-翻译检查  =======================

class TMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/tm']

    # ext-i18n/tm/No empty value
    def test_ext_i18n_tm_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/tm/visual_recognition_confidence contains [sample_index]
    def test_ext_i18n_visual_recognition_confidence(self):
        self.assertIn('visual_recognition_confidence', self.test_dict)
        test_data = self.test_dict['visual_recognition_confidence']
        self.assertIn('[sample_index]', test_data)
        
    # ext-i18n/tm/visual_recognition_result_is contains [sample_index]
    def test_ext_i18n_visual_recognition_result_is(self):
        self.assertIn('visual_recognition_result_is', self.test_dict)
        test_data = self.test_dict['visual_recognition_result_is']
        self.assertIn('[sample_index]', test_data)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TMTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

