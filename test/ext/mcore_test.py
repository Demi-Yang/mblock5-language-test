# coding:utf-8
# import requests
import json
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
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key] 
        self.assertEqual(test_data, expect_value, '\nkey: {0} \nvalue: {1} \nerror: 值不等于 {2}, '.format(key, test_data, expect_value))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0} \nvalue: {1} \n缺少参数：{2}'.format(key, test_data, p))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))

    # ext-i18n/mcore/No empty value
    def test_mcore_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/mcore/No new or missing items
    def test_mcore_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 198, '\next-i18n/mcore 模块下新增或删减了新的字段，测试用例需增减~')

    # mblock5-i18n/extensionName&codeyneuron equals mBot
    def test_ensionName(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_expect_value(key, "mBot")
        self.check_expect_value('mcore', "mBot")

    # ext-i18n/mcore/mcore_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_mcore_show_face_time(self):
        key = 'mcore_show_face_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]', '[TIME]'])

    # ext-i18n/mcore/mcore_show_face contains [ICON] [PORT] [FACE_PANEL] 
    def test_mcore_show_face(self):
        key = 'mcore_show_face'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]'])

    # ext-i18n/mcore/mcore_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y] 
    def test_mcore_show_face_position(self):
        key = 'mcore_show_face_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FACE_PANEL]', 'x: [X] y: [Y]'])

    # ext-i18n/mcore/mcore_show_text contains [ICON] [PORT] [TEXT] 
    def test_mcore_show_text(self):
        key = 'mcore_show_text'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[TEXT]'])

    # ext-i18n/mcore/mcore_show_text_position contains [ICON] [PORT] [TEXT] x: [X] y: [Y] 
    def test_mcore_show_text_position(self):
        key = 'mcore_show_text_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[TEXT]', 'x: [X] y: [Y]'])

    # ext-i18n/mcore/mcore_show_number contains [ICON] [PORT] [NUMBER] 
    def test_mcore_show_number(self):
        key = 'mcore_show_number'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER]'])

    # ext-i18n/mcore/mcore_show_time contains [ICON] [PORT] [NUMBER1]: [NUMBER2]
    def test_mcore_show_time(self):
        key = 'mcore_show_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER1]: [NUMBER2]'])

    # ext-i18n/mcore/mcore_show_face_off contains [ICON] [PORT] 
    def test_mcore_show_face_off(self):
        key = 'mcore_show_face_off'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_show_7segments_number contains [ICON] [PORT] [NUMBER] 
    def test_mcore_show_7segments_number(self):
        key = 'mcore_show_7segments_number'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[NUMBER]'])

    # ext-i18n/mcore/mcore_show_led_time contains [ICON] [LED_POSTION] [COLOR] [TIME]
    def test_mcore_show_led_time(self):
        key = 'mcore_show_led_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[LED_POSTION]', '[COLOR]', '[TIME]'])

    # ext-i18n/mcore/mcore_show_led contains [ICON] [LED_POSTION] [COLOR] 
    def test_mcore_show_led(self):
        key = 'mcore_show_led'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[LED_POSTION]', '[COLOR]'])

    # ext-i18n/mcore/mcore_show_led_rgb contains [ICON] [LED_POSTION] [R] [G][B]
    def test_mcore_show_led_rgb(self):
        key = 'mcore_show_led_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[LED_POSTION]', '[R]','[G]','[B]'])

    # ext-i18n/mcore/mcore_sound_play_note contains [ICON] [NOTE] [BEAT] 
    def test_mcore_sound_play_note(self):
        key = 'mcore_sound_play_note'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[NOTE]', '[BEAT]'])

    # ext-i18n/mcore/mcore_sound_play_hz contains [ICON] [HZ] [TIME] 
    def test_mcore_sound_play_hz(self):
        key = 'mcore_sound_play_hz'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[HZ]', '[TIME]'])

    # ext-i18n/mcore/mcore_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME] 
    def test_mcore_show_external_led_time(self):
        key = 'mcore_show_external_led_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]', '[TIME]'])

    # ext-i18n/mcore/mcore_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR] 
    def test_mcore_show_external_led(self):
        key = 'mcore_show_external_led'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[COLOR]'])

    # ext-i18n/mcore/mcore_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_mcore_show_external_led_rgb(self):
        key = 'mcore_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LED_POSTION]', '[R]','[G]','[B]'])

    # ext-i18n/mcore/mcore_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_mcore_show_all_ledstrip_color(self):
        key = 'mcore_show_all_ledstrip_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[COLOR_LIST]'])

    # ext-i18n/mcore/mcore_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_mcore_show_ledstrip_color(self):
        key = 'mcore_show_ledstrip_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[POS]','[COLOR_LIST]'])

    # ext-i18n/mcore/mcore_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
    def test_mcore_show_ledstrip_rbg(self):
        key = 'mcore_show_ledstrip_rbg'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[POS]','[R]','[G]','[B]'])

    # ext-i18n/mcore/mcore_forward_time contains [ICON] [POWER] % [TIME]
    def test_mcore_forward_time(self):
        key = 'mcore_forward_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/mcore/mcore_backward_time contains [ICON] [POWER] % [TIME]
    def test_mcore_backward_time(self):
        key = 'mcore_backward_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/mcore/mcore_turnleft_time contains [ICON] [POWER] % [TIME]
    def test_mcore_turnleft_time(self):
        key = 'mcore_turnleft_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/mcore/mcore_turnright_time contains [ICON] [POWER] % [TIME]
    def test_mcore_turnright_time(self):
        key = 'mcore_turnright_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[TIME]'])

    # ext-i18n/mcore/mcore_move contains [ICON] [POWER] % [MOVE_DIRECTION]
    def test_mcore_move(self):
        key = 'mcore_move'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER] %', '[MOVE_DIRECTION]'])

    # ext-i18n/mcore/mcore_move_wheel_speed contains [ICON] [POWER_LEFT] % [POWER_RIGHT] %
    def test_mcore_move_wheel_speed(self):
        key = 'mcore_move_wheel_speed'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[POWER_LEFT] %', '[POWER_RIGHT] %', '[MOVE_DIRECTION]'])

    # ext-i18n/mcore/mcore_move_stop contains [ICON] 
    def test_mcore_move_stop(self):
        key = 'mcore_move_stop'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_run_shutter contains [ICON] [PORT][SHUTTER_ACTION]
    def test_mcore_run_shutter(self):
        key = 'mcore_run_shutter'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SHUTTER_ACTION]'])

    # ext-i18n/mcore/mcore_run_motor contains [ICON] [PORT][ROTATE][POWER] %
    def test_mcore_run_motor(self):
        key = 'mcore_run_motor'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[ROTATE]', '[POWER] %'])

    # ext-i18n/mcore/mcore_run_servo contains [ICON] [PORT][SLOT][DEGREE]
    def test_mcore_run_servo(self):
        key = 'mcore_run_servo'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]', '[DEGREE]'])

    # ext-i18n/mcore/mcore_run_fan contains [ICON] [PORT][FAN_ROTATE]
    def test_mcore_run_fan(self):
        key = 'mcore_run_fan'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FAN_ROTATE]'])

    # ext-i18n/mcore/mcore_detect_external_light contains [ICON] [PORT]
    def test_mcore_detect_external_light(self):
        key = 'mcore_detect_external_light'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_external_ultrasonic contains [ICON] [PORT]
    def test_mcore_detect_external_ultrasonic(self):
        key = 'mcore_detect_external_ultrasonic'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_external_linefollower contains [ICON] [PORT]
    def test_mcore_detect_external_linefollower(self):
        key = 'mcore_detect_external_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_mcore_event_external_linefollower(self):
        key = 'mcore_event_external_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[LINEFOLLOW_STATE]', '[BLACK_WHITE]'])

    # ext-i18n/mcore/mcore_event_board_button_pressed contains [ICON] [OPTION]
    def test_mcore_event_board_button_pressed(self):
        key = 'mcore_event_board_button_pressed'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[OPTION]'])

    # ext-i18n/mcore/mcore_event_ir_remote contains [ICON] [REMOTE_KEY]
    def test_mcore_event_ir_remote(self):
        key = 'mcore_event_ir_remote'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[REMOTE_KEY]'])

    # ext-i18n/mcore/mcore_send_ir contains [ICON] [MESSAGE]
    def test_mcore_send_ir(self):
        key = 'mcore_send_ir'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[MESSAGE]'])

    # ext-i18n/mcore/mcore_detect_ir contains [ICON]
    def test_mcore_detect_ir(self):
        key = 'mcore_detect_ir'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_detect_timer contains [ICON]
    def test_mcore_detect_timer(self):
        key = 'mcore_detect_timer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_reset_timer contains [ICON]
    def test_mcore_reset_timer(self):
        key = 'mcore_reset_timer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_detect_external_loudness contains [ICON] [PORT]
    def test_mcore_detect_external_loudness(self):
        key = 'mcore_detect_external_loudness'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detec_temperature contains [ICON] [PORT] [SLOT]
    def test_mcore_detec_temperature(self):
        key = 'mcore_detec_temperature'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[SLOT]', '[PORT]'])

    # ext-i18n/mcore/mcore_detect_humiture contains [ICON] [PORT] [TEMP_HUMITURE]
    def test_mcore_detect_humiture(self):
        key = 'mcore_detect_humiture'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[TEMP_HUMITURE]', '[PORT]'])

    # ext-i18n/mcore/mcore_event_touch contains [ICON] [PORT]
    def test_mcore_event_touch(self):
        key = 'mcore_event_touch'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_compass contains [ICON] [PORT]
    def test_mcore_detect_compass(self):
        key = 'mcore_detect_compass'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_flame contains [ICON] [PORT]
    def test_mcore_detect_flame(self):
        key = 'mcore_detect_flame'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_gas contains [ICON] [PORT]
    def test_mcore_detect_gas(self):
        key = 'mcore_detect_gas'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_gyro_angle contains [ICON] [AXIS]
    def test_mcore_detect_gyro_angle(self):
        key = 'mcore_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[AXIS]'])

    # ext-i18n/mcore/mcore_event_pir_motion contains [ICON] [PORT]
    def test_mcore_event_pir_motion(self):
        key = 'mcore_event_pir_motion'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_event_button_press contains [ICON] [PORT][FOUR_KEY]
    def test_mcore_event_button_press(self):
        key = 'mcore_event_button_press'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[FOUR_KEY]'])

    # ext-i18n/mcore/mcore_event_limit_switch contains [ICON] [PORT][SLOT]
    def test_mcore_event_limit_switch(self):
        key = 'mcore_event_limit_switch'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[SLOT]'])

    # ext-i18n/mcore/mcore_detect_potentiometer contains [ICON] [PORT]
    def test_mcore_detect_potentiometer(self):
        key = 'mcore_detect_potentiometer'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_detect_joystick contains [ICON] [PORT][AXIS_X_Y]
    def test_mcore_detect_joystick(self):
        key = 'mcore_detect_joystick'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]', '[AXIS_X_Y]'])

    # ext-i18n/mcore/mcore_detect_infrared contains [ICON] [PORT]
    def test_ext_i18n_mcore_detect_infrared(self):
        key = 'mcore_detect_infrared'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[PORT]'])

    # ext-i18n/mcore/mcore_event_linefollower contains [ICON]
    def test_mcore_event_linefollower(self):
        key = 'mcore_event_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_event_obstacle contains [ICON]
    def test_mcore_event_obstacle(self):
        key = 'mcore_event_obstacle'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_detect_obstacle_distance contains [ICON]
    def test_mcore_detect_obstacle_distance(self):
        key = 'mcore_detect_obstacle_distance'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_detect_light contains [ICON]
    def test_mcore_detect_light(self):
        key = 'mcore_detect_light'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/mcore/mcore_when_board_button contains [IS_PRESS]
    def test_mcore_when_board_button(self):
        key = 'mcore_when_board_button'
        self.check_key_exists(key)
        self.check_params(key, ['[IS_PRESS]'])


    # ext-i18n/mcore/MCORE_EVENT_IR_REMOTE_REMOTE_KEY is right
    def test_MCORE_EVENT_IR_REMOTE_REMOTE_KEY(self):
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_0', "A")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_1', "B")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_2', "C")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_3', "D")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_4', "E")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_5', "F")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_11', "0")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_12', "1")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_13', "2")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_14', "3")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_15', "4")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_16', "5")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_17', "6")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_18', "7")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_19', "8")
        self.check_expect_value('MCORE_EVENT_IR_REMOTE_REMOTE_KEY_20', "9")

    # ext-i18n/mcore/MCORE_SOUND_PLAY_NOTE_NOTE is right
    def test_MCORE_SOUND_PLAY_NOTE_NOTE(self):
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_0', "C2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_1', "D2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_2', "E2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_3', "F2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_4', "G2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_5', "A2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_6', "B2")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_7', "C3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_8', "D3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_9', "E3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_10', "F3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_11', "G3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_12', "A3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_13', "B3")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_14', "C4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_15', "D4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_16', "E4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_17', "F4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_18', "G4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_19', "A4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_20', "B4")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_21', "C5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_22', "D5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_23', "E5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_24', "F5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_25', "G5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_26', "A5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_27', "B5")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_28', "C6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_29', "D6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_30', "E6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_31', "F6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_32', "G6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_33', "A6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_34', "B6")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_35', "C7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_36', "D7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_37', "E7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_38', "F7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_39', "G7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_40', "A7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_41', "B7")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_42', "C8")
        self.check_expect_value('MCORE_SOUND_PLAY_NOTE_NOTE_43', "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(McoreTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)