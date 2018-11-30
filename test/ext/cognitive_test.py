# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle


# ======================  cognitive項目-翻译检查  =======================

class CognitiveTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['ext-i18n/cognitive']
    
    def check_key_exists(self, key):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_params(self, key, params):
        test_data = self.test_dict[key]
        for p in params:
            self.assertIn(p, test_data, '\nkey: {0} \nvalue:{1} \n缺少参数：{2}'.format(key, test_data, p))

    # ext-i18n/cognitive/No empty value
    def test_cognitive_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n缺少翻译的字段：" + key)
            self.assertNotEqual(value, '', "\n缺少翻译的字段：" + key)

    # ext-i18n/cognitive/No new or missing items
    def test_cognitive_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 46, '\ncognitive 模块下新增或删减了新的字段，测试用例需增减~')

    # ext-i18n/cognitive/beginSpeechToText contains [LANGUAGE]、[TIMER]
    def test_beginSpeechToText(self):
        key = 'beginSpeechToText'
        self.check_key_exists(key)
        self.check_params(key, ['[LANGUAGE]', '[TIMER]'])

    # ext-i18n/cognitive/beginFaceDetection contains [TIMER]
    def test_beginFaceDetection(self):
        key = 'beginFaceDetection'
        self.check_key_exists(key)
        self.check_params(key, ['[TIMER]'])

    # ext-i18n/cognitive/beginEmotionRecognition contains [TIMER]
    def test_beginEmotionRecognition(self):
        key = 'beginEmotionRecognition'
        self.check_key_exists(key)
        self.check_params(key, ['[TIMER]'])

    # ext-i18n/cognitive/emotionValue contains [TYPE]
    def test_emotionValue(self):
        key = 'emotionValue'
        self.check_key_exists(key)
        self.check_params(key, ['[TYPE]'])

    # ext-i18n/cognitive/emotionType contains [TYPE]
    def test_emotionType(self):
        key = 'emotionType'
        self.check_key_exists(key)
        self.check_params(key, ['[TYPE]'])

    # ext-i18n/cognitive/beginImageToText contains [LANGUAGE]、[TIMER]
    def test_beginImageToText(self):
        key = 'beginImageToText'
        self.check_key_exists(key)
        self.check_params(key, ['[LANGUAGE]', '[TIMER]'])

    # ext-i18n/cognitive/beginHandwrittenToText contains [TIMER]
    def test_beginHandwrittenToText(self):
        key = 'beginHandwrittenToText'
        self.check_key_exists(key)
        self.check_params(key, ['[TIMER]'])



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CognitiveTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

