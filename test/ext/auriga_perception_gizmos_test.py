# coding:utf-8
# import requests
import json
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


    def check_key_exists(self, key, ):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0} \nvalue: {1} \n error: 值不等于 {2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey: {0} \nvalue: {1} \n缺少参数：{2}'.format(key, test_data, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))




    # ext-i18n/auriga_perception_gizmos/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/auriga_perception_gizmos/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 18, "\nauriga_perception_gizmos 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/auriga_perception_gizmos/auriga_run_fan contains [ICON] [PORT] [FAN_ROTATE]
    def test_auriga_run_fan(self):
        key = 'auriga_run_fan'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FAN_ROTATE]')
        self.check_icon(key)

    # ext-i18n/auriga_perception_gizmos/auriga_detect_external_loudness contains [ICON] [PORT] 
    def test_auriga_detect_external_loudness(self):
        key = 'auriga_detect_external_loudness'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_perception_gizmos/auriga_detec_temperature contains [ICON] [PORT] [SLOT]
    def test_auriga_detec_temperature(self):
        key = 'auriga_detec_temperature'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/auriga_perception_gizmos/auriga_detect_potentiometer contains [ICON] [PORT]
    def test_auriga_detect_potentiometer(self):
        key = 'auriga_detect_potentiometer'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaPerceptionGizmosTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)