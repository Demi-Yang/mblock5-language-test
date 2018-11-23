# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mcore項目-翻译检查  =======================

class McoreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/mcore']

    # ext-i18n/mcore/No empty value
    def test_ext_i18n_mcore_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/mcore/No new or missing items
    def test_ext_i18n_mcore_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 198)

    # mblock5-i18n/extensionName&codeyneuron equals mBot
    def test_mblock5_i18n_extensionName_equals_mBot(self):
        self.assertIn('extensionName', self.test_dict)
        self.assertIn('mcore', self.test_dict)
        self.assertEqual(self.test_dict['extensionName'], "mBot")
        self.assertEqual(self.test_dict['mcore'], "mBot")

    # ext-i18n/mcore/mcore_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_ext_i18n_mcore_show_face_time(self):
        self.assertIn('mcore_show_face_time', self.test_dict)
        test_data = self.test_dict['mcore_show_face_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_face contains [ICON] [PORT] [FACE_PANEL] 
    def test_ext_i18n_mcore_show_face(self):
        self.assertIn('mcore_show_face', self.test_dict)
        test_data = self.test_dict['mcore_show_face']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y] 
    def test_ext_i18n_mcore_show_face_position(self):
        self.assertIn('mcore_show_face_position', self.test_dict)
        test_data = self.test_dict['mcore_show_face_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FACE_PANEL]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_text contains [ICON] [PORT] [TEXT] 
    def test_ext_i18n_mcore_show_text(self):
        self.assertIn('mcore_show_text', self.test_dict)
        test_data = self.test_dict['mcore_show_text']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_text_position contains [ICON] [PORT] [TEXT] x: [X] y: [Y] 
    def test_ext_i18n_mcore_show_text_position(self):
        self.assertIn('mcore_show_text_position', self.test_dict)
        test_data = self.test_dict['mcore_show_text_position']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_number contains [ICON] [PORT] [NUMBER] 
    def test_ext_i18n_mcore_show_number(self):
        self.assertIn('mcore_show_number', self.test_dict)
        test_data = self.test_dict['mcore_show_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_time contains [ICON] [PORT] [NUMBER1]: [NUMBER2]
    def test_ext_i18n_mcore_show_time(self):
        self.assertIn('mcore_show_time', self.test_dict)
        test_data = self.test_dict['mcore_show_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER1]: [NUMBER2]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_face_off contains [ICON] [PORT] 
    def test_ext_i18n_mcore_show_face_off(self):
        self.assertIn('mcore_show_face_off', self.test_dict)
        test_data = self.test_dict['mcore_show_face_off']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER] 
    def test_ext_i18n_mcore_show_7segments_number(self):
        self.assertIn('mcore_show_7segments_number', self.test_dict)
        test_data = self.test_dict['mcore_show_7segments_number']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[NUMBER]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_led_time contains [ICON] [LED_POSTION] [COLOR] [TIME]
    def test_ext_i18n_mcore_show_led_time(self):
        self.assertIn('mcore_show_led_time', self.test_dict)
        test_data = self.test_dict['mcore_show_led_time']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_led contains [ICON] [LED_POSTION] [COLOR] 
    def test_ext_i18n_mcore_show_led(self):
        self.assertIn('mcore_show_led', self.test_dict)
        test_data = self.test_dict['mcore_show_led']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_led_rgb contains [ICON] [LED_POSTION] [R] [G][B]
    def test_ext_i18n_mcore_show_led_rgb(self):
        self.assertIn('mcore_show_led_rgb', self.test_dict)
        test_data = self.test_dict['mcore_show_led_rgb']
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_sound_play_note contains [ICON] [NOTE] [BEAT] 
    def test_ext_i18n_mcore_sound_play_note(self):
        self.assertIn('mcore_sound_play_note', self.test_dict)
        test_data = self.test_dict['mcore_sound_play_note']
        self.assertIn('[NOTE]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_sound_play_hz contains [ICON] [HZ] [TIME] 
    def test_ext_i18n_mcore_sound_play_hz(self):
        self.assertIn('mcore_sound_play_hz', self.test_dict)
        test_data = self.test_dict['mcore_sound_play_hz']
        self.assertIn('[HZ]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_ext_i18n_mcore_show_external_led_time(self):
        self.assertIn('mcore_show_external_led_time', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led_time']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_ext_i18n_mcore_show_external_led(self):
        self.assertIn('mcore_show_external_led', self.test_dict)
        test_data = self.test_dict['mcore_show_external_led']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LED_POSTION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
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

    # ext-i18n/mcore/mcore_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_ext_i18n_mcore_show_all_ledstrip_color(self):
        self.assertIn('mcore_show_all_ledstrip_color', self.test_dict)
        test_data = self.test_dict['mcore_show_all_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_ext_i18n_mcore_show_ledstrip_color(self):
        self.assertIn('mcore_show_ledstrip_color', self.test_dict)
        test_data = self.test_dict['mcore_show_ledstrip_color']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POS]', test_data)
        self.assertIn('[COLOR_LIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
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

    # ext-i18n/mcore/mcore_forward_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_mcore_forward_time(self):
        self.assertIn('mcore_forward_time', self.test_dict)
        test_data = self.test_dict['mcore_forward_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_backward_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_mcore_backward_time(self):
        self.assertIn('mcore_backward_time', self.test_dict)
        test_data = self.test_dict['mcore_backward_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_turnleft_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_mcore_turnleft_time(self):
        self.assertIn('mcore_turnleft_time', self.test_dict)
        test_data = self.test_dict['mcore_turnleft_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_turnright_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_mcore_turnright_time(self):
        self.assertIn('mcore_turnright_time', self.test_dict)
        test_data = self.test_dict['mcore_turnright_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_move contains [ICON] [POWER] % [MOVE_DIRECTION]
    def test_ext_i18n_mcore_move(self):
        self.assertIn('mcore_move', self.test_dict)
        test_data = self.test_dict['mcore_move']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[MOVE_DIRECTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_move_wheel_speed contains [ICON] [POWER_LEFT] % [POWER_RIGHT] %
    def test_ext_i18n_mcore_move_wheel_speed(self):
        self.assertIn('mcore_move_wheel_speed', self.test_dict)
        test_data = self.test_dict['mcore_move_wheel_speed']
        self.assertIn('[POWER_LEFT] %', test_data)
        self.assertIn('[POWER_RIGHT] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_move_stop contains [ICON] 
    def test_ext_i18n_mcore_move_stop(self):
        self.assertIn('mcore_move_stop', self.test_dict)
        test_data = self.test_dict['mcore_move_stop']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_run_shutter contains [ICON] [PORT][SHUTTER_ACTION]
    def test_ext_i18n_mcore_run_shutter(self):
        self.assertIn('mcore_run_shutter', self.test_dict)
        test_data = self.test_dict['mcore_run_shutter']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SHUTTER_ACTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_run_motor contains [ICON] [PORT][ROTATE][POWER] %
    def test_ext_i18n_mcore_run_motor(self):
        self.assertIn('mcore_run_motor', self.test_dict)
        test_data = self.test_dict['mcore_run_motor']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ROTATE]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_ext_i18n_mcore_run_servo(self):
        self.assertIn('mcore_run_servo', self.test_dict)
        test_data = self.test_dict['mcore_run_servo']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[DEGREE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_run_fan contains [ICON] [PORT][FAN_ROTATE]
    def test_ext_i18n_mcore_run_fan(self):
        self.assertIn('mcore_run_fan', self.test_dict)
        test_data = self.test_dict['mcore_run_fan']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FAN_ROTATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_external_light contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_light(self):
        self.assertIn('mcore_detect_external_light', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_light']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_external_ultrasonic contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_ultrasonic(self):
        self.assertIn('mcore_detect_external_ultrasonic', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_ultrasonic']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_external_linefollower contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_linefollower(self):
        self.assertIn('mcore_detect_external_linefollower', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_ext_i18n_mcore_event_external_linefollower(self):
        self.assertIn('mcore_event_external_linefollower', self.test_dict)
        test_data = self.test_dict['mcore_event_external_linefollower']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[LINEFOLLOW_STATE]', test_data)
        self.assertIn('[BLACK_WHITE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_board_button_pressed contains [ICON] [OPTION]
    def test_ext_i18n_mcore_event_board_button_pressed(self):
        self.assertIn('mcore_event_board_button_pressed', self.test_dict)
        test_data = self.test_dict['mcore_event_board_button_pressed']
        self.assertIn('[OPTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_ir_remote contains [ICON] [REMOTE_KEY]
    def test_ext_i18n_mcore_event_ir_remote(self):
        self.assertIn('mcore_event_ir_remote', self.test_dict)
        test_data = self.test_dict['mcore_event_ir_remote']
        self.assertIn('[REMOTE_KEY]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_send_ir contains [ICON] [MESSAGE]
    def test_ext_i18n_mcore_send_ir(self):
        self.assertIn('mcore_send_ir', self.test_dict)
        test_data = self.test_dict['mcore_send_ir']
        self.assertIn('[MESSAGE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_ir contains [ICON]
    def test_ext_i18n_mcore_detect_ir(self):
        self.assertIn('mcore_detect_ir', self.test_dict)
        test_data = self.test_dict['mcore_detect_ir']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_timer contains [ICON]
    def test_ext_i18n_mcore_detect_timer(self):
        self.assertIn('mcore_detect_timer', self.test_dict)
        test_data = self.test_dict['mcore_detect_timer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_reset_timer contains [ICON]
    def test_ext_i18n_mcore_reset_timer(self):
        self.assertIn('mcore_reset_timer', self.test_dict)
        test_data = self.test_dict['mcore_reset_timer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_external_loudness contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_external_loudness(self):
        self.assertIn('mcore_detect_external_loudness', self.test_dict)
        test_data = self.test_dict['mcore_detect_external_loudness']
        self.assertIn('[ICON]', test_data)
        self.assertIn('[PORT]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detec_temperature contains [ICON] [PORT] [SLOT]
    def test_ext_i18n_mcore_detec_temperature(self):
        self.assertIn('mcore_detec_temperature', self.test_dict)
        test_data = self.test_dict['mcore_detec_temperature']
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_humiture contains [ICON] [PORT] [TEMP_HUMITURE]
    def test_ext_i18n_mcore_detect_humiture(self):
        self.assertIn('mcore_detect_humiture', self.test_dict)
        test_data = self.test_dict['mcore_detect_humiture']
        self.assertIn('[TEMP_HUMITURE]', test_data)
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_touch contains [ICON] [PORT]
    def test_ext_i18n_mcore_event_touch(self):
        self.assertIn('mcore_event_touch', self.test_dict)
        test_data = self.test_dict['mcore_event_touch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_compass contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_compass(self):
        self.assertIn('mcore_detect_compass', self.test_dict)
        test_data = self.test_dict['mcore_detect_compass']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_flame contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_flame(self):
        self.assertIn('mcore_detect_flame', self.test_dict)
        test_data = self.test_dict['mcore_detect_flame']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_gas contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_gas(self):
        self.assertIn('mcore_detect_gas', self.test_dict)
        test_data = self.test_dict['mcore_detect_gas']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_gyro_angle contains [ICON] [AXIS]
    def test_ext_i18n_mcore_detect_gyro_angle(self):
        self.assertIn('mcore_detect_gyro_angle', self.test_dict)
        test_data = self.test_dict['mcore_detect_gyro_angle']
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_pir_motion contains [ICON] [PORT]
    def test_ext_i18n_mcore_event_pir_motion(self):
        self.assertIn('mcore_event_pir_motion', self.test_dict)
        test_data = self.test_dict['mcore_event_pir_motion']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_button_press contains [ICON] [PORT][FOUR_KEY]
    def test_ext_i18n_mcore_event_button_press(self):
        self.assertIn('mcore_event_button_press', self.test_dict)
        test_data = self.test_dict['mcore_event_button_press']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[FOUR_KEY]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_ext_i18n_mcore_event_limit_switch(self):
        self.assertIn('mcore_event_limit_switch', self.test_dict)
        test_data = self.test_dict['mcore_event_limit_switch']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_potentiometer contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_potentiometer(self):
        self.assertIn('mcore_detect_potentiometer', self.test_dict)
        test_data = self.test_dict['mcore_detect_potentiometer']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_joystick contains [ICON] [PORT][AXIS_X_Y]
    def test_ext_i18n_mcore_detect_joystick(self):
        self.assertIn('mcore_detect_joystick', self.test_dict)
        test_data = self.test_dict['mcore_detect_joystick']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[AXIS_X_Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_infrared contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_infrared(self):
        self.assertIn('mcore_detect_infrared', self.test_dict)
        test_data = self.test_dict['mcore_detect_infrared']
        self.assertIn('[PORT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_linefollower contains [ICON]
    def test_ext_i18n_mcore_event_linefollower(self):
        self.assertIn('mcore_event_linefollower', self.test_dict)
        test_data = self.test_dict['mcore_event_linefollower']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_event_obstacle contains [ICON]
    def test_ext_i18n_mcore_event_obstacle(self):
        self.assertIn('mcore_event_obstacle', self.test_dict)
        test_data = self.test_dict['mcore_event_obstacle']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_obstacle_distance contains [ICON]
    def test_ext_i18n_mcore_detect_obstacle_distance(self):
        self.assertIn('mcore_detect_obstacle_distance', self.test_dict)
        test_data = self.test_dict['mcore_detect_obstacle_distance']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_detect_light contains [ICON]
    def test_ext_i18n_mcore_detect_light(self):
        self.assertIn('mcore_detect_light', self.test_dict)
        test_data = self.test_dict['mcore_detect_light']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/mcore/mcore_when_board_button contains [IS_PRESS]
    def test_ext_i18n_mcore_when_board_button(self):
        self.assertIn('mcore_when_board_button', self.test_dict)
        test_data = self.test_dict['mcore_when_board_button']
        self.assertIn('[IS_PRESS]', test_data)

    # ext-i18n/mcore/MCORE_EVENT_IR_REMOTE_REMOTE_KEY is right
    def test_ext_i18n_MCORE_EVENT_IR_REMOTE_REMOTE_KEY(self):
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_0'], "A")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_1'], "B")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_2'], "C")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_3'], "D")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_4'], "E")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_5'], "F")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_11'], "0")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_12'], "1")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_13'], "2")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_14'], "3")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_15'], "4")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_16'], "5")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_17'], "6")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_18'], "7")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_19'], "8")
        self.assertEqual(self.test_dict['MCORE_EVENT_IR_REMOTE_REMOTE_KEY_20'], "9")

    # ext-i18n/mcore/MCORE_SOUND_PLAY_NOTE_NOTE is right
    def test_ext_i18n_MCORE_SOUND_PLAY_NOTE_NOTE(self):
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_0'], "C2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_1'], "D2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_2'], "E2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_3'], "F2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_4'], "G2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_5'], "A2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_6'], "B2")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_7'], "C3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_8'], "D3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_9'], "E3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_10'], "F3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_11'], "G3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_12'], "A3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_13'], "B3")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_14'], "C4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_15'], "D4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_16'], "E4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_17'], "F4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_18'], "G4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_19'], "A4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_20'], "B4")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_21'], "C5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_22'], "D5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_23'], "E5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_24'], "F5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_25'], "G5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_26'], "A5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_27'], "B5")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_28'], "C6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_29'], "D6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_30'], "E6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_31'], "F6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_32'], "G6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_33'], "A6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_34'], "B6")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_35'], "C7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_36'], "D7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_37'], "E7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_38'], "F7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_39'], "G7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_40'], "A7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_41'], "B7")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_42'], "C8")
        self.assertEqual(self.test_dict['MCORE_SOUND_PLAY_NOTE_NOTE_43'], "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)