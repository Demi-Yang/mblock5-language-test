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
    def test_mscratch_i18n_no_empty_value(self):
        for key,value in self.test_dict.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')



    # ==== -mscratch-gui-翻译检查  ===


    # mscratch-i18n/gui/No empty value
    def test_mscratch_i18n_gui_no_empty_value(self):
        for key,value in self.gui.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mscratch-i18n/gui/gui.modal.inputTip contains （&<>'\"）"
    def test_mscratch_i18n_gui_modal_inputTip(self):
        self.assertIn('gui.modal.inputTip', self.gui)
        test_data = self.gui['gui.modal.inputTip']
        r = re.compile(r'.&.<.>.\'.\"')
        # print(r.findall(test_data))
        self.assertRegexpMatches(test_data, r)

    # mscratch-i18n/gui/gui.modal.confirmDeleteVariable contains %2 %1 
    def test_mscratch_i18n_gui_modal_confirmDeleteVariable(self):
        self.assertIn('gui.modal.confirmDeleteVariable', self.gui)
        test_data = self.gui['gui.modal.confirmDeleteVariable']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)


    # ==== -mscratch-blocks-翻译检查  ===


    # mscratch-i18n/blocks/No empty value
    def test_mscratch_i18n_blocks_no_empty_value(self):
        for key,value in self.blocks.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mscratch-i18n/blocks/CONTROL_REPEAT contains %2 %1 
    def test_mscratch_i18n_blocks_CONTROL_REPEAT(self):
        self.assertIn('CONTROL_REPEAT', self.blocks)
        test_data = self.blocks['CONTROL_REPEAT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/CONTROL_WAIT contains %1 
    def test_mscratch_i18n_blocks_CONTROL_WAIT(self):
        self.assertIn('CONTROL_WAIT', self.blocks)
        test_data = self.blocks['CONTROL_WAIT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/CONTROL_WAITUNTIL contains %1 
    def test_mscratch_i18n_blocks_CONTROL_WAITUNTIL(self):
        self.assertIn('CONTROL_WAITUNTIL', self.blocks)
        test_data = self.blocks['CONTROL_WAITUNTIL']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/CONTROL_REPEATUNTIL contains %1 
    def test_mscratch_i18n_blocks_CONTROL_REPEATUNTIL(self):
        self.assertIn('CONTROL_REPEATUNTIL', self.blocks)
        test_data = self.blocks['CONTROL_REPEATUNTIL']
        self.assertIn('%1', test_data)


    # mscratch-i18n/blocks/CONTROL_WHILE contains %1 
    def test_mscratch_i18n_blocks_CONTROL_WHILE(self):
        self.assertIn('CONTROL_WHILE', self.blocks)
        test_data = self.blocks['CONTROL_WHILE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/CONTROL_FOREACH contains %1 %2
    def test_mscratch_i18n_blocks_CONTROL_FOREACH(self):
        self.assertIn('CONTROL_FOREACH', self.blocks)
        test_data = self.blocks['CONTROL_FOREACH']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/CONTROL_CREATECLONEOF contains %1 
    def test_mscratch_i18n_blocks_CONTROL_CREATECLONEOF(self):
        self.assertIn('CONTROL_CREATECLONEOF', self.blocks)
        test_data = self.blocks['CONTROL_CREATECLONEOF']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_SETVARIABLETO contains %1 %2
    def test_mscratch_i18n_blocks_DATA_SETVARIABLETO(self):
        self.assertIn('DATA_SETVARIABLETO', self.blocks)
        test_data = self.blocks['DATA_SETVARIABLETO']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DATA_CHANGEVARIABLEBY contains %1 %2
    def test_mscratch_i18n_blocks_DATA_CHANGEVARIABLEBY(self):
        self.assertIn('DATA_CHANGEVARIABLEBY', self.blocks)
        test_data = self.blocks['DATA_CHANGEVARIABLEBY']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DATA_SHOWVARIABLE contains %1 
    def test_mscratch_i18n_blocks_DATA_SHOWVARIABLE(self):
        self.assertIn('DATA_SHOWVARIABLE', self.blocks)
        test_data = self.blocks['DATA_SHOWVARIABLE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_HIDEVARIABLE contains %1 
    def test_mscratch_i18n_blocks_DATA_HIDEVARIABLE(self):
        self.assertIn('DATA_HIDEVARIABLE', self.blocks)
        test_data = self.blocks['DATA_HIDEVARIABLE']
        self.assertIn('%1', test_data)


    # mscratch-i18n/blocks/DATA_ADDTOLIST contains %1 %2
    def test_mscratch_i18n_blocks_DATA_ADDTOLIST(self):
        self.assertIn('DATA_ADDTOLIST', self.blocks)
        test_data = self.blocks['DATA_ADDTOLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)


    # mscratch-i18n/blocks/DATA_DELETEOFLIST contains %1 %2
    def test_mscratch_i18n_blocks_DATA_DELETEOFLIST(self):
        self.assertIn('DATA_DELETEOFLIST', self.blocks)
        test_data = self.blocks['DATA_DELETEOFLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DATA_DELETEALLOFLIST contains %1 
    def test_mscratch_i18n_blocks_DATA_DELETEALLOFLIST(self):
        self.assertIn('DATA_DELETEALLOFLIST', self.blocks)
        test_data = self.blocks['DATA_DELETEALLOFLIST']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_INSERTATLIST contains %1 %2 %3
    def test_mscratch_i18n_blocks_DATA_INSERTATLIST(self):
        self.assertIn('DATA_INSERTATLIST', self.blocks)
        test_data = self.blocks['DATA_INSERTATLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)
        self.assertIn(' %3', test_data)

    # mscratch-i18n/blocks/DATA_REPLACEITEMOFLIST contains %1 
    def test_mscratch_i18n_blocks_DATA_REPLACEITEMOFLIST(self):
        self.assertIn('DATA_REPLACEITEMOFLIST', self.blocks)
        test_data = self.blocks['DATA_REPLACEITEMOFLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)
        self.assertIn(' %3', test_data)

    # mscratch-i18n/blocks/DATA_ITEMOFLIST contains %1 
    def test_mscratch_i18n_blocks_DATA_ITEMOFLIST(self):
        self.assertIn('DATA_ITEMOFLIST', self.blocks)
        test_data = self.blocks['DATA_ITEMOFLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DATA_LENGTHOFLIST contains %1 
    def test_mscratch_i18n_blocks_DATA_LENGTHOFLIST(self):
        self.assertIn('DATA_LENGTHOFLIST', self.blocks)
        test_data = self.blocks['DATA_LENGTHOFLIST']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_LISTCONTAINSITEM contains %1 %2
    def test_mscratch_i18n_blocks_DATA_LISTCONTAINSITEM(self):
        self.assertIn('DATA_LISTCONTAINSITEM', self.blocks)
        test_data = self.blocks['DATA_LISTCONTAINSITEM']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DATA_SHOWLIST contains %1 
    def test_mscratch_i18n_blocks_DATA_SHOWLIST(self):
        self.assertIn('DATA_SHOWLIST', self.blocks)
        test_data = self.blocks['DATA_SHOWLIST']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_HIDELIST contains %1 
    def test_mscratch_i18n_blocks_DATA_HIDELIST(self):
        self.assertIn('DATA_HIDELIST', self.blocks)
        test_data = self.blocks['DATA_HIDELIST']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENFLAGCLICKED contains %1 
    def test_mscratch_i18n_blocks_EVENT_WHENFLAGCLICKED(self):
        self.assertIn('EVENT_WHENFLAGCLICKED', self.blocks)
        test_data = self.blocks['EVENT_WHENFLAGCLICKED']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENTOUCHINGOBJECT contains %1 
    def test_mscratch_i18n_blocks_EVENT_WHENTOUCHINGOBJECT(self):
        self.assertIn('EVENT_WHENTOUCHINGOBJECT', self.blocks)
        test_data = self.blocks['EVENT_WHENTOUCHINGOBJECT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENBROADCASTRECEIVED contains %1 
    def test_mscratch_i18n_blocks_EVENT_WHENBROADCASTRECEIVED(self):
        self.assertIn('EVENT_WHENBROADCASTRECEIVED', self.blocks)
        test_data = self.blocks['EVENT_WHENBROADCASTRECEIVED']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENBACKDROPSWITCHESTO contains %1 
    def test_mscratch_i18n_blocks_EVENT_WHENBACKDROPSWITCHESTO(self):
        self.assertIn('EVENT_WHENBACKDROPSWITCHESTO', self.blocks)
        test_data = self.blocks['EVENT_WHENBACKDROPSWITCHESTO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENGREATERTHAN contains %1 > %2
    def test_mscratch_i18n_blocks_EVENT_WHENGREATERTHAN(self):
        self.assertIn('EVENT_WHENGREATERTHAN', self.blocks)
        test_data = self.blocks['EVENT_WHENGREATERTHAN']
        self.assertIn(' %1 > %2', test_data)

    # mscratch-i18n/blocks/EVENT_BROADCAST contains %1 
    def test_mscratch_i18n_blocks_EVENT_BROADCAST(self):
        self.assertIn('EVENT_BROADCAST', self.blocks)
        test_data = self.blocks['EVENT_BROADCAST']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_BROADCASTANDWAIT contains %1 
    def test_mscratch_i18n_blocks_EVENT_BROADCASTANDWAIT(self):
        self.assertIn('EVENT_BROADCASTANDWAIT', self.blocks)
        test_data = self.blocks['EVENT_BROADCASTANDWAIT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/EVENT_WHENKEYPRESSED contains %1 
    def test_mscratch_i18n_blocks_EVENT_WHENKEYPRESSED(self):
        self.assertIn('EVENT_WHENKEYPRESSED', self.blocks)
        test_data = self.blocks['EVENT_WHENKEYPRESSED']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_SAYFORSECS contains %1 %2
    def test_mscratch_i18n_blocks_LOOKS_SAYFORSECS(self):
        self.assertIn('LOOKS_SAYFORSECS', self.blocks)
        test_data = self.blocks['LOOKS_SAYFORSECS']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/LOOKS_SAY contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SAY(self):
        self.assertIn('LOOKS_SAY', self.blocks)
        test_data = self.blocks['LOOKS_SAY']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_THINKFORSECS contains %1 %2
    def test_mscratch_i18n_blocks_LOOKS_THINKFORSECS(self):
        self.assertIn('LOOKS_THINKFORSECS', self.blocks)
        test_data = self.blocks['LOOKS_THINKFORSECS']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/LOOKS_THINK contains %1 
    def test_mscratch_i18n_blocks_LOOKS_THINK(self):
        self.assertIn('LOOKS_THINK', self.blocks)
        test_data = self.blocks['LOOKS_THINK']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_CHANGEEFFECTBY contains %1 %2
    def test_mscratch_i18n_blocks_LOOKS_CHANGEEFFECTBY(self):
        self.assertIn('LOOKS_CHANGEEFFECTBY', self.blocks)
        test_data = self.blocks['LOOKS_CHANGEEFFECTBY']
        self.assertIn('%1', test_data)
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_SETEFFECTTO contains %1 %2
    def test_mscratch_i18n_blocks_LOOKS_SETEFFECTTO(self):
        self.assertIn('LOOKS_SETEFFECTTO', self.blocks)
        test_data = self.blocks['LOOKS_SETEFFECTTO']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/LOOKS_CHANGESIZEBY contains %1 
    def test_mscratch_i18n_blocks_LOOKS_CHANGESIZEBY(self):
        self.assertIn('LOOKS_CHANGESIZEBY', self.blocks)
        test_data = self.blocks['LOOKS_CHANGESIZEBY']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_SETSIZETO contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SETSIZETO(self):
        self.assertIn('LOOKS_SETSIZETO', self.blocks)
        test_data = self.blocks['LOOKS_SETSIZETO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_CHANGESTRETCHBY contains %1 
    def test_mscratch_i18n_blocks_LOOKS_CHANGESTRETCHBY(self):
        self.assertIn('LOOKS_CHANGESTRETCHBY', self.blocks)
        test_data = self.blocks['LOOKS_CHANGESTRETCHBY']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_SETSTRETCHTO contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SETSTRETCHTO(self):
        self.assertIn('LOOKS_SETSTRETCHTO', self.blocks)
        test_data = self.blocks['LOOKS_SETSTRETCHTO']
        self.assertIn(' %1 %', test_data)

    # mscratch-i18n/blocks/LOOKS_SWITCHCOSTUMETO contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SWITCHCOSTUMETO(self):
        self.assertIn('LOOKS_SWITCHCOSTUMETO', self.blocks)
        test_data = self.blocks['LOOKS_SWITCHCOSTUMETO']
        self.assertIn('%1', test_data)
        
    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTO contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SWITCHBACKDROPTO(self):
        self.assertIn('LOOKS_SWITCHBACKDROPTO', self.blocks)
        test_data = self.blocks['LOOKS_SWITCHBACKDROPTO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_GOTOFRONTBACK contains %1 
    def test_mscratch_i18n_blocks_LOOKS_GOTOFRONTBACK(self):
        self.assertIn('LOOKS_GOTOFRONTBACK', self.blocks)
        test_data = self.blocks['LOOKS_GOTOFRONTBACK']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_GOFORWARDBACKWARDLAYERS contains %1 
    def test_mscratch_i18n_blocks_LOOKS_GOFORWARDBACKWARDLAYERS(self):
        self.assertIn('LOOKS_GOFORWARDBACKWARDLAYERS', self.blocks)
        test_data = self.blocks['LOOKS_GOFORWARDBACKWARDLAYERS']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/LOOKS_BACKDROPNUMBERNAME contains %1 
    def test_mscratch_i18n_blocks_LOOKS_BACKDROPNUMBERNAME(self):
        self.assertIn('LOOKS_BACKDROPNUMBERNAME', self.blocks)
        test_data = self.blocks['LOOKS_BACKDROPNUMBERNAME']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_COSTUMENUMBERNAME contains %1 
    def test_mscratch_i18n_blocks_LOOKS_COSTUMENUMBERNAME(self):
        self.assertIn('LOOKS_COSTUMENUMBERNAME', self.blocks)
        test_data = self.blocks['LOOKS_COSTUMENUMBERNAME']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LOOKS_SWITCHBACKDROPTOANDWAIT contains %1 
    def test_mscratch_i18n_blocks_LOOKS_SWITCHBACKDROPTOANDWAIT(self):
        self.assertIn('LOOKS_SWITCHBACKDROPTOANDWAIT', self.blocks)
        test_data = self.blocks['LOOKS_SWITCHBACKDROPTOANDWAIT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_MOVESTEPS contains %1 
    def test_mscratch_i18n_blocks_MOTION_MOVESTEPS(self):
        self.assertIn('MOTION_MOVESTEPS', self.blocks)
        test_data = self.blocks['MOTION_MOVESTEPS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_TURNLEFT contains %1 
    def test_mscratch_i18n_blocks_MOTION_TURNLEFT(self):
        self.assertIn('MOTION_TURNLEFT', self.blocks)
        test_data = self.blocks['MOTION_TURNLEFT']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/MOTION_TURNRIGHT contains %1 
    def test_mscratch_i18n_blocks_MOTION_TURNRIGHT(self):
        self.assertIn('MOTION_TURNRIGHT', self.blocks)
        test_data = self.blocks['MOTION_TURNRIGHT']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/MOTION_POINTINDIRECTION contains %1 
    def test_mscratch_i18n_blocks_MOTION_POINTINDIRECTION(self):
        self.assertIn('MOTION_POINTINDIRECTION', self.blocks)
        test_data = self.blocks['MOTION_POINTINDIRECTION']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_POINTTOWARDS contains %1 
    def test_mscratch_i18n_blocks_MOTION_POINTTOWARDS(self):
        self.assertIn('MOTION_POINTTOWARDS', self.blocks)
        test_data = self.blocks['MOTION_POINTTOWARDS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_GOTO contains %1 
    def test_mscratch_i18n_blocks_MOTION_GOTO(self):
        self.assertIn('MOTION_GOTO', self.blocks)
        test_data = self.blocks['MOTION_GOTO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_GOTOXY contains  x: %1 y: %2
    def test_mscratch_i18n_blocks_MOTION_GOTOXY(self):
        self.assertIn('MOTION_GOTOXY', self.blocks)
        test_data = self.blocks['MOTION_GOTOXY']
        self.assertIn(' x: %1 y: %2', test_data)

    # mscratch-i18n/blocks/MOTION_GLIDESECSTOXY contains %1 and x: %2 y: %3
    def test_mscratch_i18n_blocks_MOTION_GLIDESECSTOXY(self):
        self.assertIn('MOTION_GLIDESECSTOXY', self.blocks)
        test_data = self.blocks['MOTION_GLIDESECSTOXY']
        self.assertIn('%1', test_data)
        self.assertIn(' x: %2 y: %3', test_data)

    # mscratch-i18n/blocks/MOTION_GLIDETO contains %1 
    def test_mscratch_i18n_blocks_MOTION_GLIDETO(self):
        self.assertIn('MOTION_GLIDETO', self.blocks)
        test_data = self.blocks['MOTION_GLIDETO']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/MOTION_CHANGEXBY contains %1 and x
    def test_mscratch_i18n_blocks_MOTION_CHANGEXBY(self):
        self.assertIn('MOTION_CHANGEXBY', self.blocks)
        test_data = self.blocks['MOTION_CHANGEXBY']
        self.assertIn('%1', test_data)
        self.assertIn(' x ', test_data)

    # mscratch-i18n/blocks/MOTION_SETX contains %1 and x
    def test_mscratch_i18n_blocks_MOTION_SETX(self):
        self.assertIn('MOTION_SETX', self.blocks)
        test_data = self.blocks['MOTION_SETX']
        self.assertIn('%1', test_data)
        self.assertIn(' x ', test_data)

    # mscratch-i18n/blocks/MOTION_CHANGEYBY contains %1 and y
    def test_mscratch_i18n_blocks_MOTION_CHANGEYBY(self):
        self.assertIn('MOTION_CHANGEYBY', self.blocks)
        test_data = self.blocks['MOTION_CHANGEYBY']
        self.assertIn('%1', test_data)
        self.assertIn(' y ', test_data)

    # mscratch-i18n/blocks/MOTION_SETY contains %1 and y
    def test_mscratch_i18n_blocks_MOTION_SETY(self):
        self.assertIn('MOTION_SETY', self.blocks)
        test_data = self.blocks['MOTION_SETY']
        self.assertIn('%1', test_data)
        self.assertIn(' y ', test_data)

    # mscratch-i18n/blocks/MOTION_SETROTATIONSTYLE contains %1 
    def test_mscratch_i18n_blocks_MOTION_SETROTATIONSTYLE(self):
        self.assertIn('MOTION_SETROTATIONSTYLE', self.blocks)
        test_data = self.blocks['MOTION_SETROTATIONSTYLE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_XPOSITION contains %1 
    def test_mscratch_i18n_blocks_MOTION_XPOSITION(self):
        self.assertIn('MOTION_XPOSITION', self.blocks)
        test_data = self.blocks['MOTION_XPOSITION']
        self.assertIn('x', test_data)

    # mscratch-i18n/blocks/MOTION_YPOSITION contains %1 
    def test_mscratch_i18n_blocks_MOTION_YPOSITION(self):
        self.assertIn('MOTION_YPOSITION', self.blocks)
        test_data = self.blocks['MOTION_YPOSITION']
        self.assertIn('y', test_data)

    # mscratch-i18n/blocks/MOTION_SCROLLRIGHT contains %1 
    def test_mscratch_i18n_blocks_MOTION_SCROLLRIGHT(self):
        self.assertIn('MOTION_SCROLLRIGHT', self.blocks)
        test_data = self.blocks['MOTION_SCROLLRIGHT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_SCROLLUP contains %1 
    def test_mscratch_i18n_blocks_MOTION_SCROLLUP(self):
        self.assertIn('MOTION_SCROLLUP', self.blocks)
        test_data = self.blocks['MOTION_SCROLLUP']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_ALIGNSCENE contains %1 
    def test_mscratch_i18n_blocks_MOTION_ALIGNSCENE(self):
        self.assertIn('MOTION_ALIGNSCENE', self.blocks)
        test_data = self.blocks['MOTION_ALIGNSCENE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/MOTION_XSCROLL contains %1 
    def test_mscratch_i18n_blocks_MOTION_XSCROLL(self):
        self.assertIn('MOTION_XSCROLL', self.blocks)
        test_data = self.blocks['MOTION_XSCROLL']
        self.assertIn('x ', test_data)

    # mscratch-i18n/blocks/MOTION_YSCROLL contains %1 
    def test_mscratch_i18n_blocks_MOTION_YSCROLL(self):
        self.assertIn('MOTION_YSCROLL', self.blocks)
        test_data = self.blocks['MOTION_YSCROLL']
        self.assertIn('y ', test_data)

    # mscratch-i18n/blocks/OPERATORS_ADD contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_ADD(self):
        self.assertIn('OPERATORS_ADD', self.blocks)
        test_data = self.blocks['OPERATORS_ADD']
        self.assertEqual(test_data, '%1 + %2')

    # mscratch-i18n/blocks/OPERATORS_SUBTRACT contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_SUBTRACT(self):
        self.assertIn('OPERATORS_SUBTRACT', self.blocks)
        test_data = self.blocks['OPERATORS_SUBTRACT']
        self.assertEqual(test_data, '%1 - %2')

    # mscratch-i18n/blocks/OPERATORS_MULTIPLY contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_MULTIPLY(self):
        self.assertIn('OPERATORS_MULTIPLY', self.blocks)
        test_data = self.blocks['OPERATORS_MULTIPLY']
        self.assertEqual(test_data, '%1 * %2')

    # mscratch-i18n/blocks/OPERATORS_DIVIDE contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_DIVIDE(self):
        self.assertIn('OPERATORS_DIVIDE', self.blocks)
        test_data = self.blocks['OPERATORS_DIVIDE']
        self.assertEqual(test_data, '%1 / %2')

    # mscratch-i18n/blocks/OPERATORS_RANDOM contains %1 %2
    def test_mscratch_i18n_blocks_OPERATORS_RANDOM(self):
        self.assertIn('OPERATORS_RANDOM', self.blocks)
        test_data = self.blocks['OPERATORS_RANDOM']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_GT contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_GT(self):
        self.assertIn('OPERATORS_GT', self.blocks)
        test_data = self.blocks['OPERATORS_GT']
        self.assertEqual(test_data, '%1 > %2')


    # mscratch-i18n/blocks/OPERATORS_LT contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_LT(self):
        self.assertIn('OPERATORS_LT', self.blocks)
        test_data = self.blocks['OPERATORS_LT']
        self.assertEqual(test_data, '%1 < %2')

    # mscratch-i18n/blocks/OPERATORS_EQUALS contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_EQUALS(self):
        self.assertIn('OPERATORS_EQUALS', self.blocks)
        test_data = self.blocks['OPERATORS_EQUALS']
        self.assertEqual(test_data, '%1 = %2')

    # mscratch-i18n/blocks/OPERATORS_AND contains %1 %2
    def test_mscratch_i18n_blocks_OPERATORS_AND(self):
        self.assertIn('OPERATORS_AND', self.blocks)
        test_data = self.blocks['OPERATORS_AND']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_OR contains %1 %2
    def test_mscratch_i18n_blocks_OPERATORS_OR(self):
        self.assertIn('OPERATORS_OR', self.blocks)
        test_data = self.blocks['OPERATORS_OR']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_NOT contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_NOT(self):
        self.assertIn('OPERATORS_NOT', self.blocks)
        test_data = self.blocks['OPERATORS_NOT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/OPERATORS_JOIN contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_JOIN(self):
        self.assertIn('OPERATORS_JOIN', self.blocks)
        test_data = self.blocks['OPERATORS_JOIN']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_LETTEROF contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_LETTEROF(self):
        self.assertIn('OPERATORS_LETTEROF', self.blocks)
        test_data = self.blocks['OPERATORS_LETTEROF']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_LENGTH contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_LENGTH(self):
        self.assertIn('OPERATORS_LENGTH', self.blocks)
        test_data = self.blocks['OPERATORS_LENGTH']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/OPERATORS_CONTAINS contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_CONTAINS(self):
        self.assertIn('OPERATORS_CONTAINS', self.blocks)
        test_data = self.blocks['OPERATORS_CONTAINS']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_MOD contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_MOD(self):
        self.assertIn('OPERATORS_MOD', self.blocks)
        test_data = self.blocks['OPERATORS_MOD']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/OPERATORS_ROUND contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_ROUND(self):
        self.assertIn('OPERATORS_ROUND', self.blocks)
        test_data = self.blocks['OPERATORS_ROUND']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/OPERATORS_MATHOP contains %1 
    def test_mscratch_i18n_blocks_OPERATORS_MATHOP(self):
        self.assertIn('OPERATORS_MATHOP', self.blocks)
        test_data = self.blocks['OPERATORS_MATHOP']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/PROCEDURES_DEFINITION contains %1 
    def test_mscratch_i18n_blocks_PROCEDURES_DEFINITION(self):
        self.assertIn('PROCEDURES_DEFINITION', self.blocks)
        test_data = self.blocks['PROCEDURES_DEFINITION']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_TOUCHINGOBJECT contains %1 
    def test_mscratch_i18n_blocks_SENSING_TOUCHINGOBJECT(self):
        self.assertIn('SENSING_TOUCHINGOBJECT', self.blocks)
        test_data = self.blocks['SENSING_TOUCHINGOBJECT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_TOUCHINGCOLOR contains %1 
    def test_mscratch_i18n_blocks_SENSING_TOUCHINGCOLOR(self):
        self.assertIn('SENSING_TOUCHINGCOLOR', self.blocks)
        test_data = self.blocks['SENSING_TOUCHINGCOLOR']
        self.assertIn('%1', test_data)    
        
    # mscratch-i18n/blocks/SENSING_COLORISTOUCHINGCOLOR contains %1 %2
    def test_mscratch_i18n_blocks_SENSING_COLORISTOUCHINGCOLOR(self):
        self.assertIn('SENSING_COLORISTOUCHINGCOLOR', self.blocks)
        test_data = self.blocks['SENSING_COLORISTOUCHINGCOLOR']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)    
    
    # mscratch-i18n/blocks/SENSING_DISTANCETO contains %1 
    def test_mscratch_i18n_blocks_SENSING_DISTANCETO(self):
        self.assertIn('SENSING_DISTANCETO', self.blocks)
        test_data = self.blocks['SENSING_DISTANCETO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_ASKANDWAIT contains %1 
    def test_mscratch_i18n_blocks_SENSING_ASKANDWAIT(self):
        self.assertIn('SENSING_ASKANDWAIT', self.blocks)
        test_data = self.blocks['SENSING_ASKANDWAIT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_KEYPRESSED contains %1 
    def test_mscratch_i18n_blocks_SENSING_KEYPRESSED(self):
        self.assertIn('SENSING_KEYPRESSED', self.blocks)
        test_data = self.blocks['SENSING_KEYPRESSED']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_SETDRAGMODE contains %1 
    def test_mscratch_i18n_blocks_SENSING_SETDRAGMODE(self):
        self.assertIn('SENSING_SETDRAGMODE', self.blocks)
        test_data = self.blocks['SENSING_SETDRAGMODE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SENSING_OF contains %1 %2
    def test_mscratch_i18n_blocks_SENSING_OF(self):
        self.assertIn('SENSING_OF', self.blocks)
        test_data = self.blocks['SENSING_OF']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/SENSING_CURRENT contains %1 
    def test_mscratch_i18n_blocks_SENSING_CURRENT(self):
        self.assertIn('SENSING_CURRENT', self.blocks)
        test_data = self.blocks['SENSING_CURRENT']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SOUND_PLAY contains %1 
    def test_mscratch_i18n_blocks_SOUND_PLAY(self):
        self.assertIn('SOUND_PLAY', self.blocks)
        test_data = self.blocks['SOUND_PLAY']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SOUND_PLAYUNTILDONE contains %1 
    def test_mscratch_i18n_blocks_SOUND_PLAYUNTILDONE(self):
        self.assertIn('SOUND_PLAYUNTILDONE', self.blocks)
        test_data = self.blocks['SOUND_PLAYUNTILDONE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/SOUND_SETEFFECTO contains %1 %2
    def test_mscratch_i18n_blocks_SOUND_SETEFFECTO(self):
        self.assertIn('SOUND_SETEFFECTO', self.blocks)
        test_data = self.blocks['SOUND_SETEFFECTO']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/SOUND_CHANGEEFFECTBY contains %1 %2
    def test_mscratch_i18n_blocks_SOUND_CHANGEEFFECTBY(self):
        self.assertIn('SOUND_CHANGEEFFECTBY', self.blocks)
        test_data = self.blocks['SOUND_CHANGEEFFECTBY']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/SOUND_CHANGEVOLUMEBY contains %1 
    def test_mscratch_i18n_blocks_SOUND_CHANGEVOLUMEBY(self):
        self.assertIn('SOUND_CHANGEVOLUMEBY', self.blocks)
        test_data = self.blocks['SOUND_CHANGEVOLUMEBY']
        self.assertIn('%1', test_data)    
    
    # mscratch-i18n/blocks/SOUND_SETVOLUMETO contains %1 
    def test_mscratch_i18n_blocks_SOUND_SETVOLUMETO(self):
        self.assertIn('SOUND_SETVOLUMETO', self.blocks)
        test_data = self.blocks['SOUND_SETVOLUMETO']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DELETE_X_BLOCKS contains %1 
    def test_mscratch_i18n_blocks_DELETE_X_BLOCKS(self):
        self.assertIn('DELETE_X_BLOCKS', self.blocks)
        test_data = self.blocks['DELETE_X_BLOCKS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DELETE_ALL_BLOCKS contains %1 
    def test_mscratch_i18n_blocks_DELETE_ALL_BLOCKS(self):
        self.assertIn('DELETE_ALL_BLOCKS', self.blocks)
        test_data = self.blocks['DELETE_ALL_BLOCKS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/RENAME_VARIABLE_TITLE contains %1 
    def test_mscratch_i18n_blocks_RENAME_VARIABLE_TITLE(self):
        self.assertIn('RENAME_VARIABLE_TITLE', self.blocks)
        test_data = self.blocks['RENAME_VARIABLE_TITLE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS contains %1 
    def test_mscratch_i18n_blocks_VARIABLE_ALREADY_EXISTS(self):
        self.assertIn('VARIABLE_ALREADY_EXISTS', self.blocks)
        test_data = self.blocks['VARIABLE_ALREADY_EXISTS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE contains %1 %2
    def test_mscratch_i18n_blocks_VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE(self):
        self.assertIn('VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE', self.blocks)
        test_data = self.blocks['VARIABLE_ALREADY_EXISTS_FOR_ANOTHER_TYPE']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DELETE_VARIABLE_CONFIRMATION contains %1 
    def test_mscratch_i18n_blocks_DELETE_VARIABLE_CONFIRMATION(self):
        self.assertIn('DELETE_VARIABLE_CONFIRMATION', self.blocks)
        test_data = self.blocks['DELETE_VARIABLE_CONFIRMATION']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/CANNOT_DELETE_VARIABLE_PROCEDURE contains %1 
    def test_mscratch_i18n_blocks_CANNOT_DELETE_VARIABLE_PROCEDURE(self):
        self.assertIn('CANNOT_DELETE_VARIABLE_PROCEDURE', self.blocks)
        test_data = self.blocks['CANNOT_DELETE_VARIABLE_PROCEDURE']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DELETE_VARIABLE contains %1 
    def test_mscratch_i18n_blocks_DELETE_VARIABLE(self):
        self.assertIn('DELETE_VARIABLE', self.blocks)
        test_data = self.blocks['DELETE_VARIABLE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/PROCEDURE_ALREADY_EXISTS contains %1 
    def test_mscratch_i18n_blocks_PROCEDURE_ALREADY_EXISTS(self):
        self.assertIn('PROCEDURE_ALREADY_EXISTS', self.blocks)
        test_data = self.blocks['PROCEDURE_ALREADY_EXISTS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/LIST_ALREADY_EXISTS contains %1 
    def test_mscratch_i18n_blocks_LIST_ALREADY_EXISTS(self):
        self.assertIn('LIST_ALREADY_EXISTS', self.blocks)
        test_data = self.blocks['LIST_ALREADY_EXISTS']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/RENAME_LIST_TITLE contains %1 
    def test_mscratch_i18n_blocks_RENAME_LIST_TITLE(self):
        self.assertIn('RENAME_LIST_TITLE', self.blocks)
        test_data = self.blocks['RENAME_LIST_TITLE']
        self.assertIn('%1', test_data)

    # mscratch-i18n/blocks/DATA_ITEMNUMOFLIST contains %1 %2
    def test_mscratch_i18n_blocks_DATA_ITEMNUMOFLIST(self):
        self.assertIn('DATA_ITEMNUMOFLIST', self.blocks)
        test_data = self.blocks['DATA_ITEMNUMOFLIST']
        self.assertIn('%1', test_data)
        self.assertIn('%2', test_data)

    # mscratch-i18n/blocks/DELETE_LIST contains %1 
    def test_mscratch_i18n_blocks_DELETE_LIST(self):
        self.assertIn('DELETE_LIST', self.blocks)
        test_data = self.blocks['DELETE_LIST']
        self.assertIn('%1', test_data)


    # ==== -mscratch-extensions-翻译检查  ===

    # mscratch-i18n/extensions/music/No empty value
    def test_mscratch_i18n_extensions_music_no_empty_value(self):
        for key,value in self.extensions_music.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mscratch-i18n/extensions/music/music.playDrumForBeats contains [DRUM] [BEATS]
    def test_mscratch_i18n_extensions_music_playDrumForBeats(self):
        self.assertIn('music.playDrumForBeats', self.extensions_music)
        test_data = self.extensions_music['music.playDrumForBeats']
        self.assertIn('[DRUM]', test_data)
        self.assertIn('[BEATS]', test_data)

    # mscratch-i18n/extensions/music/music.playNoteForBeats contains [BEATS]
    def test_mscratch_i18n_extensions_music_playNoteForBeats(self):
        self.assertIn('music.playNoteForBeats', self.extensions_music)
        test_data = self.extensions_music['music.playNoteForBeats']
        self.assertIn('[BEATS]', test_data)

    # mscratch-i18n/extensions/music/music.setInstrument contains [INSTRUMENT]
    def test_mscratch_i18n_extensions_music_setInstrument(self):
        self.assertIn('music.setInstrument', self.extensions_music)
        test_data = self.extensions_music['music.setInstrument']
        self.assertIn('[INSTRUMENT]', test_data)

    # mscratch-i18n/extensions/music/music.setTempo contains [DRUM] [TEMPO]
    def test_mscratch_i18n_extensions_music_setTempo(self):
        self.assertIn('music.setTempo', self.extensions_music)
        test_data = self.extensions_music['music.setTempo']
        self.assertIn('[TEMPO]', test_data)

    # mscratch-i18n/extensions/music/music.changeTempo contains [DRUM] [TEMPO]
    def test_mscratch_i18n_extensions_music_changeTempo(self):
        self.assertIn('music.changeTempo', self.extensions_music)
        test_data = self.extensions_music['music.changeTempo']
        self.assertIn('[TEMPO]', test_data)


    # mscratch-i18n/extensions/pen/No empty value
    def test_mscratch_i18n_extensions_pen_no_empty_value(self):
        for key,value in self.extensions_pen.items():
            self.assertIsNotNone(value)
            self.assertNotEqual(value, '')

    # mscratch-i18n/extensions/pen/pen.setColor contains [COLOR] 
    def test_mscratch_i18n_extensions_music_setColor(self):
        self.assertIn('pen.setColor', self.extensions_pen)
        test_data = self.extensions_pen['pen.setColor']
        self.assertIn('[COLOR]', test_data)

    # mscratch-i18n/extensions/pen/pen.changeColorParam contains [COLOR_PARAM] [VALUE] 
    def test_mscratch_i18n_extensions_music_changeColorParam(self):
        self.assertIn('pen.changeColorParam', self.extensions_pen)
        test_data = self.extensions_pen['pen.changeColorParam']
        self.assertIn('[COLOR_PARAM]', test_data)
        self.assertIn('[VALUE]', test_data)

    # mscratch-i18n/extensions/pen/pen.setColorParam contains [COLOR_PARAM] [VALUE] 
    def test_mscratch_i18n_extensions_music_setColorParam(self):
        self.assertIn('pen.setColorParam', self.extensions_pen)
        test_data = self.extensions_pen['pen.setColorParam']
        self.assertIn('[COLOR_PARAM]', test_data)
        self.assertIn('[VALUE]', test_data)

    # mscratch-i18n/extensions/pen/pen.changeSize contains [SIZE] 
    def test_mscratch_i18n_extensions_music_changeSize(self):
        self.assertIn('pen.changeSize', self.extensions_pen)
        test_data = self.extensions_pen['pen.changeSize']
        self.assertIn('[SIZE]', test_data)

    # mscratch-i18n/extensions/pen/pen.setSize contains [SIZE] 
    def test_mscratch_i18n_extensions_music_setSize(self):
        self.assertIn('pen.setSize', self.extensions_pen)
        test_data = self.extensions_pen['pen.setSize']
        self.assertIn('[SIZE]', test_data)

    # mscratch-i18n/extensions/pen/pen.setShade contains [SHADE] 
    def test_mscratch_i18n_extensions_music_setShade(self):
        self.assertIn('pen.setShade', self.extensions_pen)
        test_data = self.extensions_pen['pen.setShade']
        self.assertIn('[SHADE]', test_data)

    # mscratch-i18n/extensions/pen/pen.changeShade contains [SHADE] 
    def test_mscratch_i18n_extensions_music_changeShade(self):
        self.assertIn('pen.changeShade', self.extensions_pen)
        test_data = self.extensions_pen['pen.changeShade']
        self.assertIn('[SHADE]', test_data)

    # mscratch-i18n/extensions/pen/pen.setHue contains [HUE] 
    def test_mscratch_i18n_extensions_music_setHue(self):
        self.assertIn('pen.setHue', self.extensions_pen)
        test_data = self.extensions_pen['pen.setHue']
        self.assertIn('[HUE]', test_data)

    # mscratch-i18n/extensions/pen/pen.changeHue contains [HUE] 
    def test_mscratch_i18n_extensions_music_changeHue(self):
        self.assertIn('pen.changeHue', self.extensions_pen)
        test_data = self.extensions_pen['pen.changeHue']
        self.assertIn('[HUE]', test_data)


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    # #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MscratchTest) 
    # suite = unittest.TestSuite([suite1, suite2, suite3]) 
    unittest.TextTestRunner(verbosity=2).run(suite1)
