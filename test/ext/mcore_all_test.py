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

    # ext-i18n/mcore_all/No empty value
    def test_ext_i18n_mcore_all_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/mcore_all/mcore_run_shutter contains [ICON] [PORT] [SHUTTER_ACTION]
    def test_ext_i18n_mcore_run_shutter(self):
        self.assertIn('mcore_run_shutter', self.test_dict)
        test_data = self.test_dict['mcore_run_shutter']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SHUTTER_ACTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_run_motor contains [ICON] [PORT][ROTATE][POWER] %
    def test_ext_i18n_mcore_run_motor(self):
        self.assertIn('mcore_run_motor', self.test_dict)
        test_data = self.test_dict['mcore_run_motor']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_ext_i18n_mcore_run_servo(self):
        self.assertIn('mcore_run_servo', self.test_dict)
        test_data = self.test_dict['mcore_run_servo']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_run_fan contains [ICON] [PORT][FAN_ROTATE]
    def test_ext_i18n_mcore_run_fan(self):
        self.assertIn('mcore_run_fan', self.test_dict)
        test_data = self.test_dict['mcore_run_fan']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FAN_ROTATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_ext_i18n_mcore_show_face_time(self):
        self.assertIn('mcore_show_face_time', self.test_dict)
        test_data = self.test_dict['mcore_show_face_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_face contains [ICON] [PORT] [FACE_PANEL] 
    def test_ext_i18n_mcore_show_face(self):
        self.assertIn('mcore_show_face', self.test_dict)
        test_data = self.test_dict['mcore_show_face']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y] 
    def test_ext_i18n_mcore_show_face_position(self):
        self.assertIn('mcore_show_face_position', self.test_dict)
        test_data = self.test_dict['mcore_show_face_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_text contains [ICON] [PORT] [TEXT] 
    def test_ext_i18n_mcore_show_text(self):
        self.assertIn('mcore_show_text', self.test_dict)
        test_data = self.test_dict['mcore_show_text']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_text_position contains [ICON] [PORT] [TEXT] x: [X] y: [Y] 
    def test_ext_i18n_mcore_show_text_position(self):
        self.assertIn('mcore_show_text_position', self.test_dict)
        test_data = self.test_dict['mcore_show_text_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_number contains [ICON] [PORT] [NUMBER] 
    def test_ext_i18n_mcore_show_number(self):
        self.assertIn('mcore_show_number', self.test_dict)
        test_data = self.test_dict['mcore_show_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_time contains [ICON] [PORT] [NUMBER1]: [NUMBER2]
    def test_ext_i18n_mcore_show_time(self):
        self.assertIn('mcore_show_time', self.test_dict)
        test_data = self.test_dict['mcore_show_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER1]: [NUMBER2]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_face_off contains [ICON] [PORT] 
    def test_ext_i18n_mcore_show_face_off(self):
        self.assertIn('mcore_show_face_off', self.test_dict)
        test_data = self.test_dict['mcore_show_face_off']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_ext_i18n_mcore_show_external_led_time(self):
        self.assertIn('mcore_show_external_led_time', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_ext_i18n_mcore_show_external_led(self):
        self.assertIn('mcore_show_external_led', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_ext_i18n_mcore_show_external_led_rgb(self):
        self.assertIn('mcore_show_external_led_rgb', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_rgb']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_ext_i18n_mcore_show_all_ledstrip_color(self):
        self.assertIn('mcore_show_all_ledstrip_color', self.test_dict)
        test_data = self.test_dict['mcore_show_all_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_ext_i18n_mcore_show_ledstrip_color(self):
        self.assertIn('mcore_show_ledstrip_color', self.test_dict)
        test_data = self.test_dict['mcore_show_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
    def test_ext_i18n_mcore_show_ledstrip_rbg(self):
        self.assertIn('mcore_show_ledstrip_rbg', self.test_dict)
        test_data = self.test_dict['mcore_show_ledstrip_rbg']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER] 
    def test_ext_i18n_mcore_show_7segments_number(self):
        self.assertIn('mcore_show_7segments_number', self.test_dict)
        test_data = self.test_dict['mcore_show_7segments_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_detect_external_ultrasonic contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_ultrasonic(self):
        self.assertIn('mcore_detect_external_ultrasonic', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_ultrasonic']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_detect_external_light contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_light(self):
        self.assertIn('mcore_detect_external_light', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_light']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_detect_external_loudness contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_loudness(self):
        self.assertIn('mcore_detect_external_loudness', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_loudness']
        self.assertIn('[ICON]', test_data)
        self.assertIn('[PORT]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/mcore_all/mcore_detect_external_linefollower contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_linefollower(self):
        self.assertIn('mcore_detect_external_linefollower', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_ext_i18n_mcore_event_external_linefollower(self):
        self.assertIn('mcore_event_external_linefollower', self.test_dict)
        test_data = self.test_dict['mcore_event_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LINEFOLLOW_STATE]', test_data)
        self.assertIn('[BLACK_WHITE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_ext_i18n_mcore_event_limit_switch(self):
        self.assertIn('mcore_event_limit_switch', self.test_dict)
        test_data = self.test_dict['mcore_event_limit_switch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_detect_potentiometer contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_potentiometer(self):
        self.assertIn('mcore_detect_potentiometer', self.test_dict)
        test_data = self.test_dict['mcore_detect_potentiometer']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_detect_joystick contains [ICON] [PORT][AXIS_X_Y]
    def test_ext_i18n_mcore_detect_joystick(self):
        self.assertIn('mcore_detect_joystick', self.test_dict)
        test_data = self.test_dict['mcore_detect_joystick']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[AXIS_X_Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore_all/mcore_detect_infrared contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_infrared(self):
        self.assertIn('mcore_detect_infrared', self.test_dict)
        test_data = self.test_dict['mcore_detect_infrared']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreAllTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)