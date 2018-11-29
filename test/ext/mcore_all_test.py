# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mcore_all項目-翻译检查  =======================

class McoreAllTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/mcore_all']

    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0}, value:{1}, error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0}, value: {1}, 缺少参数:{2}'.format(key, test_data, p))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, value: {1}, 缺少参数：[ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, 参数[ICON]必须在首位'.format(key))

    # ext-i18n/mcore_all/No empty value
    def test_mcore_all_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/mcore_all/No new or missing items
    def test_mcore_all_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 92, 'ext-i18n/mcore_all 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/mcore_all/mcore_run_shutter contains [ICON] [PORT] [SHUTTER_ACTION]
    def test_mcore_run_shutter(self):
        key = 'mcore_run_shutter'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SHUTTER_ACTION]'])

    # ext-i18n/mcore_all/mcore_run_motor contains [ICON] [PORT][ROTATE][POWER] %
    def test_mcore_run_motor(self):
        key = 'mcore_run_motor'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[ROTATE]', '[POWER] %'])

    # ext-i18n/mcore_all/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_mcore_run_servo(self):
        key = 'mcore_run_servo'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[DEGREE]'])

    # ext-i18n/mcore_all/mcore_run_fan contains [ICON] [PORT][FAN_ROTATE]
    def test_mcore_run_fan(self):
        key = 'mcore_run_fan'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FAN_ROTATE]'])

    # ext-i18n/mcore_all/mcore_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_mcore_show_face_time(self):
        key = 'mcore_show_face_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]', '[TIME]'])

    # ext-i18n/mcore_all/mcore_show_face contains [ICON] [PORT] [FACE_PANEL] 
    def test_mcore_show_face(self):
        key = 'mcore_show_face'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]'])

    # ext-i18n/mcore_all/mcore_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y] 
    def test_mcore_show_face_position(self):
        key = 'mcore_show_face_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]', 'x: [X] y: [Y]'])

    # ext-i18n/mcore_all/mcore_show_text contains [ICON] [PORT] [TEXT] 
    def test_mcore_show_text(self):
        self.assertIn('mcore_show_text', self.test_dict)
        test_data = self.test_dict['mcore_show_text']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_text_position contains [ICON] [PORT] [TEXT] x: [X] y: [Y] 
    def test_mcore_show_text_position(self):
        key = 'mcore_show_text_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[TEXT]', 'x: [X] y: [Y]'])

    # ext-i18n/mcore_all/mcore_show_number contains [ICON] [PORT] [NUMBER] 
    def test_mcore_show_number(self):
        key = 'mcore_show_number'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER]'])

    # ext-i18n/mcore_all/mcore_show_time contains [ICON] [PORT] [NUMBER1]: [NUMBER2]
    def test_mcore_show_time(self):
        key = 'mcore_show_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER1]: [NUMBER2]'])

    # ext-i18n/mcore_all/mcore_show_face_off contains [ICON] [PORT] 
    def test_mcore_show_face_off(self):
        key = 'mcore_show_face_off'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])


    # ext-i18n/mcore_all/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_mcore_show_external_led_time(self):
        key = 'mcore_show_external_led_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]', '[TIME]'])

    # ext-i18n/mcore_all/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_mcore_show_external_led(self):
        key = 'mcore_show_external_led'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]'])

    # ext-i18n/mcore_all/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_mcore_show_external_led_rgb(self):
        key = 'mcore_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[R]', '[G]', '[B]'])


    # ext-i18n/mcore_all/mcore_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_mcore_show_all_ledstrip_color(self):
        key = 'mcore_show_all_ledstrip_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[COLOR_LIST]'])

    # ext-i18n/mcore_all/mcore_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_mcore_show_ledstrip_color(self):
        key = 'mcore_show_ledstrip_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[POS]', '[COLOR_LIST]'])

    # ext-i18n/mcore_all/mcore_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
    def test_mcore_show_ledstrip_rbg(self):
        key = 'mcore_show_ledstrip_rbg'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[POS]', '[R]', '[G]', '[B]'])


    # ext-i18n/mcore_all/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER] 
    def test_mcore_show_7segments_number(self):
        key = 'mcore_show_7segments_number'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER]'])


    # ext-i18n/mcore_all/mcore_detect_external_ultrasonic contains [ICON] [PORT]
    def test_mcore_detect_external_ultrasonic(self):
        key = 'mcore_detect_external_ultrasonic'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])


    # ext-i18n/mcore_all/mcore_detect_external_light contains [ICON] [PORT]
    def test_mcore_detect_external_light(self):
        key = 'mcore_detect_external_light'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])


    # ext-i18n/mcore_all/mcore_detect_external_loudness contains [ICON] [PORT]
    def test_mcore_detect_external_loudness(self):
        key = 'mcore_detect_external_loudness'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])


    # ext-i18n/mcore_all/mcore_detect_external_linefollower contains [ICON] [PORT]
    def test_mcore_detect_external_linefollower(self):
        key = 'mcore_detect_external_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore_all/mcore_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_mcore_event_external_linefollower(self):
        key = 'mcore_event_external_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LINEFOLLOW_STATE]', '[BLACK_WHITE]'])

    # ext-i18n/mcore_all/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_mcore_event_limit_switch(self):
        key = 'mcore_event_limit_switch'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]'])

    # ext-i18n/mcore_all/mcore_detect_potentiometer contains [ICON] [PORT]
    def test_mcore_detect_potentiometer(self):
        key = 'mcore_detect_potentiometer'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore_all/mcore_detect_joystick contains [ICON] [PORT][AXIS_X_Y]
    def test_mcore_detect_joystick(self):
        key = 'mcore_detect_joystick'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[AXIS_X_Y]'])

    # ext-i18n/mcore_all/mcore_detect_infrared contains [ICON] [PORT]
    def test_mcore_detect_infrared(self):
        key = 'mcore_detect_infrared'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreAllTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)