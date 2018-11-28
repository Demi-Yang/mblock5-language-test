# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  auriga_all項目-翻译检查  =======================

class AurigaAllTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/auriga_all']


    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0},\n value:{1},\n error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey:{0}, 缺少参数：{1}'.format(key, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, 缺少参数：[ICON]'.format(key))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, error:参数[ICON]必须在首位'.format(key))











    # ext-i18n/auriga_all/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "翻译为空的字段：" + key)

    # ext-i18n/auriga_all/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 110, "auriga_all 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/auriga_all/auriga_run_board_encoder_motor contains [ICON] [ROTATE] [POWER] [PORT]%
    def test_auriga_run_board_encoder_motor(self):
        key = 'auriga_run_board_encoder_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')  
        self.check_param(key, '[ROTATE]')  
        self.check_param(key, '[POWER]%')  
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_board_encoder_motor_speed contains [ICON] [PORT] [ROTATE] [POWER]
    def test_auriga_run_board_encoder_motor_speed(self):
        key = 'auriga_run_board_encoder_motor_speed'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER]')  
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_board_encoder_motor_pos contains [ICON] [PORT] [ROTATE] [DEGREE] [POWER][G][B]
    def test_auriga_run_board_encoder_motor_pos(self):
        key = 'auriga_run_board_encoder_motor_pos'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]') 
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_encoder_motor contains [ICON] [PORT] [SLOT] [ROTATE] [DEGREE][POWER]
    def test_auriga_run_encoder_motor(self):
        key = 'auriga_run_encoder_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]') 
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_motor contains [ICON] [PORT] [ROTATE] [POWER] %
    def test_auriga_run_motor(self):
        key = 'auriga_run_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER] %') 
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_stepper_motor_pos contains [ICON] [PORT] [ROTATE] [DISTANCE] [POWER]
    def test_auriga_run_stepper_motor_pos(self):
        key = 'auriga_run_stepper_motor_pos'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DISTANCE]')  
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_servo contains [ICON] [PORT] [SLOT] [DEGREE]
    def test_auriga_run_servo(self):
        key = 'auriga_run_servo'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[DEGREE]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_fan contains [ICON] [PORT] [FAN_ROTATE]
    def test_auriga_run_fan(self):
        key = 'auriga_run_fan'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FAN_ROTATE]')   
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_shutter contains [ICON] [PORT] [SHUTTER_ACTION]
    def test_auriga_run_shutter(self):
        key = 'auriga_run_shutter'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SHUTTER_ACTION]') 
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_smart_servo_to_zero contains [ICON] [INDEX]
    def test_auriga_run_smart_servo_to_zero(self):
        key = 'auriga_run_smart_servo_to_zero'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')  
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_smart_servo contains [ICON] [INDEX] [ROTATE] [POWER]
    def test_auriga_run_smart_servo(self):
        key = 'auriga_run_smart_servo'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_smart_servo_absolute contains [ICON] [INDEX] [ROTATE] [POSITION] [POWER]
    def test_auriga_run_smart_servo_absolute(self):
        key = 'auriga_run_smart_servo_absolute'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POSITION]') 
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_run_smart_servo_to_relative contains [ICON] [INDEX] [ROTATE] [DEGREE] [POWER]
    def test_auriga_run_smart_servo_to_relative(self):
        key = 'auriga_run_smart_servo_to_relative'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_auriga_show_face_time(self):
        key = 'auriga_show_face_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_face contains [ICON] [PORT] [FACE_PANEL]
    def test_auriga_show_face(self):
        key = 'auriga_show_face'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y]
    def test_auriga_show_face_position(self):
        key = 'auriga_show_face_position'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_param(key, 'x: [X] y: [Y]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_text contains [ICON] [PORT] [TEXT]
    def test_auriga_show_text(self):
        key = 'auriga_show_text'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEXT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_text_position contains [ICON]  [PORT] [TEXT] x: [X] y: [Y]
    def test_auriga_show_text_position(self):
        key = 'auriga_show_text_position'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEXT]')
        self.check_param(key, 'x: [X] y: [Y]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_number contains [ICON] [PORT] [NUMBER]
    def test_auriga_show_number(self):
        key = 'auriga_show_number'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_time contains [ICON] [PORT] [NUMBER1] [NUMBER2]
    def test_auriga_show_time(self):
        key = 'auriga_show_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER1]')
        self.check_param(key, '[NUMBER2]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_face_off contains [ICON] [PORT]
    def test_auriga_show_face_off(self):
        key = 'auriga_show_face_off'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME]
    def test_auriga_show_external_led_time(self):
        key = 'auriga_show_external_led_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR]
    def test_auriga_show_external_led(self):
        key = 'auriga_show_external_led'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_auriga_show_external_led_rgb(self):
        key = 'auriga_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)


    # ext-i18n/auriga_all/auriga_show_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_auriga_show_all_ledstrip_color(self):
        key = 'auriga_show_ledstrip_color'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[COLOR_LIST]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_auriga_show_ledstrip_color(self):
        key = 'auriga_show_ledstrip_color'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[POS]')
        self.check_param(key, '[COLOR_LIST]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
    def test_auriga_show_ledstrip_rbg(self):
        key = 'auriga_show_ledstrip_rbg'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[POS]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_show_7segments_number contains [ICON] [PORT] [NUMBER]
    def test_auriga_show_7segments_number(self):
        key = 'auriga_show_7segments_number'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_external_ultrasonic contains [ICON] [PORT]
    def test_auriga_detect_external_ultrasonic(self):
        key = 'auriga_detect_external_ultrasonic'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_external_light contains [ICON] [PORT]
    def test_auriga_detect_external_light(self):
        key = 'auriga_detect_external_light'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_external_loudness contains [ICON] [PORT]
    def test_auriga_detect_external_loudness(self):
        key = 'auriga_detect_external_loudness'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_external_linefollower contains [ICON] [PORT]
    def test_auriga_detect_external_linefollower(self):
        key = 'auriga_detect_external_linefollower'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_auriga_event_external_linefollower(self):
        key = 'auriga_event_external_linefollower'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LINEFOLLOW_STATE]')
        self.check_param(key, '[BLACK_WHITE]')
        self.check_icon(key)


    # ext-i18n/auriga_all/auriga_detec_temperature contains [ICON] [SLOT] [PORT] 
    def test_auriga_detec_temperature(self):
        key = 'auriga_detec_temperature'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_humiture contains [ICON] [TEMP_HUMITURE] [PORT]
    def test_auriga_detect_humiture(self):
        key = 'auriga_detect_humiture'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEMP_HUMITURE]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_event_touch contains [ICON] [PORT]
    def test_auriga_event_touch(self):
        key = 'auriga_event_touch'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_compass contains [ICON] [PORT]
    def test_auriga_detect_compass(self):
        key = 'auriga_detect_compass'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_flame contains [ICON] [PORT]
    def test_auriga_detect_flame(self):
        key = 'auriga_detect_flame'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_gas contains [ICON] [PORT]
    def test_auriga_detect_gas(self):
        key = 'auriga_detect_gas'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_board_gyro_angle contains [ICON] [AXIS]
    def test_auriga_detect_board_gyro_angle(self):
        key = 'auriga_detect_board_gyro_angle'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_gyro_angle contains [ICON] [AXIS]
    def test_auriga_detect_gyro_angle(self):
        key = 'auriga_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_event_pir_motion contains [ICON] [PORT]
    def test_auriga_event_pir_motion(self):
        key = 'auriga_event_pir_motion'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_event_button_press contains [ICON] [FOUR_KEY] [PORT]
    def test_auriga_event_button_press(self):
        key = 'auriga_event_button_press'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FOUR_KEY]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_event_limit_switch contains [ICON] [PORT] [SLOT]
    def test_auriga_event_limit_switch(self):
        key = 'auriga_event_limit_switch'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_potentiometer contains [ICON] [PORT]
    def test_auriga_detect_potentiometer(self):
        key = 'auriga_detect_potentiometer'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_joystick contains [ICON] [PORT] [AXIS_X_Y]
    def test_auriga_detect_joystick(self):
        key = 'auriga_detect_joystick'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[AXIS_X_Y]')
        self.check_icon(key)

    # ext-i18n/auriga_all/auriga_detect_infrared contains [ICON] [PORT]
    def test_auriga_detect_infrared(self):
        key = 'auriga_detect_infrared'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaAllTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)