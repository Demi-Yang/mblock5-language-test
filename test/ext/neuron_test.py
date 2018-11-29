# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  neuron項目-翻译检查  =======================

class NeuronTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/neuron']

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





    # ext-i18n/neuron/No empty value
    def test_neuron_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/neuron/No new or missing items
    def test_neuron_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 160, "neuron 模块下存在新增或者删减的字段，需要修改测试用例！")

    # mblock5-i18n/neuron/extensionName&neuron equals Neuron
    def test_extensionName_equals_neuron(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_expect_value(key, "Neuron")
        self.check_expect_value('neuron', "Neuron")

    # ext-i18n/neuron/neuron_run_dcmotor_with_time contains [ICON]、[ID]、[SLOT]、[POWER] %、[TIME]
    def test_neuron_run_dcmotor_with_time(self):
        key = 'neuron_run_dcmotor_with_time'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[POWER] %')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_run_dcmotor_with_speed contains [ICON]、[ID]、[SLOT]、[POWER] %
    def test_neuron_run_dcmotor_with_speed(self):
        key = 'neuron_run_dcmotor_with_speed'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[POWER] %')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_run_dcmotors contains [ICON]、[ID]、[POWER_LEFT] %、[POWER_RIGHT] %
    def test_neuron_run_dcmotors(self):
        key = 'neuron_run_dcmotors'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[POWER_LEFT] %')
        self.check_param(key, '[POWER_RIGHT] %')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_run_servo contains [ICON]、[ID]、[SLOT]、[ANGLE]
    def test_neuron_run_servo(self):
        key = 'neuron_run_servo'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[SLOT]')
        self.check_param(key, '[ANGLE]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_led_with_time contains [ICON]、[ID]、[COLOR]、[TIME]
    def test_neuron_set_led_with_time(self):
        key = 'neuron_set_led_with_time'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COLOR]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_led contains [ICON]、[ID]、[COLOR]
    def test_neuron_set_led(self):
        key = 'neuron_set_led'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_led_with_rgb contains [ICON]、[ID]、[R]、[G]、[B]
    def test_neuron_set_led_with_rgb(self):
        key = 'neuron_set_led_with_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_turn_off_led contains [ICON]
    def test_neuron_turn_off_led(self):
        key = 'neuron_turn_off_led'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledstrip_mode contains [ICON]、[ID]、[STRIP]
    def test_neuron_set_ledstrip_mode(self):
        key = 'neuron_set_ledstrip_mode'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[STRIP]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledstrip_with_rgb contains [ICON]、[ID]、[POSITION]、[R]、[G]、[B]
    def test_neuron_set_ledstrip_with_rgb(self):
        key = 'neuron_set_ledstrip_with_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[POSITION]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledstrip_with_color contains [ICON]、[ID]、[POSITION]、[COLOR]
    def test_neuron_set_ledstrip_with_color(self):
        key = 'neuron_set_ledstrip_with_color'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[POSITION]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_turn_off_ledstrip contains [ICON]
    def test_neuron_turn_off_ledstrip(self):
        key = 'neuron_turn_off_ledstrip'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledpanel_with_time contains [ICON]、[ID]、[PANEL]、[TIME]
    def test_neuron_set_ledpanel_with_time(self):
        key = 'neuron_set_ledpanel_with_time'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[PANEL]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledpanel_face contains [ICON]、[ID]、[PANEL]
    def test_neuron_set_ledpanel_face(self):
        key = 'neuron_set_ledpanel_face'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[PANEL]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledpanel_postion contains [ICON]、[ID]、[COLOR]、x: [X] y: [Y]
    def test_neuron_set_ledpanel_postion(self):
        key = 'neuron_set_ledpanel_postion'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_set_ledpanel_postion_rgb contains [ICON]、[ID]、[R]、[G]、[B]、x: [X] y: [Y]
    def test_neuron_set_ledpanel_postion_rgb(self):
        key = 'neuron_set_ledpanel_postion_rgb'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_param(key, '[R]')
        self.check_param(key, '[G]')
        self.check_param(key, '[B]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_turn_off_ledpanel_postion contains [ICON]、[ID]、x: [X] y: [Y]
    def test_neuron_turn_off_ledpanel_postion(self):
        key = 'neuron_turn_off_ledpanel_postion'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_turn_off_ledpanel contains [ICON]
    def test_neuron_turn_off_ledpanel(self):
        key = 'neuron_turn_off_ledpanel'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/neuron/neuron_display_emotion contains [ICON]、[ID]、[EMOTION]
    def test_neuron_display_emotion(self):
        key = 'neuron_display_emotion'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[EMOTION]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_display_emotion_with_time contains [ICON]、[ID]、[EMOTION]、[DURATION]
    def test_neuron_display_emotion_with_time(self):
        key = 'neuron_display_emotion_with_time'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[EMOTION]')
        self.check_param(key, '[DURATION]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_display_icon contains [ICON]、[ID]、[ICON_ID]、[STRING]
    def test_neuron_display_icon(self):
        key = 'neuron_display_icon'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[ICON_ID]')
        self.check_param(key, '[STRING]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_display_icon_with_pos contains [ICON]、[ID]、[ICON_ID_1]、[STRING_1]、[ICON_ID_2]、[STRING_2]
    def test_neuron_display_icon_with_pos(self):
        key = 'neuron_display_icon_with_pos'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[ICON_ID_1]')
        self.check_param(key, '[STRING_1]')
        self.check_param(key, '[ICON_ID_2]')
        self.check_param(key, '[STRING_2]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_light_on_el_wiredriver contains [ICON]、[ID]、[SLOT]
    def test_neuron_light_on_el_wiredriver(self):
        key = 'neuron_light_on_el_wiredriver'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_light_off_el_wiredriver contains [ICON]、[ID]、[SLOT]
    def test_neuron_light_off_el_wiredriver(self):
        key = 'neuron_light_off_el_wiredriver'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[SLOT]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_play_tone contains [ICON]、[ID]、[TONE]、[BEAT]
    def test_neuron_play_tone(self):
        key = 'neuron_play_tone'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[TONE]')
        self.check_param(key, '[BEAT]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_play_hz contains [ICON]、[ID]、[HZ]、[TIME]
    def test_neuron_play_hz(self):
        key = 'neuron_play_hz'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[HZ]')
        self.check_param(key, '[TIME]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_button_pressed contains [ICON]、[ID]
    def test_neuron_event_button_pressed(self):
        key = 'neuron_event_button_pressed'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_knob contains [ICON]、[ID]
    def test_neuron_detect_knob(self):
        key = 'neuron_detect_knob'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_temperature contains [ICON]、[ID]
    def test_neuron_detect_temperature(self):
        key = 'neuron_detect_temperature'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_linefollow contains [ICON]、[ID]、[AXIS]
    def test_neuron_event_linefollow(self):
        key = 'neuron_event_linefollow'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_lightness contains [ICON]、[ID]
    def test_neuron_detect_lightness(self):
        key = 'neuron_detect_lightness'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_touch_color contains [ICON]、[ID]、[COLOR]
    def test_neuron_event_touch_color(self):
        key = 'neuron_event_touch_color'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_volume contains [ICON]、[ID]
    def test_neuron_detect_volume(self):
        key = 'neuron_detect_volume'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_ultrasonic contains [ICON]、[ID]
    def test_neuron_detect_ultrasonic(self):
        key = 'neuron_detect_ultrasonic'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_tilt contains [ICON]、[ID]、[DIRECTION]
    def test_neuron_event_tilt(self):
        key = 'neuron_event_tilt'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[DIRECTION]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_shaked contains [ICON]、[ID]
    def test_neuron_event_shaked(self):
        key = 'neuron_event_shaked'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_gyro_angle contains [ICON]、[ID]、[COORDINATE]
    def test_neuron_detect_gyro_angle(self):
        key = 'neuron_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COORDINATE]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_gyro_speed contains [ICON]、[ID]、[COORDINATE]
    def test_neuron_detect_gyro_speed(self):
        key = 'neuron_detect_gyro_speed'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COORDINATE]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_color_sensor contains [ICON]、[ID]、[COLOR]
    def test_neuron_detect_color_sensor(self):
        key = 'neuron_detect_color_sensor'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[COLOR]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_josystick_direction contains [ICON]、[ID]、[DIRECTION]
    def test_neuron_event_josystick_direction(self):
        key = 'neuron_event_josystick_direction'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[DIRECTION]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_joystick contains [ICON]、[ID]、[AXIS]
    def test_neuron_detect_joystick(self):
        key = 'neuron_detect_joystick'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_event_pir contains [ICON]、[ID]
    def test_neuron_event_pir(self):
        key = 'neuron_event_pir'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/neuron_detect_humidity contains [ICON]、[ID]
    def test_neuron_detect_humidity(self):
        key = 'neuron_detect_humidity'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/op_ranging contains [ICON]、[ID]
    def test_op_ranging(self):
        key = 'op_ranging'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/op_temperature contains [ICON]、[ID]
    def test_op_temperature(self):
        key = 'op_temperature'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/op_htemperature contains [ICON]、[ID]
    def test_op_htemperature(self):
        key = 'op_htemperature'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/op_humidity contains [ICON]、[ID]
    def test_op_humidity(self):
        key = 'op_humidity'
        self.check_key_exists(key)
        self.check_param(key, '[ID]')
        self.check_icon(key)

    # ext-i18n/neuron/NEURON_DETECT_JOYSTICK_AXIS is right
    def test_NEURON_DETECT_JOYSTICK_AXIS(self):
        self.check_expect_value('NEURON_DETECT_JOYSTICK_AXIS_0', 'x')
        self.check_expect_value('NEURON_DETECT_JOYSTICK_AXIS_1', 'y')

    # ext-i18n/neuron/NEURON_DETECT_GYRO_SPEED_COORDINATE is right
    def test_NEURON_DETECT_GYRO_SPEED_COORDINATE(self):
        self.check_expect_value('NEURON_DETECT_GYRO_SPEED_COORDINATE_0', 'x')
        self.check_expect_value('NEURON_DETECT_GYRO_SPEED_COORDINATE_1', 'y')
        self.check_expect_value('NEURON_DETECT_GYRO_SPEED_COORDINATE_2', 'z')

    # ext-i18n/neuron/NEURON_PLAY_TONE_TONE is right
    def test_NEURON_PLAY_TONE_TONE(self):
        self.check_expect_value("NEURON_PLAY_TONE_TONE_0", "C7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_1", "C2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_2", "D2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_3", "E2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_4", "F2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_5", "G2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_6", "A2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_7", "B2")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_8", "C3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_9", "D3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_10", "E3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_11", "F3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_12", "F3m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_13", "G3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_14", "G3m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_15", "A3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_16", "A3m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_17", "B3")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_18", "C4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_19", "C4m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_20", "D4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_21", "D4m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_22", "E4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_23", "F4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_24", "F4m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_25", "G4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_26", "G4m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_27", "A4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_28", "A4m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_29", "B4")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_30", "C5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_31", "C5m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_32", "D5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_33", "D5m")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_34", "E5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_35", "F5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_36", "G5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_37", "A5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_38", "B5")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_39", "C6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_40", "D6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_41", "E6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_42", "F6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_43", "G6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_44", "A6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_45", "B6")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_46", "D7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_47", "E7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_48", "F7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_49", "G7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_50", "A7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_51", "B7")
        self.check_expect_value("NEURON_PLAY_TONE_TONE_52", "C8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(NeuronTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
























