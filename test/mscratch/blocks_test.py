# coding:utf-8
# import requests
import json
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mscratch項目-翻译检查  =======================

class BlocksTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mscratch-i18n']['blocks']

    def check_key_exists(self, key, ):
        self.assertIn(key, self.test_dict, '\n缺少key: {0}'.format(key))

    def check_expect_value(self, key, expect_value):
        test_data = self.test_dict[key]
        self.assertEqual(test_data, expect_value, '\nkey: {0} \nvalue: {1} \n error: 值不等于 {2}, '.format(key, test_data, expect_value))

    def check_param(self, key, param):
        test_data = self.test_dict[key]
        self.assertIn(param, test_data, '\nkey: {0} \nvalue: {1} \n缺少参数：{2}'.format(key, test_data, param))

    def check_icon(self, key):
        test_data = self.test_dict[key]
        self.assertIn('[ICON]', test_data, '\nkey: {0} \nvalue: {1} \n缺少参数： [ICON]'.format(key, test_data))
        self.assertEqual(test_data.index('[ICON]'), 0, '\nkey: {0} \nvalue: {1} \nerror: 参数[ICON]必须在首位'.format(key, test_data))




    # mscratch-i18n/blocks/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value, "\n该字段的翻译为空，错误 key: " + key)
            self.assertNotEqual(value, '', "\n该字段的翻译为空，错误 key: " + key)

    # mscratch-i18n/blocks/No new or missing items
    def test_no_new_or_missing_items(self):
        self.assertEqual(len(self.test_dict), 301, "\nmscratch-i18n/blocks/ 模块下新增或删减了翻译字段")

    # mscratch-i18n/blocks/CONTROL_REPEAT contains %2 %1 
    def test_CONTROL_REPEAT(self):
        key = 'CONTROL_REPEAT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/CONTROL_WAIT contains %1 
    def test_CONTROL_WAIT(self):
        key = 'CONTROL_WAIT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/CONTROL_WAITUNTIL contains %1 
    def test_CONTROL_WAITUNTIL(self):
        key = 'CONTROL_WAITUNTIL'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/CONTROL_REPEATUNTIL contains %1 
    def test_CONTROL_REPEATUNTIL(self):
        key = 'CONTROL_REPEATUNTIL'
        self.check_key_exists(key)
        self.check_param(key, '%1')


    # mscratch-i18n/blocks/CONTROL_WHILE contains %1 
    def test_CONTROL_WHILE(self):
        key = 'CONTROL_WHILE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/CONTROL_FOREACH contains %1 %2
    def test_CONTROL_FOREACH(self):
        key = 'CONTROL_FOREACH'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/CONTROL_CREATECLONEOF contains %1 
    def test_CONTROL_CREATECLONEOF(self):
        key = 'CONTROL_CREATECLONEOF'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_SETVARIABLETO contains %1 %2
    def test_DATA_SETVARIABLETO(self):
        key = 'DATA_SETVARIABLETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DATA_CHANGEVARIABLEBY contains %1 %2
    def test_DATA_CHANGEVARIABLEBY(self):
        key = 'DATA_CHANGEVARIABLEBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DATA_SHOWVARIABLE contains %1 
    def test_DATA_SHOWVARIABLE(self):
        key = 'DATA_SHOWVARIABLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_HIDEVARIABLE contains %1 
    def test_DATA_HIDEVARIABLE(self):
        key = 'DATA_HIDEVARIABLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')


    # mscratch-i18n/blocks/DATA_ADDTOLIST contains %1 %2
    def test_DATA_ADDTOLIST(self):
        key = 'DATA_ADDTOLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')


    # mscratch-i18n/blocks/DATA_DELETEOFLIST contains %1 %2
    def test_DATA_DELETEOFLIST(self):
        key = 'DATA_DELETEOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DATA_DELETEALLOFLIST contains %1 
    def test_DATA_DELETEALLOFLIST(self):
        key = 'DATA_DELETEALLOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_INSERTATLIST contains %1 %2 %3
    def test_DATA_INSERTATLIST(self):
        key = 'DATA_INSERTATLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')
        self.check_param(key, '%3')

    # mscratch-i18n/blocks/DATA_REPLACEITEMOFLIST contains %1 
    def test_DATA_REPLACEITEMOFLIST(self):
        key = 'DATA_REPLACEITEMOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')
        self.check_param(key, '%3')

    # mscratch-i18n/blocks/DATA_ITEMOFLIST contains %1 
    def test_DATA_ITEMOFLIST(self):
        key = 'DATA_ITEMOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DATA_LENGTHOFLIST contains %1 
    def test_DATA_LENGTHOFLIST(self):
        key = 'DATA_LENGTHOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_LISTCONTAINSITEM contains %1 %2
    def test_DATA_LISTCONTAINSITEM(self):
        key = 'DATA_LISTCONTAINSITEM'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DATA_SHOWLIST contains %1 
    def test_DATA_SHOWLIST(self):
        key = 'DATA_SHOWLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_HIDELIST contains %1 
    def test_DATA_HIDELIST(self):
        key = 'DATA_HIDELIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENFLAGCLICKED contains %1 
    def test_EVENT_WHENFLAGCLICKED(self):
        key = 'EVENT_WHENFLAGCLICKED'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENTOUCHINGOBJECT contains %1 
    def test_EVENT_WHENTOUCHINGOBJECT(self):
        key = 'EVENT_WHENTOUCHINGOBJECT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENBROADCASTRECEIVED contains %1 
    def test_EVENT_WHENBROADCASTRECEIVED(self):
        key = 'EVENT_WHENBROADCASTRECEIVED'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENBACKDROPSWITCHESTO contains %1 
    def test_EVENT_WHENBACKDROPSWITCHESTO(self):
        key = 'EVENT_WHENBACKDROPSWITCHESTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENGREATERTHAN contains %1 > %2
    def test_EVENT_WHENGREATERTHAN(self):
        key = 'EVENT_WHENGREATERTHAN'
        self.check_key_exists(key)
        test_data = self.test_dict[key]
        self.check_param(key, '%1 > %2')

    # mscratch-i18n/blocks/EVENT_BROADCAST contains %1 
    def test_EVENT_BROADCAST(self):
        key = 'EVENT_BROADCAST'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_BROADCASTANDWAIT contains %1 
    def test_EVENT_BROADCASTANDWAIT(self):
        key = 'EVENT_BROADCASTANDWAIT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/EVENT_WHENKEYPRESSED contains %1 
    def test_EVENT_WHENKEYPRESSED(self):
        key = 'EVENT_WHENKEYPRESSED'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_SAYFORSECS contains %1 %2
    def test_LOOKS_SAYFORSECS(self):
        key = 'LOOKS_SAYFORSECS'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/LOOKS_SAY contains %1 
    def test_LOOKS_SAY(self):
        key = 'LOOKS_SAY'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_THINKFORSECS contains %1 %2
    def test_LOOKS_THINKFORSECS(self):
        key = 'LOOKS_THINKFORSECS'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/LOOKS_THINK contains %1 
    def test_LOOKS_THINK(self):
        key = 'LOOKS_THINK'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_CHANGEEFFECTBY contains %1 %2
    def test_LOOKS_CHANGEEFFECTBY(self):
        key = 'LOOKS_CHANGEEFFECTBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/LOOKS_SETEFFECTTO contains %1 %2
    def test_LOOKS_SETEFFECTTO(self):
        key = 'LOOKS_SETEFFECTTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/LOOKS_CHANGESIZEBY contains %1 
    def test_LOOKS_CHANGESIZEBY(self):
        key = 'LOOKS_CHANGESIZEBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_SETSIZETO contains %1 
    def test_LOOKS_SETSIZETO(self):
        key = 'LOOKS_SETSIZETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_CHANGESTRETCHBY contains %1 
    def test_LOOKS_CHANGESTRETCHBY(self):
        key = 'LOOKS_CHANGESTRETCHBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_SETSTRETCHTO contains %1 
    def test_LOOKS_SETSTRETCHTO(self):
        key = 'LOOKS_SETSTRETCHTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_SWITCHCOSTUMETO contains %1 
    def test_LOOKS_SWITCHCOSTUMETO(self):
        key = 'LOOKS_SWITCHCOSTUMETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        
    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTO contains %1 
    def test_LOOKS_SWITCHBACKDROPTO(self):
        key = 'LOOKS_SWITCHBACKDROPTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_GOTOFRONTBACK contains %1 
    def test_LOOKS_GOTOFRONTBACK(self):
        key = 'LOOKS_GOTOFRONTBACK'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_GOFORWARDBACKWARDLAYERS contains %1 
    def test_LOOKS_GOFORWARDBACKWARDLAYERS(self):
        key = 'LOOKS_GOFORWARDBACKWARDLAYERS'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/LOOKS_BACKDROPNUMBERNAME contains %1 
    def test_LOOKS_BACKDROPNUMBERNAME(self):
        key = 'LOOKS_BACKDROPNUMBERNAME'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_COSTUMENUMBERNAME contains %1 
    def test_LOOKS_COSTUMENUMBERNAME(self):
        key = 'LOOKS_COSTUMENUMBERNAME'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTOANDWAIT contains %1 
    def test_LOOKS_SWITCHBACKDROPTOANDWAIT(self):
        key = 'LOOKS_SWITCHBACKDROPTOANDWAIT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_MOVESTEPS contains %1 
    def test_MOTION_MOVESTEPS(self):
        key = 'MOTION_MOVESTEPS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_TURNLEFT contains %1 
    def test_MOTION_TURNLEFT(self):
        key = 'MOTION_TURNLEFT'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/MOTION_TURNRIGHT contains %1 
    def test_MOTION_TURNRIGHT(self):
        key = 'MOTION_TURNRIGHT'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/MOTION_POINTINDIRECTION contains %1 
    def test_MOTION_POINTINDIRECTION(self):
        key = 'MOTION_POINTINDIRECTION'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_POINTTOWARDS contains %1 
    def test_MOTION_POINTTOWARDS(self):
        key = 'MOTION_POINTTOWARDS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_GOTO contains %1 
    def test_MOTION_GOTO(self):
        key = 'MOTION_GOTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_GOTOXY contains  x: %1 y: %2
    def test_MOTION_GOTOXY(self):
        key = 'MOTION_GOTOXY'
        self.check_key_exists(key)
        self.check_param(key, 'x: %1')
        self.check_param(key, 'y: %2')

    # mscratch-i18n/blocks/MOTION_GLIDESECSTOXY contains %1 and x: %2 y: %3
    def test_MOTION_GLIDESECSTOXY(self):
        key = 'MOTION_GLIDESECSTOXY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, 'x: %2')
        self.check_param(key, 'y: %3')

    # mscratch-i18n/blocks/MOTION_GLIDETO contains %1 
    def test_MOTION_GLIDETO(self):
        key = 'MOTION_GLIDETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/MOTION_CHANGEXBY contains %1 and x
    def test_MOTION_CHANGEXBY(self):
        key = 'MOTION_CHANGEXBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, 'x')

    # mscratch-i18n/blocks/MOTION_SETX contains %1 and x
    def test_MOTION_SETX(self):
        key = 'MOTION_SETX'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, 'x')

    # mscratch-i18n/blocks/MOTION_CHANGEYBY contains %1 and y
    def test_MOTION_CHANGEYBY(self):
        key = 'MOTION_CHANGEYBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, 'y')

    # mscratch-i18n/blocks/MOTION_SETY contains %1 and y
    def test_MOTION_SETY(self):
        key = 'MOTION_SETY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, 'y')

    # mscratch-i18n/blocks/MOTION_SETROTATIONSTYLE contains %1 
    def test_MOTION_SETROTATIONSTYLE(self):
        key = 'MOTION_SETROTATIONSTYLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_XPOSITION contains %1 
    def test_MOTION_XPOSITION(self):
        key = 'MOTION_XPOSITION'
        self.check_key_exists(key)
        self.check_param(key, 'x')

    # mscratch-i18n/blocks/MOTION_YPOSITION contains %1 
    def test_MOTION_YPOSITION(self):
        key = 'MOTION_YPOSITION'
        self.check_key_exists(key)
        self.check_param(key, 'y')

    # mscratch-i18n/blocks/MOTION_SCROLLRIGHT contains %1 
    def test_MOTION_SCROLLRIGHT(self):
        key = 'MOTION_SCROLLRIGHT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_SCROLLUP contains %1 
    def test_MOTION_SCROLLUP(self):
        key = 'MOTION_SCROLLUP'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_ALIGNSCENE contains %1 
    def test_MOTION_ALIGNSCENE(self):
        key = 'MOTION_ALIGNSCENE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/MOTION_XSCROLL contains x
    def test_MOTION_XSCROLL(self):
        key = 'MOTION_XSCROLL'
        self.check_key_exists(key)
        self.check_param(key, 'x')

    # mscratch-i18n/blocks/MOTION_YSCROLL contains y 
    def test_MOTION_YSCROLL(self):
        key = 'MOTION_YSCROLL'
        self.check_key_exists(key)
        self.check_param(key, 'y')

    # mscratch-i18n/blocks/OPERATORS_ADD contains '%1 + %2'
    def test_OPERATORS_ADD(self):
        key = 'OPERATORS_ADD'
        self.check_key_exists(key)
        self.check_param(key, '%1 + %2')

    # mscratch-i18n/blocks/OPERATORS_SUBTRACT contains '%1 - %2'
    def test_OPERATORS_SUBTRACT(self):
        key = 'OPERATORS_SUBTRACT'
        self.check_key_exists(key)
        self.check_param(key, '%1 - %2')

    # mscratch-i18n/blocks/OPERATORS_MULTIPLY contains '%1 * %2' 
    def test_OPERATORS_MULTIPLY(self):
        key = 'OPERATORS_MULTIPLY'
        self.check_key_exists(key)
        self.check_param(key, '%1 * %2')

    # mscratch-i18n/blocks/OPERATORS_DIVIDE contains '%1 / %2'
    def test_OPERATORS_DIVIDE(self):
        key = 'OPERATORS_DIVIDE'
        self.check_key_exists(key)
        self.check_param(key, '%1 / %2')

    # mscratch-i18n/blocks/OPERATORS_RANDOM contains %1 %2
    def test_OPERATORS_RANDOM(self):
        key = 'OPERATORS_RANDOM'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_GT contains %1 > %2 
    def test_OPERATORS_GT(self):
        key = 'OPERATORS_GT'
        self.check_key_exists(key)
        self.check_param(key, '%1 > %2')

    # mscratch-i18n/blocks/OPERATORS_LT contains %1 < %2
    def test_OPERATORS_LT(self):
        key = 'OPERATORS_LT'
        self.check_key_exists(key)
        self.check_param(key, '%1 < %2')

    # mscratch-i18n/blocks/OPERATORS_EQUALS contains %1 = %2
    def test_OPERATORS_EQUALS(self):
        key = 'OPERATORS_EQUALS'
        self.check_key_exists(key)
        self.check_param(key, '%1 = %2')

    # mscratch-i18n/blocks/OPERATORS_AND contains %1 %2
    def test_OPERATORS_AND(self):
        key = 'OPERATORS_AND'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_OR contains %1 %2
    def test_OPERATORS_OR(self):
        key = 'OPERATORS_OR'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_NOT contains %1 
    def test_OPERATORS_NOT(self):
        key = 'OPERATORS_NOT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/OPERATORS_JOIN contains %1 
    def test_OPERATORS_JOIN(self):
        key = 'OPERATORS_JOIN'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_LETTEROF contains %1 
    def test_OPERATORS_LETTEROF(self):
        key = 'OPERATORS_LETTEROF'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_LENGTH contains %1 
    def test_OPERATORS_LENGTH(self):
        key = 'OPERATORS_LENGTH'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/OPERATORS_CONTAINS contains %1 
    def test_OPERATORS_CONTAINS(self):
        key = 'OPERATORS_CONTAINS'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_MOD contains %1 
    def test_OPERATORS_MOD(self):
        key = 'OPERATORS_MOD'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/OPERATORS_ROUND contains %1 
    def test_OPERATORS_ROUND(self):
        key = 'OPERATORS_ROUND'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/OPERATORS_MATHOP contains %1 
    def test_OPERATORS_MATHOP(self):
        key = 'OPERATORS_MATHOP'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/PROCEDURES_DEFINITION contains %1 
    def test_PROCEDURES_DEFINITION(self):
        key = 'PROCEDURES_DEFINITION'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_TOUCHINGOBJECT contains %1 
    def test_SENSING_TOUCHINGOBJECT(self):
        key = 'SENSING_TOUCHINGOBJECT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_TOUCHINGCOLOR contains %1 
    def test_SENSING_TOUCHINGCOLOR(self):
        key = 'SENSING_TOUCHINGCOLOR'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        
    # mscratch-i18n/blocks/SENSING_COLORISTOUCHINGCOLOR contains %1 %2
    def test_SENSING_COLORISTOUCHINGCOLOR(self):
        key = 'SENSING_COLORISTOUCHINGCOLOR'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')
    
    # mscratch-i18n/blocks/SENSING_DISTANCETO contains %1 
    def test_SENSING_DISTANCETO(self):
        key = 'SENSING_DISTANCETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_ASKANDWAIT contains %1 
    def test_SENSING_ASKANDWAIT(self):
        key = 'SENSING_ASKANDWAIT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_KEYPRESSED contains %1 
    def test_SENSING_KEYPRESSED(self):
        key = 'SENSING_KEYPRESSED'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_SETDRAGMODE contains %1 
    def test_SENSING_SETDRAGMODE(self):
        key = 'SENSING_SETDRAGMODE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SENSING_OF contains %1 %2
    def test_SENSING_OF(self):
        key = 'SENSING_OF'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/SENSING_CURRENT contains %1 
    def test_SENSING_CURRENT(self):
        key = 'SENSING_CURRENT'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SOUND_PLAY contains %1 
    def test_SOUND_PLAY(self):
        key = 'SOUND_PLAY'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SOUND_PLAYUNTILDONE contains %1 
    def test_SOUND_PLAYUNTILDONE(self):
        key = 'SOUND_PLAYUNTILDONE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/SOUND_SETEFFECTO contains %1 %2
    def test_SOUND_SETEFFECTO(self):
        key = 'SOUND_SETEFFECTO'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/SOUND_CHANGEEFFECTBY contains %1 %2
    def test_SOUND_CHANGEEFFECTBY(self):
        key = 'SOUND_CHANGEEFFECTBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/SOUND_CHANGEVOLUMEBY contains %1 
    def test_SOUND_CHANGEVOLUMEBY(self):
        key = 'SOUND_CHANGEVOLUMEBY'
        self.check_key_exists(key)
        self.check_param(key, '%1')
    
    # mscratch-i18n/blocks/SOUND_SETVOLUMETO contains %1 
    def test_SOUND_SETVOLUMETO(self):
        key = 'SOUND_SETVOLUMETO'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DELETE_X_BLOCKS contains %1 
    def test_DELETE_X_BLOCKS(self):
        key = 'DELETE_X_BLOCKS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DELETE_ALL_BLOCKS contains %1 
    def test_DELETE_ALL_BLOCKS(self):
        key = 'DELETE_ALL_BLOCKS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/RENAME_VARIABLE_TITLE contains %1 
    def test_RENAME_VARIABLE_TITLE(self):
        key = 'RENAME_VARIABLE_TITLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS contains %1 
    def test_VARIABLE_ALREADY_EXISTS(self):
        key = 'VARIABLE_ALREADY_EXISTS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE contains %1 %2
    def test_VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE(self):
        key = 'VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DELETE_VARIABLE_CONFIRMATION contains %1 
    def test_DELETE_VARIABLE_CONFIRMATION(self):
        key = 'DELETE_VARIABLE_CONFIRMATION'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/CANNOT_DELETE_VARIABLE_PROCEDURE contains %1 
    def test_CANNOT_DELETE_VARIABLE_PROCEDURE(self):
        key = 'CANNOT_DELETE_VARIABLE_PROCEDURE'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DELETE_VARIABLE contains %1 
    def test_DELETE_VARIABLE(self):
        key = 'DELETE_VARIABLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/PROCEDURE_ALREADY_EXISTS contains %1 
    def test_PROCEDURE_ALREADY_EXISTS(self):
        key = 'PROCEDURE_ALREADY_EXISTS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/LIST_ALREADY_EXISTS contains %1 
    def test_LIST_ALREADY_EXISTS(self):
        key = 'LIST_ALREADY_EXISTS'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/RENAME_LIST_TITLE contains %1 
    def test_RENAME_LIST_TITLE(self):
        key = 'RENAME_LIST_TITLE'
        self.check_key_exists(key)
        self.check_param(key, '%1')

    # mscratch-i18n/blocks/DATA_ITEMNUMOFLIST contains %1 %2
    def test_DATA_ITEMNUMOFLIST(self):
        key = 'DATA_ITEMNUMOFLIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')
        self.check_param(key, '%2')

    # mscratch-i18n/blocks/DELETE_LIST contains %1 
    def test_DELETE_LIST(self):
        key = 'DELETE_LIST'
        self.check_key_exists(key)
        self.check_param(key, '%1')


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(BlocksTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
