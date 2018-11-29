# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  microbit項目-翻译检查  =======================

class MicrobitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/microbit']

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





    # ext-i18n/microbit/No empty value
    def test_microbit_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/microbit/No new or missing items
    def test_microbit_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 214, "microbit 模块下存在新增或者删减的字段，需要修改测试用例！")

    # mblock5-i18n/microbit/extensionName&microbit equals microbit
    def test_extensionName_equals_microbit(self):
        key = 'extensionName'
        self.check_key_exists(key)
        self.check_key_exists('microbit')
        self.check_expect_value(key, "microbit")
        self.check_expect_value('microbit', "microbit")

    # ext-i18n/microbit/microbit_show_led_matrix_happy contains [ICON] [PANEL]
    def test_microbit_show_led_matrix_happy(self):
        key = 'microbit_show_led_matrix_happy'
        self.check_key_exists(key)
        self.check_param(key, '[PANEL]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix_happy_with_time contains [ICON] [PANEL]
    def test_microbit_show_led_matrix_happy_with_time(self):
        key = 'microbit_show_led_matrix_happy_with_time'
        self.check_key_exists(key)
        self.check_param(key, '[PANEL]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_mirrored_led_matrix contains [ICON] [PANEL]
    def test_microbit_show_mirrored_led_matrix(self):
        key = 'microbit_show_mirrored_led_matrix'
        self.check_key_exists(key)
        self.check_param(key, '[PANEL]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix_with_shift_pixel contains [ICON] [PANEL] [DIRECTION] [DISTANCE]
    def test_microbit_show_led_matrix_with_shift_pixel(self):
        key = 'microbit_show_led_matrix_with_shift_pixel'
        self.check_key_exists(key)
        self.check_param(key, '[PANEL]')
        self.check_param(key, '[DIRECTION]')
        self.check_param(key, '[DISTANCE]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix contains [ICON] [STRING]
    def test_microbit_show_led_matrix(self):
        key = 'microbit_show_led_matrix'
        self.check_key_exists(key)
        self.check_param(key, '[STRING]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix_scroll contains [ICON] [STRING]
    def test_microbit_show_led_matrix_scroll(self):
        key = 'microbit_show_led_matrix_scroll'
        self.check_key_exists(key)
        self.check_param(key, '[STRING]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix_turn_off contains [ICON]
    def test_microbit_show_led_matrix_turn_off(self):
        key = 'microbit_show_led_matrix_turn_off'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_toggle_led_matrix_position contains [ICON] [STATUS] x: [X] y: [Y]
    def test_microbit_toggle_led_matrix_position(self):
        key = 'microbit_toggle_led_matrix_position'
        self.check_key_exists(key)
        self.check_param(key, '[STATUS]')
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_show_led_matrix_light_position contains [ICON] [LIGHTNESS] x: [X] y: [Y]
    def test_microbit_show_led_matrix_light_position(self):
        key = 'microbit_show_led_matrix_light_position'
        self.check_key_exists(key)
        self.check_param(key, '[LIGHTNESS]')
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_get_led_matrix_pixel_lightness contains [ICON] x: [X] y: [Y]
    def test_microbit_get_led_matrix_pixel_lightness(self):
        key = 'microbit_get_led_matrix_pixel_lightness'
        self.check_key_exists(key)
        self.check_param(key, 'x: [X]')
        self.check_param(key, 'y: [Y]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_event_button_pressed contains [ICON] [BUTTON]
    def test_microbit_event_button_pressed(self):
        key = 'microbit_event_button_pressed'
        self.check_key_exists(key)
        self.check_param(key, '[BUTTON]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_event_gesture contains [ICON] [GESTURE]
    def test_microbit_event_gesture(self):
        key = 'microbit_event_gesture'
        self.check_key_exists(key)
        self.check_param(key, '[GESTURE]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_accelerometer contains [ICON] [AXIS]
    def test_microbit_detect_accelerometer(self):
        key = 'microbit_detect_accelerometer'
        self.check_key_exists(key)
        self.check_param(key, '[AXIS]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_compass contains [ICON]
    def test_microbit_detect_compass(self):
        key = 'microbit_detect_compass'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_field_strength contains [ICON]
    def test_microbit_detect_field_strength(self):
        key = 'microbit_detect_field_strength'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_compass_calibrate contains [ICON]
    def test_microbit_compass_calibrate(self):
        key = 'microbit_compass_calibrate'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_temperature contains [ICON]
    def test_microbit_detect_temperature(self):
        key = 'microbit_detect_temperature'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_time contains [ICON]
    def test_microbit_detect_time(self):
        key = 'microbit_detect_time'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_event_pin_connected contains [ICON] [PIN]
    def test_microbit_event_pin_connected(self):
        key = 'microbit_event_pin_connected'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_detect_pin_analog_value contains [ICON] [PIN]
    def test_microbit_detect_pin_analog_value(self):
        key = 'microbit_detect_pin_analog_value'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_set_pin_analog_value contains [ICON] [PIN] [ANALOG_VALUE]
    def test_microbit_set_pin_analog_value(self):
        key = 'microbit_set_pin_analog_value'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_param(key, '[ANALOG_VALUE]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_event_pin_input_digital contains [ICON] [PIN]
    def test_microbit_event_pin_input_digital(self):
        key = 'microbit_event_pin_input_digital'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_turn_on contains [ICON]
    def test_microbit_radio_turn_on(self):
        key = 'microbit_radio_turn_on'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_turn_off contains [ICON]
    def test_microbit_radio_turn_off(self):
        key = 'microbit_radio_turn_off'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_reset contains [ICON]
    def test_microbit_radio_reset(self):
        key = 'microbit_radio_reset'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_send contains [ICON] [MESSAGE]
    def test_microbit_radio_send(self):
        key = 'microbit_radio_send'
        self.check_key_exists(key)
        self.check_param(key, '[MESSAGE]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_receive contains [ICON]
    def test_microbit_radio_receive(self):
        key = 'microbit_radio_receive'
        self.check_key_exists(key)
        self.check_icon(key)

    # ext-i18n/microbit/microbit_radio_set_channel contains [ICON] [CHANNEL]
    def test_microbit_radio_set_channel(self):
        key = 'microbit_radio_set_channel'
        self.check_key_exists(key)
        self.check_param(key, '[CHANNEL]')
        self.check_icon(key)

    # ext-i18n/microbit/microbit_when_button_press contains [BUTTON]
    def test_microbit_when_button_press(self):
        key = 'microbit_when_button_press'
        self.check_key_exists(key)
        self.check_param(key, '[BUTTON]')

    # ext-i18n/microbit/microbit_when_pin_connect contains [PIN]
    def test_microbit_when_pin_connect(self):
        key = 'microbit_when_pin_connect'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')

    # ext-i18n/microbit/microbit_when_gesture contains [GESTURE]
    def test_microbit_when_gesture(self):
        key = 'microbit_when_gesture'
        self.check_key_exists(key)
        self.check_param(key, '[GESTURE]')

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_8 equals 3g
    def test_MICROBIT_WHEN_GESTURE_GESTURE_8(self):
        key = 'MICROBIT_WHEN_GESTURE_GESTURE_8'
        self.check_key_exists(key)
        self.check_expect_value(key, '3g')

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_9 equals 6g
    def test_MICROBIT_WHEN_GESTURE_GESTURE_9(self):
        key = 'MICROBIT_WHEN_GESTURE_GESTURE_9'
        self.check_key_exists(key)
        self.check_expect_value(key, '6g')

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_10 equals 8g
    def test_MICROBIT_WHEN_GESTURE_GESTURE_10(self):
        key = 'MICROBIT_WHEN_GESTURE_GESTURE_10'
        self.check_key_exists(key)
        self.check_expect_value(key, '8g')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0 equals A
    def test_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0(self):
        key = 'MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0'
        self.check_key_exists(key)
        self.check_expect_value(key, 'A')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1 equals B
    def test_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1(self):
        key = 'MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1'
        self.check_key_exists(key)
        self.check_expect_value(key, 'B')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2 equals A+B
    def test_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2(self):
        key = 'MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2'
        self.check_key_exists(key)
        self.check_expect_value(key, 'A+B')

    # ext-i18n/microbit/MICROBIT_RADIO_SET_CHANNEL_CHANNEL is right
    def test_MICROBIT_RADIO_SET_CHANNEL_CHANNEL(self):
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_0', "0")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_1', "1")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_2', "2")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_3', "3")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_4', "4")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_5', "5")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_6', "6")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_7', "7")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_8', "8")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_9', "9")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_10',  "10")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_11',  "11")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_12',  "12")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_13',  "13")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_14',  "14")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_15',  "15")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_16',  "16")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_17',  "17")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_18',  "18")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_19',  "19")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_20',  "20")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_21',  "21")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_22',  "22")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_23',  "23")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_24',  "24")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_25',  "25")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_26',  "26")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_27',  "27")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_28',  "28")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_29',  "29")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_30',  "30")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_31',  "31")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_32',  "32")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_33',  "33")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_34',  "34")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_35',  "35")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_36',  "36")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_37',  "37")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_38',  "38")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_39',  "39")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_40',  "40")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_41',  "41")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_42',  "42")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_43',  "43")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_44',  "44")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_45',  "45")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_46',  "46")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_47',  "47")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_48',  "48")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_49',  "49")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_50',  "50")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_51',  "51")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_52',  "52")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_53',  "53")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_54',  "54")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_55',  "55")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_56',  "56")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_57',  "57")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_58',  "58")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_59',  "59")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_60',  "60")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_61',  "61")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_62',  "62")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_63',  "63")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_64',  "64")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_65',  "65")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_66',  "66")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_67',  "67")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_68',  "68")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_69',  "69")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_70',  "70")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_71',  "71")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_72',  "72")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_73',  "73")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_74',  "74")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_75',  "75")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_76',  "76")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_77',  "77")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_78',  "78")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_79',  "79")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_80',  "80")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_81',  "81")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_82',  "82")
        self.check_expect_value('MICROBIT_RADIO_SET_CHANNEL_CHANNEL_83',  "83")

    # ext-i18n/microbit/MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN is right
    def test_MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN(self):
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_0', "0")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_1', "1")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_2', "2")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_3', "3")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_4', "4")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_5', "5")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_6', "6")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_7', "7")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_8', "8")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_9', "9")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_10',  "10")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_11',  "11")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_12',  "12")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_13',  "13")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_14',  "14")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_15',  "15")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_16',  "16")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_17',  "17")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_18',  "18")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_19',  "19")
        self.check_expect_value('MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_20',  "20")

    # ext-i18n/microbit/MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN is right
    def test_MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN(self):
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_0', "0")
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_1', "1")
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_2', "2")
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_3', "3")
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_4', "4")
        self.check_expect_value('MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_5', "10")
    
    # ext-i18n/microbit/MICROBIT_EVENT_PIN_CONNECTED_PIN is right
    def test_MICROBIT_EVENT_PIN_CONNECTED_PIN(self):
        self.check_expect_value('MICROBIT_EVENT_PIN_CONNECTED_PIN_0', "0")
        self.check_expect_value('MICROBIT_EVENT_PIN_CONNECTED_PIN_1', "1")
        self.check_expect_value('MICROBIT_EVENT_PIN_CONNECTED_PIN_2', "2")

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_8 equals 3g
    def test_MICROBIT_EVENT_GESTURE_GESTURE_8(self):
        key = 'MICROBIT_EVENT_GESTURE_GESTURE_8'
        self.check_key_exists(key)
        self.check_expect_value(key, '3g')

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_9 equals 6g
    def test_MICROBIT_EVENT_GESTURE_GESTURE_9(self):
        key = 'MICROBIT_EVENT_GESTURE_GESTURE_9'
        self.check_key_exists(key)
        self.check_expect_value(key, '6g')

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_10 equals 8g
    def test_MICROBIT_EVENT_GESTURE_GESTURE_10(self):
        key = 'MICROBIT_EVENT_GESTURE_GESTURE_10'
        self.check_key_exists(key)
        self.check_expect_value(key, '8g')

    # ext-i18n/microbit/MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0 equals A
    def test_MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0(self):
        key = 'MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0'
        self.check_key_exists(key)
        self.check_expect_value(key, 'A')

    # ext-i18n/microbit/MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1 equals B
    def test_MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1(self):
        key = 'MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1'
        self.check_key_exists(key)
        self.check_expect_value(key, 'B')
    
    # ext-i18n/microbit/MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS is right
    def MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS(self):
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_0", "9")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_1", "8")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_2", "7")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_3", "6")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_4", "5")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_5", "4")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_6", "3")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_7", "2")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_8", "1")
        self.check_expect_value("MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_9", "0")




if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MicrobitTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)