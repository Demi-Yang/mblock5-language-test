# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  cognitive項目-翻译检查  =======================

class IotTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/iot']
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0}, value:{1}, error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0}, value:{1}, 缺少参数：{2}'.format(key, test_data, p))

    # ext-i18n/iot/No empty value
    def test_iot_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/iot/No new or missing items
    def test_iot_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 66, 'iot 模块下新增或删减了新的字段，测试用例需增减~')

    # mblock5-i18n/extensionName equals IoT
    def test_extensionName(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_expect_value(key, "IoT")
        
    # ext-i18n/iot/iot_connect_network contains [SSID] [PASSWORD] 
    def test_iot_connect_network(self):
        key = 'iot_connect_network'
        self.check_key_exists(key)
        self.check_params(key, ['[SSID]', '[PASSWORD]'])

    # ext-i18n/iot/iot_connect_network_password_value equals 12345678 
    def test_iot_connect_network_password_value(self):
        self.check_key_exists('iot_connect_network_password_value')
        self.check_expect_value('iot_connect_network_password_value', '12345678')

    # ext-i18n/iot/iot_weather contains [LOCATION] [WEATHER_TYPE] 
    def test_iot_weather(self):
        key = 'iot_weather'
        self.check_key_exists(key)
        self.check_params(key, ['[LOCATION]', '[WEATHER_TYPE]'])

    # ext-i18n/iot/iot_air contains [LOCATION] [WEATHER_TYPE] 
    def test_iot_air(self):
        key = 'iot_air'
        self.check_key_exists(key)
        self.check_params(key, ['[LOCATION]', '[WEATHER_TYPE]'])

    # ext-i18n/iot/iot_sun contains [LOCATION] [WEATHER_TYPE] [TIME] 
    def test_iot_sun(self):
        key = 'iot_sun'
        self.check_key_exists(key)
        self.check_params(key, ['[LOCATION]', '[WEATHER_TYPE]', '[TIME]'])

    # ext-i18n/iot/data_addtolist_cloudlist contains [VALUE] [ICON] [CLOUD_VARIABLE] 
    def test_data_addtolist_cloudlist(self):
        key = 'data_addtolist_cloudlist'
        self.check_key_exists(key)
        self.check_params(key, ['[VALUE]', '[ICON]', '[CLOUD_VARIABLE]'])

    # ext-i18n/iot/data_itemoflist_cloudlist contains [VALUE] [ICON] [CLOUD_VARIABLE] 
    def test_data_itemoflist_cloudlist(self):
        key = 'data_itemoflist_cloudlist'
        self.check_key_exists(key)
        self.check_params(key, ['[VALUE]', '[ICON]', '[CLOUD_VARIABLE]'])

    # ext-i18n/iot/data_lengthoflist_cloudlist contains [ICON] [CLOUD_VARIABLE] 
    def test_data_lengthoflist_cloudlist(self):
        key = 'data_lengthoflist_cloudlist'
        self.check_key_exists(key)
        self.check_params(key, ['[ICON]',  '[CLOUD_VARIABLE]'])

    # # ext-i18n/iot/ifttt_pub contains [MESSAGE] [TRIGGER] 
    # def test_ext_i18n_ifttt_pub(self):
    #     self.assertIn('ifttt_pub', self.test_dict)
    #     test_data = self.test_dict['ifttt_pub']
    #     self.assertIn('[MESSAGE]', test_data)
    #     self.assertIn('[TRIGGER]', test_data)





if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(IotTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

