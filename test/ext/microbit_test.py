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

    # ext-i18n/microbit/No empty value
    def test_ext_i18n_microbit_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/microbit/No new or missing items
    def test_ext_i18n_microbit_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 214)

    # mblock5-i18n/microbit/extensionName&microbit equals microbit
    def test_mblock5_i18n_extensionName_equals_microbit(self):
        self.assertIn('extensionName', self.test_dict)
        self.assertIn('microbit', self.test_dict)
        self.assertEqual(self.test_dict['extensionName'], "microbit")
        self.assertEqual(self.test_dict['microbit'], "microbit")

    # ext-i18n/microbit/microbit_show_led_matrix_happy contains [ICON] [PANEL]
    def test_ext_i18n_microbit_show_led_matrix_happy(self):
        self.assertIn('microbit_show_led_matrix_happy', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_happy']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix_happy_with_time contains [ICON] [PANEL]
    def test_ext_i18n_microbit_show_led_matrix_happy_with_time(self):
        self.assertIn('microbit_show_led_matrix_happy_with_time', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_happy_with_time']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_mirrored_led_matrix contains [ICON] [PANEL]
    def test_ext_i18n_microbit_show_mirrored_led_matrix(self):
        self.assertIn('microbit_show_mirrored_led_matrix', self.test_dict)
        test_data = self.test_dict['microbit_show_mirrored_led_matrix']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix_with_shift_pixel contains [ICON] [PANEL] [DIRECTION] [DISTANCE]
    def test_ext_i18n_microbit_show_led_matrix_with_shift_pixel(self):
        self.assertIn('microbit_show_led_matrix_with_shift_pixel', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_with_shift_pixel']
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[DISTANCE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix contains [ICON] [STRING]
    def test_ext_i18n_microbit_show_led_matrix(self):
        self.assertIn('microbit_show_led_matrix', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix']
        self.assertIn('[STRING]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix_scroll contains [ICON] [STRING]
    def test_ext_i18n_microbit_show_led_matrix_scroll(self):
        self.assertIn('microbit_show_led_matrix_scroll', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_scroll']
        self.assertIn('[STRING]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix_turn_off contains [ICON]
    def test_ext_i18n_microbit_show_led_matrix_turn_off(self):
        self.assertIn('microbit_show_led_matrix_turn_off', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_turn_off']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_toggle_led_matrix_position contains [ICON] [STATUS] x: [X] y: [Y]
    def test_ext_i18n_microbit_toggle_led_matrix_position(self):
        self.assertIn('microbit_toggle_led_matrix_position', self.test_dict)
        test_data = self.test_dict['microbit_toggle_led_matrix_position']
        self.assertIn('[STATUS]', test_data)
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_show_led_matrix_light_position contains [ICON] [LIGHTNESS] x: [X] y: [Y]
    def test_ext_i18n_microbit_show_led_matrix_light_position(self):
        self.assertIn('microbit_show_led_matrix_light_position', self.test_dict)
        test_data = self.test_dict['microbit_show_led_matrix_light_position']
        self.assertIn('[LIGHTNESS]', test_data)
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_get_led_matrix_pixel_lightness contains [ICON] x: [X] y: [Y]
    def test_ext_i18n_microbit_get_led_matrix_pixel_lightness(self):
        self.assertIn('microbit_get_led_matrix_pixel_lightness', self.test_dict)
        test_data = self.test_dict['microbit_get_led_matrix_pixel_lightness']
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_event_button_pressed contains [ICON] [BUTTON]
    def test_ext_i18n_microbit_event_button_pressed(self):
        self.assertIn('microbit_event_button_pressed', self.test_dict)
        test_data = self.test_dict['microbit_event_button_pressed']
        self.assertIn('[BUTTON]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_event_gesture contains [ICON] [GESTURE]
    def test_ext_i18n_microbit_event_gesture(self):
        self.assertIn('microbit_event_gesture', self.test_dict)
        test_data = self.test_dict['microbit_event_gesture']
        self.assertIn('[GESTURE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_accelerometer contains [ICON] [AXIS]
    def test_ext_i18n_microbit_detect_accelerometer(self):
        self.assertIn('microbit_detect_accelerometer', self.test_dict)
        test_data = self.test_dict['microbit_detect_accelerometer']
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_compass contains [ICON]
    def test_ext_i18n_microbit_detect_compass(self):
        self.assertIn('microbit_detect_compass', self.test_dict)
        test_data = self.test_dict['microbit_detect_compass']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_field_strength contains [ICON]
    def test_ext_i18n_microbit_detect_field_strength(self):
        self.assertIn('microbit_detect_field_strength', self.test_dict)
        test_data = self.test_dict['microbit_detect_field_strength']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_compass_calibrate contains [ICON]
    def test_ext_i18n_microbit_compass_calibrate(self):
        self.assertIn('microbit_compass_calibrate', self.test_dict)
        test_data = self.test_dict['microbit_compass_calibrate']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_temperature contains [ICON]
    def test_ext_i18n_microbit_detect_temperature(self):
        self.assertIn('microbit_detect_temperature', self.test_dict)
        test_data = self.test_dict['microbit_detect_temperature']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_time contains [ICON]
    def test_ext_i18n_microbit_detect_time(self):
        self.assertIn('microbit_detect_time', self.test_dict)
        test_data = self.test_dict['microbit_detect_time']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_event_pin_connected contains [ICON] [PIN]
    def test_ext_i18n_microbit_event_pin_connected(self):
        self.assertIn('microbit_event_pin_connected', self.test_dict)
        test_data = self.test_dict['microbit_event_pin_connected']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_detect_pin_analog_value contains [ICON] [PIN]
    def test_ext_i18n_microbit_detect_pin_analog_value(self):
        self.assertIn('microbit_detect_pin_analog_value', self.test_dict)
        test_data = self.test_dict['microbit_detect_pin_analog_value']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_set_pin_analog_value contains [ICON] [PIN] [ANALOG_VALUE]
    def test_ext_i18n_microbit_set_pin_analog_value(self):
        self.assertIn('microbit_set_pin_analog_value', self.test_dict)
        test_data = self.test_dict['microbit_set_pin_analog_value']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[ANALOG_VALUE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_event_pin_input_digital contains [ICON] [PIN]
    def test_ext_i18n_microbit_event_pin_input_digital(self):
        self.assertIn('microbit_event_pin_input_digital', self.test_dict)
        test_data = self.test_dict['microbit_event_pin_input_digital']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_turn_on contains [ICON]
    def test_ext_i18n_microbit_radio_turn_on(self):
        self.assertIn('microbit_radio_turn_on', self.test_dict)
        test_data = self.test_dict['microbit_radio_turn_on']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_turn_off contains [ICON]
    def test_ext_i18n_microbit_radio_turn_off(self):
        self.assertIn('microbit_radio_turn_off', self.test_dict)
        test_data = self.test_dict['microbit_radio_turn_off']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_reset contains [ICON]
    def test_ext_i18n_microbit_radio_reset(self):
        self.assertIn('microbit_radio_reset', self.test_dict)
        test_data = self.test_dict['microbit_radio_reset']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_send contains [ICON] [MESSAGE]
    def test_ext_i18n_microbit_radio_send(self):
        self.assertIn('microbit_radio_send', self.test_dict)
        test_data = self.test_dict['microbit_radio_send']
        self.assertIn('[MESSAGE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_receive contains [ICON]
    def test_ext_i18n_microbit_radio_receive(self):
        self.assertIn('microbit_radio_receive', self.test_dict)
        test_data = self.test_dict['microbit_radio_receive']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_radio_set_channel contains [ICON] [CHANNEL]
    def test_ext_i18n_microbit_radio_set_channel(self):
        self.assertIn('microbit_radio_set_channel', self.test_dict)
        test_data = self.test_dict['microbit_radio_set_channel']
        self.assertIn('[CHANNEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit/microbit_when_button_press contains [BUTTON]
    def test_ext_i18n_microbit_when_button_press(self):
        self.assertIn('microbit_when_button_press', self.test_dict)
        test_data = self.test_dict['microbit_when_button_press']
        self.assertIn('[BUTTON]', test_data)

    # ext-i18n/microbit/microbit_when_pin_connect contains [PIN]
    def test_ext_i18n_microbit_when_pin_connect(self):
        self.assertIn('microbit_when_pin_connect', self.test_dict)
        test_data = self.test_dict['microbit_when_pin_connect']
        self.assertIn('[PIN]', test_data)

    # ext-i18n/microbit/microbit_when_gesture contains [GESTURE]
    def test_ext_i18n_microbit_when_gesture(self):
        self.assertIn('microbit_when_gesture', self.test_dict)
        test_data = self.test_dict['microbit_when_gesture']
        self.assertIn('[GESTURE]', test_data)

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_8 equals 3g
    def test_ext_i18n_MICROBIT_WHEN_GESTURE_GESTURE_8(self):
        self.assertIn('MICROBIT_WHEN_GESTURE_GESTURE_8', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_GESTURE_GESTURE_8']
        self.assertEqual(test_data, '3g')

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_9 equals 6g
    def test_ext_i18n_MICROBIT_WHEN_GESTURE_GESTURE_9(self):
        self.assertIn('MICROBIT_WHEN_GESTURE_GESTURE_9', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_GESTURE_GESTURE_9']
        self.assertEqual(test_data, '6g')

    # ext-i18n/microbit/MICROBIT_WHEN_GESTURE_GESTURE_10 equals 8g
    def test_ext_i18n_MICROBIT_WHEN_GESTURE_GESTURE_10(self):
        self.assertIn('MICROBIT_WHEN_GESTURE_GESTURE_10', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_GESTURE_GESTURE_10']
        self.assertEqual(test_data, '8g')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0 equals A
    def test_ext_i18n_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0(self):
        self.assertIn('MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_BUTTON_PRESS_BUTTON_0']
        self.assertEqual(test_data, 'A')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1 equals B
    def test_ext_i18n_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1(self):
        self.assertIn('MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_BUTTON_PRESS_BUTTON_1']
        self.assertEqual(test_data, 'B')

    # ext-i18n/microbit/MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2 equals A+B
    def test_ext_i18n_MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2(self):
        self.assertIn('MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2', self.test_dict)
        test_data = self.test_dict['MICROBIT_WHEN_BUTTON_PRESS_BUTTON_2']
        self.assertEqual(test_data, 'A+B')

    # ext-i18n/microbit/MICROBIT_RADIO_SET_CHANNEL_CHANNEL is right
    def test_ext_i18n_MICROBIT_RADIO_SET_CHANNEL_CHANNEL(self):
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_0'], "0")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_1'], "1")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_2'], "2")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_3'], "3")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_4'], "4")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_5'], "5")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_6'], "6")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_7'], "7")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_8'], "8")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_9'], "9")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_10'],  "10")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_11'],  "11")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_12'],  "12")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_13'],  "13")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_14'],  "14")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_15'],  "15")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_16'],  "16")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_17'],  "17")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_18'],  "18")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_19'],  "19")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_20'],  "20")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_21'],  "21")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_22'],  "22")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_23'],  "23")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_24'],  "24")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_25'],  "25")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_26'],  "26")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_27'],  "27")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_28'],  "28")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_29'],  "29")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_30'],  "30")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_31'],  "31")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_32'],  "32")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_33'],  "33")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_34'],  "34")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_35'],  "35")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_36'],  "36")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_37'],  "37")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_38'],  "38")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_39'],  "39")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_40'],  "40")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_41'],  "41")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_42'],  "42")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_43'],  "43")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_44'],  "44")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_45'],  "45")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_46'],  "46")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_47'],  "47")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_48'],  "48")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_49'],  "49")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_50'],  "50")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_51'],  "51")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_52'],  "52")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_53'],  "53")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_54'],  "54")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_55'],  "55")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_56'],  "56")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_57'],  "57")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_58'],  "58")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_59'],  "59")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_60'],  "60")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_61'],  "61")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_62'],  "62")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_63'],  "63")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_64'],  "64")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_65'],  "65")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_66'],  "66")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_67'],  "67")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_68'],  "68")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_69'],  "69")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_70'],  "70")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_71'],  "71")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_72'],  "72")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_73'],  "73")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_74'],  "74")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_75'],  "75")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_76'],  "76")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_77'],  "77")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_78'],  "78")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_79'],  "79")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_80'],  "80")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_81'],  "81")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_82'],  "82")
        self.assertEqual(self.test_dict['MICROBIT_RADIO_SET_CHANNEL_CHANNEL_83'],  "83")

    # ext-i18n/microbit/MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN is right
    def test_ext_i18n_MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN(self):
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_0'], "0")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_1'], "1")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_2'], "2")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_3'], "3")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_4'], "4")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_5'], "5")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_6'], "6")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_7'], "7")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_8'], "8")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_9'], "9")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_10'],  "10")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_11'],  "11")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_12'],  "12")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_13'],  "13")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_14'],  "14")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_15'],  "15")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_16'],  "16")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_17'],  "17")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_18'],  "18")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_19'],  "19")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_INPUT_DIGITAL_PIN_20'],  "20")

    # ext-i18n/microbit/MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN is right
    def test_ext_i18n_MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN(self):
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_0'], "0")
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_1'], "1")
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_2'], "2")
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_3'], "3")
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_4'], "4")
        self.assertEqual(self.test_dict['MICROBIT_DETECT_PIN_ANALOG_VALUE_PIN_5'], "10")
    
    # ext-i18n/microbit/MICROBIT_EVENT_PIN_CONNECTED_PIN is right
    def test_ext_i18n_MICROBIT_EVENT_PIN_CONNECTED_PIN(self):
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_CONNECTED_PIN_0'], "0")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_CONNECTED_PIN_1'], "1")
        self.assertEqual(self.test_dict['MICROBIT_EVENT_PIN_CONNECTED_PIN_2'], "2")

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_8 equals 3g
    def test_ext_i18n_MICROBIT_EVENT_GESTURE_GESTURE_8(self):
        self.assertIn('MICROBIT_EVENT_GESTURE_GESTURE_8', self.test_dict)
        test_data = self.test_dict['MICROBIT_EVENT_GESTURE_GESTURE_8']
        self.assertEqual(test_data, '3g')

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_9 equals 6g
    def test_ext_i18n_MICROBIT_EVENT_GESTURE_GESTURE_9(self):
        self.assertIn('MICROBIT_EVENT_GESTURE_GESTURE_9', self.test_dict)
        test_data = self.test_dict['MICROBIT_EVENT_GESTURE_GESTURE_9']
        self.assertEqual(test_data, '6g')

    # ext-i18n/microbit/MICROBIT_EVENT_GESTURE_GESTURE_10 equals 8g
    def test_ext_i18n_MICROBIT_EVENT_GESTURE_GESTURE_10(self):
        self.assertIn('MICROBIT_EVENT_GESTURE_GESTURE_10', self.test_dict)
        test_data = self.test_dict['MICROBIT_EVENT_GESTURE_GESTURE_10']
        self.assertEqual(test_data, '8g')

    # ext-i18n/microbit/MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0 equals A
    def test_ext_i18n_MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0(self):
        self.assertIn('MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0', self.test_dict)
        test_data = self.test_dict['MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_0']
        self.assertEqual(test_data, 'A')

    # ext-i18n/microbit/MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1 equals B
    def test_ext_i18n_MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1(self):
        self.assertIn('MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1', self.test_dict)
        test_data = self.test_dict['MICROBIT_EVENT_BUTTON_PRESSED_BUTTON_1']
        self.assertEqual(test_data, 'B')
    
    # ext-i18n/microbit/MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS is right
    def MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS(self):
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_0"], "9")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_1"], "8")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_2"], "7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_3"], "6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_4"], "5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_5"], "4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_6"], "3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_7"], "2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_8"], "1")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_LED_MATRIX_LIGHT_POSITION_LIGHTNESS_9"], "0")




if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MicrobitTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)