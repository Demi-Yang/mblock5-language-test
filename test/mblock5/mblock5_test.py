# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle
assert_msg = "key: {0}, error: {1}";

# ======================  mblock5項目-翻译检查  =======================

class Mblock5Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mblock5-i18n']

    def check_params(self, key, param):
        self.assertIn(key, self.test_dict, assert_msg.format(key, 'key缺失'))
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, "key: {0}, 缺少参数: {1}, value: {2} ".format(key, param, test_data))

    # mblock5-i18n/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, 'mblock5-i18n 模块下存在未翻译的字段: {0}'.format(key))
            self.assertNotEqual(value, "", 'mblock5-i18n 模块下存在未翻译的字段: {0}'.format(key))

    # mblock5-i18n/No new or missing items
    def test_no_new_or_missing_items(self):
        key_len = 473
        self.assertEqual(len(self.test_dict), key_len, "mblock5-i18n 模块下新增或删减了新的字段，测试用例需增减~")

    # mblock5-i18n/MBLOCK equals mBlock
    def test_MBLOCK(self):
        key = 'MBLOCK'
        self.assertIn(key, self.test_dict)
        test_data = self.test_dict[key]
        self.assertEqual(test_data, 'mBlock', assert_msg.format(key, 'expect value: mBlock'))

    # mblock5-i18n/FORM.BUTTON.CODE.SENDED contains {0}
    def test_FORM_BUTTON_CODE_SENDED(self):
        key='FORM.BUTTON.CODE.SENDED'
        self.check_params(key, '{0}')

    # mblock5-i18n/RENAME.ERR.CONTAIN.MSG contains \\ / : * ? \" < > | @ , # $ & ( ) 
    def test_RENAME_ERR_CONTAIN_MSG(self):
        key='RENAME.ERR.CONTAIN.MSG'
        self.assertIn(key, self.test_dict, assert_msg.format(key, 'key缺失'))
        test_data = self.test_dict[key]
        r = re.compile(r'\\./:.\*.\\?.".<.>.\|.@.\,.#.\$.\&.\(.\).')
        # print(r.findall(test_data))
        self.assertRegexpMatches(test_data, r)
    
    # mblock5-i18n/DEVICE.INSTALL.STATUS.FAIL contains {0}
    def test_DEVICE_INSTALL_STATUS_FAIL(self):
        key='DEVICE.INSTALL.STATUS.FAIL'
        self.check_params(key, '{0}')

    # mblock5-i18n/DEVICE.UPDATE.STATUS.FAIL contains {0}
    def test_DEVICE_UPDATE_STATUS_FAIL(self):
        key='DEVICE.UPDATE.STATUS.FAIL'
        self.check_params(key, '{0}')

    # mblock5-i18n/UPDATER.PROGRESS.PERCENT contains {0}%
    def test_UPDATER_PROGRESS_PERCENT(self):
        key='UPDATER.PROGRESS.PERCENT'
        self.check_params(key, '{0}%')

    # mblock5-i18n/FEEDBACK.PROFESSION.LIST is list & length equals 4
    def test_FEEDBACK_PROFESSION_LIST(self):
        key='FEEDBACK.PROFESSION.LIST'
        self.assertIn(key, self.test_dict, assert_msg.format(key, 'key缺失'))
        test_data = self.test_dict[key]
        self.assertEqual(len(test_data), 4, assert_msg.format(key, '包含4项，请检查！分别为："Teacher","Student", "Parent","Maker"'))
        for i in test_data:
            self.assertNotEqual(i, '', '选项不能为空！')

    # mblock5-i18n/PROJECT.EXPORT.LOCAL.MSG contains {0}
    def test_PROJECT_EXPORT_LOCAL_MSG(self):
        key='PROJECT.EXPORT.LOCAL.MSG'
        self.check_params(key, '{0}')

     # mblock5-i18n/SPRITE.UPLOAD.MSG contains "{0}"
    def test_SPRITE_UPLOAD_MSG(self):
        key='SPRITE.UPLOAD.MSG'
        self.check_params(key, '\"{0}\"')

    # mblock5-i18n/SPRITE.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_SPRITE_UPLOAD_SIZE_LIMIT_MSG(self):
        key='SPRITE.UPLOAD.SIZE.LIMIT.MSG'
        self.check_params(key, '\"{0}\"') 

    # mblock5-i18n/SPRITE.SVG.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_SPRITE_SVG_UPLOAD_SIZE_LIMIT_MSG(self):
        key='SPRITE.SVG.UPLOAD.SIZE.LIMIT.MSG'
        self.check_params(key, '\"{0}\"')

    # mblock5-i18n/SPRITE.SOUNDS.UPLOAD.MSG contains "{0}"
    def test_SPRITE_SOUNDS_UPLOAD_MSG(self):
        key='SPRITE.SOUNDS.UPLOAD.MSG'
        self.check_params(key, '\"{0}\"')   

    # mblock5-i18n/SPRITE.SOUNDS.UPLOAD.SIZE.LIMIT.MSG contains "{0}"
    def test_SPRITE_SOUNDS_UPLOAD_SIZE_LIMIT_MSG(self):
        key='SPRITE.SOUNDS.UPLOAD.SIZE.LIMIT.MSG'
        self.check_params(key, '\"{0}\"')

    # mblock5-i18n/SPRITE.UPLOAD.EXISTS.MSG contains {0}
    def test_SPRITE_UPLOAD_EXISTS_MSG(self):
        key='SPRITE.UPLOAD.EXISTS.MSG'
        self.check_params(key, '\"{0}\"')  
           
    # mblock5-i18n/CALIBRATE_COLOR_DESCRIPTION is list & length equals 4
    def test_CALIBRATE_COLOR_DESCRIPTION(self):
        key='CALIBRATE_COLOR_DESCRIPTION'
        self.assertIn(key, self.test_dict, assert_msg.format(key, 'key缺失'))
        test_data = self.test_dict[key]
        self.assertEqual(len(test_data), 4, assert_msg.format(key, '包含4项，请检查！分别为： "Put your Codey Rocky in the environment that needs calibration (working environment), and rotate the IR color sensor to the bottom.",'\
            '"Place the white color identification card under the color sensor (if your color card is damaged or lost, use a white printer paper then).",'\
            '"Just click the Calibrate button below. Calibration finished!",'\
            '"Please aim the color sensor to the center of the Color Identification Card."'))
        for i in test_data:
            self.assertNotEqual(i, '', '选项不能为空！')

    # mblock5-i18n/CALIBRATE_GYRO_DESCRIPTION is list & length equals 2
    def test_CALIBRATE_GYRO_DESCRIPTION(self):
        key='CALIBRATE_GYRO_DESCRIPTION'
        self.assertIn(key, self.test_dict)
        test_data = self.test_dict[key]
        self.assertEqual(len(test_data), 2, assert_msg.format(key , '包含两项，请检查！分别为："Put your Codey in a stable place.",'\
            '"Just click the Calibrate button below.Calibration finished!"'))
        for i in test_data:
            self.assertNotEqual(i, '', '选项不能为空！')

    # mblock5-i18n/CONNECT.UNABLE.TEXT contains {0}
    def test_CONNECT_UNABLE_TEXT(self):
        key='CONNECT.UNABLE.TEXT'
        self.assertIn(key, self.test_dict, assert_msg.format(key, 'key缺失'))
        test_data = self.test_dict[key]
        r = re.compile(r'{[0]}')
        # print(r.findall(result))
        self.assertRegexpMatches(test_data, r, assert_msg.format(key, '缺少参数：[0], source: The device you connected may be not {0}, or the firmware of {0} has been damaged.\n\n\tYou can: \n\t- Change another COM port.\n\t- Update the device firmware\n\nIf you are using a Bluetooth adapter, please check if the adapter is well connected to the device.'))


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Mblock5Test) 
    
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)