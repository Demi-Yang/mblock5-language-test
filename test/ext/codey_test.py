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
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0}, value:{1}, error: 值不等于{2}, '.format(key, test_data, expect_value))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0}, value: {1}, 缺少参数：{2}'.format(key, test_data, p))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, value: {1}, 缺少参数：[ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, value: {1}, error:参数[ICON]必须在首位'.format(key, test_data))

    # ext-i18n/codey/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/codey/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 225, 'codey 模块下新增或删减了新的字段，测试用例需增减~')

    # mblock5-i18n/extensionName equals Codey
    def test_extensionName(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_expect_value(key, "Codey")

    # ext-i18n/codey/meos_show_led_matrix_face_with_time contains [ICON] [PANEL] [TIME]
    def test_meos_show_led_matrix_face_with_time(self):
        key = 'meos_show_led_matrix_face_with_time'
        self.check_key_exists(key)
        self.check_icon(key);
        self.check_params(key, ['[PANEL]', '[TIME]'])

    # ext-i18n/codey/meos_show_led_matrix_face contains [ICON] [PANEL] 
    def test_meos_show_led_matrix_face(self):
        key = 'meos_show_led_matrix_face'
        self.check_key_exists(key)
        self.check_icon(key);
        self.check_params(key, ['[PANEL]'])

    # ext-i18n/codey/meos_show_led_matrix_face_position contains [ICON] [PANEL] x: [AXIS-X]  y: [AXIS-Y]
    def test_meos_show_led_matrix_face_position(self):
        key = 'meos_show_led_matrix_face_position'
        self.check_key_exists(key)
        self.check_icon(key);
        self.check_params(key, ['[PANEL]', 'x: [AXIS-X] y: [AXIS-Y]'])

    # ext-i18n/codey/meos_show_led_matrix_turn_off contains [ICON]
    def test_meos_show_led_matrix_turn_off(self):
        key = 'meos_show_led_matrix_turn_off'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_show_led_matrix contains [ICON] [STRING] 
    def test_meos_show_led_matrix(self):
        key = 'meos_show_led_matrix'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['STRING'])

    # ext-i18n/codey/meos_show_led_matrix_string contains [ICON] [STRING] 
    def test_meos_show_led_matrix_string(self):
        key = 'meos_show_led_matrix_string'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['STRING'])

    # ext-i18n/codey/meos_show_led_matrix_string_position contains [ICON] [STRING]  x: [X]   y: [Y]
    def test_meos_show_led_matrix_string_position(self):
        key = 'meos_show_led_matrix_string_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x: [X] y: [Y]', 'STRING'])

    # ext-i18n/codey/meos_show_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_meos_show_led_matrix_position(self):
        key = 'meos_show_led_matrix_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x: [X] y: [Y]'])

    # ext-i18n/codey/meos_light_off_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_meos_light_off_led_matrix_position(self):
        key = 'meos_light_off_led_matrix_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x: [X] y: [Y]'])

    # ext-i18n/codey/meos_toggle_led_matrix_position contains [ICON]  x: [X]   y: [Y]
    def test_meos_toggle_led_matrix_position(self):
        key = 'meos_toggle_led_matrix_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x: [X] y: [Y]'])


    # ext-i18n/codey/meos_event_led_matrix_position_is_light contains [ICON]  x: [X]   y: [Y]
    def test_meos_event_led_matrix_position_is_light(self):
        key = 'meos_event_led_matrix_position_is_light'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x: [X] y: [Y]'])

    # ext-i18n/codey/meos_show_led_with_time contains [ICON]   [COLOR]   [TIME] 
    def test_meos_show_led_with_time(self):
        key = 'meos_show_led_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[COLOR]', '[TIME]'])

    # ext-i18n/codey/meos_show_led contains [ICON]   [COLOR] 
    def test_meos_show_led(self):
        key = 'meos_show_led'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[COLOR]'])

    # ext-i18n/codey/meos_show_led_rgb contains [ICON] [VALUE] [RGB] 
    def test_meos_show_led_rgb(self):
        key = 'meos_show_led_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[RGB]', '[VALUE]'])


    # ext-i18n/codey/meos_turn_off_led contains [ICON]
    def test_meos_turn_off_led(self):
        key="meos_turn_off_led"
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_show_led_color contains [ICON] [COLORLIST]
    def test_meos_rocky_show_led_color(self):
        key = 'meos_rocky_show_led_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[COLORLIST]'])

    # ext-i18n/codey/meos_rocky_turn_off_led_color contains [ICON]
    def test_meos_rocky_turn_off_led_color(self):
        self.assertIn('meos_rocky_turn_off_led_color', self.test_dict)
        test_data = self.test_dict['meos_rocky_turn_off_led_color']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey/meos_show_play_sound contains [ICON] [SOUNDLIST]
    def test_meos_show_play_sound(self):
        key = 'meos_show_play_sound'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[SOUNDLIST]'])

    # ext-i18n/codey/meos_show_play_sound_wait contains [ICON] [SOUNDLIST]
    def test_meos_show_play_sound_wait(self):
        key = 'meos_show_play_sound_wait'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[SOUNDLIST]'])

    # ext-i18n/codey/meos_show_stop_allsound contains [ICON]
    def test_meos_show_stop_allsound(self):
        key = 'meos_show_stop_allsound'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_show_play_note_with_string contains [ICON] [SOUNDNOTE] [SOUNDBEAT]
    def test_meos_show_play_note_with_string(self):
        key = 'meos_show_play_note_with_string'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[SOUNDNOTE]', '[SOUNDBEAT]'])

    # ext-i18n/codey/meos_show_pause_note contains [ICON] [TIME]
    def test_meos_show_pause_note(self):
        key = 'meos_show_pause_note'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[TIME]'])

    # ext-i18n/codey/meos_show_play_hz contains [ICON] [HZ] [TIME]
    def test_meos_show_play_hz(self):
        key = 'meos_show_play_hz'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[HZ]', '[TIME]'])

    # ext-i18n/codey/meos_show_change_volume contains [ICON] [VOLUME]
    def test_meos_show_change_volume(self):
        key = 'meos_show_change_volume'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[VOLUME]'])

    # ext-i18n/codey/meos_show_set_volume contains [ICON] [VOLUME] %
    def test_meos_show_set_volume(self):
        key = 'meos_show_set_volume'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[VOLUME] %'])

    # ext-i18n/codey/meos_detect_sound_volume contains [ICON] 
    def test_meos_detect_sound_volume(self):
        key = 'meos_detect_sound_volume'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_move_forward_with_time contains [ICON] [POWER] % [TIME]
    def test_meos_move_forward_with_time(self):
        key = 'meos_move_forward_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_move_backward_with_time contains [ICON] [POWER] % [TIME]
    def test_meos_move_backward_with_time(self):
        key = 'meos_move_backward_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_move_left_with_time contains [ICON] [POWER] % [TIME]
    def test_meos_move_left_with_time(self):
        key = 'meos_move_left_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_move_right_with_time contains [ICON] [POWER] % [TIME]
    def test_meos_move_right_with_time(self):
        key = 'meos_move_right_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_rocky_keep_absolute_forward contains [ICON] [POWER] % [TIME]
    def test_meos_rocky_keep_absolute_forward(self):
        key = 'meos_rocky_keep_absolute_forward'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_rocky_keep_absolute_backward contains [ICON] [POWER] % [TIME]
    def test_meos_rocky_keep_absolute_backward(self):
        key = 'meos_rocky_keep_absolute_backward'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/codey/meos_move_left_with_angle contains [ICON] [image_4] [ANGLE]
    def test_meos_move_left_with_angle(self):
        key = 'meos_move_left_with_angle'
        test_data = self.test_dict[key]
        self.check_key_exists(key)
        self.check_params(key, ['[image_4]', '[ANGLE]', '[ICON]'])
        self.assertEqual(test_data.index('[image_4]'), 0, 'key: {0}, 参数[image_4]位置不正确，应该在首位')
    
    # ext-i18n/codey/meos_move_right_with_angle contains [ICON] [image_5] [ANGLE]
    def test_meos_move_right_with_angle(self):
        key = 'meos_move_right_with_angle'
        test_data = self.test_dict[key]
        self.check_key_exists(key)
        self.check_params(key, ['[image_5]', '[ANGLE]', '[ICON]'])
        self.assertEqual(test_data.index('[image_5]'), 0, 'key: {0}, 参数[image_5]位置不正确，应该在首位')

    # ext-i18n/codey/meos_move contains [ICON] [DIRECTION] [[POWER] %]
    def test_meos_move(self):
        key = 'meos_move'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[DIRECTION]', '[POWER]'])

    # ext-i18n/codey/meos_move_with_motors contains [ICON] [LEFT_POWER] % [RIGHT_POWER] %
    def test_meos_move_with_motors(self):
        key = 'meos_move_with_motors'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[LEFT_POWER] %', '[RIGHT_POWER] %'])

    # ext-i18n/codey/meos_move_stop contains [ICON]
    def test_meos_move_stop(self):
        key = 'meos_move_stop'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_keep_absolute_run contains [ICON] [DIRECTION] [POWER] % [TIME]
    def test_meos_rocky_keep_absolute_run(self):
        key = 'meos_rocky_keep_absolute_run'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[DIRECTION]', '[POWER] %', '[TIME]'])

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0 euqals A
    def test_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0(self):
        key = 'MEOS_EVENT_BUTTON_PRESSED_BUTTONS_0'
        self.check_key_exists(key)
        self.check_params(key, ['A'])

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1 euqals B
    def test_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1(self):
        key = 'MEOS_EVENT_BUTTON_PRESSED_BUTTONS_1'
        self.check_key_exists(key)
        self.check_params(key, ['B'])

    # ext-i18n/codey/MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2 euqals C
    def test_MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2(self):
        key = 'MEOS_EVENT_BUTTON_PRESSED_BUTTONS_2'
        self.check_key_exists(key)
        self.check_params(key, ['C'])


    # ext-i18n/codey/meos_event_button_pressed contains [ICON] [BUTTONS]
    def test_meos_event_button_pressed(self):
        key = 'meos_event_button_pressed'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['BUTTONS'])

    # ext-i18n/codey/meos_event_connect_rocky contains [ICON]
    def test_meos_event_connect_rocky(self):
        key = 'meos_event_connect_rocky'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_potentiometer contains [ICON]
    def test_meos_detect_potentiometer(self):
        key = 'meos_detect_potentiometer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_volume contains [ICON]
    def test_meos_detect_volume(self):
        key = 'meos_detect_volume'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_lightness contains [ICON]
    def test_meos_detect_lightness(self):
        key = 'meos_detect_lightness'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_dump_energy contains [ICON]
    def test_meos_dump_energy(self):
        key = 'meos_dump_energy'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_event_is_shaked contains [ICON]
    def test_meos_event_is_shaked(self):
        key = 'meos_event_is_shaked'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_shaked_strength contains [ICON]
    def test_meos_detect_shaked_strength(self):
        key = 'meos_detect_shaked_strength'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_event_is_tilt contains [ICON] [DIRECTION]
    def test_meos_event_is_tilt(self):
        key = 'meos_event_is_tilt'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[DIRECTION]'])

    # ext-i18n/codey/meos_event_is_orientate_to contains [ICON] [ORIENTATE]
    def test_meos_event_is_orientate_to(self):
        key = 'meos_event_is_orientate_to'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ORIENTATE]'])

    # ext-i18n/codey/meos_detect_gyro_roll_angle contains [ICON]
    def test_meos_detect_gyro_roll_angle(self):
        key = 'meos_detect_gyro_roll_angle'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_gyro_pitch_angle contains [ICON]
    def test_meos_detect_gyro_pitch_angle(self):
        key = 'meos_detect_gyro_pitch_angle'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_detect_rotatex_angle contains [ICON] x
    def test_meos_detect_rotatex_angle(self):
        key = 'meos_detect_rotatex_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x'])

    # ext-i18n/codey/meos_detect_rotatey_angle contains [ICON] y
    def test_meos_detect_rotatey_angle(self):
        key = 'meos_detect_rotatey_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['y'])

    # ext-i18n/codey/meos_detect_rotatez_angle contains [ICON] z
    def test_meos_detect_rotatez_angle(self):
        key = 'meos_detect_rotatez_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['z'])

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_0 contains x
    def test_MEOS_RESET_ANGLE_AXIS_0(self):
        key = 'MEOS_RESET_ANGLE_AXIS_0'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x'])

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_1 contains y
    def test_MEOS_RESET_ANGLE_AXIS_1(self):
        key = 'MEOS_RESET_ANGLE_AXIS_1'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['y'])

    # ext-i18n/codey/MEOS_RESET_ANGLE_AXIS_2 contains z
    def test_MEOS_RESET_ANGLE_AXIS_2(self):
        key = 'MEOS_RESET_ANGLE_AXIS_2'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['z'])

    # ext-i18n/codey/meos_reset_angle contains [ICON] AXIS
    def test_meos_reset_angle(self):
        key = 'meos_reset_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['AXIS'])

    # ext-i18n/codey/meos_detect_time contains [ICON] 
    def test_meos_detect_time(self):
        key = 'meos_detect_time'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_show_reset_time contains [ICON] 
    def test_meos_show_reset_time(self):
        key = 'meos_show_reset_time'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_event_obstacles_ahead contains [ICON] 
    def test_meos_rocky_event_obstacles_ahead(self):
        key = 'meos_rocky_event_obstacles_ahead'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_event_is_color contains [ICON] COLOR
    def test_meos_event_is_color(self):
        key = 'meos_event_is_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['COLOR'])


    # ext-i18n/codey/meos_rocky_detect_rgb contains [ICON] RGB
    def tesT_meos_rocky_detect_rgb(self):
        key = 'meos_rocky_detect_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['RGB'])

    # ext-i18n/codey/meos_rocky_detect_lightness contains [ICON] 
    def test_meos_rocky_detect_lightness(self):
        key = 'meos_rocky_detect_lightness'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_detect_reflection contains [ICON] 
    def test_meos_rocky_detect_reflection(self):
        key = 'meos_rocky_detect_reflection'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_detect_ir_reflection contains [ICON] 
    def test_meos_rocky_detect_ir_reflection(self):
        key = 'meos_rocky_detect_ir_reflection'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_rocky_detect_grey contains [ICON] 
    def test_meos_rocky_detect_grey(self):
        key = 'meos_rocky_detect_grey'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_0 contains x
    def test_MEOS_DETECT_ROTATE_ANGLE_AXIS_0(self):
        key = 'MEOS_DETECT_ROTATE_ANGLE_AXIS_0'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['x'])

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_1 contains y
    def test_MEOS_DETECT_ROTATE_ANGLE_AXIS_1(self):
        key = 'MEOS_DETECT_ROTATE_ANGLE_AXIS_1'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['y'])

    # ext-i18n/codey/MEOS_DETECT_ROTATE_ANGLE_AXIS_2 contains z
    def test_MEOS_DETECT_ROTATE_ANGLE_AXIS_2(self):
        key = 'MEOS_DETECT_ROTATE_ANGLE_AXIS_2'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['z'])

    # ext-i18n/codey/meos_detect_rotate_angle contains [ICON] AXIS
    def test_meos_detect_rotate_angle(self):
        key = 'meos_detect_rotate_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['AXIS'])

    # ext-i18n/codey/meos_detect_gyro_angle contains [ICON] AXIS
    def test_meos_detect_gyro_angle(self):
        key = 'meos_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['AXIS'])

    # ext-i18n/codey/meos_comm_send_ir contains [ICON] STRING
    def test_meos_comm_send_ir(self):
        key = 'meos_comm_send_ir'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['STRING'])

    # ext-i18n/codey/meos_comm_receive_ir contains [ICON] 
    def test_meos_comm_receive_ir(self):
        key = 'meos_comm_receive_ir'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_comm_learn_with_time contains [ICON] 
    def test_meos_comm_learn_with_time(self):
        key = 'meos_comm_learn_with_time'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_comm_send_learn_result contains [ICON] 
    def test_meos_comm_send_learn_result(self):
        key = 'meos_comm_send_learn_result'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/codey/meos_when_button_press contains [BUTTONS] 
    def test_meos_when_button_press(self):
        key = 'meos_when_button_press'
        self.check_key_exists(key)
        self.check_params(key, ['[BUTTONS]'])

    # ext-i18n/codey/meos_when_board_tilt contains [DIRECTION] 
    def test_meos_when_board_tilt(self):
        key = 'meos_when_board_tilt'
        self.check_key_exists(key)
        self.check_params(key, ['[DIRECTION]'])

    # ext-i18n/codey/meos_when_volume_over contains [MENU_LIST] > [SOUNDVOLUME] 
    def test_meos_when_volume_over(self):
        key = 'meos_when_volume_over'
        self.check_key_exists(key)
        self.check_params(key, ['[MENU_LIST] > [SOUNDVOLUME]'])


    # ext-i18n/codey/meos_when_brightness_less contains < [BRIGHTNESS]
    def test_meos_when_brightness_less(self):
        key = 'meos_when_brightness_less'
        self.check_key_exists(key)
        self.check_params(key, ['< [BRIGHTNESS]'])

    # ext-i18n/codey/MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE is right
    def test_MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE(self):
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_0', "C2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_1', "D2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_2', "E2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_3', "F2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_4', "G2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_5', "A2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_6', "B2")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_7', "C3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_8', "D3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_9', "E3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_10', "F3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_11', "G3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_12', "A3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_13', "B3")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_14', "C4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_15', "D4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_16', "E4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_17', "F4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_18', "G4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_19', "A4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_20', "B4")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_21', "C5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_22', "D5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_23', "E5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_24', "F5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_25', "G5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_26', "A5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_27', "B5")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_28', "C6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_29', "D6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_30', "E6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_31', "F6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_32', "G6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_33', "A6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_34', "B6")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_35', "C7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_36', "D7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_37', "E7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_38', "F7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_39', "G7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_40', "A7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_41', "B7")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_42', "C8")
        self.check_expect_value('MEOS_SHOW_PLAY_NOTE_WITH_STRING_SOUNDNOTE_43', "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)