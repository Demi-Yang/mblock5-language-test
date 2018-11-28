# coding:utf-8
# import requests
import json
import re
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

from util import data_handle

# ======================  mscratch項目-翻译检查  =======================

class MscratchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lang = sys.argv[1]
        cls.path = os.getcwd() + '/FORMAT_RESULT/' + lang + '.json'
        f = open(cls.path, 'r')
        test_file = data_handle.byteify(json.load(f))
        cls.test_dict = test_file['mscratch-i18n']
        cls.gui = cls.test_dict['gui']
        cls.blocks = cls.test_dict['blocks']
        cls.extensions = cls.test_dict['extensions']
        cls.extensions_music = cls.extensions['music']
        cls.extensions_pen = cls.extensions['pen']

    # @classmethod
    # def tearDownClass(cls):
    #     print('\n\n====: ' + lang + ' translation test of module mscratch is completed')

    # mscratch-i18n/No empty value
    def test_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')



    # ==== -mscratch-gui-翻译检查  ===


    # mscratch-i18n/gui/No empty value
    def test_gui_no_empty_value(self):
        for key,value in self.gui.items():
            self.assertIsNotNone(value, "该字段的翻译为空，错误的 key: " + key)
            self.assertNotEqual(value, '', "该字段的翻译为空，错误的 key: " + key)

    # mscratch-i18n/gui/No new or missing items
    def test_gui_no_new_or_missing_items(self):
        self.assertEqual(len(self.gui), 194, "mscratch-i18n/gui/ 模块下新增或删减了翻译字段")

    # mscratch-i18n/gui/gui.modal.inputTip contains （&<>'\"）"
    def test_gui_modal_inputTip(self):
        key = 'gui.modal.inputTip'
        self.assertIn(key, self.gui, "缺少翻译字段，错误 key: " + key)
        test_data = self.gui[key]
        r = re.compile(r'.&.<.>.\'.\"')
        # print(r.findall(test_data))
        self.assertRegexpMatches(test_data, r, "没有包含 &<>'\"，错误 key: " + key)

    # mscratch-i18n/gui/gui.modal.confirmDeleteVariable contains %2 %1 
    def test_gui_modal_confirmDeleteVariable(self):
        key = 'gui.modal.confirmDeleteVariable'
        self.assertIn(key, self.gui, "缺少翻译字段，错误 key: " + key)
        test_data = self.gui[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2 ,错误 key: " + key)


    # ==== -mscratch-blocks-翻译检查  ===


    # mscratch-i18n/blocks/No empty value
    def test_blocks_no_empty_value(self):
        for key,value in self.blocks.items():
            self.assertIsNotNone(value, "该字段的翻译为空，错误 key: " + key)
            self.assertNotEqual(value, '', "该字段的翻译为空，错误 key: " + key)

    # mscratch-i18n/blocks/No new or missing items
    def test_blocks_no_new_or_missing_items(self):
        self.assertEqual(len(self.blocks), 301, "mscratch-i18n/blocks/ 模块下新增或删减了翻译字段")

    # mscratch-i18n/blocks/CONTROL_REPEAT contains %2 %1 
    def test_blocks_CONTROL_REPEAT(self):
        key = 'CONTROL_REPEAT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/CONTROL_WAIT contains %1 
    def test_blocks_CONTROL_WAIT(self):
        key = 'CONTROL_WAIT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/CONTROL_WAITUNTIL contains %1 
    def test_blocks_CONTROL_WAITUNTIL(self):
        key = 'CONTROL_WAITUNTIL'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/CONTROL_REPEATUNTIL contains %1 
    def test_blocks_CONTROL_REPEATUNTIL(self):
        key = 'CONTROL_REPEATUNTIL'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)


    # mscratch-i18n/blocks/CONTROL_WHILE contains %1 
    def test_blocks_CONTROL_WHILE(self):
        key = 'CONTROL_WHILE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/CONTROL_FOREACH contains %1 %2
    def test_blocks_CONTROL_FOREACH(self):
        key = 'CONTROL_FOREACH'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/CONTROL_CREATECLONEOF contains %1 
    def test_blocks_CONTROL_CREATECLONEOF(self):
        key = 'CONTROL_CREATECLONEOF'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_SETVARIABLETO contains %1 %2
    def test_blocks_DATA_SETVARIABLETO(self):
        key = 'DATA_SETVARIABLETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_CHANGEVARIABLEBY contains %1 %2
    def test_blocks_DATA_CHANGEVARIABLEBY(self):
        key = 'DATA_CHANGEVARIABLEBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_SHOWVARIABLE contains %1 
    def test_blocks_DATA_SHOWVARIABLE(self):
        key = 'DATA_SHOWVARIABLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_HIDEVARIABLE contains %1 
    def test_blocks_DATA_HIDEVARIABLE(self):
        key = 'DATA_HIDEVARIABLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)


    # mscratch-i18n/blocks/DATA_ADDTOLIST contains %1 %2
    def test_blocks_DATA_ADDTOLIST(self):
        key = 'DATA_ADDTOLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)


    # mscratch-i18n/blocks/DATA_DELETEOFLIST contains %1 %2
    def test_blocks_DATA_DELETEOFLIST(self):
        key = 'DATA_DELETEOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_DELETEALLOFLIST contains %1 
    def test_blocks_DATA_DELETEALLOFLIST(self):
        key = 'DATA_DELETEALLOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_INSERTATLIST contains %1 %2 %3
    def test_blocks_DATA_INSERTATLIST(self):
        key = 'DATA_INSERTATLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)
        self.assertIn('%3', test_data, "缺少参数 %3，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_REPLACEITEMOFLIST contains %1 
    def test_blocks_DATA_REPLACEITEMOFLIST(self):
        key = 'DATA_REPLACEITEMOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)
        self.assertIn('%3', test_data, "缺少参数 %3，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_ITEMOFLIST contains %1 
    def test_blocks_DATA_ITEMOFLIST(self):
        key = 'DATA_ITEMOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_LENGTHOFLIST contains %1 
    def test_blocks_DATA_LENGTHOFLIST(self):
        key = 'DATA_LENGTHOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_LISTCONTAINSITEM contains %1 %2
    def test_blocks_DATA_LISTCONTAINSITEM(self):
        key = 'DATA_LISTCONTAINSITEM'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_SHOWLIST contains %1 
    def test_blocks_DATA_SHOWLIST(self):
        key = 'DATA_SHOWLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_HIDELIST contains %1 
    def test_blocks_DATA_HIDELIST(self):
        key = 'DATA_HIDELIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENFLAGCLICKED contains %1 
    def test_blocks_EVENT_WHENFLAGCLICKED(self):
        key = 'EVENT_WHENFLAGCLICKED'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENTOUCHINGOBJECT contains %1 
    def test_blocks_EVENT_WHENTOUCHINGOBJECT(self):
        key = 'EVENT_WHENTOUCHINGOBJECT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENBROADCASTRECEIVED contains %1 
    def test_blocks_EVENT_WHENBROADCASTRECEIVED(self):
        key = 'EVENT_WHENBROADCASTRECEIVED'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENBACKDROPSWITCHESTO contains %1 
    def test_blocks_EVENT_WHENBACKDROPSWITCHESTO(self):
        key = 'EVENT_WHENBACKDROPSWITCHESTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENGREATERTHAN contains %1 > %2
    def test_blocks_EVENT_WHENGREATERTHAN(self):
        key = 'EVENT_WHENGREATERTHAN'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1 > %2', test_data, "未匹配到 %1 > %2，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_BROADCAST contains %1 
    def test_blocks_EVENT_BROADCAST(self):
        key = 'EVENT_BROADCAST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_BROADCASTANDWAIT contains %1 
    def test_blocks_EVENT_BROADCASTANDWAIT(self):
        key = 'EVENT_BROADCASTANDWAIT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/EVENT_WHENKEYPRESSED contains %1 
    def test_blocks_EVENT_WHENKEYPRESSED(self):
        key = 'EVENT_WHENKEYPRESSED'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SAYFORSECS contains %1 %2
    def test_blocks_LOOKS_SAYFORSECS(self):
        key = 'LOOKS_SAYFORSECS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SAY contains %1 
    def test_blocks_LOOKS_SAY(self):
        key = 'LOOKS_SAY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_THINKFORSECS contains %1 %2
    def test_blocks_LOOKS_THINKFORSECS(self):
        key = 'LOOKS_THINKFORSECS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_THINK contains %1 
    def test_blocks_LOOKS_THINK(self):
        key = 'LOOKS_THINK'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_CHANGEEFFECTBY contains %1 %2
    def test_blocks_LOOKS_CHANGEEFFECTBY(self):
        key = 'LOOKS_CHANGEEFFECTBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SETEFFECTTO contains %1 %2
    def test_blocks_LOOKS_SETEFFECTTO(self):
        key = 'LOOKS_SETEFFECTTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_CHANGESIZEBY contains %1 
    def test_blocks_LOOKS_CHANGESIZEBY(self):
        key = 'LOOKS_CHANGESIZEBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SETSIZETO contains %1 
    def test_blocks_LOOKS_SETSIZETO(self):
        key = 'LOOKS_SETSIZETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_CHANGESTRETCHBY contains %1 
    def test_blocks_LOOKS_CHANGESTRETCHBY(self):
        key = 'LOOKS_CHANGESTRETCHBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SETSTRETCHTO contains %1 
    def test_blocks_LOOKS_SETSTRETCHTO(self):
        key = 'LOOKS_SETSTRETCHTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SWITCHCOSTUMETO contains %1 
    def test_blocks_LOOKS_SWITCHCOSTUMETO(self):
        key = 'LOOKS_SWITCHCOSTUMETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        
    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTO contains %1 
    def test_blocks_LOOKS_SWITCHBACKDROPTO(self):
        key = 'LOOKS_SWITCHBACKDROPTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_GOTOFRONTBACK contains %1 
    def test_blocks_LOOKS_GOTOFRONTBACK(self):
        key = 'LOOKS_GOTOFRONTBACK'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_GOFORWARDBACKWARDLAYERS contains %1 
    def test_blocks_LOOKS_GOFORWARDBACKWARDLAYERS(self):
        key = 'LOOKS_GOFORWARDBACKWARDLAYERS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_BACKDROPNUMBERNAME contains %1 
    def test_blocks_LOOKS_BACKDROPNUMBERNAME(self):
        key = 'LOOKS_BACKDROPNUMBERNAME'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_COSTUMENUMBERNAME contains %1 
    def test_blocks_LOOKS_COSTUMENUMBERNAME(self):
        key = 'LOOKS_COSTUMENUMBERNAME'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTOANDWAIT contains %1 
    def test_blocks_LOOKS_SWITCHBACKDROPTOANDWAIT(self):
        key = 'LOOKS_SWITCHBACKDROPTOANDWAIT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_MOVESTEPS contains %1 
    def test_blocks_MOTION_MOVESTEPS(self):
        key = 'MOTION_MOVESTEPS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_TURNLEFT contains %1 
    def test_blocks_MOTION_TURNLEFT(self):
        key = 'MOTION_TURNLEFT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_TURNRIGHT contains %1 
    def test_blocks_MOTION_TURNRIGHT(self):
        key = 'MOTION_TURNRIGHT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_POINTINDIRECTION contains %1 
    def test_blocks_MOTION_POINTINDIRECTION(self):
        key = 'MOTION_POINTINDIRECTION'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_POINTTOWARDS contains %1 
    def test_blocks_MOTION_POINTTOWARDS(self):
        key = 'MOTION_POINTTOWARDS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_GOTO contains %1 
    def test_blocks_MOTION_GOTO(self):
        key = 'MOTION_GOTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_GOTOXY contains  x: %1 y: %2
    def test_blocks_MOTION_GOTOXY(self):
        key = 'MOTION_GOTOXY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn(' x: %1 y: %2', test_data, "未匹配到 x: %1 y: %2，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_GLIDESECSTOXY contains %1 and x: %2 y: %3
    def test_blocks_MOTION_GLIDESECSTOXY(self):
        key = 'MOTION_GLIDESECSTOXY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn(' x: %2 y: %3', test_data, "未匹配到 x: %2 y: %3，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_GLIDETO contains %1 
    def test_blocks_MOTION_GLIDETO(self):
        key = 'MOTION_GLIDETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_CHANGEXBY contains %1 and x
    def test_blocks_MOTION_CHANGEXBY(self):
        key = 'MOTION_CHANGEXBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn(' x ', test_data, "缺少字段 x，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_SETX contains %1 and x
    def test_blocks_MOTION_SETX(self):
        key = 'MOTION_SETX'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn(' x ', test_data, "缺少字段 x，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_CHANGEYBY contains %1 and y
    def test_blocks_MOTION_CHANGEYBY(self):
        key = 'MOTION_CHANGEYBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn(' y ', test_data, "缺少字段 y，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_SETY contains %1 and y
    def test_blocks_MOTION_SETY(self):
        key = 'MOTION_SETY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn(' y ', test_data, "缺少字段 y，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_SETROTATIONSTYLE contains %1 
    def test_blocks_MOTION_SETROTATIONSTYLE(self):
        key = 'MOTION_SETROTATIONSTYLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_XPOSITION contains %1 
    def test_blocks_MOTION_XPOSITION(self):
        key = 'MOTION_XPOSITION'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('x', test_data, "缺少字段 x，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_YPOSITION contains %1 
    def test_blocks_MOTION_YPOSITION(self):
        key = 'MOTION_YPOSITION'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('y', test_data, "缺少字段 y，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_SCROLLRIGHT contains %1 
    def test_blocks_MOTION_SCROLLRIGHT(self):
        key = 'MOTION_SCROLLRIGHT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_SCROLLUP contains %1 
    def test_blocks_MOTION_SCROLLUP(self):
        key = 'MOTION_SCROLLUP'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_ALIGNSCENE contains %1 
    def test_blocks_MOTION_ALIGNSCENE(self):
        key = 'MOTION_ALIGNSCENE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_XSCROLL contains x
    def test_blocks_MOTION_XSCROLL(self):
        key = 'MOTION_XSCROLL'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('x ', test_data, "缺少字段 x，错误 key: " + key)

    # mscratch-i18n/blocks/MOTION_YSCROLL contains y 
    def test_blocks_MOTION_YSCROLL(self):
        key = 'MOTION_YSCROLL'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('y ', test_data, "缺少字段 y，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_ADD contains '%1 + %2'
    def test_blocks_OPERATORS_ADD(self):
        key = 'OPERATORS_ADD'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 + %2', "未匹配到 %1 + %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_SUBTRACT contains '%1 - %2'
    def test_blocks_OPERATORS_SUBTRACT(self):
        key = 'OPERATORS_SUBTRACT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 - %2', "未匹配到 %1 - %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_MULTIPLY contains '%1 * %2' 
    def test_blocks_OPERATORS_MULTIPLY(self):
        key = 'OPERATORS_MULTIPLY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 * %2', "未匹配到 %1 * %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_DIVIDE contains '%1 / %2'
    def test_blocks_OPERATORS_DIVIDE(self):
        key = 'OPERATORS_DIVIDE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 / %2', "未匹配到 %1 / %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_RANDOM contains %1 %2
    def test_blocks_OPERATORS_RANDOM(self):
        key = 'OPERATORS_RANDOM'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_GT contains %1 > %2 
    def test_blocks_OPERATORS_GT(self):
        key = 'OPERATORS_GT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 > %2', "未匹配到 %1 > %2，错误 key: " + key)


    # mscratch-i18n/blocks/OPERATORS_LT contains %1 < %2
    def test_blocks_OPERATORS_LT(self):
        key = 'OPERATORS_LT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 < %2', "未匹配到 %1 < %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_EQUALS contains %1 = %2
    def test_blocks_OPERATORS_EQUALS(self):
        key = 'OPERATORS_EQUALS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertEqual(test_data, '%1 = %2', "未匹配到 %1 = %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_AND contains %1 %2
    def test_blocks_OPERATORS_AND(self):
        key = 'OPERATORS_AND'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_OR contains %1 %2
    def test_blocks_OPERATORS_OR(self):
        key = 'OPERATORS_OR'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_NOT contains %1 
    def test_blocks_OPERATORS_NOT(self):
        key = 'OPERATORS_NOT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_JOIN contains %1 
    def test_blocks_OPERATORS_JOIN(self):
        key = 'OPERATORS_JOIN'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_LETTEROF contains %1 
    def test_blocks_OPERATORS_LETTEROF(self):
        key = 'OPERATORS_LETTEROF'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_LENGTH contains %1 
    def test_blocks_OPERATORS_LENGTH(self):
        key = 'OPERATORS_LENGTH'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_CONTAINS contains %1 
    def test_blocks_OPERATORS_CONTAINS(self):
        key = 'OPERATORS_CONTAINS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_MOD contains %1 
    def test_blocks_OPERATORS_MOD(self):
        key = 'OPERATORS_MOD'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_ROUND contains %1 
    def test_blocks_OPERATORS_ROUND(self):
        key = 'OPERATORS_ROUND'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/OPERATORS_MATHOP contains %1 
    def test_blocks_OPERATORS_MATHOP(self):
        key = 'OPERATORS_MATHOP'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/PROCEDURES_DEFINITION contains %1 
    def test_blocks_PROCEDURES_DEFINITION(self):
        key = 'PROCEDURES_DEFINITION'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_TOUCHINGOBJECT contains %1 
    def test_blocks_SENSING_TOUCHINGOBJECT(self):
        key = 'SENSING_TOUCHINGOBJECT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_TOUCHINGCOLOR contains %1 
    def test_blocks_SENSING_TOUCHINGCOLOR(self):
        key = 'SENSING_TOUCHINGCOLOR'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        
    # mscratch-i18n/blocks/SENSING_COLORISTOUCHINGCOLOR contains %1 %2
    def test_blocks_SENSING_COLORISTOUCHINGCOLOR(self):
        key = 'SENSING_COLORISTOUCHINGCOLOR'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)
    
    # mscratch-i18n/blocks/SENSING_DISTANCETO contains %1 
    def test_blocks_SENSING_DISTANCETO(self):
        key = 'SENSING_DISTANCETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_ASKANDWAIT contains %1 
    def test_blocks_SENSING_ASKANDWAIT(self):
        key = 'SENSING_ASKANDWAIT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_KEYPRESSED contains %1 
    def test_blocks_SENSING_KEYPRESSED(self):
        key = 'SENSING_KEYPRESSED'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_SETDRAGMODE contains %1 
    def test_blocks_SENSING_SETDRAGMODE(self):
        key = 'SENSING_SETDRAGMODE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_OF contains %1 %2
    def test_blocks_SENSING_OF(self):
        key = 'SENSING_OF'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/SENSING_CURRENT contains %1 
    def test_blocks_SENSING_CURRENT(self):
        key = 'SENSING_CURRENT'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SOUND_PLAY contains %1 
    def test_blocks_SOUND_PLAY(self):
        key = 'SOUND_PLAY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SOUND_PLAYUNTILDONE contains %1 
    def test_blocks_SOUND_PLAYUNTILDONE(self):
        key = 'SOUND_PLAYUNTILDONE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/SOUND_SETEFFECTO contains %1 %2
    def test_blocks_SOUND_SETEFFECTO(self):
        key = 'SOUND_SETEFFECTO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/SOUND_CHANGEEFFECTBY contains %1 %2
    def test_blocks_SOUND_CHANGEEFFECTBY(self):
        key = 'SOUND_CHANGEEFFECTBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/SOUND_CHANGEVOLUMEBY contains %1 
    def test_blocks_SOUND_CHANGEVOLUMEBY(self):
        key = 'SOUND_CHANGEVOLUMEBY'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
    
    # mscratch-i18n/blocks/SOUND_SETVOLUMETO contains %1 
    def test_blocks_SOUND_SETVOLUMETO(self):
        key = 'SOUND_SETVOLUMETO'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DELETE_X_BLOCKS contains %1 
    def test_blocks_DELETE_X_BLOCKS(self):
        key = 'DELETE_X_BLOCKS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DELETE_ALL_BLOCKS contains %1 
    def test_blocks_DELETE_ALL_BLOCKS(self):
        key = 'DELETE_ALL_BLOCKS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/RENAME_VARIABLE_TITLE contains %1 
    def test_blocks_RENAME_VARIABLE_TITLE(self):
        key = 'RENAME_VARIABLE_TITLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS contains %1 
    def test_blocks_VARIABLE_ALREADY_EXISTS(self):
        key = 'VARIABLE_ALREADY_EXISTS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE contains %1 %2
    def test_blocks_VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE(self):
        key = 'VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DELETE_VARIABLE_CONFIRMATION contains %1 
    def test_blocks_DELETE_VARIABLE_CONFIRMATION(self):
        key = 'DELETE_VARIABLE_CONFIRMATION'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/CANNOT_DELETE_VARIABLE_PROCEDURE contains %1 
    def test_blocks_CANNOT_DELETE_VARIABLE_PROCEDURE(self):
        key = 'CANNOT_DELETE_VARIABLE_PROCEDURE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DELETE_VARIABLE contains %1 
    def test_blocks_DELETE_VARIABLE(self):
        key = 'DELETE_VARIABLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/PROCEDURE_ALREADY_EXISTS contains %1 
    def test_blocks_PROCEDURE_ALREADY_EXISTS(self):
        key = 'PROCEDURE_ALREADY_EXISTS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/LIST_ALREADY_EXISTS contains %1 
    def test_blocks_LIST_ALREADY_EXISTS(self):
        key = 'LIST_ALREADY_EXISTS'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/RENAME_LIST_TITLE contains %1 
    def test_blocks_RENAME_LIST_TITLE(self):
        key = 'RENAME_LIST_TITLE'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)

    # mscratch-i18n/blocks/DATA_ITEMNUMOFLIST contains %1 %2
    def test_blocks_DATA_ITEMNUMOFLIST(self):
        key = 'DATA_ITEMNUMOFLIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)
        self.assertIn('%2', test_data, "缺少参数 %2，错误 key: " + key)

    # mscratch-i18n/blocks/DELETE_LIST contains %1 
    def test_blocks_DELETE_LIST(self):
        key = 'DELETE_LIST'
        self.assertIn(key, self.blocks, "缺少翻译字段，错误 key: " + key)
        test_data = self.blocks[key]
        self.assertIn('%1', test_data, "缺少参数 %1，错误 key: " + key)


    # ==== -mscratch-extensions-翻译检查  ===


    # mscratch-i18n/extensions/music/No empty value
    def test_extensions_music_no_empty_value(self):
        for key,value in self.extensions_music.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mscratch-i18n/extensions/No new or missing items
    def test_extensions_no_new_or_missing_items(self):
        self.assertEqual(len(self.extensions), 2)

    # mscratch-i18n/extensions/music/No new or missing items
    def test_extensions_music_no_new_or_missing_items(self):
        self.assertEqual(len(self.extensions_music), 47)

    # mscratch-i18n/extensions/pen/No new items or missing items
    def test_extensions_pen_no_new_or_missing_items(self):
        self.assertEqual(len(self.extensions_pen), 18)

    # mscratch-i18n/extensions/music/music.playDrumForBeats contains [DRUM] [BEATS]
    def test_extensions_music_playDrumForBeats(self):
        key = 'music.playDrumForBeats'
        self.assertIn('music.playDrumForBeats', self.extensions_music, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_music['music.playDrumForBeats']
        self.assertIn('[DRUM]', test_data, "缺少参数 [DRUM]，错误 key: " + key)
        self.assertIn('[BEATS]', test_data, "缺少参数 [BEATS]，错误 key: " + key)

    # mscratch-i18n/extensions/music/music.playNoteForBeats contains [BEATS]
    def test_extensions_music_playNoteForBeats(self):
        key = 'music.playNoteForBeats'
        self.assertIn(key, self.extensions_music, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_music[key]
        self.assertIn('[BEATS]', test_data, "缺少参数 [BEATS]，错误 key: " + key)

    # mscratch-i18n/extensions/music/music.setInstrument contains [INSTRUMENT]
    def test_extensions_music_setInstrument(self):
        key = 'music.setInstrument'
        self.assertIn(key, self.extensions_music, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_music[key]
        self.assertIn('[INSTRUMENT]', test_data, "缺少参数 [INSTRUMENT]，错误 key: " + key)

    # mscratch-i18n/extensions/music/music.setTempo contains [DRUM] [TEMPO]
    def test_extensions_music_setTempo(self):
        key = 'music.setTempo'
        self.assertIn(key, self.extensions_music, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_music[key]
        self.assertIn('[TEMPO]', test_data, "缺少参数 [TEMPO]，错误 key: " + key)

    # mscratch-i18n/extensions/music/music.changeTempo contains [DRUM] [TEMPO]
    def test_extensions_music_changeTempo(self):
        key = 'music.changeTempo'
        self.assertIn(key, self.extensions_music, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_music[key]
        self.assertIn('[TEMPO]', test_data, "缺少参数 [TEMPO]，错误 key: " + key)


    # mscratch-i18n/extensions/pen/No empty value
    def test_extensions_pen_no_empty_value(self):
        for key,value in self.extensions_pen.items():
            self.assertIsNotNone(value, "该字段的翻译为空，错误 key: " + key)
            self.assertNotEqual(value, '', "该字段的翻译为空，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setColor contains [COLOR] 
    def test_extensions_pen_setColor(self):
        key = 'pen.setColor'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[COLOR]', test_data, "缺少参数 [COLOR]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.changeColorParam contains [COLOR_PARAM] [VALUE] 
    def test_extensions_pen_changeColorParam(self):
        key = 'pen.changeColorParam'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[COLOR_PARAM]', test_data, "缺少参数 [COLOR_PARAM]，错误 key: " + key)
        self.assertIn('[VALUE]', test_data, "缺少参数 [VALUE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setColorParam contains [COLOR_PARAM] [VALUE] 
    def test_extensions_pen_setColorParam(self):
        key = 'pen.setColorParam'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[COLOR_PARAM]', test_data, "缺少参数 [COLOR_PARAM]，错误 key: " + key)
        self.assertIn('[VALUE]', test_data, "缺少参数 [VALUE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.changeSize contains [SIZE] 
    def test_extensions_pen_changeSize(self):
        key = 'pen.changeSize'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[SIZE]', test_data, "缺少参数 [SIZE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setSize contains [SIZE] 
    def test_extensions_pen_setSize(self):
        key = 'pen.setSize'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[SIZE]', test_data, "缺少参数 [SIZE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setShade contains [SHADE] 
    def test_extensions_pen_setShade(self):
        key = 'pen.setShade'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[SHADE]', test_data, "缺少参数 [SHADE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.changeShade contains [SHADE] 
    def test_extensions_pen_changeShade(self):
        key = 'pen.changeShade'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[SHADE]', test_data, "缺少参数 [SHADE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.setHue contains [HUE] 
    def test_extensions_pen_setHue(self):
        key = 'pen.setHue'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[HUE]', test_data, "缺少参数 [HUE]，错误 key: " + key)

    # mscratch-i18n/extensions/pen/pen.changeHue contains [HUE] 
    def test_extensions_pen_changeHue(self):
        key = 'pen.changeHue'
        self.assertIn(key, self.extensions_pen, "缺少翻译字段，错误 key: " + key)
        test_data = self.extensions_pen[key]
        self.assertIn('[HUE]', test_data, "缺少参数 [HUE]，错误 key: " + key)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MscratchTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
