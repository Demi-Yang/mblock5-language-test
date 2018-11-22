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

    # ext-i18n/arduino_mega2560/No empty value
    def test_ext_i18n_arduino_mega2560_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/arduino_mega2560/extensionName equals "Arduino Mega2560"
    def test_ext_i18n_arduino_mega2560_extensionName_equals_Arduino_Mega2560(self):
        self.assertIn('extensionName', self.test_dict)
        test_data = self.test_dict['extensionName']
        self.assertEqual(test_data, "Arduino Mega2560")

    # ext-i18n/arduino_mega2560/getDigital contains [ICON] [PORT]
    def test_ext_i18n_arduino_mega2560_getDigital(self):
        self.assertIn('getDigital', self.test_dict)
        test_data = self.test_dict['getDigital']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/getAnalog contains [ICON] [PORT]
    def test_ext_i18n_arduino_mega2560_getAnalog(self):
        self.assertIn('getAnalog', self.test_dict)
        test_data = self.test_dict['getAnalog']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/getPulse contains [ICON] [PORT] [TIME]
    def test_ext_i18n_arduino_mega2560_getPulse(self):
        self.assertIn('getPulse', self.test_dict)
        test_data = self.test_dict['getPulse']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/setDigitale contains [ICON] [PORT] [LEVEL]
    def test_ext_i18n_arduino_mega2560_setDigital(self):
        self.assertIn('setDigital', self.test_dict)
        test_data = self.test_dict['setDigital']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[LEVEL]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/setPwm contains [ICON] [PORT] [POWER]
    def test_ext_i18n_arduino_mega2560_setPwm(self):
        self.assertIn('setPwm', self.test_dict)
        test_data = self.test_dict['setPwm']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/setTone contains [ICON] [PORT] [NOTE] [BEAT]
    def test_ext_i18n_arduino_mega2560_setTone(self):
        self.assertIn('setTone', self.test_dict)
        test_data = self.test_dict['setTone']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertIn('[NOTE]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/setServo contains [ICON] [PORT] [ANGLE]
    def test_ext_i18n_arduino_mega2560_setServo(self):
        self.assertIn('setServo', self.test_dict)
        test_data = self.test_dict['setServo']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[ANGLE]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/serialWrite contains [ICON] [TEXT]
    def test_ext_i18n_arduino_mega2560_serialWrite(self):
        self.assertIn('serialWrite', self.test_dict)
        test_data = self.test_dict['serialWrite']
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/getSerialAvailable contains [ICON] 
    def test_ext_i18n_arduino_mega2560_getSerialAvailable(self):
        self.assertIn('getSerialAvailable', self.test_dict)
        test_data = self.test_dict['getSerialAvailable']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/serialRead contains [ICON] 
    def test_ext_i18n_arduino_mega2560_serialRead(self):
        self.assertIn('serialRead', self.test_dict)
        test_data = self.test_dict['serialRead']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/getUltrasonic contains [ICON] [PORT1] [PORT2]
    def test_ext_i18n_arduino_mega2560_getUltrasonic(self):
        self.assertIn('getUltrasonic', self.test_dict)
        test_data = self.test_dict['getUltrasonic']
        self.assertIn('[PORT1]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[PORT2]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/getTimer contains [ICON] 
    def test_ext_i18n_arduino_mega2560_getTimer(self):
        self.assertIn('getTimer', self.test_dict)
        test_data = self.test_dict['getTimer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/resetTimer contains [ICON] 
    def test_ext_i18n_arduino_mega2560_resetTimer(self):
        self.assertIn('resetTimer', self.test_dict)
        test_data = self.test_dict['resetTimer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/arduino_mega2560/SETTONE_NOTE is right
    def test_ext_i18n_arduino_mega2560_SETTONE_NOTE(self):
        self.assertEqual(self.test_dict['SETTONE_NOTE_0'], "C2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_1'], "D2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_2'], "E2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_3'], "F2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_4'], "G2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_5'], "A2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_6'], "B2")
        self.assertEqual(self.test_dict['SETTONE_NOTE_7'], "C3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_8'], "D3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_9'], "E3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_10'], "F3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_11'], "G3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_12'], "A3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_13'], "B3")
        self.assertEqual(self.test_dict['SETTONE_NOTE_14'], "C4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_15'], "D4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_16'], "E4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_17'], "F4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_18'], "G4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_19'], "A4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_20'], "B4")
        self.assertEqual(self.test_dict['SETTONE_NOTE_21'], "C5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_22'], "D5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_23'], "E5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_24'], "F5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_25'], "G5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_26'], "A5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_27'], "B5")
        self.assertEqual(self.test_dict['SETTONE_NOTE_28'], "C6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_29'], "D6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_30'], "E6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_31'], "F6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_32'], "G6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_33'], "A6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_34'], "B6")
        self.assertEqual(self.test_dict['SETTONE_NOTE_35'], "C7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_36'], "D7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_37'], "E7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_38'], "F7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_39'], "G7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_40'], "A7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_41'], "B7")
        self.assertEqual(self.test_dict['SETTONE_NOTE_42'], "C8")
 
 
if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ArduinoMega2560Test) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)