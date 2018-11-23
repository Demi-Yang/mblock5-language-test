
# coding:utf-8
# import requests
import json
import re
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

    # ext-i18n/microbit_music/No empty value
    def test_ext_i18n_microbit_music_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/microbit_music/No new or missing items
    def test_ext_i18n_microbit_music_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 78)

    # ext-i18n/microbit_music/microbit_show_play_sound contains [ICON] [PIN] [SOUND]
    def test_ext_i18n_microbit_show_play_sound(self):
        self.assertIn('microbit_show_play_sound', self.test_dict)
        test_data = self.test_dict['microbit_show_play_sound']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[SOUND]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit_music/microbit_show_play_sound_wait contains [ICON] [PIN] [SOUND]
    def test_ext_i18n_microbit_show_play_sound_wait(self):
        self.assertIn('microbit_show_play_sound_wait', self.test_dict)
        test_data = self.test_dict['microbit_show_play_sound_wait']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[SOUND]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit_music/microbit_show_play_note_with_string contains [ICON] [PIN] [NOTE] [BEAT]
    def test_ext_i18n_microbit_show_play_note_with_string(self):
        self.assertIn('microbit_show_play_note_with_string', self.test_dict)
        test_data = self.test_dict['microbit_show_play_note_with_string']
        self.assertIn('[PIN]', test_data)
        self.assertIn('[NOTE]', test_data)
        self.assertIn('[BEAT]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit_music/microbit_show_change_tempo contains [ICON] [TEMPO]
    def test_ext_i18n_microbit_show_change_tempo(self):
        self.assertIn('microbit_show_change_tempo', self.test_dict)
        test_data = self.test_dict['microbit_show_change_tempo']
        self.assertIn('[TEMPO]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit_music/microbit_show_set_tempo contains [ICON] [TEMPO]
    def test_ext_i18n_microbit_show_set_tempo(self):
        self.assertIn('microbit_show_set_tempo', self.test_dict)
        test_data = self.test_dict['microbit_show_set_tempo']
        self.assertIn('[TEMPO]', test_data)
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/microbit_music/microbit_detect_tempo_volume contains [ICON]
    def test_ext_i18n_microbit_detect_tempo_volume(self):
        self.assertIn('microbit_detect_tempo_volume', self.test_dict)
        test_data = self.test_dict['microbit_detect_tempo_volume']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
  
    # ext-i18n/microbit_music/MICROBIT_SHOW_PLAY_SOUND_PIN is right
    def test_ext_i18n_MICROBIT_SHOW_PLAY_SOUND_PIN(self):
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_SOUND_PIN_0"], "0")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_SOUND_PIN_1"], "1")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_SOUND_PIN_2"], "2")

    # ext-i18n/microbit_music/MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE is right
    def test_ext_i18n_MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE(self):   
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_0"], "C2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_1"], "D2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_2"], "E2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_3"], "F2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_4"], "G2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_5"], "A2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_6"], "B2")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_7"], "C3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_8"], "D3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_9"], "E3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_10"], "F3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_11"], "G3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_12"], "A3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_13"], "B3")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_14"], "C4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_15"], "D4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_16"], "E4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_17"], "F4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_18"], "G4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_19"], "A4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_20"], "B4")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_21"], "C5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_22"], "D5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_23"], "E5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_24"], "F5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_25"], "G5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_26"], "A5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_27"], "B5")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_28"], "C6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_29"], "D6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_30"], "E6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_31"], "F6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_32"], "G6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_33"], "A6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_34"], "B6")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_35"], "C7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_36"], "D7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_37"], "E7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_38"], "F7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_39"], "G7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_40"], "A7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_41"], "B7")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_42"], "C8")
        self.assertEqual(self.test_dict["MICROBIT_SHOW_PLAY_NOTE_WITH_STRING_NOTE_43"], "D8")






if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MicrobitMusicTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)