# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mscratch項目-翻译检查  =======================

class GuiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mscratch-i18n']['gui']

    def check_key_exists(self, key, ):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0},\n value:{1},\n error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey:{0}, 缺少参数：{1}'.format(key, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, 缺少参数：[ICON]'.format(key))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, error:参数[ICON]必须在首位'.format(key))




    # mscratch-i18n/gui/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "mscratch-i18n/gui/ 模块下存在未翻译的字段: " + key)
            self.assertNotEqual(value, '', "mscratch-i18n/gui/ 模块下存在翻译为空的字段: " + key)

    # mscratch-i18n/gui/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 194, "mscratch-i18n/gui/ 模块下新增或删减了翻译字段")

    # mscratch-i18n/gui/gui.modal.inputTip contains （&<>'\"）"
    def test_modal_inputTip(self):
        key = 'gui.modal.inputTip'
        self.check_key_exists(key)
        r = re.compile(r'.&.<.>.\'.\"')     # print(r.findall(test_data))
        test_data = self.test_dict[key]
        self.assertRegexpMatches(test_data, r, '\nkey:{0}, 缺少其中某个字符：{1}\n'.format(key, "&<>'\""))

    # mscratch-i18n/gui/gui.modal.confirmDeleteVariable contains %2 %1 
    def test_modal_confirmDeleteVariable(self):
        key = 'gui.modal.confirmDeleteVariable'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')
        # self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        # self.assertIn('%2', test_data, "缺少参数 %2 ,错误 key: " + key)

if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(GuiTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
