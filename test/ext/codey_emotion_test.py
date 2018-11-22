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

    # ext-i18n/codey_emotion/No empty value
    def test_ext_i18n_tm_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/codey_emotion/codey_emotion_look_up contains [ICON]
    def test_ext_i18n_codey_emotion_look_up(self):
        self.assertIn('codey_emotion_look_up', self.test_dict)
        test_data = self.test_dict['codey_emotion_look_up']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
        
    # ext-i18n/codey_emotion/codey_emotion_look_down contains [ICON]
    def test_ext_i18n_codey_emotion_look_down(self):
        self.assertIn('codey_emotion_look_down', self.test_dict)
        test_data = self.test_dict['codey_emotion_look_down']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
  
    # ext-i18n/codey_emotion/codey_emotion_look_left contains [ICON]
    def test_ext_i18n_codey_emotion_look_left(self):
        self.assertIn('codey_emotion_look_left', self.test_dict)
        test_data = self.test_dict['codey_emotion_look_left']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
  
    # ext-i18n/codey_emotion/codey_emotion_look_right contains [ICON]
    def test_ext_i18n_codey_emotion_look_right(self):
        self.assertIn('codey_emotion_look_right', self.test_dict)
        test_data = self.test_dict['codey_emotion_look_right']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
  
    # ext-i18n/codey_emotion/codey_emotion_look_around contains [ICON]
    def test_ext_i18n_codey_emotion_look_around(self):
        self.assertIn('codey_emotion_look_around', self.test_dict)
        test_data = self.test_dict['codey_emotion_look_around']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_smile contains [ICON]
    def test_ext_i18n_codey_emotion_smile(self):
        self.assertIn('codey_emotion_smile', self.test_dict)
        test_data = self.test_dict['codey_emotion_smile']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_yeah contains [ICON]
    def test_ext_i18n_codey_emotion_yeah(self):
        self.assertIn('codey_emotion_yeah', self.test_dict)
        test_data = self.test_dict['codey_emotion_yeah']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_naughty contains [ICON]
    def test_ext_i18n_codey_emotion_naughty(self):
        self.assertIn('codey_emotion_naughty', self.test_dict)
        test_data = self.test_dict['codey_emotion_naughty']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_greeting contains [ICON]
    def test_ext_i18n_codey_emotion_greeting(self):
        self.assertIn('codey_emotion_greeting', self.test_dict)
        test_data = self.test_dict['codey_emotion_greeting']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_proud contains [ICON]
    def test_ext_i18n_codey_emotion_proud(self):
        self.assertIn('codey_emotion_proud', self.test_dict)
        test_data = self.test_dict['codey_emotion_proud']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_coquetry contains [ICON]
    def test_ext_i18n_codey_emotion_coquetry(self):
        self.assertIn('codey_emotion_coquetry', self.test_dict)
        test_data = self.test_dict['codey_emotion_coquetry']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_awkward contains [ICON]
    def test_ext_i18n_codey_emotion_awkward(self):
        self.assertIn('codey_emotion_awkward', self.test_dict)
        test_data = self.test_dict['codey_emotion_awkward']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_exclaim contains [ICON]
    def test_ext_i18n_codey_emotion_exclaim(self):
        self.assertIn('codey_emotion_exclaim', self.test_dict)
        test_data = self.test_dict['codey_emotion_exclaim']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_aggrieved contains [ICON]
    def test_ext_i18n_codey_emotion_aggrieved(self):
        self.assertIn('codey_emotion_aggrieved', self.test_dict)
        test_data = self.test_dict['codey_emotion_aggrieved']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_sad contains [ICON]
    def test_ext_i18n_codey_emotion_sad(self):
        self.assertIn('codey_emotion_sad', self.test_dict)
        test_data = self.test_dict['codey_emotion_sad']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
    # ext-i18n/codey_emotion/codey_emotion_angry contains [ICON]
    def test_ext_i18n_codey_emotion_angry(self):
        self.assertIn('codey_emotion_angry', self.test_dict)
        test_data = self.test_dict['codey_emotion_angry']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
    # ext-i18n/codey_emotion/codey_emotion_sprint contains [ICON]
    def test_ext_i18n_codey_emotion_sprint(self):
        self.assertIn('codey_emotion_sprint', self.test_dict)
        test_data = self.test_dict['codey_emotion_sprint']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_startle contains [ICON]
    def test_ext_i18n_codey_emotion_startle(self):
        self.assertIn('codey_emotion_startle', self.test_dict)
        test_data = self.test_dict['codey_emotion_startle']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)
    # ext-i18n/codey_emotion/codey_emotion_shiver contains [ICON]
    def test_ext_i18n_codey_emotion_shiver(self):
        self.assertIn('codey_emotion_shiver', self.test_dict)
        test_data = self.test_dict['codey_emotion_shiver']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_dizzy contains [ICON]
    def test_ext_i18n_codey_emotion_dizzy(self):
        self.assertIn('codey_emotion_dizzy', self.test_dict)
        test_data = self.test_dict['codey_emotion_dizzy']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_sleepy contains [ICON]
    def test_ext_i18n_codey_emotion_sleepy(self):
        self.assertIn('codey_emotion_sleepy', self.test_dict)
        test_data = self.test_dict['codey_emotion_sleepy']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_sleeping contains [ICON]
    def test_ext_i18n_codey_emotion_sleeping(self):
        self.assertIn('codey_emotion_sleeping', self.test_dict)
        test_data = self.test_dict['codey_emotion_sleeping']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


    # ext-i18n/codey_emotion/codey_emotion_revive contains [ICON]
    def test_ext_i18n_codey_emotion_revive(self):
        self.assertIn('codey_emotion_revive', self.test_dict)
        test_data = self.test_dict['codey_emotion_revive']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_agree contains [ICON]
    def test_ext_i18n_codey_emotion_agree(self):
        self.assertIn('codey_emotion_agree', self.test_dict)
        test_data = self.test_dict['codey_emotion_agree']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)

    # ext-i18n/codey_emotion/codey_emotion_deny contains [ICON]
    def test_ext_i18n_codey_emotion_deny(self):
        self.assertIn('codey_emotion_deny', self.test_dict)
        test_data = self.test_dict['codey_emotion_deny']
        self.assertIn('[ICON]', test_data)
        self.assertEqual(test_data.index('[ICON]'), 0)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CodeyEmotionTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

