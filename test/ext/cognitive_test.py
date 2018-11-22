# coding:utf-8
# import requests
import json
import re
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

    # ext-i18n/cognitive/No empty value
    def test_ext_i18n_cognitive_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # ext-i18n/cognitive/beginSpeechToText contains [LANGUAGE]、[TIMER]
    def test_ext_i18n_beginSpeechToText(self):
        self.assertIn('beginSpeechToText', self.test_dict)
        test_data = self.test_dict['beginSpeechToText']
        self.assertIn('[LANGUAGE]', test_data)
        self.assertIn('[TIMER]', test_data)

    # ext-i18n/cognitive/beginFaceDetection contains [TIMER]
    def test_ext_i18n_beginFaceDetection(self):
        self.assertIn('beginFaceDetection', self.test_dict)
        test_data = self.test_dict['beginFaceDetection']
        self.assertIn('[TIMER]', test_data)

    # ext-i18n/cognitive/beginEmotionRecognition contains [TIMER]
    def test_ext_i18n_beginEmotionRecognition(self):
        self.assertIn('beginEmotionRecognition', self.test_dict)
        test_data = self.test_dict['beginEmotionRecognition']
        self.assertIn('[TIMER]', test_data)

    # ext-i18n/cognitive/emotionValue contains [TYPE]
    def test_ext_i18n_emotionValue(self):
        self.assertIn('emotionValue', self.test_dict)
        test_data = self.test_dict['emotionValue']
        self.assertIn('[TYPE]', test_data)

    # ext-i18n/cognitive/emotionType contains [TYPE]
    def test_ext_i18n_emotionType(self):
        self.assertIn('emotionType', self.test_dict)
        test_data = self.test_dict['emotionType']
        self.assertIn('[TYPE]', test_data)

    # ext-i18n/cognitive/beginImageToText contains [LANGUAGE]、[TIMER]
    def test_ext_i18n_beginImageToText(self):
        self.assertIn('beginImageToText', self.test_dict)
        test_data = self.test_dict['beginImageToText']
        self.assertIn('[LANGUAGE]', test_data)
        self.assertIn('[TIMER]', test_data)

    # ext-i18n/cognitive/beginHandwrittenToText contains [TIMER]
    def test_ext_i18n_beginHandwrittenToText(self):
        self.assertIn('beginHandwrittenToText', self.test_dict)
        test_data = self.test_dict['beginHandwrittenToText']
        self.assertIn('[TIMER]', test_data)



if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(CognitiveTest) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)

