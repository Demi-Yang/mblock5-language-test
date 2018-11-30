# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  mcore_servo_pack項目-翻译检查  =======================

class McoreServoPackTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/mcore_servo_pack']
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0} \nvalue: {1} \n缺少参数: {2}'.format(key, test_data, p))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))

    # ext-i18n/mcore_servo_pack/No empty value
    def test_mcore_servo_pack_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/mcore_servo_pack/No new or missing items
    def test_mcore_servo_pack_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 20, '\next-i18n/mcore_servo_pack 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/mcore_servo_pack/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_mcore_show_external_led_time(self):
        key = 'mcore_show_external_led_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]', '[TIME]'])

    # ext-i18n/mcore_servo_pack/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_mcore_show_external_led(self):
        key = 'mcore_show_external_led'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]'])

    # ext-i18n/mcore_servo_pack/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_mcore_show_external_led_rgb(self):
        key = 'mcore_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[R]', '[G]', '[B]'])

    # ext-i18n/mcore_servo_pack/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_mcore_run_servo(self):
        key = 'mcore_run_servo'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]'])



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreServoPackTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)