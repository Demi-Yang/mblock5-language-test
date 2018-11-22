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

    # ext-i18n/iot/No empty value
    def test_ext_i18n_iot_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mblock5-i18n/extensionName equals IoT
    def test_mblock5_i18n_extensionName_equals_IoT(self):
        self.assertIn('extensionName', self.test_dict)
        self.assertEqual(self.test_dict['extensionName'], "IoT")
        
    # ext-i18n/iot/iot_connect_network contains [SSID] [PASSWORD] 
    def test_ext_i18n_iot_connect_network(self):
        self.assertIn('iot_connect_network', self.test_dict)
        test_data = self.test_dict['iot_connect_network']
        self.assertIn('[SSID]', test_data)
        self.assertIn('[PASSWORD]', test_data)

    # ext-i18n/iot/iot_connect_network_password_value equals 12345678 
    def test_ext_i18n_iot_connect_network_password_value(self):
        self.assertIn('iot_connect_network_password_value', self.test_dict)
        self.assertEqual(self.test_dict['iot_connect_network_password_value'], '12345678')

    # ext-i18n/iot/iot_weather contains [LOCATION] [WEATHER_TYPE] 
    def test_ext_i18n_iot_weather(self):
        self.assertIn('iot_weather', self.test_dict)
        test_data = self.test_dict['iot_weather']
        self.assertIn('[LOCATION]', test_data)
        self.assertIn('[WEATHER_TYPE]', test_data)

    # ext-i18n/iot/iot_air contains [LOCATION] [WEATHER_TYPE] 
    def test_ext_i18n_iot_air(self):
        self.assertIn('iot_air', self.test_dict)
        test_data = self.test_dict['iot_air']
        self.assertIn('[LOCATION]', test_data)
        self.assertIn('[WEATHER_TYPE]', test_data)

    # ext-i18n/iot/iot_sun contains [LOCATION] [WEATHER_TYPE] [TIME] 
    def test_ext_i18n_iot_sun(self):
        self.assertIn('iot_sun', self.test_dict)
        test_data = self.test_dict['iot_sun']
        self.assertIn('[LOCATION]', test_data)
        self.assertIn('[WEATHER_TYPE]', test_data)
        self.assertIn('[TIME]', test_data)

    # ext-i18n/iot/data_addtolist_cloudlist contains [VALUE] [ICON] [CLOUD_VARIABLE] 
    def test_ext_i18n_data_addtolist_cloudlist(self):
        self.assertIn('data_addtolist_cloudlist', self.test_dict)
        test_data = self.test_dict['data_addtolist_cloudlist']
        self.assertIn('[VALUE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[CLOUD_VARIABLE]', test_data)

    # ext-i18n/iot/data_itemoflist_cloudlist contains [VALUE] [ICON] [CLOUD_VARIABLE] 
    def test_ext_i18n_data_itemoflist_cloudlist(self):
        self.assertIn('data_itemoflist_cloudlist', self.test_dict)
        test_data = self.test_dict['data_itemoflist_cloudlist']
        self.assertIn('[VALUE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[CLOUD_VARIABLE]', test_data)

    # ext-i18n/iot/data_lengthoflist_cloudlist contains [ICON] [CLOUD_VARIABLE] 
    def test_ext_i18n_data_lengthoflist_cloudlist(self):
        self.assertIn('data_lengthoflist_cloudlist', self.test_dict)
        test_data = self.test_dict['data_lengthoflist_cloudlist']
        self.assertIn('[ICON]', test_data)
        self.assertIn('[CLOUD_VARIABLE]', test_data)

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

