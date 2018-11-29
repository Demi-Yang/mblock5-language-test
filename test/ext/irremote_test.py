# coding:utf-8
# import requests
import json
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
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0}, value:{1}, error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0} \nvalue:{1} \n缺少参数：{2}'.format(key, test_data, p))

    # ext-i18n/irremote/No empty value
    def test_irremote_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/irremote/No new or missing items
    def test_irremote_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 28, 'irremote 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/irremote/meos_ir_remote_letter_press contains [LETTER]
    def test_meos_ir_remote_letter_press(self):
        key = 'meos_ir_remote_letter_press'
        self.check_key_exists(key)
        self.check_params(key, ['[LETTER]'])

    # ext-i18n/irremote/meos_ir_remote_arrow_press contains [LETTER]
    def test_meos_ir_remote_arrow_press(self):
        key = 'meos_ir_remote_arrow_press'
        self.check_key_exists(key)
        self.check_params(key, ['[LETTER]'])

    # ext-i18n/irremote/meos_ir_remote_number_press contains [LETTER]
    def test_meos_ir_remote_number_press(self):
        key = 'meos_ir_remote_number_press'
        self.check_key_exists(key)
        self.check_params(key, ['[LETTER]'])

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0 euqals A
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_0'
        self.check_key_exists(key)
        self.check_expect_value(key, 'A')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1 euqals B
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_1'
        self.check_key_exists(key)
        self.check_expect_value(key, 'B')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2 euqals C
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_2'
        self.check_key_exists(key)
        self.check_expect_value(key, 'C')
        

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3 euqals D
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_3'
        self.check_key_exists(key)
        self.check_expect_value(key, 'D')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4 euqals E
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_4'
        self.check_key_exists(key)
        self.check_expect_value(key, 'E')

    # ext-i18n/irremote/MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5 euqals F
    def test_MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5(self):
        key = 'MEOS_IR_REMOTE_LETTER_PRESS_LETTER_5'
        self.check_key_exists(key)
        self.check_expect_value(key, 'F')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0 euqals "↑"
    def test_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0(self):
        key = 'MEOS_IR_REMOTE_ARROW_PRESS_LETTER_0'
        self.check_key_exists(key)
        self.check_expect_value(key, '↑')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1 euqals "↓"
    def test_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1(self):
        key = 'MEOS_IR_REMOTE_ARROW_PRESS_LETTER_1'
        self.check_key_exists(key)
        self.check_expect_value(key, '↓')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2 euqals "←"
    def test_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2(self):
        key = 'MEOS_IR_REMOTE_ARROW_PRESS_LETTER_2'
        self.check_key_exists(key)
        self.check_expect_value(key, '←')

    # ext-i18n/irremote/MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3 euqals "→"
    def test_MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3(self):
        key = 'MEOS_IR_REMOTE_ARROW_PRESS_LETTER_3'
        self.check_key_exists(key)
        self.check_expect_value(key, '→')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0 euqals "0"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_0'
        self.check_key_exists(key)
        self.check_expect_value(key, '0')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1 euqals "1"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_1'
        self.check_key_exists(key)
        self.check_expect_value(key, '1')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2 euqals "2"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_2'
        self.check_key_exists(key)
        self.check_expect_value(key, '2')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3 euqals "3"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_3'
        self.check_key_exists(key)
        self.check_expect_value(key, '3')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4 euqals "4"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_4'
        self.check_key_exists(key)
        self.check_expect_value(key, '4')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5 euqals "5"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_5'
        self.check_key_exists(key)
        self.check_expect_value(key, '5')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6 euqals "6"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_6'
        self.check_key_exists(key)
        self.check_expect_value(key, '6')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7 euqals "7"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_7'
        self.check_key_exists(key)
        self.check_expect_value(key, '7')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8 euqals "8"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_8'
        self.check_key_exists(key)
        self.check_expect_value(key, '8')

    # ext-i18n/irremote/MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9 euqals "9"
    def test_MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9(self):
        key = 'MEOS_IR_REMOTE_NUMBER_PRESS_LETTER_9'
        self.check_key_exists(key)
        self.check_expect_value(key, '9')




if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(IrRemoteTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)