# -*- coding: utf-8 -*-
# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from importlib.resources import path
from remi.gui import *
from remi import start, App
import PyATEMMax
import time
from Config import *

# ─── API CONFIG AND SETUP ───────────────────────────────────────────────────────
#PyATEMMax config and setup
switcher = PyATEMMax.ATEMMax()

switcher.connect(SWITCHERIP)
switcher.waitForConnection()

class SwitcherWeb(App):
    #Initiation
    def __init__(self, *args, **kwargs):
        super(SwitcherWeb, self).__init__(*args)

    #Auto update
    def idle(self):
        #Update detection

        tally_1 = str(switcher.tally.bySource.flags[1])

        if tally_1 == "[PGM]":
            self.src1.css_background_color = "rgb(245,0,0)"
        elif tally_1 == "[PVW]":
            self.src1.css_background_color = "rgb(80,164,0)"
        elif tally_1 == "[]":
            self.src1.css_background_color = "rgb(170,170,170)"
        elif tally_1 == "[PGM][PVW]":
            self.src1.css_background_color = "rgb(245,0,0)"
        
        tally_2 = str(switcher.tally.bySource.flags[2])

        if tally_2 == "[PGM]":
            self.src2.css_background_color = "rgb(245,0,0)"
        elif tally_2 == "[PVW]":
            self.src2.css_background_color = "rgb(80,164,0)"
        elif tally_2 == "[]":
            self.src2.css_background_color = "rgb(170,170,170)"
        elif tally_2 == "[PGM][PVW]":
            self.src2.css_background_color = "rgb(245,0,0)"
        
        tally_3 = str(switcher.tally.bySource.flags[3])

        if tally_3 == "[PGM]":
            self.src3.css_background_color = "rgb(245,0,0)"
        elif tally_3 == "[PVW]":
            self.src3.css_background_color = "rgb(80,164,0)"
        elif tally_3 == "[]":
            self.src3.css_background_color = "rgb(170,170,170)"
        elif tally_3 == "[PGM][PVW]":
            self.src3.css_background_color = "rgb(245,0,0)"

        tally_4 = str(switcher.tally.bySource.flags[4])

        if tally_4 == "[PGM]":
            self.src4.css_background_color = "rgb(245,0,0)"
        elif tally_4 == "[PVW]":
            self.src4.css_background_color = "rgb(80,164,0)"
        elif tally_4 == "[]":
            self.src4.css_background_color = "rgb(170,170,170)"
        elif tally_4 == "[PGM][PVW]":
            self.src4.css_background_color = "rgb(245,0,0)"
        pass
    
    def main(self):
        #returns design
        return SwitcherWeb.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #Design
        self.container0 = Container()
        self.container0.attr_class = "Container"
        self.container0.attr_editor_newclass = False
        self.container0.css_background_color = "rgb(254,79,73)"
        self.container0.css_height = "570.0px"
        self.container0.css_left = "20px"
        self.container0.css_position = "absolute"
        self.container0.css_top = "20px"
        self.container0.css_width = "1035.0px"
        self.container0.variable_name = "container0"
        self.src1 = Button()
        self.src1.attr_class = "Button"
        self.src1.attr_editor_newclass = False
        self.src1.css_background_color = "rgb(170,170,170)"
        self.src1.css_font_size = "40px"
        self.src1.css_height = "75.0px"
        self.src1.css_left = "30.0px"
        self.src1.css_position = "absolute"
        self.src1.css_top = "465.0px"
        self.src1.css_width = "120.0px"
        self.src1.text = "1"
        self.src1.variable_name = "src1"
        self.container0.append(self.src1,'src1')
        self.src2 = Button()
        self.src2.attr_class = "Button"
        self.src2.attr_editor_newclass = False
        self.src2.css_background_color = "rgb(170,170,170)"
        self.src2.css_font_size = "40px"
        self.src2.css_height = "75px"
        self.src2.css_left = "180.0px"
        self.src2.css_position = "absolute"
        self.src2.css_top = "465.0px"
        self.src2.css_width = "120px"
        self.src2.text = "2"
        self.src2.variable_name = "src2"
        self.container0.append(self.src2,'src2')
        self.src3 = Button()
        self.src3.attr_class = "Button"
        self.src3.attr_editor_newclass = False
        self.src3.css_background_color = "rgb(170,170,170)"
        self.src3.css_font_size = "40px"
        self.src3.css_height = "75.0px"
        self.src3.css_left = "330.0px"
        self.src3.css_position = "absolute"
        self.src3.css_top = "465.0px"
        self.src3.css_width = "120.0px"
        self.src3.text = "3"
        self.src3.variable_name = "src3"
        self.container0.append(self.src3,'src3')
        self.src4 = Button()
        self.src4.attr_class = "Button"
        self.src4.attr_editor_newclass = False
        self.src4.css_background_color = "rgb(170,170,170)"
        self.src4.css_font_size = "40px"
        self.src4.css_height = "75px"
        self.src4.css_left = "480.0px"
        self.src4.css_position = "absolute"
        self.src4.css_top = "465.0px"
        self.src4.css_width = "120px"
        self.src4.text = "4"
        self.src4.variable_name = "src4"
        self.container0.append(self.src4,'src4')
        self.cut = Button()
        self.cut.attr_class = "Button"
        self.cut.attr_editor_newclass = False
        self.cut.css_background_color = "rgb(170,170,170)"
        self.cut.css_font_size = "39px"
        self.cut.css_height = "75px"
        self.cut.css_left = "735.0px"
        self.cut.css_position = "absolute"
        self.cut.css_top = "465.0px"
        self.cut.css_width = "120px"
        self.cut.text = "CUT"
        self.cut.variable_name = "cut"
        self.container0.append(self.cut,'cut')
        self.auto = Button()
        self.auto.attr_class = "Button"
        self.auto.attr_editor_newclass = False
        self.auto.css_background_color = "rgb(170,170,170)"
        self.auto.css_font_size = "40px"
        self.auto.css_height = "75.0px"
        self.auto.css_left = "885.0px"
        self.auto.css_position = "absolute"
        self.auto.css_top = "465.0px"
        self.auto.css_width = "120.0px"
        self.auto.text = "AUTO"
        self.auto.variable_name = "auto"
        self.container0.append(self.auto,'auto')
        self.brand = Label()
        self.brand.attr_class = "Label"
        self.brand.attr_editor_newclass = False
        self.brand.css_align_content = "center"
        self.brand.css_align_items = "center"
        self.brand.css_align_self = "center"
        self.brand.css_color = "rgb(255,255,255)"
        self.brand.css_font_size = "35px"
        self.brand.css_height = "45.0px"
        self.brand.css_justify_content = "center"
        self.brand.css_left = "20px"
        self.brand.css_position = "absolute"
        self.brand.css_text_align = "center"
        self.brand.css_top = "20px"
        self.brand.css_width = "990.0px"
        self.brand.text = BRAND
        self.brand.variable_name = "brand"
        self.container0.append(self.brand,'brand')

        #Button detection
        self.cut.onclick.do(self.on_button_pressed_cut)
        self.auto.onclick.do(self.on_button_pressed_auto)
        self.src1.onclick.do(self.on_button_pressed_1)
        self.src2.onclick.do(self.on_button_pressed_2)
        self.src3.onclick.do(self.on_button_pressed_3)
        self.src4.onclick.do(self.on_button_pressed_4)

        return self.container0
    # ─── BUTTON FUNCTIONS ───────────────────────────────────────────────────────────
    def on_button_pressed_cut(self, widget):
        switcher.execCutME(0)
    def on_button_pressed_auto(self, widget):
        switcher.execAutoME(0)
    def on_button_pressed_1(self, widget):
        switcher.setPreviewInputVideoSource(0,1)
    def on_button_pressed_2(self, widget):
        switcher.setPreviewInputVideoSource(0,2)
    def on_button_pressed_3(self, widget):
        switcher.setPreviewInputVideoSource(0,3)
    def on_button_pressed_4(self, widget):
        switcher.setPreviewInputVideoSource(0,4)

# ─── WEB STARTUP ────────────────────────────────────────────────────────────────
start(SwitcherWeb, address='0.0.0.0', port=8080, multiple_instance=True, enable_file_cache=True, update_interval=0.08, start_browser=True)