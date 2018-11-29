# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mscratch項目-翻译检查  =======================

class ExtensionsMusicTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mscratch-i18n']['extensions']['music']

    def check_key_exists(self, key, ):
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




    # mscratch-i18n/extensions/music/No empty value
    def test_extensions_music_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "该字段的翻译为空，错误 key: " + key)
            self.assertNotEqual(value, '', "该字段的翻译为空，错误 key: " + key)

    # mscratch-i18n/extensions/music/No new or missing items
    def test_extensions_music_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 47, "mscratch-i18n/extensions/music 模块下新增或删减了翻译字段")

    # mscratch-i18n/extensions/music/music.playDrumForBeats contains [DRUM] [BEATS]
    def test_extensions_music_playDrumForBeats(self):
        key = 'music.playDrumForBeats'
        self.check_key_exists(key)
        self.check_param(key, '[DRUM]')
        self.check_param(key, '[BEATS]')

    # mscratch-i18n/extensions/music/music.playNoteForBeats contains [BEATS]
    def test_extensions_music_playNoteForBeats(self):
        key = 'music.playNoteForBeats'
        self.check_key_exists(key)
        self.check_param(key, '[BEATS]')

    # mscratch-i18n/extensions/music/music.setInstrument contains [INSTRUMENT]
    def test_extensions_music_setInstrument(self):
        key = 'music.setInstrument'
        self.check_key_exists(key)
        self.check_param(key, '[INSTRUMENT]')

    # mscratch-i18n/extensions/music/music.setTempo contains [DRUM] [TEMPO]
    def test_extensions_music_setTempo(self):
        key = 'music.setTempo'
        self.check_key_exists(key)
        self.check_param(key, '[TEMPO]')

    # mscratch-i18n/extensions/music/music.changeTempo contains [DRUM] [TEMPO]
    def test_extensions_music_changeTempo(self):
        key = 'music.changeTempo'
        self.check_key_exists(key)
        self.check_param(key, '[TEMPO]')

if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ExtensionsMusicTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
