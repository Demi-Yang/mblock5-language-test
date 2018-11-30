# coding:utf-8
# import requests
import json
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

    def check_key_exists(self, key, ):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0} \nvalue: {1} \n error: 值不等于 {2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey: {0} \nvalue: {1} \n缺少参数：{2}'.format(key, test_data, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))




    # ext-i18n/auriga/No empty value
    def test_auriga_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/auriga/No new or missing items
    def test_auriga_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 208, "\nauriga 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/auriga/extensionName equals "mBot Ranger"
    def test_auriga_extensionName_equals_Arduino_Uno(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_expect_value(key,"mBot Ranger")

    # ext-i18n/auriga/auriga_show_all_led_time contains [ICON] [COLOR] [TIME]
    def test_auriga_show_all_led_time(self):
        key = 'auriga_show_all_led_time'
        self.check_key_exists(key)
        self.check_param(key, '[COLOR]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_all_led contains [ICON] [COLOR]
    def test_auriga_show_all_led(self):
        key = 'auriga_show_all_led'
        self.check_key_exists(key)
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_all_led_rgb contains [ICON] [R] [G] [B]
    def test_auriga_show_all_led_rgb(self):
        key = 'auriga_show_all_led_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_led_time contains [ICON] [LED_POSTION] [COLOR] [TIME]
    def test_auriga_show_led_time(self):
        key = 'auriga_show_led_time'
        self.check_key_exists(key)
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[TIME]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_led contains [ICON] [LED_POSTION] [COLOR]
    def test_auriga_show_led(self):
        key = 'auriga_show_led'
        self.check_key_exists(key)
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_led_rgb contains [ICON] [LED_POSTION] [R] [B] [G]
    def test_auriga_show_led_rgb(self):
        key = 'auriga_show_led_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[B]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_sound_play_note contains [ICON] [NOTE] [BEAT]
    def test_auriga_sound_play_note(self):
        key = 'auriga_sound_play_note'
        self.check_key_exists(key)
        self.check_param(key, '[NOTE]')
        self.check_param(key, '[BEAT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_sound_play_hz contains [ICON] [HZ] [TIME]
    def test_auriga_sound_play_hz(self):
        key = 'auriga_sound_play_hz'
        self.check_key_exists(key)
        self.check_param(key, '[TIME]')
        self.check_param(key, '[HZ]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_face_time contains [ICON] [PORT] [FACE_PANEL] [TIME]
    def test_auriga_show_face_time(self):
        key = 'auriga_show_face_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_face contains [ICON] [PORT] [FACE_PANEL]
    def test_auriga_show_face(self):
        key = 'auriga_show_face'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_face_position contains [ICON] [PORT] [FACE_PANEL] x: [X] y: [Y]
    def test_auriga_show_face_position(self):
        key = 'auriga_show_face_position'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FACE_PANEL]')
        self.check_param(key, 'x: [X] y: [Y]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_text contains [ICON] [PORT] [TEXT]
    def test_auriga_show_text(self):
        key = 'auriga_show_text'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEXT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_text_position contains [ICON]  [PORT] [TEXT] x: [X] y: [Y]
    def test_auriga_show_text_position(self):
        key = 'auriga_show_text_position'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEXT]')
        self.check_param(key, 'x: [X] y: [Y]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_number contains [ICON] [PORT] [NUMBER]
    def test_auriga_show_number(self):
        key = 'auriga_show_number'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_time contains [ICON] [PORT] [NUMBER1] [NUMBER2]
    def test_auriga_show_time(self):
        key = 'auriga_show_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER1]')
        self.check_param(key, '[NUMBER2]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_face_off contains [ICON] [PORT]
    def test_auriga_show_face_off(self):
        key = 'auriga_show_face_off'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_external_led_time contains [ICON] [PORT] [LED_POSTION] [COLOR] [TIME]
    def test_auriga_show_external_led_time(self):
        key = 'auriga_show_external_led_time'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_external_led contains [ICON] [PORT] [LED_POSTION] [COLOR]
    def test_auriga_show_external_led(self):
        key = 'auriga_show_external_led'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_external_led_rgb contains [ICON] [PORT] [LED_POSTION] [R] [G] [B]
    def test_auriga_show_external_led_rgb(self):
        key = 'auriga_show_external_led_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LED_POSTION]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_all_ledstrip_color contains [ICON] [PORT] [SLOT] [COLOR_LIST]
    def test_auriga_show_all_ledstrip_color(self):
        key = 'auriga_show_all_ledstrip_color'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[COLOR_LIST]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_ledstrip_color contains [ICON] [PORT] [SLOT] [POS] [COLOR_LIST]
    def test_auriga_show_ledstrip_color(self):
        key = 'auriga_show_ledstrip_color'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[POS]')
        self.check_param(key, '[COLOR_LIST]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_show_ledstrip_rbg contains [ICON] [PORT] [SLOT] [POS] [R][G][B]
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

    # ext-i18n/auriga/auriga_show_7segments_number contains [ICON] [PORT] [NUMBER]
    def test_auriga_show_7segments_number(self):
        key = 'auriga_show_7segments_number'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[NUMBER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_forward_time contains [ICON] [POWER] [TIME]
    def test_auriga_forward_time(self):
        key = 'auriga_forward_time'
        self.check_key_exists(key)
        self.check_param(key, '[POWER]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_backward_time contains [ICON]  [POWER] [TIME]
    def test_auriga_backward_time(self):
        key = 'auriga_backward_time'
        self.check_key_exists(key)
        self.check_param(key, '[POWER]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_turnleft_time contains [ICON]  [POWER] [TIME]
    def test_auriga_turnleft_time(self):
        key = 'auriga_turnleft_time'
        self.check_key_exists(key)
        self.check_param(key, '[POWER]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_turnright_time contains [ICON]  [POWER] [TIME]
    def test_auriga_turnright_time(self):
        key = 'auriga_turnright_time'
        self.check_key_exists(key)
        self.check_param(key, '[POWER]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_sauriga_movehow_ledstrip_rbg contains [ICON] [MOVE_DIRECTION] [POWER] 
    def test_auriga_move(self):
        key = 'auriga_move'
        self.check_key_exists(key)
        self.check_param(key, '[MOVE_DIRECTION]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_move_wheel_speed contains [ICON] [POWER_LEFT] [POWER_RIGHT]
    def test_auriga_move_wheel_speed(self):
        key = 'auriga_move_wheel_speed'
        self.check_key_exists(key)
        self.check_param(key, '[POWER_LEFT]')
        self.check_param(key, '[POWER_RIGHT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_move_stop contains [ICON]
    def test_auriga_move_stop(self):
        key = 'auriga_move_stop'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_board_encoder_motor contains [ICON] [ROTATE] [POWER] [PORT]%
    def test_auriga_run_board_encoder_motor(self):
        key = 'auriga_run_board_encoder_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER]%')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_board_encoder_motor_speed contains [ICON] [PORT] [ROTATE] [POWER]
    def test_auriga_run_board_encoder_motor_speed(self):
        key = 'auriga_run_board_encoder_motor_speed'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_board_encoder_motor_pos contains [ICON] [PORT] [ROTATE] [DEGREE] [POWER][G][B]
    def test_auriga_run_board_encoder_motor_pos(self):
        key = 'auriga_run_board_encoder_motor_pos'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_encoder_motor contains [ICON] [PORT] [SLOT] [ROTATE] [DEGREE][POWER]
    def test_auriga_run_encoder_motor(self):
        key = 'auriga_run_encoder_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_motor contains [ICON] [PORT] [ROTATE] [POWER] %
    def test_auriga_run_motor(self):
        key = 'auriga_run_motor'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER] %')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_stepper_motor_pos contains [ICON] [PORT] [ROTATE] [DISTANCE] [POWER]
    def test_auriga_run_stepper_motor_pos(self):
        key = 'auriga_run_stepper_motor_pos'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DISTANCE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_servo contains [ICON] [PORT] [SLOT] [DEGREE]
    def test_auriga_run_servo(self):
        key = 'auriga_run_servo'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[DEGREE]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_fan contains [ICON] [PORT] [FAN_ROTATE]
    def test_auriga_run_fan(self):
        key = 'auriga_run_fan'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FAN_ROTATE]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_shutter contains [ICON] [PORT] [SHUTTER_ACTION]
    def test_auriga_run_shutter(self):
        key = 'auriga_run_shutter'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SHUTTER_ACTION]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_smart_servo_to_zero contains [ICON] [INDEX]
    def test_auriga_run_smart_servo_to_zero(self):
        key = 'auriga_run_smart_servo_to_zero'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_smart_servo contains [ICON] [INDEX] [ROTATE] [POWER]
    def test_auriga_run_smart_servo(self):
        key = 'auriga_run_smart_servo'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_smart_servo_absolute contains [ICON] [INDEX] [ROTATE] [POSITION] [POWER]
    def test_auriga_run_smart_servo_absolute(self):
        key = 'auriga_run_smart_servo_absolute'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[POSITION]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_run_smart_servo_to_relative contains [ICON] [INDEX] [ROTATE] [DEGREE] [POWER]
    def test_auriga_run_smart_servo_to_relative(self):
        key = 'auriga_run_smart_servo_to_relative'
        self.check_key_exists(key)
        self.check_param(key, '[INDEX]')
        self.check_param(key, '[ROTATE]')
        self.check_param(key, '[DEGREE]')
        self.check_param(key, '[POWER]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_light contains [ICON] [PORT]
    def test_auriga_detect_light(self):
        key = 'auriga_detect_light'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_temperature contains [ICON] 
    def test_auriga_detect_temperature(self):
        key = 'auriga_detect_temperature'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_loudness contains [ICON] [PORT]
    def test_auriga_detect_loudness(self):
        key = 'auriga_detect_loudness'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_board_gyro_angle contains [ICON] [AXIS]
    def test_auriga_detect_board_gyro_angle(self):
        key = 'auriga_detect_board_gyro_angle'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_external_ultrasonic contains [ICON] [PORT]
    def test_auriga_detect_external_ultrasonic(self):
        key = 'auriga_detect_external_ultrasonic'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_external_linefollower contains [ICON] [PORT]
    def test_auriga_detect_external_linefollower(self):
        key = 'auriga_detect_external_linefollower'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_external_linefollower contains [ICON] [PORT] [LINEFOLLOW_STATE] [BLACK_WHITE]
    def test_auriga_event_external_linefollower(self):
        key = 'auriga_event_external_linefollower'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[LINEFOLLOW_STATE]')
        self.check_param(key, '[BLACK_WHITE]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_timer contains [ICON]
    def test_auriga_detect_timer(self):
        key = 'auriga_detect_timer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_reset_timer contains [ICON]
    def test_auriga_reset_timer(self):
        key = 'auriga_reset_timer'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_external_light contains [ICON] [PORT]
    def test_auriga_detect_external_light(self):
        key = 'auriga_detect_external_light'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_external_loudness contains [ICON] [PORT]
    def test_auriga_detect_external_loudness(self):
        key = 'auriga_detect_external_loudness'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detec_temperature contains [ICON] [SLOT] [PORT] 
    def test_auriga_detec_temperature(self):
        key = 'auriga_detec_temperature'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_humiture contains [ICON] [TEMP_HUMITURE] [PORT]
    def test_auriga_detect_humiture(self):
        key = 'auriga_detect_humiture'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[TEMP_HUMITURE]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_touch contains [ICON] [PORT]
    def test_auriga_event_touch(self):
        key = 'auriga_event_touch'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_compass contains [ICON] [PORT]
    def test_auriga_detect_compass(self):
        key = 'auriga_detect_compass'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_flame contains [ICON] [PORT]
    def test_auriga_detect_flame(self):
        key = 'auriga_detect_flame'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_gas contains [ICON] [PORT]
    def test_auriga_detect_gas(self):
        key = 'auriga_detect_gas'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_gyro_angle contains [ICON] [AXIS]
    def test_auriga_detect_gyro_angle(self):
        key = 'auriga_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_pir_motion contains [ICON] [PORT]
    def test_auriga_event_pir_motion(self):
        key = 'auriga_event_pir_motion'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_button_press contains [ICON] [FOUR_KEY] [PORT]
    def test_auriga_event_button_press(self):
        key = 'auriga_event_button_press'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[FOUR_KEY]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_limit_switch contains [ICON] [PORT] [SLOT]
    def test_auriga_event_limit_switch(self):
        key = 'auriga_event_limit_switch'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_potentiometer contains [ICON] [PORT]
    def test_auriga_detect_potentiometer(self):
        key = 'auriga_detect_potentiometer'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_joystick contains [ICON] [PORT] [AXIS_X_Y]
    def test_auriga_detect_joystick(self):
        key = 'auriga_detect_joystick'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_param(key, '[AXIS_X_Y]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_infrared contains [ICON] [PORT]
    def test_auriga_detect_infrared(self):
        key = 'auriga_detect_infrared'
        self.check_key_exists(key)
        self.check_param(key, '[PORT]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_obstacle contains [ICON]=
    def test_auriga_event_obstacle(self):
        key = 'auriga_event_obstacle'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_obstacle_distance contains [ICON]
    def test_auriga_detect_obstacle_distance(self):
        key = 'auriga_detect_obstacle_distance'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_event_linefollower contains [ICON] 
    def test_auriga_event_linefollower(self):
        key = 'auriga_event_linefollower'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/auriga/auriga_detect_angle contains [ICON] [AXIS]
    def test_auriga_detect_angle(self):
        key = 'auriga_detect_angle'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/auriga/auriga_when_board_launch contains  mBot Ranger(Auriga)
    def test_auriga_when_board_launch(self):
        key = 'auriga_when_board_launch'
        self.check_key_exists(key)
        self.check_param(key, 'mBot Ranger(Auriga)')

    # ext-i18n/auriga/AURIGA_SOUND_PLAY_NOTE_NOTE is right
    def test_AURIGA_SOUND_PLAY_NOTE_NOTE(self):
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_0', "C2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_1', "D2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_2', "E2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_3', "F2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_4', "G2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_5', "A2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_6', "B2")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_7', "C3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_8', "D3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_9', "E3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_10', "F3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_11', "G3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_12', "A3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_13', "B3")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_14', "C4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_15', "D4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_16', "E4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_17', "F4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_18', "G4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_19', "A4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_20', "B4")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_21', "C5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_22', "D5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_23', "E5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_24', "F5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_25', "G5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_26', "A5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_27', "B5")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_28', "C6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_29', "D6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_30', "E6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_31', "F6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_32', "G6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_33', "A6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_34', "B6")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_35', "C7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_36', "D7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_37', "E7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_38', "F7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_39', "G7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_40', "A7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_41', "B7")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_42', "C8")
        self.check_expect_value('AURIGA_SOUND_PLAY_NOTE_NOTE_43', "D8")


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AurigaTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)