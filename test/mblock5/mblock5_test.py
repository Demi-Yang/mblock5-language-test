# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mblock5項目-翻译检查  =======================

class Mblock5Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mblock5-i18n']

    # mblock5-i18n/No empty value
    def test_mblock5_i18n_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mblock5-i18n/MBLOCK equals mBlock
    def test_mblock5_i18n_MBLOCK_equals_mBlock(self):
        self.assertIn('MBLOCK', self.test_dict)
        test_data = self.test_dict['MBLOCK']
        self.assertEqual(test_data, "mBlock")

    # mblock5-i18n/FORM.BUTTON.CODE.SENDED contains {0}
    def test_mblock5_i18n_FORM_BUTTON_CODE_SENDED(self):
        self.assertIn('FORM.BUTTON.CODE.SENDED', self.test_dict)
        test_data = self.test_dict['FORM.BUTTON.CODE.SENDED']
        self.assertIn('{0}', test_data)

    # mblock5-i18n/RENAME.ERR.CONTAIN.MSG contains \\ / : * ? \" < > | @ , # $ & ( ) 
    def test_mblock5_i18n_RENAME_ERR_CONTAIN_MSG(self):
        self.assertIn('RENAME.ERR.CONTAIN.MSG', self.test_dict)
        test_data = self.test_dict['RENAME.ERR.CONTAIN.MSG']
        r = re.compile(r'\\./:.\*.\\?.".<.>.\|.@.\,.#.\$.\&.\(.\).')
        # print(r.findall(test_data))
        self.assertRegexpMatches(test_data, r)
    
    # mblock5-i18n/DEVICE.INSTALL.STATUS.FAIL contains {0}
    def test_mblock5_i18n_DEVICE_INSTALL_STATUS_FAIL(self):
        self.assertIn('DEVICE.INSTALL.STATUS.FAIL', self.test_dict)
        test_data = self.test_dict['DEVICE.INSTALL.STATUS.FAIL']
        self.assertIn('{0}', test_data)

    # mblock5-i18n/DEVICE.UPDATE.STATUS.FAIL contains {0}
    def test_mblock5_i18n_DEVICE_UPDATE_STATUS_FAIL(self):
        self.assertIn('DEVICE.UPDATE.STATUS.FAIL', self.test_dict)
        test_data = self.test_dict['DEVICE.UPDATE.STATUS.FAIL']
        self.assertIn('{0}', test_data)

    # mblock5-i18n/UPDATER.PROGRESS.PERCENT contains {0}%
    def test_mblock5_i18n_UPDATER_PROGRESS_PERCENT(self):
        self.assertIn('UPDATER.PROGRESS.PERCENT', self.test_dict)
        test_data = self.test_dict['UPDATER.PROGRESS.PERCENT']
        self.assertIn('{0}%', test_data)

    # mblock5-i18n/FEEDBACK.PROFESSION.LIST is list & length equals 4
    def test_mblock5_i18n_FEEDBACK_PROFESSION_LIST(self):
        self.assertIn('FEEDBACK.PROFESSION.LIST', self.test_dict)
        test_data = self.test_dict['FEEDBACK.PROFESSION.LIST']
        self.assertEqual(len(test_data), 4)
        for i in test_data:
            self.assertNotEqual(i, '')

    # mblock5-i18n/PROJECT.EXPORT.LOCAL.MSG contains {0}
    def test_mblock5_i18n_PROJECT_EXPORT_LOCAL_MSG(self):
        self.assertIn('PROJECT.EXPORT.LOCAL.MSG', self.test_dict)
        test_data = self.test_dict['PROJECT.EXPORT.LOCAL.MSG']
        self.assertIn('{0}', test_data)

     # mblock5-i18n/SPRITE.UPLOAD.MSG contains "{0}"
    def test_mblock5_i18n_SPRITE_UPLOAD_MSG(self):
        self.assertIn('SPRITE.UPLOAD.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.UPLOAD.MSG']
        self.assertIn('\"{0}\"', test_data)

    # mblock5-i18n/SPRITE.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_mblock5_i18n_SPRITE_UPLOAD_SIZE_LIMIT_MSG(self):
        self.assertIn('SPRITE.UPLOAD.SIZE.LIMIT.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.UPLOAD.SIZE.LIMIT.MSG']
        self.assertIn('\"{0}\"', test_data)    

    # mblock5-i18n/SPRITE.SVG.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_mblock5_i18n_SPRITE_SVG_UPLOAD_SIZE_LIMIT_MSG(self):
        self.assertIn('SPRITE.SVG.UPLOAD.SIZE.LIMIT.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.SVG.UPLOAD.SIZE.LIMIT.MSG']
        self.assertIn('\"{0}\"', test_data)   

    # mblock5-i18n/SPRITE.SOUNDS.UPLOAD.MSG contains "{0}"
    def test_mblock5_i18n_SPRITE_SOUNDS_UPLOAD_MSG(self):
        self.assertIn('SPRITE.SOUNDS.UPLOAD.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.SOUNDS.UPLOAD.MSG']
        self.assertIn('\"{0}\"', test_data)   

    # mblock5-i18n/SPRITE.SOUNDS.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_mblock5_i18n_SPRITE_SOUNDS_UPLOAD_SIZE_LIMIT_MSG(self):
        self.assertIn('SPRITE.SOUNDS.UPLOAD.SIZE.LIMIT.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.SOUNDS.UPLOAD.SIZE.LIMIT.MSG']
        self.assertIn('\"{0}\"', test_data)   

    # mblock5-i18n/SPRITE.UPLOAD.EXISTS.MSG contains {0}
    def test_mblock5_i18n_SPRITE_UPLOAD_EXISTS_MSG(self):
        self.assertIn('SPRITE.UPLOAD.EXISTS.MSG', self.test_dict)
        test_data = self.test_dict['SPRITE.UPLOAD.EXISTS.MSG']
        self.assertIn('\"{0}\"', test_data)   
           
    # mblock5-i18n/CALIBRATE_COLOR_DESCRIPTION is list & length equals 4
    def test_mblock5_i18n_CALIBRATE_COLOR_DESCRIPTION(self):
        self.assertIn('CALIBRATE_COLOR_DESCRIPTION', self.test_dict)
        test_data = self.test_dict['CALIBRATE_COLOR_DESCRIPTION']
        self.assertEqual(len(test_data), 4)
        for i in test_data:
            self.assertNotEqual(i, '')

    # mblock5-i18n/CALIBRATE_GYRO_DESCRIPTION is list & length equals 2
    def test_mblock5_i18n_CALIBRATE_GYRO_DESCRIPTION(self):
        self.assertIn('CALIBRATE_GYRO_DESCRIPTION', self.test_dict)
        test_data = self.test_dict['CALIBRATE_GYRO_DESCRIPTION']
        self.assertEqual(len(test_data), 2)
        for i in test_data:
            self.assertNotEqual(i, '')

    # mblock5-i18n/CONNECT.UNABLE.TEXT contains {0}
    def test_mblock5_i18n_CONNECT_UNABLE_TEXT(self):
        self.assertIn('CONNECT.UNABLE.TEXT', self.test_dict)
        test_data = self.test_dict['CONNECT.UNABLE.TEXT']
        r = re.compile(r'{[0]}')
        # print(r.findall(result))
        self.assertRegexpMatches(test_data, r)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Mblock5Test) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)