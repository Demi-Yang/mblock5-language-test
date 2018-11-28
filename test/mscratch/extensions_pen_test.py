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

class ExtensionsPenTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mscratch-i18n']['extensions']['pen']

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




    # mscratch-i18n/extensions/pen/No new items or missing items
    def test_extensions_pen_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 18, "mscratch-i18n/extensions/pen 模块下新增或删减了翻译字段")

    # mscratch-i18n/extensions/pen/No empty value
    def test_extensions_pen_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "该字段的翻译为空，错误 key: " + key)
            self.assertNotEqual(value, '', "该字段的翻译为空，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setColor contains [COLOR] 
    def test_extensions_pen_setColor(self):
        key = 'pen.setColor'
        self.check_key_exists(key)
        self.check_param(key, '[COLOR]')

    # mscratch-i18n/extensions/pen/pen.changeColorParam contains [COLOR_PARAM] [VALUE] 
    def test_extensions_pen_changeColorParam(self):
        key = 'pen.changeColorParam'
        self.check_key_exists(key)
        self.check_param(key, '[COLOR_PARAM]')
        self.check_param(key, '[VALUE]')

    # mscratch-i18n/extensions/pen/pen.setColorParam contains [COLOR_PARAM] [VALUE] 
    def test_extensions_pen_setColorParam(self):
        key = 'pen.setColorParam'
        self.check_key_exists(key)
        self.check_param(key, '[COLOR_PARAM]')
        self.check_param(key, '[VALUE]')

    # mscratch-i18n/extensions/pen/pen.changeSize contains [SIZE] 
    def test_extensions_pen_changeSize(self):
        key = 'pen.changeSize'
        self.check_key_exists(key)
        self.check_param(key, '[SIZE]')

    # mscratch-i18n/extensions/pen/pen.setSize contains [SIZE] 
    def test_extensions_pen_setSize(self):
        key = 'pen.setSize'
        self.check_key_exists(key)
        self.check_param(key, '[SIZE]')

    # mscratch-i18n/extensions/pen/pen.setShade contains [SHADE] 
    def test_extensions_pen_setShade(self):
        key = 'pen.setShade'
        self.check_key_exists(key)
        self.check_param(key, '[SHADE]')

    # mscratch-i18n/extensions/pen/pen.changeShade contains [SHADE] 
    def test_extensions_pen_changeShade(self):
        key = 'pen.changeShade'
        self.check_key_exists(key)
        self.check_param(key, '[SHADE]')

    # mscratch-i18n/extensions/pen/pen.setHue contains [HUE] 
    def test_extensions_pen_setHue(self):
        key = 'pen.setHue'
        self.check_key_exists(key)
        self.check_param(key, '[HUE]')

    # mscratch-i18n/extensions/pen/pen.changeHue contains [HUE] 
    def test_extensions_pen_changeHue(self):
        key = 'pen.changeHue'
        self.check_key_exists(key)
        self.check_param(key, '[HUE]')


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ExtensionsPenTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
