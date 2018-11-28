# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  arduino_uno項目-翻译检查  =======================

class ArduinoUnoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/arduino_uno']

    # ext-i18n/arduino_uno/No empty value
    def test_ext_i18n_arduino_uno_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "arduino_uno 模块下存在未翻译的字段: " + key)
            self.assertNotEqual(value, '', "arduino_uno 模块下存在未翻译的字段：" + key)

    # ext-i18n/arduino_uno/No new or missing items
    def test_ext_i18n_arduino_uno_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 69, "arduino_uno 模块下新增或删减了新的字段，测试用例需增减~")

    # ext-i18n/arduino_uno/extensionName equals "Arduino Uno"
    def test_ext_i18n_arduino_uno_extensionName_equals_Arduino_Uno(self):
        key = 'extensionName'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertEqual(test_data, "Arduino Uno", key + " 的值不等于：'Arduino Uno'")

    # ext-i18n/arduino_uno/getDigital contains [ICON] [PORT]
    def test_ext_i18n_arduino_uno_getDigital(self):
        key = 'getDigital'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/getAnalog contains [ICON] [PORT]
    def test_ext_i18n_arduino_uno_getAnalog(self):
        key = 'getAnalog'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/getPulse contains [ICON] [PORT] [TIME]
    def test_ext_i18n_arduino_uno_getPulse(self):
        key = 'getPulse'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[TIME]', test_data, key + " 的值缺少参数：[TIME]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/setDigitale contains [ICON] [PORT] [LEVEL]
    def test_ext_i18n_arduino_uno_setDigital(self):
        key = 'setDigital'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[LEVEL]', test_data, key + " 的值缺少参数：[LEVEL]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/setPwm contains [ICON] [PORT] [POWER]
    def test_ext_i18n_arduino_uno_setPwm(self):
        key = 'setPwm'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[POWER]', test_data, key + " 的值缺少参数：[POWER]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/setTone contains [ICON] [PORT] [NOTE] [BEAT]
    def test_ext_i18n_arduino_uno_setTone(self):
        key = 'setTone'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[BEAT]', test_data, key + " 的值缺少参数：[BEAT]")
        self.assertIn('[NOTE]', test_data, key + " 的值缺少参数：[NOTE]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/setServo contains [ICON] [PORT] [ANGLE]
    def test_ext_i18n_arduino_uno_setServo(self):
        key = 'setServo'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT]', test_data, key + " 的值缺少参数：[PORT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[ANGLE]', test_data, key + " 的值缺少参数：[ANGLE]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/serialWrite contains [ICON] [TEXT]
    def test_ext_i18n_arduino_uno_serialWrite(self):
        key = 'serialWrite'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[TEXT]', test_data, key + " 的值缺少参数：[TEXT]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/getSerialAvailable contains [ICON] 
    def test_ext_i18n_arduino_uno_getSerialAvailable(self):
        key = 'getSerialAvailable'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/serialRead contains [ICON] 
    def test_ext_i18n_arduino_uno_serialRead(self):
        key = 'serialRead'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/getUltrasonic contains [ICON] [PORT1] [PORT2]
    def test_ext_i18n_arduino_uno_getUltrasonic(self):
        key = 'getUltrasonic'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[PORT1]', test_data, key + " 的值缺少参数：[PORT1]")
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertIn('[PORT2]', test_data, key + " 的值缺少参数：[PORT2]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/getTimer contains [ICON] 
    def test_ext_i18n_arduino_uno_getTimer(self):
        key = 'getTimer'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/resetTimer contains [ICON] 
    def test_ext_i18n_arduino_uno_resetTimer(self):
        key = 'resetTimer'
        self.assertIn(key, self.test_dict, "arduino_uno 模块下缺少字段：" + key)
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, key + " 的值缺少参数：[ICON]")
        self.assertEqual(test_data.index('[ICON]'), 0, key + " 的值中 [ICON] 参数位置错误")

    # ext-i18n/arduino_uno/SETTONE_NOTE is right
    def test_ext_i18n_arduino_uno_SETTONE_NOTE(self):
        self.assertEqual(self.test_dict['SETTONE_NOTE_0'], "C2", "SETTONE_NOTE_0 的值不等于 C2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_1'], "D2", "SETTONE_NOTE_1 的值不等于 D2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_2'], "E2", "SETTONE_NOTE_2 的值不等于 E2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_3'], "F2", "SETTONE_NOTE_3 的值不等于 F2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_4'], "G2", "SETTONE_NOTE_4 的值不等于 G2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_5'], "A2", "SETTONE_NOTE_5 的值不等于 A2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_6'], "B2", "SETTONE_NOTE_6 的值不等于 B2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_7'], "C3", "SETTONE_NOTE_7 的值不等于 C3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_8'], "D3", "SETTONE_NOTE_8 的值不等于 D3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_9'], "E3", "SETTONE_NOTE_9 的值不等于 E3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_10'], "F3", "SETTONE_NOTE_10 的值不等于 F3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_11'], "G3", "SETTONE_NOTE_11 的值不等于 G3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_12'], "A3", "SETTONE_NOTE_12 的值不等于 A3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_13'], "B3", "SETTONE_NOTE_13 的值不等于 B3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_14'], "C4", "SETTONE_NOTE_14 的值不等于 C4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_15'], "D4", "SETTONE_NOTE_15 的值不等于 D4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_16'], "E4", "SETTONE_NOTE_16 的值不等于 E4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_17'], "F4", "SETTONE_NOTE_17 的值不等于 F4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_18'], "G4", "SETTONE_NOTE_18 的值不等于 G4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_19'], "A4", "SETTONE_NOTE_19 的值不等于 A4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_20'], "B4", "SETTONE_NOTE_20 的值不等于 B4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_21'], "C5", "SETTONE_NOTE_21 的值不等于 C5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_22'], "D5", "SETTONE_NOTE_22 的值不等于 D5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_23'], "E5", "SETTONE_NOTE_23 的值不等于 E5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_24'], "F5", "SETTONE_NOTE_24 的值不等于 F5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_25'], "G5", "SETTONE_NOTE_25 的值不等于 G5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_26'], "A5", "SETTONE_NOTE_26 的值不等于 A5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_27'], "B5", "SETTONE_NOTE_27 的值不等于 B5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_28'], "C6", "SETTONE_NOTE_28 的值不等于 C6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_29'], "D6", "SETTONE_NOTE_29 的值不等于 D6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_30'], "E6", "SETTONE_NOTE_30 的值不等于 E6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_31'], "F6", "SETTONE_NOTE_31 的值不等于 F6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_32'], "G6", "SETTONE_NOTE_32 的值不等于 G6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_33'], "A6", "SETTONE_NOTE_33 的值不等于 A6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_34'], "B6", "SETTONE_NOTE_34 的值不等于 B6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_35'], "C7", "SETTONE_NOTE_35 的值不等于 C7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_36'], "D7", "SETTONE_NOTE_36 的值不等于 D7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_37'], "E7", "SETTONE_NOTE_37 的值不等于 E7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_38'], "F7", "SETTONE_NOTE_38 的值不等于 F7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_39'], "G7", "SETTONE_NOTE_39 的值不等于 G7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_40'], "A7", "SETTONE_NOTE_40 的值不等于 A7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_41'], "B7", "SETTONE_NOTE_41 的值不等于 B7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_42'], "C8", "SETTONE_NOTE_42 的值不等于 C8")
  
  
if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ArduinoUnoTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)