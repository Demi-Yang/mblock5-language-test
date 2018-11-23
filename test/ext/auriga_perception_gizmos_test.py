# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  auriga_perception_gizmos項目-翻译检查  =======================

class AurigaPerceptionGizmosTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/auriga_perception_gizmos']

    # ext-i18n/auriga_perception_gizmos/No empty value
    def test_ext_i18n_auriga_perception_gizmos_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/auriga_perception_gizmos/No new or missing items
    def test_ext_i18n_auriga_perception_gizmos_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 18)

    # ext-i18n/auriga_perception_gizmos/mcore_run_fan contains [ICON] [PORT] [FAN_ROTATE]
    def test_ext_i18n_auriga_perception_gizmos_mcore_run_fan(self):
        self.assertIn('mcore_run_fan', self.test_dict)
        test_data = self.test_dict['mcore_run_fan']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FAN_ROTATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga_perception_gizmos/mcore_detect_external_loudness contains [ICON] [PORT] 
    def test_ext_i18n_auriga_perception_gizmos_mcore_detect_external_loudness(self):
        self.assertIn('mcore_detect_external_loudness', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_loudness']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga_perception_gizmos/mcore_detec_temperature contains [ICON] [PORT] [SLOT]
    def test_ext_i18n_auriga_perception_gizmos_mcore_detec_temperature(self):
        self.assertIn('mcore_detec_temperature', self.test_dict)
        test_data = self.test_dict['mcore_detec_temperature']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga_perception_gizmos/mcore_detect_potentiometer contains [ICON] [PORT] [FAN_ROTATE]
    def test_ext_i18n_auriga_perception_gizmos_mcore_detect_potentiometer(self):
        self.assertIn('mcore_detect_potentiometer', self.test_dict)
        test_data = self.test_dict['mcore_detect_potentiometer']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaPerceptionGizmosTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)