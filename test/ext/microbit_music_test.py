
# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  microbit_music項目-翻译检查  =======================

class MicrobitMusicTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/microbit_music']

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




    # ext-i18n/microbit_music/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/microbit_music/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 78, "microbit_music 模块下存在新增或者删减的字段，需要修改测试用例！")

    # ext-i18n/microbit_music/microbit_show_play_sound contains [ICON] [PIN] [SOUND]
    def test_microbit_show_play_sound(self):
        key = 'microbit_show_play_sound'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_param(key, '[SOUND]')
        self.check_icon(key)

    # ext-i18n/microbit_music/microbit_show_play_sound_wait contains [ICON] [PIN] [SOUND]
    def test_microbit_show_play_sound_wait(self):
        key = 'microbit_show_play_sound_wait'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_param(key, '[SOUND]')
        self.check_icon(key)

    # ext-i18n/microbit_music/microbit_show_play_note_with_string contains [ICON] [PIN] [NOTE] [BEAT]
    def test_microbit_show_play_note_with_string(self):
        key = 'microbit_show_play_note_with_string'
        self.check_key_exists(key)
        self.check_param(key, '[PIN]')
        self.check_param(key, '[NOTE]')
        self.check_param(key, '[BEAT]')
        self.check_icon(key)

    # ext-i18n/microbit_music/microbit_show_change_tempo contains [ICON] [TEMPO]
    def test_microbit_show_change_tempo(self):
        key = 'microbit_show_change_tempo'
        self.check_key_exists(key)
        self.check_param(key, '[TEMPO]')
        self.check_icon(key)

    # ext-i18n/microbit_music/microbit_show_set_tempo contains [ICON] [TEMPO]
    def test_microbit_show_set_tempo(self):
        key = 'microbit_show_set_tempo'
        self.check_key_exists(key)
        self.check_param(key, '[TEMPO]')
        self.check_icon(key)

    # ext-i18n/microbit_music/microbit_detect_tempo_volume contains [ICON]
    def test_microbit_detect_tempo_volume(self):
        key = 'microbit_detect_tempo_volume'
        self.check_key_exists(key)
        self.check_icon(key)
  
    # ext-i18n/microbit_music/MICROBIT_SHOW_PLAY_SOUND_PIN is right
    def test_MICROBIT_SHOW_PLAY_SOUND_PIN(self):
        self.check_expect_value("MICROBIT_SHOW_PLAY_SOUND_PIN_0", "0")
        self.check_expect_value("MICROBIT_SHOW_PLAY_SOUND_PIN_1", "1")
        self.check_expect_value("MICROBIT_SHOW_PLAY_SOUND_PIN_2", "2")

    # ext-i18n/microbit_music/MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE is right
    def test_MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE(self):   
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_0", "C2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_1", "D2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_2", "E2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_3", "F2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_4", "G2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_5", "A2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_6", "B2")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_7", "C3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_8", "D3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_9", "E3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_10", "F3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_11", "G3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_12", "A3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_13", "B3")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_14", "C4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_15", "D4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_16", "E4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_17", "F4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_18", "G4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_19", "A4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_20", "B4")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_21", "C5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_22", "D5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_23", "E5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_24", "F5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_25", "G5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_26", "A5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_27", "B5")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_28", "C6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_29", "D6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_30", "E6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_31", "F6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_32", "G6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_33", "A6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_34", "B6")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_35", "C7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_36", "D7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_37", "E7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_38", "F7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_39", "G7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_40", "A7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_41", "B7")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_42", "C8")
        self.check_expect_value("MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_43", "D8")






if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MicrobitMusicTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)