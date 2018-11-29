# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  arduino_mega2560項目-翻译检查  =======================

class ArduinoMega2560Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/arduino_mega2560']
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0}, value:{1}, error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey:{0}, 缺少参数：{1}'.format(key, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, 缺少参数：[ICON]'.format(key))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, error:参数[ICON]必须在首位'.format(key))

    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/arduino_mega2560/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 68, 'arduino_mega2560 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/arduino_mega2560/extensionName equals "Arduino Mega2560"
    def test_extensionName(self):
        key = 'extensionName'
        expect_value = "Arduino Mega2560"
        self.check_key_exists(key)
        self.check_expect_value(key, expect_value)
        

    # ext-i18n/arduino_mega2560/getDigital contains [ICON] [PORT]
    def test_getDigital(self):
        key = 'getDigital'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')

    # ext-i18n/arduino_mega2560/getAnalog contains [ICON] [PORT]
    def test_getAnalog(self):
        key = 'getAnalog'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')

    # ext-i18n/arduino_mega2560/getPulse contains [ICON] [PORT] [TIME]
    def test_getPulse(self):
        key = 'getPulse'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TIME]')

    # ext-i18n/arduino_mega2560/setDigitale contains [ICON] [PORT] [LEVEL]
    def test_setDigital(self):
        key = 'setDigital'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LEVEL]')

    # ext-i18n/arduino_mega2560/setPwm contains [ICON] [PORT] [POWER]
    def test_setPwm(self):
        key = 'setPwm'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[POWER]')

    # ext-i18n/arduino_mega2560/setTone contains [ICON] [PORT] [NOTE] [BEAT]
    def test_setTone(self):
        key = 'setTone'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[BEAT]')
        self.check_param(key, '[NOTE]')

    # ext-i18n/arduino_mega2560/setServo contains [ICON] [PORT] [ANGLE]
    def test_setServo(self):
        key = 'setServo'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ANGLE]')


    # ext-i18n/arduino_mega2560/serialWrite contains [ICON] [TEXT]
    def test_serialWrite(self):
        key = 'serialWrite'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[TEXT]')

    # ext-i18n/arduino_mega2560/getSerialAvailable contains [ICON] 
    def test_getSerialAvailable(self):
        key = 'getSerialAvailable'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/arduino_mega2560/serialRead contains [ICON] 
    def test_serialRead(self):
        key = 'serialRead'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/arduino_mega2560/getUltrasonic contains [ICON] [PORT1] [PORT2]
    def test_getUltrasonic(self):
        key = 'getUltrasonic'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_param(key, '[PORT1]')
        self.check_param(key, '[PORT2]')

    # ext-i18n/arduino_mega2560/getTimer contains [ICON] 
    def test_getTimer(self):
        key = 'getTimer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/arduino_mega2560/resetTimer contains [ICON] 
    def test_mega2560_resetTimer(self):
        key = 'resetTimer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/arduino_mega2560/SETTONE_NOTE is right
    def test_SETTONE_NOTE(self):
        self.check_expect_value('SETTONE_NOTE_0', "C2")
        self.check_expect_value('SETTONE_NOTE_1', "D2")
        self.check_expect_value('SETTONE_NOTE_2', "E2")
        self.check_expect_value('SETTONE_NOTE_3', "F2")
        self.check_expect_value('SETTONE_NOTE_4', "G2")
        self.check_expect_value('SETTONE_NOTE_5', "A2")
        self.check_expect_value('SETTONE_NOTE_6', "B2")
        self.check_expect_value('SETTONE_NOTE_7', "C3")
        self.check_expect_value('SETTONE_NOTE_8', "D3")
        self.check_expect_value('SETTONE_NOTE_9', "E3")
        self.check_expect_value('SETTONE_NOTE_10', "F3")
        self.check_expect_value('SETTONE_NOTE_11', "G3")
        self.check_expect_value('SETTONE_NOTE_12', "A3")
        self.check_expect_value('SETTONE_NOTE_13', "B3")
        self.check_expect_value('SETTONE_NOTE_14', "C4")
        self.check_expect_value('SETTONE_NOTE_15', "D4")
        self.check_expect_value('SETTONE_NOTE_16', "E4")
        self.check_expect_value('SETTONE_NOTE_17', "F4")
        self.check_expect_value('SETTONE_NOTE_18', "G4")
        self.check_expect_value('SETTONE_NOTE_19', "A4")
        self.check_expect_value('SETTONE_NOTE_20', "B4")
        self.check_expect_value('SETTONE_NOTE_21', "C5")
        self.check_expect_value('SETTONE_NOTE_22', "D5")
        self.check_expect_value('SETTONE_NOTE_23', "E5")
        self.check_expect_value('SETTONE_NOTE_24', "F5")
        self.check_expect_value('SETTONE_NOTE_25', "G5")
        self.check_expect_value('SETTONE_NOTE_26', "A5")
        self.check_expect_value('SETTONE_NOTE_27', "B5")
        self.check_expect_value('SETTONE_NOTE_28', "C6")
        self.check_expect_value('SETTONE_NOTE_29', "D6")
        self.check_expect_value('SETTONE_NOTE_30', "E6")
        self.check_expect_value('SETTONE_NOTE_31', "F6")
        self.check_expect_value('SETTONE_NOTE_32', "G6")
        self.check_expect_value('SETTONE_NOTE_33', "A6")
        self.check_expect_value('SETTONE_NOTE_34', "B6")
        self.check_expect_value('SETTONE_NOTE_35', "C7")
        self.check_expect_value('SETTONE_NOTE_36', "D7")
        self.check_expect_value('SETTONE_NOTE_37', "E7")
        self.check_expect_value('SETTONE_NOTE_38', "F7")
        self.check_expect_value('SETTONE_NOTE_39', "G7")
        self.check_expect_value('SETTONE_NOTE_40', "A7")
        self.check_expect_value('SETTONE_NOTE_41', "B7")
        self.check_expect_value('SETTONE_NOTE_42', "C8")
 
 
if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ArduinoMega2560Test) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)