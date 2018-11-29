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

    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey:{0}, 缺少参数：{1}'.format(key, param))



    # ext-i18n/tm/No empty value
    def test_tm_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/tm/No new or missing items
    def test_tm_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 33, "tm 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/tm/visual_recognition_confidence contains [sample_index]
    def test_visual_recognition_confidence(self):
        key = 'visual_recognition_confidence'
        self.check_key_exists(key)
        self.check_param(key, '[sample_index]')
        
    # ext-i18n/tm/visual_recognition_result_is contains [sample_index]
    def test_visual_recognition_result_is(self):
        key = 'visual_recognition_result_is'
        self.check_key_exists(key)
        self.check_param(key, '[sample_index]')


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TMTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

