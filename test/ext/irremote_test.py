# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  irremote項目-翻译检查  =======================

class IrRemoteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/irremote']

    # ext-i18n/irremote/No empty value
    def test_ext_i18n_irremote_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/irremote/meos_ir_remote_letter_press contains [LETTER]
    def test_ext_i18n_meos_ir_remote_letter_press(self):
        self.assertIn('meos_ir_remote_letter_press', self.test_dict)
        test_data = self.test_dict['meos_ir_remote_letter_press']
        self.assertIn('[LETTER]', test_data)

    # ext-i18n/irremote/meos_ir_remote_arrow_press contains [LETTER]
    def test_ext_i18n_meos_ir_remote_arrow_press(self):
        self.assertIn('meos_ir_remote_arrow_press', self.test_dict)
        test_data = self.test_dict['meos_ir_remote_arrow_press']
        self.assertIn('[LETTER]', test_data)

    # ext-i18n/irremote/meos_ir_remote_number_press contains [LETTER]
    def test_ext_i18n_meos_ir_remote_number_press(self):
        self.assertIn('meos_ir_remote_number_press', self.test_dict)
        test_data = self.test_dict['meos_ir_remote_number_press']
        self.assertIn('[LETTER]', test_data)

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0 euqals A
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0']
        self.assertEqual(test_data, 'A')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1 euqals B
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1']
        self.assertEqual(test_data, 'B')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2 euqals C
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2']
        self.assertEqual(test_data, 'C')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3 euqals D
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3']
        self.assertEqual(test_data, 'D')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4 euqals E
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4']
        self.assertEqual(test_data, 'E')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5 euqals F
    def test_ext_i18n_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5(self):
        self.assertIn('MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5']
        self.assertEqual(test_data, 'F')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0 euqals "↑"
    def test_ext_i18n_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0(self):
        self.assertIn('MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0']
        self.assertEqual(test_data, '↑')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1 euqals "↓"
    def test_ext_i18n_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1(self):
        self.assertIn('MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1']
        self.assertEqual(test_data, '↓')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2 euqals "←"
    def test_ext_i18n_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2(self):
        self.assertIn('MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2']
        self.assertEqual(test_data, '←')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3 euqals "→"
    def test_ext_i18n_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3(self):
        self.assertIn('MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3']
        self.assertEqual(test_data, '→')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0 euqals "0"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0']
        self.assertEqual(test_data, '0')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1 euqals "1"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1']
        self.assertEqual(test_data, '1')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2 euqals "2"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2']
        self.assertEqual(test_data, '2')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3 euqals "3"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3']
        self.assertEqual(test_data, '3')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4 euqals "4"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4']
        self.assertEqual(test_data, '4')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5 euqals "5"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5']
        self.assertEqual(test_data, '5')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6 euqals "6"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6']
        self.assertEqual(test_data, '6')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7 euqals "7"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7']
        self.assertEqual(test_data, '7')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8 euqals "8"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8']
        self.assertEqual(test_data, '8')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9 euqals "9"
    def test_ext_i18n_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9(self):
        self.assertIn('MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9', self.test_dict)
        test_data = self.test_dict['MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9']
        self.assertEqual(test_data, '9')




if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(IrRemoteTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)