# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  codey_emotion項目-翻译检查  =======================

class CodeyEmotionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/codey_emotion']

    def check_icon(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0}, 缺少参数：[ICON]'.format(key))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0}, error:参数[ICON]必须在首位'.format(key))

    # ext-i18n/codey_emotion/No empty value
    def test_tm_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "缺少翻译的字段：" + key)

    # ext-i18n/codey_emotion/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 29, 'codey_emotion 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/codey_emotion/codey_emotion_look_up contains [ICON]
    def test_look_up(self):
        key = 'codey_emotion_look_up' 
        self.check_icon(key)
        
    # ext-i18n/codey_emotion/codey_emotion_look_down contains [ICON]
    def test_look_down(self):
        key = 'codey_emotion_look_down' 
        self.check_icon(key)
  
    # ext-i18n/codey_emotion/codey_emotion_look_left contains [ICON]
    def test_look_left(self):
        key = 'codey_emotion_look_left' 
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_look_right contains [ICON]
    def test_look_right(self):
        key = 'codey_emotion_look_right' 
        self.check_icon(key)
  
    # ext-i18n/codey_emotion/codey_emotion_look_around contains [ICON]
    def test_look_around(self):
        key = 'codey_emotion_look_around' 
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_smile contains [ICON]
    def test_smile(self):
        key = 'codey_emotion_smile'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_yeah contains [ICON]
    def test_yeah(self):
        key = 'codey_emotion_yeah'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_naughty contains [ICON]
    def test_naughty(self):
        key = 'codey_emotion_naughty'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_greeting contains [ICON]
    def test_greeting(self):
        key = 'codey_emotion_greeting'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_proud contains [ICON]
    def test_proud(self):
        key = 'codey_emotion_proud'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_coquetry contains [ICON]
    def test_coquetry(self):
        key = 'codey_emotion_coquetry'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_awkward contains [ICON]
    def test_awkward(self):
        key = 'codey_emotion_awkward'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_exclaim contains [ICON]
    def test_exclaim(self):
        key = 'codey_emotion_exclaim'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_aggrieved contains [ICON]
    def test_aggrieved(self):
        key = 'codey_emotion_aggrieved'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_sad contains [ICON]
    def test_sad(self):
        key = 'codey_emotion_sad'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_angry contains [ICON]
    def test_angry(self):
        key = 'codey_emotion_angry'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_sprint contains [ICON]
    def test_sprint(self):
        key = 'codey_emotion_sprint'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_startle contains [ICON]
    def test_ext_i18n_codey_emotion_startle(self):
        key = 'codey_emotion_startle'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_shiver contains [ICON]
    def test_shiver(self):
        key = 'codey_emotion_shiver'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_dizzy contains [ICON]
    def test_dizzy(self):
        key = 'codey_emotion_dizzy'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_sleepy contains [ICON]
    def test_sleepy(self):
        key = 'codey_emotion_sleepy'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_sleeping contains [ICON]
    def test_sleeping(self):
        key = 'codey_emotion_sleeping'
        self.check_icon(key)


    # ext-i18n/codey_emotion/codey_emotion_revive contains [ICON]
    def test_revive(self):
        key = 'codey_emotion_revive'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_agree contains [ICON]
    def test_agree(self):
        key = 'codey_emotion_agree'
        self.check_icon(key)

    # ext-i18n/codey_emotion/codey_emotion_deny contains [ICON]
    def test_deny(self):
        key = 'codey_emotion_deny'
        self.check_icon(key)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyEmotionTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

