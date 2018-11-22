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

    # ext-i18n/mcore_variety_gizmos/No empty value
    def test_ext_i18n_mcore_variety_gizmos_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_ext_i18n_mcore_show_external_led_time(self):
        self.assertIn('mcore_show_external_led_time', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_ext_i18n_mcore_show_external_led(self):
        self.assertIn('mcore_show_external_led', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_variety_gizmos/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_ext_i18n_mcore_show_external_led_rgb(self):
        self.assertIn('mcore_show_external_led_rgb', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_rgb']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_variety_gizmos/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_ext_i18n_mcore_run_servo(self):
        self.assertIn('mcore_run_servo', self.test_dict)
        test_data = self.test_dict['mcore_run_servo']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_variety_gizmos/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER]
    def test_ext_i18n_auriga_variety_gizmos_mcore_show_7segments_number(self):
        self.assertIn('mcore_show_7segments_number', self.test_dict)
        test_data = self.test_dict['mcore_show_7segments_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_variety_gizmos/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_ext_i18n_mcore_event_limit_switch(self):
        self.assertIn('mcore_event_limit_switch', self.test_dict)
        test_data = self.test_dict['mcore_event_limit_switch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreVarietyGizmosTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)