# coding: UTF-8
#
# TileCutter User Interface Module - offsetControl
#

# Copyright © 2008-2011 Timothy Baldock. All Rights Reserved.

import wx, imres

# Utility functions
import translator
gt = translator.Translator()

import logger
debug = logger.Log()

class offsetControl(wx.Panel):
    """Box containing offset controls"""
    def __init__(self, parent, app):
        """"""
        debug(u"tcui.OffsetControl: __init__")
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.app = app
        # Setup sizers
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.s_offset_flex = wx.FlexGridSizer(0,3,2,2)
        # Header text
        self.label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        # Add items
        self.offset_button_up = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveUpDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_left = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveLeftDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_reset = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveCenter"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_right = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveRightDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_down = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveDownDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_up_left = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveUpAndLeftDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_up_right = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveUpAndRightDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_down_left = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveDownAndLeftDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_button_down_right = wx.BitmapButton(self, wx.ID_ANY, imres.catalog["MoveDownAndRightDouble"].getBitmap(), (-1,-1), (-1,-1))
        self.offset_selector = wx.CheckBox(self, wx.ID_ANY, "", (-1,-1), (-1,-1))

        # Add to sizers
        self.s_offset_flex.Add(self.offset_button_up_left, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_up, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_up_right, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_left, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_reset, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_right, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_down_left, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_down, 0, wx.LEFT, 0)
        self.s_offset_flex.Add(self.offset_button_down_right, 0, wx.LEFT, 0)

        # Add to default sizer with header and line
        self.sizer.Add((0,2))
        self.sizer.Add(self.label, 0, wx.LEFT, 2)
        self.sizer.Add((0,4))
        self.sizer.Add(self.s_offset_flex, 1, wx.ALIGN_CENTER_HORIZONTAL)
        # Add fine button to vertical sizer
        self.sizer.Add((0,7))
        self.sizer.Add(self.offset_selector, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add((0,4))

        # Set panel's sizer
        self.SetSizer(self.sizer)

        # Bind functions
        self.offset_button_up.Bind(wx.EVT_BUTTON, self.OnUp, self.offset_button_up)
        self.offset_button_left.Bind(wx.EVT_BUTTON, self.OnLeft, self.offset_button_left)
        self.offset_button_reset.Bind(wx.EVT_BUTTON, self.OnCenter, self.offset_button_reset)
        self.offset_button_right.Bind(wx.EVT_BUTTON, self.OnRight, self.offset_button_right)
        self.offset_button_down.Bind(wx.EVT_BUTTON, self.OnDown, self.offset_button_down)
        self.offset_button_up_left.Bind(wx.EVT_BUTTON, self.OnUpLeft, self.offset_button_up_left)
        self.offset_button_up_right.Bind(wx.EVT_BUTTON, self.OnUpRight, self.offset_button_up_right)
        self.offset_button_down_left.Bind(wx.EVT_BUTTON, self.OnDownLeft, self.offset_button_down_left)
        self.offset_button_down_right.Bind(wx.EVT_BUTTON, self.OnDownRight, self.offset_button_down_right)
        self.offset_selector.Bind(wx.EVT_CHECKBOX, self.OnFine, self.offset_selector)

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        debug(u"tcui.OffsetControl: translate")
        self.label.SetLabel(gt("Mask Offset:"))
        self.offset_button_up.SetToolTipString(gt("tt_offset_button_up"))
        self.offset_button_left.SetToolTipString(gt("tt_offset_button_left"))
        self.offset_button_reset.SetToolTipString(gt("offset_button_reset"))
        self.offset_button_right.SetToolTipString(gt("tt_offset_button_right"))
        self.offset_button_down.SetToolTipString(gt("tt_offset_button_down"))
        self.offset_selector.SetLabel(gt("Fine"))
        self.offset_selector.SetToolTipString(gt("tt_offset_selector"))

        self.Fit()

    def update(self):
        """Set the values of the controls in this group to the values in the model"""
        debug(u"tcui.OffsetControl: update")
        # Offset control doesn't have any controls which are determined by the model, "fine" checkbox always off by default

    def OnFine(self,e):
        """On toggle of the "fine" checkbox, change images on the buttons"""
        debug(u"tcui.OffsetControl: OnFine")
        if self.offset_selector.GetValue():
            self.offset_button_up.SetBitmapLabel(imres.catalog["MoveUp"].getBitmap())
            self.offset_button_left.SetBitmapLabel(imres.catalog["MoveLeft"].getBitmap())
            self.offset_button_right.SetBitmapLabel(imres.catalog["MoveRight"].getBitmap())
            self.offset_button_down.SetBitmapLabel(imres.catalog["MoveDown"].getBitmap())
            self.offset_button_up_left.SetBitmapLabel(imres.catalog["MoveUpAndLeft"].getBitmap())
            self.offset_button_up_right.SetBitmapLabel(imres.catalog["MoveUpAndRight"].getBitmap())
            self.offset_button_down_left.SetBitmapLabel(imres.catalog["MoveDownAndLeft"].getBitmap())
            self.offset_button_down_right.SetBitmapLabel(imres.catalog["MoveDownAndRight"].getBitmap())
        else:
            self.offset_button_up.SetBitmapLabel(imres.catalog["MoveUpDouble"].getBitmap())
            self.offset_button_left.SetBitmapLabel(imres.catalog["MoveLeftDouble"].getBitmap())
            self.offset_button_right.SetBitmapLabel(imres.catalog["MoveRightDouble"].getBitmap())
            self.offset_button_down.SetBitmapLabel(imres.catalog["MoveDownDouble"].getBitmap())
            self.offset_button_up_left.SetBitmapLabel(imres.catalog["MoveUpAndLeftDouble"].getBitmap())
            self.offset_button_up_right.SetBitmapLabel(imres.catalog["MoveUpAndRightDouble"].getBitmap())
            self.offset_button_down_left.SetBitmapLabel(imres.catalog["MoveDownAndLeftDouble"].getBitmap())
            self.offset_button_down_right.SetBitmapLabel(imres.catalog["MoveDownAndRightDouble"].getBitmap())

    def OnUpLeft(self,e):
        """Move mask up and left"""
        debug(u"tcui.OffsetControl: OnUpLeft")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_offset([max(self.app.activeproject.active_x_offset() - 2, 0), 
                                                  self.app.activeproject.active_y_offset() + 1])
        else:
            self.app.activeproject.active_offset([max(self.app.activeproject.active_x_offset() - self.app.activeproject.paksize()/2, 0), 
                                                  self.app.activeproject.active_y_offset() + self.app.activeproject.paksize()/4])
    def OnUpRight(self,e):
        """Move mask up and right"""
        debug(u"tcui.OffsetControl: OnUpRight")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_offset([self.app.activeproject.active_x_offset() + 2, 
                                                  self.app.activeproject.active_y_offset() + 1])
        else:
            self.app.activeproject.active_offset([self.app.activeproject.active_x_offset() + self.app.activeproject.paksize()/2, 
                                                  self.app.activeproject.active_y_offset() + self.app.activeproject.paksize()/4])
    def OnDownLeft(self,e):
        """Move mask down and left"""
        debug(u"tcui.OffsetControl: OnDownLeft")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_offset([max(self.app.activeproject.active_x_offset() - 2, 0), 
                                                  max(self.app.activeproject.active_y_offset() - 1, 0)])
        else:
            self.app.activeproject.active_offset([max(self.app.activeproject.active_x_offset() - self.app.activeproject.paksize()/2, 0), 
                                                  max(self.app.activeproject.active_y_offset() - self.app.activeproject.paksize()/4, 0)])
    def OnDownRight(self,e):
        """Move mask down and right"""
        debug(u"tcui.OffsetControl: OnDownRight")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_offset([self.app.activeproject.active_x_offset() + 2, 
                                                  max(self.app.activeproject.active_y_offset() - 1, 0)])
        else:
            self.app.activeproject.active_offset([self.app.activeproject.active_x_offset() + self.app.activeproject.paksize()/2, 
                                                  max(self.app.activeproject.active_y_offset() - self.app.activeproject.paksize()/4, 0)])
    def OnUp(self,e):
        """Move mask up"""
        debug(u"tcui.OffsetControl: OnUp")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_y_offset(self.app.activeproject.active_y_offset() + 1)
        else:
            self.app.activeproject.active_y_offset(self.app.activeproject.active_y_offset() + self.app.activeproject.paksize())
    def OnLeft(self,e):
        """Move mask left"""
        debug(u"tcui.OffsetControl: OnLeft")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_x_offset(max(self.app.activeproject.active_x_offset() - 1, 0))
        else:
            self.app.activeproject.active_x_offset(max(self.app.activeproject.active_x_offset() - self.app.activeproject.paksize(), 0))
    def OnCenter(self,e):
        """Reset mask position"""
        debug(u"tcui.OffsetControl: OnCenter")
        self.app.activeproject.active_offset([0,0])
    def OnRight(self,e):
        """Move mask right"""
        debug(u"tcui.OffsetControl: OnRight")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_x_offset(self.app.activeproject.active_x_offset() + 1)
        else:
            self.app.activeproject.active_x_offset(self.app.activeproject.active_x_offset() + self.app.activeproject.paksize())
    def OnDown(self,e):
        """Move mask down"""
        debug(u"tcui.OffsetControl: OnDown")
        if self.offset_selector.GetValue():
            self.app.activeproject.active_y_offset(max(self.app.activeproject.active_y_offset() - 1, 0))
        else:
            self.app.activeproject.active_y_offset(max(self.app.activeproject.active_y_offset() - self.app.activeproject.paksize(), 0))
