# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  arduino_mega2560項目-翻译检查  =======================

class DeviceConnectUploadFirmwareTipTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.lang = lang
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        cls.test_json = data_handle.byteify(json.load(f))
        zh_f = open(os.getcwd() + '/FORMAT_RESULT/zh.json', 'r')
        cls.zh_json = data_handle.byteify(json.load(zh_f))
    
    def check_key(self, key, test, zh ):
        self.assertIn(key, test, '\n缺少key: {0}'.format(key))
        self.assertIsNotNone(test[key], "\n没有翻译的字段：" + key)
        if(self.lang != "zh"):
            self.assertNotEqual(test[key], zh[key], "\n未翻译的字段：{0}，翻译不能为中文".format(key))

    # ext-i18n/codey
    def test_codey(self):
        device_key = "ext-i18n/"+"codey"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_dc0edd70", test_device_value,  zh_device_value )
        self.check_key("connect_fail_ac025070", test_device_value,  zh_device_value )
        self.check_key("connect_fail_3a075878", test_device_value,  zh_device_value )
        self.check_key("connect_fail_12b07c7c", test_device_value,  zh_device_value )
        self.check_key("connect_fail_ccd91361", test_device_value,  zh_device_value )
        self.check_key("connect_fail_1e4caec6", test_device_value,  zh_device_value )
        self.check_key("upload_fail_d5fa5444", test_device_value,  zh_device_value )
        self.check_key("upload_fail_ae3a4ed5", test_device_value,  zh_device_value )
        self.check_key("upload_fail_d36df56a", test_device_value,  zh_device_value )
        self.check_key("firmware_success_c205609a", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_34b7a344", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_340c3de8", test_device_value,  zh_device_value )

    def test_mcore(self):
        device_key = "ext-i18n/"+"mcore"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_2a0b1f15", test_device_value,  zh_device_value )
        self.check_key("connect_fail_488c674d", test_device_value,  zh_device_value )
        self.check_key("connect_fail_0adf83ae", test_device_value,  zh_device_value )
        self.check_key("connect_fail_9a020618", test_device_value,  zh_device_value )
        self.check_key("connect_fail_f0f225df", test_device_value,  zh_device_value )
        self.check_key("connect_fail_3d459770", test_device_value,  zh_device_value )
        self.check_key("connect_fail_13e00731", test_device_value,  zh_device_value )
        self.check_key("upload_fail_fded06b5", test_device_value,  zh_device_value )
        self.check_key("upload_fail_17773a37", test_device_value,  zh_device_value )
        self.check_key("firmware_success_ddc56406", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_f1b7513c", test_device_value,  zh_device_value )

    def test_auriga(self):
        device_key = "ext-i18n/"+"auriga"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_4e720cf3", test_device_value,  zh_device_value )
        self.check_key("connect_fail_29312b3b", test_device_value,  zh_device_value )
        self.check_key("connect_fail_09099d40", test_device_value,  zh_device_value )
        self.check_key("connect_fail_34866b93", test_device_value,  zh_device_value )
        self.check_key("connect_fail_c2d05fc8", test_device_value,  zh_device_value )
        self.check_key("connect_fail_f198b930", test_device_value,  zh_device_value )
        self.check_key("connect_fail_349388ff", test_device_value,  zh_device_value )
        self.check_key("upload_fail_068e0a12", test_device_value,  zh_device_value )
        self.check_key("upload_fail_62e96a5f", test_device_value,  zh_device_value )
        self.check_key("firmware_success_db9b07ee", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_901081f9", test_device_value,  zh_device_value )

    def test_arduino_uno(self):
        device_key = "ext-i18n/"+"arduino_uno"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_6d44027d", test_device_value,  zh_device_value )
        self.check_key("connect_fail_a605d9a4", test_device_value,  zh_device_value )
        self.check_key("connect_fail_7f65f6e1", test_device_value,  zh_device_value )
        self.check_key("upload_fail_6d692a95", test_device_value,  zh_device_value )
        self.check_key("upload_fail_f97d60f4", test_device_value,  zh_device_value )
        self.check_key("firmware_success_b74d4379", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_c46a5a9b", test_device_value,  zh_device_value )

    def test_arduino_mega2560(self):
        device_key = "ext-i18n/"+"arduino_mega2560"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_e30fbe5b", test_device_value,  zh_device_value )
        self.check_key("connect_fail_a0b839ac", test_device_value,  zh_device_value )
        self.check_key("connect_fail_57a56306", test_device_value,  zh_device_value )
        self.check_key("upload_fail_ffc49ed9", test_device_value,  zh_device_value )
        self.check_key("upload_fail_03de753a", test_device_value,  zh_device_value )
        self.check_key("firmware_success_f3ed430b", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_787f5461", test_device_value,  zh_device_value )
    
    def test_microbit(self):
        device_key = "ext-i18n/"+"microbit"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("upload_fail_ded32e71", test_device_value,  zh_device_value )
        self.check_key("upload_fail_a8febb81", test_device_value,  zh_device_value )

    def test_neuron(self):
        device_key = "ext-i18n/"+"neuron"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_3eef6a81", test_device_value,  zh_device_value )
        self.check_key("connect_fail_2cdd56fc", test_device_value,  zh_device_value )
        self.check_key("connect_fail_5f94d30a", test_device_value,  zh_device_value )
    
    def test_motionblock(self):
        device_key = "ext-i18n/"+"motionblock"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_c3bb41b9", test_device_value,  zh_device_value )
        self.check_key("connect_fail_a5f94f62", test_device_value,  zh_device_value )
        self.check_key("connect_fail_2714f29d", test_device_value,  zh_device_value )
        self.check_key("upload_fail_1e0c5a00", test_device_value,  zh_device_value )
        self.check_key("upload_fail_84ba9e7a", test_device_value,  zh_device_value )
        self.check_key("upload_fail_b244c914", test_device_value,  zh_device_value )
        self.check_key("firmware_success_7226c374", test_device_value,  zh_device_value )
        self.check_key("firmware_fail_73700b7a", test_device_value,  zh_device_value )

    def test_haloboard(self):
        device_key = "ext-i18n/"+"haloboard"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        self.check_key("connect_fail_418dd2b0", test_device_value,  zh_device_value )
        self.check_key("connect_fail_be44da45", test_device_value,  zh_device_value )
        self.check_key("connect_fail_81f19800", test_device_value,  zh_device_value )
        self.check_key("connect_fail_a2244e18", test_device_value,  zh_device_value )
        self.check_key("connect_fail_2ff4c830", test_device_value,  zh_device_value )
        self.check_key("connect_fail_f516f160", test_device_value,  zh_device_value )
        self.check_key("upload_fail_440e4ba6", test_device_value,  zh_device_value )
        self.check_key("upload_fail_24d8e745", test_device_value,  zh_device_value ) 
        self.check_key("upload_fail_c52d223b", test_device_value,  zh_device_value ) 
        self.check_key("firmware_success_70e9b6c0", test_device_value,  zh_device_value ) 
        self.check_key("firmware_fail_9b5aae92", test_device_value,  zh_device_value ) 
        self.check_key("firmware_fail_9a92af14", test_device_value,  zh_device_value ) 

    def test_novapi(self):
        device_key = "ext-i18n/"+"novapi"
        test_device_value = self.test_json[device_key]
        zh_device_value = self.zh_json[device_key]
        # self.check_key("connect_fail_418dd2b0", test_device_value,  zh_device_value )
        # self.check_key("connect_fail_be44da45", test_device_value,  zh_device_value )
        # self.check_key("connect_fail_81f19800", test_device_value,  zh_device_value )
        # self.check_key("connect_fail_a2244e18", test_device_value,  zh_device_value )
        # self.check_key("connect_fail_2ff4c830", test_device_value,  zh_device_value )
        # self.check_key("connect_fail_f516f160", test_device_value,  zh_device_value )
        # self.check_key("upload_fail_440e4ba6", test_device_value,  zh_device_value )
        # self.check_key("upload_fail_24d8e745", test_device_value,  zh_device_value ) 
        # self.check_key("upload_fail_c52d223b", test_device_value,  zh_device_value ) 
        # self.check_key("firmware_success_70e9b6c0", test_device_value,  zh_device_value ) 
        # self.check_key("firmware_fail_9b5aae92", test_device_value,  zh_device_value ) 
        # self.check_key("firmware_fail_9a92af14", test_device_value,  zh_device_value )
        
        
        
if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(DeviceRelaDescribeTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)