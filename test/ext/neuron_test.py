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

    # ext-i18n/neuron/No empty value
    def test_ext_i18n_neuron_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mblock5-i18n/neuron/extensionName&neuron equals Neuron
    def test_mblock5_i18n_extensionName_equals_neuron(self):
        self.assertIn('extensionName', self.test_dict)
        self.assertIn('neuron', self.test_dict)
        self.assertEqual(self.test_dict['extensionName'], "Neuron")
        self.assertEqual(self.test_dict['neuron'], "Neuron")

    # ext-i18n/neuron/neuron_run_dcmotor_with_time contains [ICON]、[ID]、[SLOT]、[POWER] %、[TIME]
    def test_ext_i18n_neuron_run_dcmotor_with_time(self):
        self.assertIn('neuron_run_dcmotor_with_time', self.test_dict)
        test_data = self.test_dict['neuron_run_dcmotor_with_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_run_dcmotor_with_speed contains [ICON]、[ID]、[SLOT]、[POWER] %
    def test_ext_i18n_neuron_run_dcmotor_with_speed(self):
        self.assertIn('neuron_run_dcmotor_with_speed', self.test_dict)
        test_data = self.test_dict['neuron_run_dcmotor_with_speed']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_run_dcmotors contains [ICON]、[ID]、[POWER_LEFT] %、[POWER_RIGHT] %
    def test_ext_i18n_neuron_run_dcmotors(self):
        self.assertIn('neuron_run_dcmotors', self.test_dict)
        test_data = self.test_dict['neuron_run_dcmotors']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POWER_LEFT] %', test_data)
        self.assertIn('[POWER_RIGHT] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_run_servo contains [ICON]、[ID]、[SLOT]、[ANGLE]
    def test_ext_i18n_neuron_run_servo(self):
        self.assertIn('neuron_run_servo', self.test_dict)
        test_data = self.test_dict['neuron_run_servo']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ANGLE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_led_with_time contains [ICON]、[ID]、[COLOR]、[TIME]
    def test_ext_i18n_neuron_set_led_with_time(self):
        self.assertIn('neuron_set_led_with_time', self.test_dict)
        test_data = self.test_dict['neuron_set_led_with_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_led contains [ICON]、[ID]、[COLOR]
    def test_ext_i18n_neuron_set_led(self):
        self.assertIn('neuron_set_led', self.test_dict)
        test_data = self.test_dict['neuron_set_led']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_led_with_rgb contains [ICON]、[ID]、[R]、[G]、[B]
    def test_ext_i18n_neuron_set_led_with_rgb(self):
        self.assertIn('neuron_set_led_with_rgb', self.test_dict)
        test_data = self.test_dict['neuron_set_led_with_rgb']
        self.assertIn('[ID]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_turn_off_led contains [ICON]
    def test_ext_i18n_neuron_turn_off_led(self):
        self.assertIn('neuron_turn_off_led', self.test_dict)
        test_data = self.test_dict['neuron_turn_off_led']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledstrip_mode contains [ICON]、[ID]、[STRIP]
    def test_ext_i18n_neuron_set_ledstrip_mode(self):
        self.assertIn('neuron_set_ledstrip_mode', self.test_dict)
        test_data = self.test_dict['neuron_set_ledstrip_mode']
        self.assertIn('[ID]', test_data)
        self.assertIn('[STRIP]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledstrip_with_rgb contains [ICON]、[ID]、[POSITION]、[R]、[G]、[B]
    def test_ext_i18n_neuron_set_ledstrip_with_rgb(self):
        self.assertIn('neuron_set_ledstrip_with_rgb', self.test_dict)
        test_data = self.test_dict['neuron_set_ledstrip_with_rgb']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POSITION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledstrip_with_color contains [ICON]、[ID]、[POSITION]、[COLOR]
    def test_ext_i18n_neuron_set_ledstrip_with_color(self):
        self.assertIn('neuron_set_ledstrip_with_color', self.test_dict)
        test_data = self.test_dict['neuron_set_ledstrip_with_color']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POSITION]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_turn_off_ledstrip contains [ICON]
    def test_ext_i18n_neuron_turn_off_ledstrip(self):
        self.assertIn('neuron_turn_off_ledstrip', self.test_dict)
        test_data = self.test_dict['neuron_turn_off_ledstrip']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledpanel_with_time contains [ICON]、[ID]、[PANEL]、[TIME]
    def test_ext_i18n_neuron_set_ledpanel_with_time(self):
        self.assertIn('neuron_set_ledpanel_with_time', self.test_dict)
        test_data = self.test_dict['neuron_set_ledpanel_with_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledpanel_face contains [ICON]、[ID]、[PANEL]
    def test_ext_i18n_neuron_set_ledpanel_face(self):
        self.assertIn('neuron_set_ledpanel_face', self.test_dict)
        test_data = self.test_dict['neuron_set_ledpanel_face']
        self.assertIn('[ID]', test_data)
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledpanel_postion contains [ICON]、[ID]、[COLOR]、x: [X] y: [Y]
    def test_ext_i18n_neuron_set_ledpanel_postion(self):
        self.assertIn('neuron_set_ledpanel_postion', self.test_dict)
        test_data = self.test_dict['neuron_set_ledpanel_postion']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_set_ledpanel_postion_rgb contains [ICON]、[ID]、[R]、[G]、[B]、x: [X] y: [Y]
    def test_ext_i18n_neuron_set_ledpanel_postion_rgb(self):
        self.assertIn('neuron_set_ledpanel_postion_rgb', self.test_dict)
        test_data = self.test_dict['neuron_set_ledpanel_postion_rgb']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_turn_off_ledpanel_postion contains [ICON]、[ID]、x: [X] y: [Y]
    def test_ext_i18n_neuron_turn_off_ledpanel_postion(self):
        self.assertIn('neuron_turn_off_ledpanel_postion', self.test_dict)
        test_data = self.test_dict['neuron_turn_off_ledpanel_postion']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]', test_data)
        self.assertIn('y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_turn_off_ledpanel contains [ICON]
    def test_ext_i18n_neuron_turn_off_ledpanel(self):
        self.assertIn('neuron_turn_off_ledpanel', self.test_dict)
        test_data = self.test_dict['neuron_turn_off_ledpanel']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_display_emotion contains [ICON]、[ID]、[EMOTION]
    def test_ext_i18n_neuron_display_emotion(self):
        self.assertIn('neuron_display_emotion', self.test_dict)
        test_data = self.test_dict['neuron_display_emotion']
        self.assertIn('[ID]', test_data)
        self.assertIn('[EMOTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_display_emotion_with_time contains [ICON]、[ID]、[EMOTION]、[DURATION]
    def test_ext_i18n_neuron_display_emotion_with_time(self):
        self.assertIn('neuron_display_emotion_with_time', self.test_dict)
        test_data = self.test_dict['neuron_display_emotion_with_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[EMOTION]', test_data)
        self.assertIn('[DURATION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_display_icon contains [ICON]、[ID]、[ICON_ID]、[STRING]
    def test_ext_i18n_neuron_display_icon(self):
        self.assertIn('neuron_display_icon', self.test_dict)
        test_data = self.test_dict['neuron_display_icon']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON_ID]', test_data)
        self.assertIn('[STRING]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_display_icon_with_pos contains [ICON]、[ID]、[ICON_ID_1]、[STRING_1]、[ICON_ID_2]、[STRING_2]
    def test_ext_i18n_neuron_display_icon_with_pos(self):
        self.assertIn('neuron_display_icon_with_pos', self.test_dict)
        test_data = self.test_dict['neuron_display_icon_with_pos']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON_ID_1]', test_data)
        self.assertIn('[STRING_1]', test_data)
        self.assertIn('[ICON_ID_2]', test_data)
        self.assertIn('[STRING_2]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_light_on_el_wiredriver contains [ICON]、[ID]、[SLOT]
    def test_ext_i18n_neuron_light_on_el_wiredriver(self):
        self.assertIn('neuron_light_on_el_wiredriver', self.test_dict)
        test_data = self.test_dict['neuron_light_on_el_wiredriver']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_light_off_el_wiredriver contains [ICON]、[ID]、[SLOT]
    def test_ext_i18n_neuron_light_off_el_wiredriver(self):
        self.assertIn('neuron_light_off_el_wiredriver', self.test_dict)
        test_data = self.test_dict['neuron_light_off_el_wiredriver']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_play_tone contains [ICON]、[ID]、[TONE]、[BEAT]
    def test_ext_i18n_neuron_play_tone(self):
        self.assertIn('neuron_play_tone', self.test_dict)
        test_data = self.test_dict['neuron_play_tone']
        self.assertIn('[ID]', test_data)
        self.assertIn('[TONE]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_play_hz contains [ICON]、[ID]、[HZ]、[TIME]
    def test_ext_i18n_neuron_play_hz(self):
        self.assertIn('neuron_play_hz', self.test_dict)
        test_data = self.test_dict['neuron_play_hz']
        self.assertIn('[ID]', test_data)
        self.assertIn('[HZ]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_button_pressed contains [ICON]、[ID]
    def test_ext_i18n_neuron_event_button_pressed(self):
        self.assertIn('neuron_event_button_pressed', self.test_dict)
        test_data = self.test_dict['neuron_event_button_pressed']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_knob contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_knob(self):
        self.assertIn('neuron_detect_knob', self.test_dict)
        test_data = self.test_dict['neuron_detect_knob']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_temperature contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_temperature(self):
        self.assertIn('neuron_detect_temperature', self.test_dict)
        test_data = self.test_dict['neuron_detect_temperature']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_linefollow contains [ICON]、[ID]、[AXIS]
    def test_ext_i18n_neuron_event_linefollow(self):
        self.assertIn('neuron_event_linefollow', self.test_dict)
        test_data = self.test_dict['neuron_event_linefollow']
        self.assertIn('[ID]', test_data)
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_lightness contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_lightness(self):
        self.assertIn('neuron_detect_lightness', self.test_dict)
        test_data = self.test_dict['neuron_detect_lightness']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_touch_color contains [ICON]、[ID]、[COLOR]
    def test_ext_i18n_neuron_event_touch_color(self):
        self.assertIn('neuron_event_touch_color', self.test_dict)
        test_data = self.test_dict['neuron_event_touch_color']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_volume contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_volume(self):
        self.assertIn('neuron_detect_volume', self.test_dict)
        test_data = self.test_dict['neuron_detect_volume']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_ultrasonic contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_ultrasonic(self):
        self.assertIn('neuron_detect_ultrasonic', self.test_dict)
        test_data = self.test_dict['neuron_detect_ultrasonic']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_tilt contains [ICON]、[ID]、[DIRECTION]
    def test_ext_i18n_neuron_event_tilt(self):
        self.assertIn('neuron_event_tilt', self.test_dict)
        test_data = self.test_dict['neuron_event_tilt']
        self.assertIn('[ID]', test_data)
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_shaked contains [ICON]、[ID]
    def test_ext_i18n_neuron_event_shaked(self):
        self.assertIn('neuron_event_shaked', self.test_dict)
        test_data = self.test_dict['neuron_event_shaked']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_gyro_angle contains [ICON]、[ID]、[COORDINATE]
    def test_ext_i18n_neuron_detect_gyro_angle(self):
        self.assertIn('neuron_detect_gyro_angle', self.test_dict)
        test_data = self.test_dict['neuron_detect_gyro_angle']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COORDINATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_gyro_speed contains [ICON]、[ID]、[COORDINATE]
    def test_ext_i18n_neuron_detect_gyro_speed(self):
        self.assertIn('neuron_detect_gyro_speed', self.test_dict)
        test_data = self.test_dict['neuron_detect_gyro_speed']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COORDINATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_color_sensor contains [ICON]、[ID]、[COLOR]
    def test_ext_i18n_neuron_detect_color_sensor(self):
        self.assertIn('neuron_detect_color_sensor', self.test_dict)
        test_data = self.test_dict['neuron_detect_color_sensor']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_josystick_direction contains [ICON]、[ID]、[DIRECTION]
    def test_ext_i18n_neuron_event_josystick_direction(self):
        self.assertIn('neuron_event_josystick_direction', self.test_dict)
        test_data = self.test_dict['neuron_event_josystick_direction']
        self.assertIn('[ID]', test_data)
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_joystick contains [ICON]、[ID]、[AXIS]
    def test_ext_i18n_neuron_detect_joystick(self):
        self.assertIn('neuron_detect_joystick', self.test_dict)
        test_data = self.test_dict['neuron_detect_joystick']
        self.assertIn('[ID]', test_data)
        self.assertIn('[AXIS]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_event_pir contains [ICON]、[ID]
    def test_ext_i18n_neuron_event_pir(self):
        self.assertIn('neuron_event_pir', self.test_dict)
        test_data = self.test_dict['neuron_event_pir']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/neuron_detect_humidity contains [ICON]、[ID]
    def test_ext_i18n_neuron_detect_humidity(self):
        self.assertIn('neuron_detect_humidity', self.test_dict)
        test_data = self.test_dict['neuron_detect_humidity']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/op_ranging contains [ICON]、[ID]
    def test_ext_i18n_op_ranging(self):
        self.assertIn('op_ranging', self.test_dict)
        test_data = self.test_dict['op_ranging']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/op_temperature contains [ICON]、[ID]
    def test_ext_i18n_op_temperature(self):
        self.assertIn('op_temperature', self.test_dict)
        test_data = self.test_dict['op_temperature']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/op_htemperature contains [ICON]、[ID]
    def test_ext_i18n_op_htemperature(self):
        self.assertIn('op_htemperature', self.test_dict)
        test_data = self.test_dict['op_htemperature']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/op_humidity contains [ICON]、[ID]
    def test_ext_i18n_op_humidity(self):
        self.assertIn('op_humidity', self.test_dict)
        test_data = self.test_dict['op_humidity']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/neuron/NEURON_DETECT_JOYSTICK_AXIS is right
    def test_ext_i18n_NEURON_DETECT_JOYSTICK_AXIS(self):
        self.assertEqual(self.test_dict['NEURON_DETECT_JOYSTICK_AXIS_0'], 'x')
        self.assertEqual(self.test_dict['NEURON_DETECT_JOYSTICK_AXIS_1'], 'y')

    # ext-i18n/neuron/NEURON_DETECT_GYRO_SPEED_COORDINATE is right
    def test_ext_i18n_NEURON_DETECT_GYRO_SPEED_COORDINATE(self):
        self.assertEqual(self.test_dict['NEURON_DETECT_GYRO_SPEED_COORDINATE_0'], 'x')
        self.assertEqual(self.test_dict['NEURON_DETECT_GYRO_SPEED_COORDINATE_1'], 'y')
        self.assertEqual(self.test_dict['NEURON_DETECT_GYRO_SPEED_COORDINATE_2'], 'z')

    # ext-i18n/neuron/NEURON_PLAY_TONE_TONE is right
    def test_ext_i18n_NEURON_PLAY_TONE_TONE(self):
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_0"], "C7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_1"], "C2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_2"], "D2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_3"], "E2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_4"], "F2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_5"], "G2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_6"], "A2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_7"], "B2")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_8"], "C3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_9"], "D3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_10"], "E3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_11"], "F3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_12"], "F3m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_13"], "G3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_14"], "G3m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_15"], "A3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_16"], "A3m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_17"], "B3")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_18"], "C4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_19"], "C4m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_20"], "D4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_21"], "D4m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_22"], "E4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_23"], "F4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_24"], "F4m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_25"], "G4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_26"], "G4m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_27"], "A4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_28"], "A4m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_29"], "B4")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_30"], "C5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_31"], "C5m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_32"], "D5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_33"], "D5m")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_34"], "E5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_35"], "F5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_36"], "G5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_37"], "A5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_38"], "B5")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_39"], "C6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_40"], "D6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_41"], "E6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_42"], "F6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_43"], "G6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_44"], "A6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_45"], "B6")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_46"], "D7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_47"], "E7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_48"], "F7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_49"], "G7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_50"], "A7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_51"], "B7")
        self.assertEqual(self.test_dict["NEURON_PLAY_TONE_TONE_52"], "C8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(NeuronTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
























