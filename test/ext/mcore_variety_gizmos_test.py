# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mcore_variety_gizmos項目-翻译检查  =======================

class McoreVarietyGizmosTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/mcore_variety_gizmos']

    def check_key_exists(self, key):
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




    # ext-i18n/mcore_variety_gizmos/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/mcore_variety_gizmos/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 22, "mcore_variety_gizmos 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_mcore_show_external_led_time(self):
        key = 'mcore_show_external_led_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_mcore_show_external_led(self):
        key = 'mcore_show_external_led'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_mcore_show_external_led_rgb(self):
        key = 'mcore_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/mcore_variety_gizmos/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_mcore_run_servo(self):
        key = 'mcore_run_servo'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[DEGREE]')
        self.check_icon(key)

    # ext-i18n/mcore_variety_gizmos/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER]
    def test_auriga_variety_gizmos_mcore_show_7segments_number(self):
        key = 'mcore_show_7segments_number'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER]')
        self.check_icon(key)

    # ext-i18n/mcore_variety_gizmos/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_mcore_event_limit_switch(self):
        key = 'mcore_event_limit_switch'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreVarietyGizmosTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)