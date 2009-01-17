# coding: UTF-8
#
# TileCutter, User Interface Module - imageControl
#
import wx, imres

# Utility functions
import translator
gt = translator.Translator()

from debug import DebugFrame as debug

class imageControl(wx.StaticBox):
    """Box containing Front/Back image controls"""
    def __init__(self, parent, app, parent_sizer):
        self.app = app
        wx.StaticBox.__init__(self, parent, wx.ID_ANY, gt("Image"))
            # Setup sizers
        self.s_images = wx.StaticBoxSizer(self, wx.VERTICAL)
        self.s_images_flex = wx.FlexGridSizer(0,2,0,0)
        self.s_images_flex.AddGrowableCol(1)
            # Add items
        self.images_select_back_im = wx.StaticBitmap(parent, wx.ID_ANY, imres.catalog["ImageBack"].getBitmap())
        self.images_select_back = wx.RadioButton(parent, wx.ID_ANY, "", (-1,-1), (-1,-1), wx.RB_GROUP)
        self.images_select_front_im = wx.StaticBitmap(parent, wx.ID_ANY, imres.catalog["ImageFront"].getBitmap())
        self.images_select_front = wx.RadioButton(parent, wx.ID_ANY, "", (-1,-1), (-1,-1))
        self.images_enable_front = wx.CheckBox(parent, wx.ID_ANY, "", (-1,-1), (-1,-1))
            # Add to sizers
        self.s_images_flex.Add(self.images_select_back_im, 0, wx.ALIGN_LEFT|wx.RIGHT|wx.LEFT, 2)
        self.s_images_flex.Add(self.images_select_back, 0, wx.ALIGN_LEFT|wx.RIGHT, 2)
        self.s_images_flex.Add(self.images_select_front_im, 0, wx.ALIGN_LEFT|wx.RIGHT|wx.LEFT, 2)
        self.s_images_flex.Add(self.images_select_front, 0, wx.ALIGN_LEFT|wx.RIGHT, 2)
        self.s_images_flex.Add(wx.Size(1,1))
        self.s_images_flex.Add(self.images_enable_front, 0, wx.ALIGN_LEFT|wx.RIGHT, 2)
        self.s_images.Add(self.s_images_flex, 1, wx.RIGHT, 0)
            # Bind events
        self.images_enable_front.Bind(wx.EVT_CHECKBOX, self.OnToggle, self.images_enable_front)
        self.images_select_back.Bind(wx.EVT_RADIOBUTTON, self.OnBackImage, self.images_select_back)
        self.images_select_front.Bind(wx.EVT_RADIOBUTTON, self.OnFrontImage, self.images_select_front)
            # Add element to its parent sizer
        parent_sizer.Add(self.s_images, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 3)

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        self.images_select_back.SetLabel(gt("BackImage"))
        self.images_select_back.SetToolTipString(gt("tt_images_select_back"))
        self.images_select_front.SetLabel(gt("FrontImage"))
        self.images_select_front.SetToolTipString(gt("tt_images_select_front"))
        self.images_enable_front.SetLabel(gt("Enable FrontImage"))
        self.images_enable_front.SetToolTipString(gt("tt_images_enable_front"))

    def update(self):
        """Set the values of the controls in this group to the values in the model"""
        if self.app.activeproject.frontimage() == 0:  # Turn frontimage off
            self.images_enable_front.SetValue(0)
            # If currently have frontimage selected, switch to backimage
            if self.images_select_front.GetValue() == True:
                # Update model
                self.app.activeproject.activeImage(layer=self.app.Back)
                self.images_select_back.SetValue(1)
                # As active layer changed, need to redraw display
                self.app.frame.display.update()
            # Then disable the control
            self.images_select_front.Disable()
        else:
            self.images_enable_front.SetValue(1)
            # User must select the frontimage if they wish to view it, so just enable the control
            self.images_select_front.Enable()

    def OnToggle(self,e):
        """Toggling frontimage on and off"""
        self.app.activeproject.frontimage(self.images_enable_front.GetValue())
        self.update()
    def OnBackImage(self,e):
        """Toggle BackImage on"""
        # Set active image to Back
        self.app.activeproject.activeImage(layer=0)
        # Redraw active image
        self.app.frame.display.update()
    def OnFrontImage(self,e):
        """Toggle FrontImage on"""
        # Set active image to Front
        self.app.activeproject.activeImage(layer=1)
        # Redraw active image
        self.app.frame.display.update()