# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  mcore_light_sound項目-翻译检查  =======================

class McoreLightSoundTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/mcore_light_sound']

    # ext-i18n/mcore_light_sound/No empty value
    def test_ext_i18n_mcore_light_sound_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/mcore_light_sound/No new or missing items
    def test_ext_i18n_mcore_light_sound_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 24)

    # ext-i18n/mcore_light_sound/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_ext_i18n_mcore_show_external_led_time(self):
        self.assertIn('mcore_show_external_led_time', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_light_sound/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_ext_i18n_mcore_show_external_led(self):
        self.assertIn('mcore_show_external_led', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_light_sound/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
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

    # ext-i18n/mcore_light_sound/mcore_detect_external_light contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_light(self):
        self.assertIn('mcore_detect_external_light', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_light']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_light_sound/mcore_detect_external_loudness contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_loudness(self):
        self.assertIn('mcore_detect_external_loudness', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_loudness']
        self.assertIn('[ICON]', test_data)
        self.assertIn('[PORT]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)




if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreLightSoundTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)