# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  codeyneuron項目-翻译检查  =======================

class CodeyNeuronTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/codeyneuron']

    # ext-i18n/codeyneuron/No empty value
    def test_ext_i18n_codeyneuron_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/codeyneuron/No new or missing items
    def test_ext_i18n_codeyneuron_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 103)

    # mblock5-i18n/extensionName&codeyneuron equals Neuron
    def test_mblock5_i18n_extensionName_equals_Neuron(self):
        self.assertIn('extensionName', self.test_dict)
        self.assertIn('codeyneuron', self.test_dict)
        self.assertEqual(self.test_dict['extensionName'], "Neuron")
        self.assertEqual(self.test_dict['codeyneuron'], "Neuron")

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_with_time contains [ICON] [ID] [PANEL] [TIME]
    def test_ext_i18n_codey_neuron_set_ledpanel_with_time(self):
        self.assertIn('codey_neuron_set_ledpanel_with_time', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledpanel_with_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_face contains [ICON] [ID] [PANEL] 
    def test_ext_i18n_codey_neuron_set_ledpanel_face(self):
        self.assertIn('codey_neuron_set_ledpanel_face', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledpanel_face']
        self.assertIn('[ID]', test_data)
        self.assertIn('[PANEL]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_text contains [ICON] [ID] [TEXT] 
    def test_ext_i18n_codey_neuron_set_ledpanel_text(self):
        self.assertIn('codey_neuron_set_ledpanel_text', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledpanel_text']
        self.assertIn('[ID]', test_data)
        self.assertIn('[TEXT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_position_color contains [ICON] [ID] x: [X]  y: [Y] [COLOR] 
    def test_ext_i18n_codey_neuron_set_ledpanel_position_color(self):
        self.assertIn('codey_neuron_set_ledpanel_position_color', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledpanel_position_color']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]  y: [Y]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_postion_rgb contains [ICON] [ID] x: [X]  y: [Y] [R][G][B] 
    def test_ext_i18n_codey_neuron_set_ledpanel_postion_rgb(self):
        self.assertIn('codey_neuron_set_ledpanel_postion_rgb', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledpanel_postion_rgb']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]  y: [Y]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_turn_off_ledpanel_position contains [ICON] [ID] x: [X]  y: [Y]
    def test_ext_i18n_codey_neuron_turn_off_ledpanel_position(self):
        self.assertIn('codey_neuron_turn_off_ledpanel_position', self.test_dict)
        test_data = self.test_dict['codey_neuron_turn_off_ledpanel_position']
        self.assertIn('[ID]', test_data)
        self.assertIn('x: [X]  y: [Y]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_turn_off_ledpanel contains [ICON] [ID]
    def test_ext_i18n_codey_neuron_turn_off_ledpanel(self):
        self.assertIn('codey_neuron_turn_off_ledpanel', self.test_dict)
        test_data = self.test_dict['codey_neuron_turn_off_ledpanel']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_mode contains [ICON] [ID] [STRIP]
    def test_ext_i18n_codey_neuron_set_ledstrip_mode(self):
        self.assertIn('codey_neuron_set_ledstrip_mode', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledstrip_mode']
        self.assertIn('[ID]', test_data)
        self.assertIn('[STRIP]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_with_color contains [ICON] [ID] [POSITION] [COLORLIST]
    def test_ext_i18n_codey_neuron_set_ledstrip_with_color(self):
        self.assertIn('codey_neuron_set_ledstrip_with_color', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledstrip_with_color']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POSITION]', test_data)
        self.assertIn('[COLORLIST]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_with_rgb contains [ICON] [ID] [POSITION] [R][G][B]
    def test_ext_i18n_codey_neuron_set_ledstrip_with_rgb(self):
        self.assertIn('codey_neuron_set_ledstrip_with_rgb', self.test_dict)
        test_data = self.test_dict['codey_neuron_set_ledstrip_with_rgb']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POSITION]', test_data)
        self.assertIn('[R]', test_data)
        self.assertIn('[G]', test_data)
        self.assertIn('[B]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_play_tone contains [ICON] [ID] [TONE] [BEAT]
    def test_ext_i18n_codey_neuron_play_tone(self):
        self.assertIn('codey_neuron_play_tone', self.test_dict)
        test_data = self.test_dict['codey_neuron_play_tone']
        self.assertIn('[ID]', test_data)
        self.assertIn('[TONE]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_play_hz contains [ICON] [ID] [HZ] [TIME]
    def test_ext_i18n_codey_neuron_play_hz(self):
        self.assertIn('codey_neuron_play_hz', self.test_dict)
        test_data = self.test_dict['codey_neuron_play_hz']
        self.assertIn('[ID]', test_data)
        self.assertIn('[HZ]', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_with_speed_time contains [ICON] [ID] [SLOT] [[POWER] %] [TIME]
    def test_ext_i18n_codey_neuron_run_dcmotor_with_speed_time(self):
        self.assertIn('codey_neuron_run_dcmotor_with_speed_time', self.test_dict)
        test_data = self.test_dict['codey_neuron_run_dcmotor_with_speed_time']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[TIME]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_with_speed contains [ICON] [ID] [SLOT] [[POWER] %]
    def test_ext_i18n_codey_neuron_run_dcmotor_with_speed(self):
        self.assertIn('codey_neuron_run_dcmotor_with_speed', self.test_dict)
        test_data = self.test_dict['codey_neuron_run_dcmotor_with_speed']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[POWER] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_wheel contains [ICON] [ID] [SLOT] [[POWER] %]
    def test_ext_i18n_codey_neuron_run_dcmotor_wheel(self):
        self.assertIn('codey_neuron_run_dcmotor_wheel', self.test_dict)
        test_data = self.test_dict['codey_neuron_run_dcmotor_wheel']
        self.assertIn('[ID]', test_data)
        self.assertIn('[POWER_RIGHT] %', test_data)
        self.assertIn('[POWER_LEFT] %', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_run_servo contains [ICON] [ID] [SLOT] [ANGLE] 
    def test_ext_i18n_codey_neuron_run_servo(self):
        self.assertIn('codey_neuron_run_servo', self.test_dict)
        test_data = self.test_dict['codey_neuron_run_servo']
        self.assertIn('[ID]', test_data)
        self.assertIn('[SLOT]', test_data)
        self.assertIn('[ANGLE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_event_touch_color contains [ICON] [ID] [COLOR] 
    def test_ext_i18n_codey_neuron_event_touch_color(self):
        self.assertIn('codey_neuron_event_touch_color', self.test_dict)
        test_data = self.test_dict['codey_neuron_event_touch_color']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COLOR]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_detect_ultrasonic contains [ICON] [ID]
    def test_ext_i18n_codey_neuron_detect_ultrasonic(self):
        self.assertIn('codey_neuron_detect_ultrasonic', self.test_dict)
        test_data = self.test_dict['codey_neuron_detect_ultrasonic']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_event_tilt contains [ICON] [ID] [DIRECTION] 
    def test_ext_i18n_codey_neuron_event_tilt(self):
        self.assertIn('codey_neuron_event_tilt', self.test_dict)
        test_data = self.test_dict['codey_neuron_event_tilt']
        self.assertIn('[ID]', test_data)
        self.assertIn('[DIRECTION]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_event_shaked contains [ICON] [ID]  
    def test_ext_i18n_codey_neuron_event_shaked(self):
        self.assertIn('codey_neuron_event_shaked', self.test_dict)
        test_data = self.test_dict['codey_neuron_event_shaked']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_detect_gyro_angle contains [ICON] [ID] [COORDINATE] 
    def test_ext_i18n_codey_neuron_detect_gyro_angle(self):
        self.assertIn('codey_neuron_detect_gyro_angle', self.test_dict)
        test_data = self.test_dict['codey_neuron_detect_gyro_angle']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COORDINATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_detect_gyro_speed contains [ICON] [ID] [COORDINATE] 
    def test_ext_i18n_codey_neuron_detect_gyro_speed(self):
        self.assertIn('codey_neuron_detect_gyro_speed', self.test_dict)
        test_data = self.test_dict['codey_neuron_detect_gyro_speed']
        self.assertIn('[ID]', test_data)
        self.assertIn('[COORDINATE]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_event_pir contains [ICON] [ID]  
    def test_ext_i18n_codey_neuron_event_pir(self):
        self.assertIn('codey_neuron_event_pir', self.test_dict)
        test_data = self.test_dict['codey_neuron_event_pir']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_detect_humidity contains [ICON] [ID]  
    def test_ext_i18n_codey_neuron_detect_humidity(self):
        self.assertIn('codey_neuron_detect_humidity', self.test_dict)
        test_data = self.test_dict['codey_neuron_detect_humidity']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/codey_neuron_button contains [ICON] [ID]  
    def test_ext_i18n_codey_neuron_button(self):
        self.assertIn('codey_neuron_button', self.test_dict)
        test_data = self.test_dict['codey_neuron_button']
        self.assertIn('[ID]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0 contains x
    def test_ext_i18n_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0(self):
        self.assertIn('CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0', self.test_dict)
        test_data = self.test_dict['CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0']
        self.assertIn('x', test_data)

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1 contains y
    def test_ext_i18n_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1(self):
        self.assertIn('CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1', self.test_dict)
        test_data = self.test_dict['CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1']
        self.assertIn('y', test_data)

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2 contains z
    def test_ext_i18n_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2(self):
        self.assertIn('CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2', self.test_dict)
        test_data = self.test_dict['CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2']
        self.assertIn('z', test_data)

    # ext-i18n/codeyneuron/CODEY_NEURON_PLAY_TONE_TONE is right
    def test_ext_i18n_CODEY_NEURON_PLAY_TONE_TONE(self):
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_0'], "C7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_1'], "C2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_2'], "D2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_3'], "E2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_4'], "F2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_5'], "G2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_6'], "A2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_7'], "B2")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_8'], "C3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_9'], "D3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_10'], "E3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_11'], "F3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_12'], "G3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_13'], "A3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_14'], "B3")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_15'], "C4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_16'], "D4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_17'], "E4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_18'], "F4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_19'], "G4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_20'], "A4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_21'], "B4")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_22'], "C5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_23'], "D5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_24'], "E5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_25'], "F5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_26'], "G5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_27'], "A5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_28'], "B5")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_29'], "C6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_30'], "D6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_31'], "E6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_32'], "F6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_33'], "G6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_34'], "A6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_35'], "B6")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_36'], "D7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_37'], "E7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_38'], "F7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_39'], "G7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_40'], "A7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_41'], "B7")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_42'], "C8")
        self.assertEqual(self.test_dict['CODEY_NEURON_PLAY_TONE_TONE_43'], "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyNeuronTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)