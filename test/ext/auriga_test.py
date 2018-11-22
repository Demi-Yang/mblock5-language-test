# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  auriga項目-翻译检查  =======================

class AurigaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/auriga']

    # ext-i18n/auriga/No empty value
    def test_ext_i18n_auriga_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/auriga/extensionName equals "mBot Ranger"
    def test_ext_i18n_auriga_extensionName_equals_Arduino_Uno(self):
        self.assertIn('extensionName', self.test_dict)
        test_data = self.test_dict['extensionName']
        self.assertEqual(test_data, "mBot Ranger")

    # ext-i18n/auriga/auriga_show_all_led_time contains [ICON] [COLOR] [TIME]
    def test_ext_i18n_auriga_show_all_led_time(self):
        self.assertIn('auriga_show_all_led_time', self.test_dict)
        test_data = self.test_dict['auriga_show_all_led_time']
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_all_led contains [ICON] [COLOR]
    def test_ext_i18n_auriga_show_all_led(self):
        self.assertIn('auriga_show_all_led', self.test_dict)
        test_data = self.test_dict['auriga_show_all_led']
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_all_led_rgb contains [ICON] [R] [G] [B]
    def test_ext_i18n_auriga_show_all_led_rgb(self):
        self.assertIn('auriga_show_all_led_rgb', self.test_dict)
        test_data = self.test_dict['auriga_show_all_led_rgb']
        self.assertIn('[R]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_led_time contains [ICON] [LED_POSTION] [COLOR] [TIME]
    def test_ext_i18n_auriga_show_led_time(self):
        self.assertIn('auriga_show_led_time', self.test_dict)
        test_data = self.test_dict['auriga_show_led_time']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_led contains [ICON] [LED_POSTION] [COLOR]
    def test_ext_i18n_auriga_show_led(self):
        self.assertIn('auriga_show_led', self.test_dict)
        test_data = self.test_dict['auriga_show_led']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_led_rgb contains [ICON] [LED_POSTION] [R] [B] [G]
    def test_ext_i18n_auriga_show_led_rgb(self):
        self.assertIn('auriga_show_led_rgb', self.test_dict)
        test_data = self.test_dict['auriga_show_led_rgb']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_sound_play_note contains [ICON] [NOTE] [BEAT]
    def test_ext_i18n_auriga_sound_play_note(self):
        self.assertIn('auriga_sound_play_note', self.test_dict)
        test_data = self.test_dict['auriga_sound_play_note']
        self.assertIn('[NOTE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_sound_play_hz contains [ICON] [HZ] [TIME]
    def test_ext_i18n_auriga_sound_play_hz(self):
        self.assertIn('auriga_sound_play_hz', self.test_dict)
        test_data = self.test_dict['auriga_sound_play_hz']
        self.assertIn('[TIME]', test_data)
        self.assertIn('[HZ]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_ext_i18n_auriga_show_face_time(self):
        self.assertIn('auriga_show_face_time', self.test_dict)
        test_data = self.test_dict['auriga_show_face_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_face contains [ICON] [PORT] [FACE_PANEL]
    def test_ext_i18n_auriga_show_face(self):
        self.assertIn('auriga_show_face', self.test_dict)
        test_data = self.test_dict['auriga_show_face']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y]
    def test_ext_i18n_auriga_show_face_position(self):
        self.assertIn('auriga_show_face_position', self.test_dict)
        test_data = self.test_dict['auriga_show_face_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_text contains [ICON] [PORT] [TEXT]
    def test_ext_i18n_auriga_show_text(self):
        self.assertIn('auriga_show_text', self.test_dict)
        test_data = self.test_dict['auriga_show_text']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_text_position contains [ICON]  [PORT] [TEXT] x: [X] y: [Y]
    def test_ext_i18n_auriga_show_text_position(self):
        self.assertIn('auriga_show_text_position', self.test_dict)
        test_data = self.test_dict['auriga_show_text_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_number contains [ICON] [PORT] [NUMBER]
    def test_ext_i18n_auriga_show_number(self):
        self.assertIn('auriga_show_number', self.test_dict)
        test_data = self.test_dict['auriga_show_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_time contains [ICON] [PORT] [NUMBER1] [NUMBER2]
    def test_ext_i18n_auriga_show_time(self):
        self.assertIn('auriga_show_time', self.test_dict)
        test_data = self.test_dict['auriga_show_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER1]', test_data)
        self.assertIn('[NUMBER2]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_face_off contains [ICON] [PORT]
    def test_ext_i18n_auriga_show_face_off(self):
        self.assertIn('auriga_show_face_off', self.test_dict)
        test_data = self.test_dict['auriga_show_face_off']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME]
    def test_ext_i18n_auriga_show_external_led_time(self):
        self.assertIn('auriga_show_external_led_time', self.test_dict)
        test_data = self.test_dict['auriga_show_external_led_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR]
    def test_ext_i18n_auriga_show_external_led(self):
        self.assertIn('auriga_show_external_led', self.test_dict)
        test_data = self.test_dict['auriga_show_external_led']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_ext_i18n_auriga_show_external_led_rgb(self):
        self.assertIn('auriga_show_external_led_rgb', self.test_dict)
        test_data = self.test_dict['auriga_show_external_led_rgb']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_ext_i18n_auriga_show_all_ledstrip_color(self):
        self.assertIn('auriga_show_all_ledstrip_color', self.test_dict)
        test_data = self.test_dict['auriga_show_all_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_ext_i18n_auriga_show_ledstrip_color(self):
        self.assertIn('auriga_show_ledstrip_color', self.test_dict)
        test_data = self.test_dict['auriga_show_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
    def test_ext_i18n_auriga_show_ledstrip_rbg(self):
        self.assertIn('auriga_show_ledstrip_rbg', self.test_dict)
        test_data = self.test_dict['auriga_show_ledstrip_rbg']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_show_7segments_number contains [ICON] [PORT] [NUMBER]
    def test_ext_i18n_auriga_show_7segments_number(self):
        self.assertIn('auriga_show_7segments_number', self.test_dict)
        test_data = self.test_dict['auriga_show_7segments_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_forward_time contains [ICON] [POWER] [TIME]
    def test_ext_i18n_auriga_forward_time(self):
        self.assertIn('auriga_forward_time', self.test_dict)
        test_data = self.test_dict['auriga_forward_time']
        self.assertIn('[POWER]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_backward_time contains [ICON]  [POWER] [TIME]
    def test_ext_i18n_auriga_backward_time(self):
        self.assertIn('auriga_backward_time', self.test_dict)
        test_data = self.test_dict['auriga_backward_time']
        self.assertIn('[POWER]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_turnleft_time contains [ICON]  [POWER] [TIME]
    def test_ext_i18n_auriga_turnleft_time(self):
        self.assertIn('auriga_turnleft_time', self.test_dict)
        test_data = self.test_dict['auriga_turnleft_time']
        self.assertIn('[POWER]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_turnright_time contains [ICON]  [POWER] [TIME]
    def test_ext_i18n_auriga_turnright_time(self):
        self.assertIn('auriga_turnright_time', self.test_dict)
        test_data = self.test_dict['auriga_turnright_time']
        self.assertIn('[POWER]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_sauriga_movehow_ledstrip_rbg contains [ICON] [MOVE_DIRECTION] [POWER] 
    def test_ext_i18n_auriga_move(self):
        self.assertIn('auriga_move', self.test_dict)
        test_data = self.test_dict['auriga_move']
        self.assertIn('[MOVE_DIRECTION]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_move_wheel_speed contains [ICON] [POWER_LEFT] [POWER_RIGHT]
    def test_ext_i18n_auriga_move_wheel_speed(self):
        self.assertIn('auriga_move_wheel_speed', self.test_dict)
        test_data = self.test_dict['auriga_move_wheel_speed']
        self.assertIn('[POWER_LEFT]', test_data)
        self.assertIn('[POWER_RIGHT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_move_stop contains [ICON]
    def test_ext_i18n_auriga_move_stop(self):
        self.assertIn('auriga_move_stop', self.test_dict)
        test_data = self.test_dict['auriga_move_stop']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_board_encoder_motor contains [ICON] [ROTATE] [POWER] [PORT]%
    def test_ext_i18n_auriga_run_board_encoder_motor(self):
        self.assertIn('auriga_run_board_encoder_motor', self.test_dict)
        test_data = self.test_dict['auriga_run_board_encoder_motor']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER]%', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_board_encoder_motor_speed contains [ICON] [PORT] [ROTATE] [POWER]
    def test_ext_i18n_auriga_run_board_encoder_motor_speed(self):
        self.assertIn('auriga_run_board_encoder_motor_speed', self.test_dict)
        test_data = self.test_dict['auriga_run_board_encoder_motor_speed']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_board_encoder_motor_pos contains [ICON] [PORT] [ROTATE] [DEGREE] [POWER][G][B]
    def test_ext_i18n_auriga_run_board_encoder_motor_pos(self):
        self.assertIn('auriga_run_board_encoder_motor_pos', self.test_dict)
        test_data = self.test_dict['auriga_run_board_encoder_motor_pos']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_encoder_motor contains [ICON] [PORT] [SLOT] [ROTATE] [DEGREE][POWER]
    def test_ext_i18n_auriga_run_encoder_motor(self):
        self.assertIn('auriga_run_encoder_motor', self.test_dict)
        test_data = self.test_dict['auriga_run_encoder_motor']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_motor contains [ICON] [PORT] [ROTATE] [POWER] %
    def test_ext_i18n_auriga_run_motor(self):
        self.assertIn('auriga_run_motor', self.test_dict)
        test_data = self.test_dict['auriga_run_motor']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_stepper_motor_pos contains [ICON] [PORT] [ROTATE] [DISTANCE] [POWER]
    def test_ext_i18n_auriga_run_stepper_motor_pos(self):
        self.assertIn('auriga_run_stepper_motor_pos', self.test_dict)
        test_data = self.test_dict['auriga_run_stepper_motor_pos']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[DISTANCE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_servo contains [ICON] [PORT] [SLOT] [DEGREE]
    def test_ext_i18n_auriga_run_servo(self):
        self.assertIn('auriga_run_servo', self.test_dict)
        test_data = self.test_dict['auriga_run_servo']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_fan contains [ICON] [PORT] [FAN_ROTATE]
    def test_ext_i18n_auriga_run_fan(self):
        self.assertIn('auriga_run_fan', self.test_dict)
        test_data = self.test_dict['auriga_run_fan']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FAN_ROTATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_shutter contains [ICON] [PORT] [SHUTTER_ACTION]
    def test_ext_i18n_auriga_run_shutter(self):
        self.assertIn('auriga_run_shutter', self.test_dict)
        test_data = self.test_dict['auriga_run_shutter']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SHUTTER_ACTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_smart_servo_to_zero contains [ICON] [INDEX]
    def test_ext_i18n_auriga_run_smart_servo_to_zero(self):
        self.assertIn('auriga_run_smart_servo_to_zero', self.test_dict)
        test_data = self.test_dict['auriga_run_smart_servo_to_zero']
        self.assertIn('[INDEX]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_smart_servo contains [ICON] [INDEX] [ROTATE] [POWER]
    def test_ext_i18n_auriga_run_smart_servo(self):
        self.assertIn('auriga_run_smart_servo', self.test_dict)
        test_data = self.test_dict['auriga_run_smart_servo']
        self.assertIn('[INDEX]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_smart_servo_absolute contains [ICON] [INDEX] [ROTATE] [POSITION] [POWER]
    def test_ext_i18n_auriga_run_smart_servo_absolute(self):
        self.assertIn('auriga_run_smart_servo_absolute', self.test_dict)
        test_data = self.test_dict['auriga_run_smart_servo_absolute']
        self.assertIn('[INDEX]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POSITION]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_run_smart_servo_to_relative contains [ICON] [INDEX] [ROTATE] [DEGREE] [POWER]
    def test_ext_i18n_auriga_run_smart_servo_to_relative(self):
        self.assertIn('auriga_run_smart_servo_to_relative', self.test_dict)
        test_data = self.test_dict['auriga_run_smart_servo_to_relative']
        self.assertIn('[INDEX]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[POWER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_light contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_light(self):
        self.assertIn('auriga_detect_light', self.test_dict)
        test_data = self.test_dict['auriga_detect_light']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_temperature contains [ICON] 
    def test_ext_i18n_auriga_detect_temperature(self):
        self.assertIn('auriga_detect_temperature', self.test_dict)
        test_data = self.test_dict['auriga_detect_temperature']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_loudness contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_loudness(self):
        self.assertIn('auriga_detect_loudness', self.test_dict)
        test_data = self.test_dict['auriga_detect_loudness']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_board_gyro_angle contains [ICON] [AXIS]
    def test_ext_i18n_auriga_detect_board_gyro_angle(self):
        self.assertIn('auriga_detect_board_gyro_angle', self.test_dict)
        test_data = self.test_dict['auriga_detect_board_gyro_angle']
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_external_ultrasonic contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_external_ultrasonic(self):
        self.assertIn('auriga_detect_external_ultrasonic', self.test_dict)
        test_data = self.test_dict['auriga_detect_external_ultrasonic']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_external_linefollower contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_external_linefollower(self):
        self.assertIn('auriga_detect_external_linefollower', self.test_dict)
        test_data = self.test_dict['auriga_detect_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_ext_i18n_auriga_event_external_linefollower(self):
        self.assertIn('auriga_event_external_linefollower', self.test_dict)
        test_data = self.test_dict['auriga_event_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LINEFOLLOW_STATE]', test_data)
        self.assertIn('[BLACK_WHITE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_timer contains [ICON]
    def test_ext_i18n_auriga_detect_timer(self):
        self.assertIn('auriga_detect_timer', self.test_dict)
        test_data = self.test_dict['auriga_detect_timer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_reset_timer contains [ICON]
    def test_ext_i18n_auriga_reset_timer(self):
        self.assertIn('auriga_reset_timer', self.test_dict)
        test_data = self.test_dict['auriga_reset_timer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_external_light contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_external_light(self):
        self.assertIn('auriga_detect_external_light', self.test_dict)
        test_data = self.test_dict['auriga_detect_external_light']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_external_loudness contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_external_loudness(self):
        self.assertIn('auriga_detect_external_loudness', self.test_dict)
        test_data = self.test_dict['auriga_detect_external_loudness']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detec_temperature contains [ICON] [SLOT] [PORT] 
    def test_ext_i18n_auriga_detec_temperature(self):
        self.assertIn('auriga_detec_temperature', self.test_dict)
        test_data = self.test_dict['auriga_detec_temperature']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_humiture contains [ICON] [TEMP_HUMITURE] [PORT]
    def test_ext_i18n_auriga_detect_humiture(self):
        self.assertIn('auriga_detect_humiture', self.test_dict)
        test_data = self.test_dict['auriga_detect_humiture']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEMP_HUMITURE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_touch contains [ICON] [PORT]
    def test_ext_i18n_auriga_event_touch(self):
        self.assertIn('auriga_event_touch', self.test_dict)
        test_data = self.test_dict['auriga_event_touch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_compass contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_compass(self):
        self.assertIn('auriga_detect_compass', self.test_dict)
        test_data = self.test_dict['auriga_detect_compass']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_flame contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_flame(self):
        self.assertIn('auriga_detect_flame', self.test_dict)
        test_data = self.test_dict['auriga_detect_flame']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_gas contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_gas(self):
        self.assertIn('auriga_detect_gas', self.test_dict)
        test_data = self.test_dict['auriga_detect_gas']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_gyro_angle contains [ICON] [AXIS]
    def test_ext_i18n_auriga_detect_gyro_angle(self):
        self.assertIn('auriga_detect_gyro_angle', self.test_dict)
        test_data = self.test_dict['auriga_detect_gyro_angle']
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_pir_motion contains [ICON] [PORT]
    def test_ext_i18n_auriga_event_pir_motion(self):
        self.assertIn('auriga_event_pir_motion', self.test_dict)
        test_data = self.test_dict['auriga_event_pir_motion']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_button_press contains [ICON] [FOUR_KEY] [PORT]
    def test_ext_i18n_auriga_event_button_press(self):
        self.assertIn('auriga_event_button_press', self.test_dict)
        test_data = self.test_dict['auriga_event_button_press']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FOUR_KEY]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_limit_switch contains [ICON] [PORT] [SLOT]
    def test_ext_i18n_auriga_event_limit_switch(self):
        self.assertIn('auriga_event_limit_switch', self.test_dict)
        test_data = self.test_dict['auriga_event_limit_switch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_potentiometer contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_potentiometer(self):
        self.assertIn('auriga_detect_potentiometer', self.test_dict)
        test_data = self.test_dict['auriga_detect_potentiometer']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_joystick contains [ICON] [PORT] [AXIS_X_Y]
    def test_ext_i18n_auriga_detect_joystick(self):
        self.assertIn('auriga_detect_joystick', self.test_dict)
        test_data = self.test_dict['auriga_detect_joystick']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[AXIS_X_Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_infrared contains [ICON] [PORT]
    def test_ext_i18n_auriga_detect_infrared(self):
        self.assertIn('auriga_detect_infrared', self.test_dict)
        test_data = self.test_dict['auriga_detect_infrared']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_obstacle contains [ICON]=
    def test_ext_i18n_auriga_event_obstacle(self):
        self.assertIn('auriga_event_obstacle', self.test_dict)
        test_data = self.test_dict['auriga_event_obstacle']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_obstacle_distance contains [ICON]
    def test_ext_i18n_auriga_detect_obstacle_distance(self):
        self.assertIn('auriga_detect_obstacle_distance', self.test_dict)
        test_data = self.test_dict['auriga_detect_obstacle_distance']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_event_linefollower contains [ICON] 
    def test_ext_i18n_auriga_event_linefollower(self):
        self.assertIn('auriga_event_linefollower', self.test_dict)
        test_data = self.test_dict['auriga_event_linefollower']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_detect_angle contains [ICON] [AXIS]
    def test_ext_i18n_auriga_detect_angle(self):
        self.assertIn('auriga_detect_angle', self.test_dict)
        test_data = self.test_dict['auriga_detect_angle']
        self.assertIn('AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/auriga/auriga_when_board_launch contains  mBot Ranger(Auriga)
    def test_ext_i18n_auriga_when_board_launch(self):
        self.assertIn('auriga_when_board_launch', self.test_dict)
        test_data = self.test_dict['auriga_when_board_launch']
        self.assertIn('mBot Ranger(Auriga)', test_data)

    # ext-i18n/auriga/AURIGA_SOUND_PLAY_NOTE_NOTE is right
    def test_ext_i18n_AURIGA_SOUND_PLAY_NOTE_NOTE(self):
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_0'], "C2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_1'], "D2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_2'], "E2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_3'], "F2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_4'], "G2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_5'], "A2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_6'], "B2")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_7'], "C3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_8'], "D3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_9'], "E3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_10'], "F3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_11'], "G3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_12'], "A3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_13'], "B3")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_14'], "C4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_15'], "D4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_16'], "E4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_17'], "F4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_18'], "G4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_19'], "A4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_20'], "B4")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_21'], "C5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_22'], "D5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_23'], "E5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_24'], "F5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_25'], "G5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_26'], "A5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_27'], "B5")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_28'], "C6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_29'], "D6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_30'], "E6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_31'], "F6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_32'], "G6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_33'], "A6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_34'], "B6")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_35'], "C7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_36'], "D7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_37'], "E7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_38'], "F7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_39'], "G7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_40'], "A7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_41'], "B7")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_42'], "C8")
        self.assertEqual(self.test_dict['AURIGA_SOUND_PLAY_NOTE_NOTE_43'], "D8")


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)