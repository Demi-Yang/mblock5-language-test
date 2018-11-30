# coding:utf-8
# import requests
import json
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

    def check_key_exists(self, key, ):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0} \nvalue: {1} \n error: 值不等于 {2}, '.format(key, test_data, expect_value))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0} \nvalue:{1} \n缺少参数：{2}'.format(key, test_data, p))


    # ext-i18n/codeyneuron/No empty value
    def test_ext_i18n_codeyneuron_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/codeyneuron/No new or missing items
    def test_ext_i18n_codeyneuron_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 103, '\ncodeyneuron 模块下新增或删减了新的字段，测试用例需增减~')

    # mblock5-i18n/extensionName&codeyneuron equals Neuron
    def test_mblock5_i18n_extensionName_equals_Neuron(self):
        key1 = 'extensionName'
        key2 = 'codeyneuron'
        self.check_key_exists(key1)
        self.check_expect_value(key1, "Neuron")
        self.check_key_exists(key2)
        self.check_expect_value(key2, "Neuron")
        
    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_with_time contains [ICON] [ID] [PANEL] [TIME]
    def test_codey_neuron_set_ledpanel_with_time(self):
        key = 'codey_neuron_set_ledpanel_with_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[PANEL]', '[TIME]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_face contains [ICON] [ID] [PANEL] 
    def test_codey_neuron_set_ledpanel_face(self):
        key = 'codey_neuron_set_ledpanel_face'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[PANEL]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_text contains [ICON] [ID] [TEXT] 
    def test_codey_neuron_set_ledpanel_text(self):
        key = 'codey_neuron_set_ledpanel_text'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[TEXT]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_position_color contains [ICON] [ID] x: [X]  y: [Y] [COLOR] 
    def test_codey_neuron_set_ledpanel_position_color(self):
        key = 'codey_neuron_set_ledpanel_position_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', 'x: [X]  y: [Y]', '[COLOR]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledpanel_postion_rgb contains [ICON] [ID] x: [X]  y: [Y] [R][G][B] 
    def test_codey_neuron_set_ledpanel_postion_rgb(self):
        key = 'codey_neuron_set_ledpanel_postion_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', 'x: [X]  y: [Y]', '[R]', '[G]', '[B]'])

    # ext-i18n/codeyneuron/codey_neuron_turn_off_ledpanel_position contains [ICON] [ID] x: [X]  y: [Y]
    def test_codey_neuron_turn_off_ledpanel_position(self):
        key = 'codey_neuron_turn_off_ledpanel_position'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', 'x: [X]  y: [Y]'])

    # ext-i18n/codeyneuron/codey_neuron_turn_off_ledpanel contains [ICON] [ID]
    def test_codey_neuron_turn_off_ledpanel(self):
        key = 'codey_neuron_turn_off_ledpanel'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_mode contains [ICON] [ID] [STRIP]
    def test_codey_neuron_set_ledstrip_mode(self):
        key = 'codey_neuron_set_ledstrip_mode'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[STRIP]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_with_color contains [ICON] [ID] [POSITION] [COLORLIST]
    def test_codey_neuron_set_ledstrip_with_color(self):
        key = 'codey_neuron_set_ledstrip_with_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[POSITION]', '[COLORLIST]'])

    # ext-i18n/codeyneuron/codey_neuron_set_ledstrip_with_rgb contains [ICON] [ID] [POSITION] [R][G][B]
    def test_codey_neuron_set_ledstrip_with_rgb(self):
        key = 'codey_neuron_set_ledstrip_with_rgb'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[POSITION]', '[BEAT]', '[R]', '[G]', '[B]'])

    # ext-i18n/codeyneuron/codey_neuron_play_tone contains [ICON] [ID] [TONE] [BEAT]
    def test_codey_neuron_play_tone(self):
        key = 'codey_neuron_play_tone'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[TONE]', '[BEAT]'])

    # ext-i18n/codeyneuron/codey_neuron_play_hz contains [ICON] [ID] [HZ] [TIME]
    def test_codey_neuron_play_hz(self):
        key = 'codey_neuron_play_hz'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[HZ]', '[TIME]'])

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_with_speed_time contains [ICON] [ID] [SLOT] [[POWER] %] [TIME]
    def test_codey_neuron_run_dcmotor_with_speed_time(self):
        key = 'codey_neuron_run_dcmotor_with_speed_time'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[SLOT]', '[POWER] %', '[TIME]'])

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_with_speed contains [ICON] [ID] [SLOT] [[POWER] %]
    def test_codey_neuron_run_dcmotor_with_speed(self):
        key = 'codey_neuron_run_dcmotor_with_speed'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[SLOT]', '[POWER] %'])

    # ext-i18n/codeyneuron/codey_neuron_run_dcmotor_wheel contains [ICON] [ID] [SLOT] [[POWER] %]
    def test_codey_neuron_run_dcmotor_wheel(self):
        key = 'codey_neuron_run_dcmotor_wheel'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[POWER_RIGHT] %', '[POWER_LEFT] %'])

    # ext-i18n/codeyneuron/codey_neuron_run_servo contains [ICON] [ID] [SLOT] [ANGLE] 
    def test_codey_neuron_run_servo(self):
        key = 'codey_neuron_run_servo'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[SLOT]', '[ANGLE]'])

    # ext-i18n/codeyneuron/codey_neuron_event_touch_color contains [ICON] [ID] [COLOR] 
    def test_codey_neuron_event_touch_color(self):
        key = 'codey_neuron_event_touch_color'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[COLOR]'])

    # ext-i18n/codeyneuron/codey_neuron_detect_ultrasonic contains [ICON] [ID]
    def test_codey_neuron_detect_ultrasonic(self):
        key = 'codey_neuron_detect_ultrasonic'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/codey_neuron_event_tilt contains [ICON] [ID] [DIRECTION] 
    def test_codey_neuron_event_tilt(self):
        key = 'codey_neuron_event_tilt'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[DIRECTION]'])

    # ext-i18n/codeyneuron/codey_neuron_event_shaked contains [ICON] [ID]  
    def test_codey_neuron_event_shaked(self):
        key = 'codey_neuron_event_shaked'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/codey_neuron_detect_gyro_angle contains [ICON] [ID] [COORDINATE] 
    def test_codey_neuron_detect_gyro_angle(self):
        key = 'codey_neuron_detect_gyro_angle'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[COORDINATE]'])

    # ext-i18n/codeyneuron/codey_neuron_detect_gyro_speed contains [ICON] [ID] [COORDINATE] 
    def test_codey_neuron_detect_gyro_speed(self):
        key = 'codey_neuron_detect_gyro_speed'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]', '[COORDINATE]'])

    # ext-i18n/codeyneuron/codey_neuron_event_pir contains [ICON] [ID]  
    def test_codey_neuron_event_pir(self):
        key = 'codey_neuron_event_pir'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/codey_neuron_detect_humidity contains [ICON] [ID]  
    def test_codey_neuron_detect_humidity(self):
        key = 'codey_neuron_detect_humidity'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/codey_neuron_button contains [ICON] [ID]  
    def test_codey_neuron_button(self):
        key = 'codey_neuron_button'
        self.check_key_exists(key)
        self.check_icon(key)
        self.check_params(key, ['[ID]'])

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0 contains x
    def test_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0(self):
        key = 'CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_0'
        self.check_key_exists(key)
        self.check_params(key, ['x'])

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1 contains y
    def test_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1(self):
        key = 'CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_1'
        self.check_key_exists(key)
        self.check_params(key, ['y'])

    # ext-i18n/codeyneuron/CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2 contains z
    def test_CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2(self):
        key = 'CODEY_NEURON_DETECT_GYRO_SPEED_COORDINATE_2'
        self.check_key_exists(key)
        self.check_params(key, ['z'])

    # ext-i18n/codeyneuron/CODEY_NEURON_PLAY_TONE_TONE is right
    def test_CODEY_NEURON_PLAY_TONE_TONE(self):
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_0', "C7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_1', "C2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_2', "D2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_3', "E2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_4', "F2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_5', "G2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_6', "A2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_7', "B2")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_8', "C3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_9', "D3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_10', "E3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_11', "F3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_12', "G3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_13', "A3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_14', "B3")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_15', "C4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_16', "D4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_17', "E4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_18', "F4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_19', "G4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_20', "A4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_21', "B4")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_22', "C5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_23', "D5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_24', "E5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_25', "F5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_26', "G5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_27', "A5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_28', "B5")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_29', "C6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_30', "D6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_31', "E6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_32', "F6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_33', "G6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_34', "A6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_35', "B6")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_36', "D7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_37', "E7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_38', "F7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_39', "G7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_40', "A7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_41', "B7")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_42', "C8")
        self.check_expect_value('CODEY_NEURON_PLAY_TONE_TONE_43', "D8")



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyNeuronTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)