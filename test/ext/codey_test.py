# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  codey項目-翻译检查  =======================

class CodeyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/codey']

    # ext-i18n/codey/No empty value
    def test_ext_i18n_codey_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mblock5-i18n/extensionName equals Codey
    def test_mblock5_i18n_extensionName_equals_Codey(self):
        self.assertIn('extensionName', self.test_dict)
        test_data = self.test_dict['extensionName']
        self.assertEqual(test_data, "Codey")

    # ext-i18n/codey/meos_show_led_matrix_face_with_time contains [ICON] [PANEL] [TIME]
    def test_ext_i18n_meos_show_led_matrix_face_with_time(self):
        self.assertIn('meos_show_led_matrix_face_with_time', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_face_with_time']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_face contains [ICON] [PANEL] 
    def test_ext_i18n_meos_show_led_matrix_face(self):
        self.assertIn('meos_show_led_matrix_face', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_face']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_face_position contains [ICON] [PANEL] x: [AXIS-X]  y: [AXIS-Y]
    def test_ext_i18n_meos_show_led_matrix_face_position(self):
        self.assertIn('meos_show_led_matrix_face_position', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_face_position']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('x: [AXIS-X] y: [AXIS-Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_turn_off contains [ICON]
    def test_ext_i18n_meos_show_led_matrix_turn_off(self):
        self.assertIn('meos_show_led_matrix_turn_off', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_turn_off']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix contains [ICON] [STRING] 
    def test_ext_i18n_meos_show_led_matrix(self):
        self.assertIn('meos_show_led_matrix', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix']
        self.assertIn('[STRING]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_string contains [ICON] [STRING] 
    def test_ext_i18n_meos_show_led_matrix_string(self):
        self.assertIn('meos_show_led_matrix_string', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_string']
        self.assertIn('[STRING]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_string_position contains [ICON] [STRING]  x: [X]   y: [Y]
    def test_ext_i18n_meos_show_led_matrix_string_position(self):
        self.assertIn('meos_show_led_matrix_string_position', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_string_position']
        self.assertIn('[STRING]', test_data)
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_ext_i18n_meos_show_led_matrix_position(self):
        self.assertIn('meos_show_led_matrix_position', self.test_dict)
        test_data = self.test_dict['meos_show_led_matrix_position']
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_light_off_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_ext_i18n_meos_light_off_led_matrix_position(self):
        self.assertIn('meos_light_off_led_matrix_position', self.test_dict)
        test_data = self.test_dict['meos_light_off_led_matrix_position']
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_toggle_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_ext_i18n_meos_toggle_led_matrix_position(self):
        self.assertIn('meos_toggle_led_matrix_position', self.test_dict)
        test_data = self.test_dict['meos_toggle_led_matrix_position']
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_led_matrix_position_is_light contains [ICON]  x: [X]   y: [Y]
    def test_ext_i18n_meos_event_led_matrix_position_is_light(self):
        self.assertIn('meos_event_led_matrix_position_is_light', self.test_dict)
        test_data = self.test_dict['meos_event_led_matrix_position_is_light']
        self.assertIn('x: [X] y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_with_time contains [ICON]   [COLOR]   [TIME] 
    def test_ext_i18n_meos_show_led_with_time(self):
        self.assertIn('meos_show_led_with_time', self.test_dict)
        test_data = self.test_dict['meos_show_led_with_time']
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led contains [ICON]   [COLOR] 
    def test_ext_i18n_meos_show_led(self):
        self.assertIn('meos_show_led', self.test_dict)
        test_data = self.test_dict['meos_show_led']
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_led_rgb contains [ICON] [VALUE] [RGB] 
    def test_ext_i18n_meos_show_led_rgb(self):
        self.assertIn('meos_show_led_rgb', self.test_dict)
        test_data = self.test_dict['meos_show_led_rgb']
        self.assertIn('[RGB]', test_data)
        self.assertIn('[VALUE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_turn_off_led contains [ICON]
    def test_ext_i18n_meos_turn_off_led(self):
        self.assertIn('meos_turn_off_led', self.test_dict)
        test_data = self.test_dict['meos_turn_off_led']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_show_led_color contains [ICON] [COLORLIST]
    def test_ext_i18n_meos_rocky_show_led_color(self):
        self.assertIn('meos_rocky_show_led_color', self.test_dict)
        test_data = self.test_dict['meos_rocky_show_led_color']
        self.assertIn('[COLORLIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_turn_off_led_color contains [ICON]
    def test_ext_i18n_meos_rocky_turn_off_led_color(self):
        self.assertIn('meos_rocky_turn_off_led_color', self.test_dict)
        test_data = self.test_dict['meos_rocky_turn_off_led_color']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_play_sound contains [ICON] [SOUNDLIST]
    def test_ext_i18n_meos_show_play_sound(self):
        self.assertIn('meos_show_play_sound', self.test_dict)
        test_data = self.test_dict['meos_show_play_sound']
        self.assertIn('[SOUNDLIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_play_sound_wait contains [ICON] [SOUNDLIST]
    def test_ext_i18n_meos_show_play_sound_wait(self):
        self.assertIn('meos_show_play_sound_wait', self.test_dict)
        test_data = self.test_dict['meos_show_play_sound_wait']
        self.assertIn('[SOUNDLIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_stop_allsound contains [ICON]
    def test_ext_i18n_meos_show_stop_allsound(self):
        self.assertIn('meos_show_stop_allsound', self.test_dict)
        test_data = self.test_dict['meos_show_stop_allsound']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_play_note_with_string contains [ICON] [SOUNDNOTE] [SOUNDBEAT]
    def test_ext_i18n_meos_show_play_note_with_string(self):
        self.assertIn('meos_show_play_note_with_string', self.test_dict)
        test_data = self.test_dict['meos_show_play_note_with_string']
        self.assertIn('[SOUNDNOTE]', test_data)
        self.assertIn('[SOUNDBEAT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_pause_note contains [ICON] [TIME]
    def test_ext_i18n_meos_show_pause_note(self):
        self.assertIn('meos_show_pause_note', self.test_dict)
        test_data = self.test_dict['meos_show_pause_note']
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_play_hz contains [ICON] [HZ] [TIME]
    def test_ext_i18n_meos_show_play_hz(self):
        self.assertIn('meos_show_play_hz', self.test_dict)
        test_data = self.test_dict['meos_show_play_hz']
        self.assertIn('[HZ]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_change_volume contains [ICON] [VOLUME]
    def test_ext_i18n_meos_show_change_volume(self):
        self.assertIn('meos_show_change_volume', self.test_dict)
        test_data = self.test_dict['meos_show_change_volume']
        self.assertIn('[VOLUME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_set_volume contains [ICON] [VOLUME] %
    def test_ext_i18n_meos_show_set_volume(self):
        self.assertIn('meos_show_set_volume', self.test_dict)
        test_data = self.test_dict['meos_show_set_volume']
        self.assertIn('[VOLUME] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_sound_volume contains [ICON] 
    def test_ext_i18n_meos_detect_sound_volume(self):
        self.assertIn('meos_detect_sound_volume', self.test_dict)
        test_data = self.test_dict['meos_detect_sound_volume']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_forward_with_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_move_forward_with_time(self):
        self.assertIn('meos_move_forward_with_time', self.test_dict)
        test_data = self.test_dict['meos_move_forward_with_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_backward_with_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_move_backward_with_time(self):
        self.assertIn('meos_move_backward_with_time', self.test_dict)
        test_data = self.test_dict['meos_move_backward_with_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_left_with_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_move_left_with_time(self):
        self.assertIn('meos_move_left_with_time', self.test_dict)
        test_data = self.test_dict['meos_move_left_with_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_right_with_time contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_move_right_with_time(self):
        self.assertIn('meos_move_right_with_time', self.test_dict)
        test_data = self.test_dict['meos_move_right_with_time']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_keep_absolute_forward contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_rocky_keep_absolute_forward(self):
        self.assertIn('meos_rocky_keep_absolute_forward', self.test_dict)
        test_data = self.test_dict['meos_rocky_keep_absolute_forward']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_keep_absolute_backward contains [ICON] [POWER] % [TIME]
    def test_ext_i18n_meos_rocky_keep_absolute_backward(self):
        self.assertIn('meos_rocky_keep_absolute_backward', self.test_dict)
        test_data = self.test_dict['meos_rocky_keep_absolute_backward']
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_left_with_angle contains [ICON] [image_4] [ANGLE]
    def test_ext_i18n_meos_move_left_with_angle(self):
        self.assertIn('meos_move_left_with_angle', self.test_dict)
        test_data = self.test_dict['meos_move_left_with_angle']
        self.assertIn('[image_4]', test_data)
        self.assertIn('[ANGLE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[image_4]'), 0)
    
    # ext-i18n/codey/meos_move_right_with_angle contains [ICON] [image_5] [ANGLE]
    def test_ext_i18n_meos_move_right_with_angle(self):
        self.assertIn('meos_move_right_with_angle', self.test_dict)
        test_data = self.test_dict['meos_move_right_with_angle']
        self.assertIn('[image_5]', test_data)
        self.assertIn('[ANGLE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[image_5]'), 0)

    # ext-i18n/codey/meos_move contains [ICON] [DIRECTION] [[POWER] %]
    def test_ext_i18n_meos_move(self):
        self.assertIn('meos_move', self.test_dict)
        test_data = self.test_dict['meos_move']
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_with_motors contains [ICON] [LEFT_POWER] % [RIGHT_POWER] %
    def test_ext_i18n_meos_move_with_motors(self):
        self.assertIn('meos_move_with_motors', self.test_dict)
        test_data = self.test_dict['meos_move_with_motors']
        self.assertIn('[LEFT_POWER] %', test_data)
        self.assertIn('[RIGHT_POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_move_stop contains [ICON]
    def test_ext_i18n_meos_move_stop(self):
        self.assertIn('meos_move_stop', self.test_dict)
        test_data = self.test_dict['meos_move_stop']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_keep_absolute_run contains [ICON] [DIRECTION] [POWER] % [TIME]
    def test_ext_i18n_meos_rocky_keep_absolute_run(self):
        self.assertIn('meos_rocky_keep_absolute_run', self.test_dict)
        test_data = self.test_dict['meos_rocky_keep_absolute_run']
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0 euqals A
    def test_ext_i18n_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0(self):
        self.assertIn('MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0', self.test_dict)
        test_data = self.test_dict['MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0']
        self.assertEqual(test_data, 'A')

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1 euqals B
    def test_ext_i18n_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1(self):
        self.assertIn('MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1', self.test_dict)
        test_data = self.test_dict['MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1']
        self.assertEqual(test_data, 'B')

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2 euqals C
    def test_ext_i18n_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2(self):
        self.assertIn('MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2', self.test_dict)
        test_data = self.test_dict['MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2']
        self.assertEqual(test_data, 'C')

    # ext-i18n/codey/meos_event_button_pressed contains [ICON] [BUTTONS]
    def test_ext_i18n_meos_event_button_pressed(self):
        self.assertIn('meos_event_button_pressed', self.test_dict)
        test_data = self.test_dict['meos_event_button_pressed']
        self.assertIn('[BUTTONS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_connect_rocky contains [ICON]
    def test_ext_i18n_meos_event_connect_rocky(self):
        self.assertIn('meos_event_connect_rocky', self.test_dict)
        test_data = self.test_dict['meos_event_connect_rocky']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_potentiometer contains [ICON]
    def test_ext_i18n_meos_detect_potentiometer(self):
        self.assertIn('meos_detect_potentiometer', self.test_dict)
        test_data = self.test_dict['meos_detect_potentiometer']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_volume contains [ICON]
    def test_ext_i18n_meos_detect_volume(self):
        self.assertIn('meos_detect_volume', self.test_dict)
        test_data = self.test_dict['meos_detect_volume']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_lightness contains [ICON]
    def test_ext_i18n_meos_detect_lightness(self):
        self.assertIn('meos_detect_lightness', self.test_dict)
        test_data = self.test_dict['meos_detect_lightness']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_dump_energy contains [ICON]
    def test_ext_i18n_meos_dump_energy(self):
        self.assertIn('meos_dump_energy', self.test_dict)
        test_data = self.test_dict['meos_dump_energy']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_is_shaked contains [ICON]
    def test_ext_i18n_meos_event_is_shaked(self):
        self.assertIn('meos_event_is_shaked', self.test_dict)
        test_data = self.test_dict['meos_event_is_shaked']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_shaked_strength contains [ICON]
    def test_ext_i18n_meos_detect_shaked_strength(self):
        self.assertIn('meos_detect_shaked_strength', self.test_dict)
        test_data = self.test_dict['meos_detect_shaked_strength']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_is_tilt contains [ICON] [DIRECTION]
    def test_ext_i18n_meos_event_is_tilt(self):
        self.assertIn('meos_event_is_tilt', self.test_dict)
        test_data = self.test_dict['meos_event_is_tilt']
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_is_orientate_to contains [ICON] [ORIENTATE]
    def test_ext_i18n_meos_event_is_orientate_to(self):
        self.assertIn('meos_event_is_orientate_to', self.test_dict)
        test_data = self.test_dict['meos_event_is_orientate_to']
        self.assertIn('[ORIENTATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_gyro_roll_angle contains [ICON]
    def test_ext_i18n_meos_detect_gyro_roll_angle(self):
        self.assertIn('meos_detect_gyro_roll_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_gyro_roll_angle']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_gyro_pitch_angle contains [ICON]
    def test_ext_i18n_meos_detect_gyro_pitch_angle(self):
        self.assertIn('meos_detect_gyro_pitch_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_gyro_pitch_angle']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_rotatex_angle contains [ICON] x
    def test_ext_i18n_meos_detect_rotatex_angle(self):
        self.assertIn('meos_detect_rotatex_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_rotatex_angle']
        self.assertIn('x', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_rotatey_angle contains [ICON] y
    def test_ext_i18n_meos_detect_rotatey_angle(self):
        self.assertIn('meos_detect_rotatey_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_rotatey_angle']
        self.assertIn('y', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_rotatez_angle contains [ICON] z
    def test_ext_i18n_meos_detect_rotatez_angle(self):
        self.assertIn('meos_detect_rotatez_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_rotatez_angle']
        self.assertIn('z', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_0 contains x
    def test_ext_i18n_MEOS_RESET_ANGLE_AXIS_0(self):
        self.assertIn('MEOS_RESET_ANGLE_AXIS_0', self.test_dict)
        test_data = self.test_dict['MEOS_RESET_ANGLE_AXIS_0']
        self.assertIn('x', test_data)

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_1 contains y
    def test_ext_i18n_MEOS_RESET_ANGLE_AXIS_1(self):
        self.assertIn('MEOS_RESET_ANGLE_AXIS_1', self.test_dict)
        test_data = self.test_dict['MEOS_RESET_ANGLE_AXIS_1']
        self.assertIn('y', test_data)

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_2 contains z
    def test_ext_i18n_MEOS_RESET_ANGLE_AXIS_2(self):
        self.assertIn('MEOS_RESET_ANGLE_AXIS_2', self.test_dict)
        test_data = self.test_dict['MEOS_RESET_ANGLE_AXIS_2']
        self.assertIn('z', test_data)

    # ext-i18n/codey/meos_reset_angle contains [ICON] AXIS
    def test_ext_i18n_meos_reset_angle(self):
        self.assertIn('meos_reset_angle', self.test_dict)
        test_data = self.test_dict['meos_reset_angle']
        self.assertIn('AXIS', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_time contains [ICON] 
    def test_ext_i18n_meos_detect_time(self):
        self.assertIn('meos_detect_time', self.test_dict)
        test_data = self.test_dict['meos_detect_time']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_reset_time contains [ICON] 
    def test_ext_i18n_meos_show_reset_time(self):
        self.assertIn('meos_show_reset_time', self.test_dict)
        test_data = self.test_dict['meos_show_reset_time']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_event_obstacles_ahead contains [ICON] 
    def test_ext_i18n_meos_rocky_event_obstacles_ahead(self):
        self.assertIn('meos_rocky_event_obstacles_ahead', self.test_dict)
        test_data = self.test_dict['meos_rocky_event_obstacles_ahead']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_event_is_color contains [ICON] COLOR
    def test_ext_i18n_meos_event_is_color(self):
        self.assertIn('meos_event_is_color', self.test_dict)
        test_data = self.test_dict['meos_event_is_color']
        self.assertIn('COLOR', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_detect_rgb contains [ICON] RGB
    def test_ext_i18n_meos_rocky_detect_rgb(self):
        self.assertIn('meos_rocky_detect_rgb', self.test_dict)
        test_data = self.test_dict['meos_rocky_detect_rgb']
        self.assertIn('RGB', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_detect_lightness contains [ICON] 
    def test_ext_i18n_meos_rocky_detect_lightness(self):
        self.assertIn('meos_rocky_detect_lightness', self.test_dict)
        test_data = self.test_dict['meos_rocky_detect_lightness']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_detect_reflection contains [ICON] 
    def test_ext_i18n_meos_rocky_detect_reflection(self):
        self.assertIn('meos_rocky_detect_reflection', self.test_dict)
        test_data = self.test_dict['meos_rocky_detect_reflection']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_detect_ir_reflection contains [ICON] 
    def test_ext_i18n_meos_rocky_detect_ir_reflection(self):
        self.assertIn('meos_rocky_detect_ir_reflection', self.test_dict)
        test_data = self.test_dict['meos_rocky_detect_ir_reflection']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_rocky_detect_grey contains [ICON] 
    def test_ext_i18n_meos_rocky_detect_grey(self):
        self.assertIn('meos_rocky_detect_grey', self.test_dict)
        test_data = self.test_dict['meos_rocky_detect_grey']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_0 contains x
    def test_ext_i18n_MEOS_DETECT_ROTATE_ANGLE_AXIS_0(self):
        self.assertIn('MEOS_DETECT_ROTATE_ANGLE_AXIS_0', self.test_dict)
        test_data = self.test_dict['MEOS_DETECT_ROTATE_ANGLE_AXIS_0']
        self.assertIn('x', test_data)

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_1 contains y
    def test_ext_i18n_MEOS_DETECT_ROTATE_ANGLE_AXIS_1(self):
        self.assertIn('MEOS_DETECT_ROTATE_ANGLE_AXIS_1', self.test_dict)
        test_data = self.test_dict['MEOS_DETECT_ROTATE_ANGLE_AXIS_1']
        self.assertIn('y', test_data)

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_2 contains z
    def test_ext_i18n_MEOS_DETECT_ROTATE_ANGLE_AXIS_2(self):
        self.assertIn('MEOS_DETECT_ROTATE_ANGLE_AXIS_2', self.test_dict)
        test_data = self.test_dict['MEOS_DETECT_ROTATE_ANGLE_AXIS_2']
        self.assertIn('z', test_data)

    # ext-i18n/codey/meos_detect_rotate_angle contains [ICON] AXIS
    def test_ext_i18n_meos_detect_rotate_angle(self):
        self.assertIn('meos_detect_rotate_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_rotate_angle']
        self.assertIn('AXIS', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_detect_gyro_angle contains [ICON] AXIS
    def test_ext_i18n_meos_detect_gyro_angle(self):
        self.assertIn('meos_detect_gyro_angle', self.test_dict)
        test_data = self.test_dict['meos_detect_gyro_angle']
        self.assertIn('AXIS', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_comm_send_ir contains [ICON] STRING
    def test_ext_i18n_meos_comm_send_ir(self):
        self.assertIn('meos_comm_send_ir', self.test_dict)
        test_data = self.test_dict['meos_comm_send_ir']
        self.assertIn('STRING', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_comm_receive_ir contains [ICON] 
    def test_ext_i18n_meos_comm_receive_ir(self):
        self.assertIn('meos_comm_receive_ir', self.test_dict)
        test_data = self.test_dict['meos_comm_receive_ir']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_comm_learn_with_time contains [ICON] 
    def test_ext_i18n_meos_comm_learn_with_time(self):
        self.assertIn('meos_comm_learn_with_time', self.test_dict)
        test_data = self.test_dict['meos_comm_learn_with_time']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_comm_send_learn_result contains [ICON] 
    def test_ext_i18n_meos_comm_send_learn_result(self):
        self.assertIn('meos_comm_send_learn_result', self.test_dict)
        test_data = self.test_dict['meos_comm_send_learn_result']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_when_button_press contains [BUTTONS] 
    def test_ext_i18n_meos_when_button_press(self):
        self.assertIn('meos_when_button_press', self.test_dict)
        test_data = self.test_dict['meos_when_button_press']
        self.assertIn('[BUTTONS]', test_data)

    # ext-i18n/codey/meos_when_board_tilt contains [DIRECTION] 
    def test_ext_i18n_meos_when_board_tilt(self):
        self.assertIn('meos_when_board_tilt', self.test_dict)
        test_data = self.test_dict['meos_when_board_tilt']
        self.assertIn('[DIRECTION]', test_data)

    # ext-i18n/codey/meos_when_volume_over contains [MENU_LIST] > [SOUNDVOLUME] 
    def test_ext_i18n_meos_when_volume_over(self):
        self.assertIn('meos_when_volume_over', self.test_dict)
        test_data = self.test_dict['meos_when_volume_over']
        self.assertIn('[MENU_LIST] > [SOUNDVOLUME]', test_data)

    # ext-i18n/codey/meos_when_brightness_less contains < [BRIGHTNESS]
    def test_ext_i18n_meos_when_brightness_less(self):
        self.assertIn('meos_when_brightness_less', self.test_dict)
        test_data = self.test_dict['meos_when_brightness_less']
        self.assertIn('< [BRIGHTNESS]', test_data)

    # ext-i18n/codey/MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE is right
    def test_ext_i18n_MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE(self):
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_0'], "C2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_1'], "D2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_2'], "E2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_3'], "F2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_4'], "G2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_5'], "A2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_6'], "B2")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_7'], "C3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_8'], "D3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_9'], "E3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_10'], "F3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_11'], "G3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_12'], "A3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_13'], "B3")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_14'], "C4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_15'], "D4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_16'], "E4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_17'], "F4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_18'], "G4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_19'], "A4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_20'], "B4")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_21'], "C5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_22'], "D5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_23'], "E5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_24'], "F5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_25'], "G5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_26'], "A5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_27'], "B5")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_28'], "C6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_29'], "D6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_30'], "E6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_31'], "F6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_32'], "G6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_33'], "A6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_34'], "B6")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_35'], "C7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_36'], "D7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_37'], "E7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_38'], "F7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_39'], "G7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_40'], "A7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_41'], "B7")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_42'], "C8")
        self.assertEqual(self.test_dict['MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_43'], "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)