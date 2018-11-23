# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  auriga_laser_sword項目-翻译检查  =======================

class AurigaLaserSwordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/auriga_laser_sword']

    # ext-i18n/auriga_laser_sword/No empty value
    def test_ext_i18n_auriga_laser_sword_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/auriga_laser_sword/No new or missing items
    def test_ext_i18n_auriga_laser_sword_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 22)

    # ext-i18n/auriga_laser_sword/auriga_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_ext_i18n_auriga_laser_sword_auriga_show_all_ledstrip_color(self):
        self.assertIn('auriga_show_all_ledstrip_color', self.test_dict)
        test_data = self.test_dict['auriga_show_all_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga_laser_sword/auriga_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_ext_i18n_auriga_laser_sword_auriga_show_ledstrip_color(self):
        self.assertIn('auriga_show_ledstrip_color', self.test_dict)
        test_data = self.test_dict['auriga_show_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga_laser_sword/auriga_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_ext_i18n_auriga_laser_sword_auriga_show_ledstrip_rbg(self):
        self.assertIn('auriga_show_ledstrip_rbg', self.test_dict)
        test_data = self.test_dict['auriga_show_ledstrip_rbg']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaLaserSwordTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)