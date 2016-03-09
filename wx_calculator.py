#!/usr/bin/env python
#coding=utf-8
from __future__ import division
import wx
from math import *
class CalcFrame(wx.Frame):
	global PI 
	def __init__(self, title):
		super(CalcFrame, self).__init__(None, title = title, size = (300,250))
		PI= 3.141592653571
		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):
		vbox = wx.BoxSizer(wx.VERTICAL)
		gridBox = wx.GridSizer(5, 4, 1, 1)
		labels = ['AC', 'DEL', 'PI', 'CLOSE', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '+', '=']

		self.textprint = wx.TextCtrl(self, -1, '', style = wx.TE_RIGHT|wx.TE_READONLY)
		vbox.Add(self.textprint, flag = wx.EXPAND|wx.TOP|wx.BOTTOM, border = 4)
		self.equation = ""
		for label in labels:
			buttonIterm = wx.Button(self, label = label)
			self.createHandler(buttonIterm, label)
			gridBox.Add(buttonIterm, 1, wx.EXPAND)

		vbox.Add(gridBox, proportion = 1, flag = wx.EXPAND)
		self.SetSizer(vbox)

	def createHandler(self, button, labels):
		item = "DEL AC = CLOSE"
		if labels not in item:
			self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
		elif labels == 'DEL':
			self.Bind(wx.EVT_BUTTON, self.OnDel, button)
		elif labels == 'AC':
			self.Bind(wx.EVT_BUTTON, self.OnAc, button)
		elif labels == '=':
			self.Bind(wx.EVT_BUTTON, self.OnTarget, button)
		elif labels == 'CLOSE':
			self.Bind(wx.EVT_BUTTON, self.OnExit, button)

	def OnAppend(self, event):
		eventbutton = event.GetEventObject()
		label = eventbutton.GetLabel()
		self.equation += label
		self.textprint.SetValue(self.equation)
	def OnDel(self, event):
		self.equation = self.equation[:-1]
	def OnAc(self,event):
		self.textprint.Clear()
		self.equation=""
	def OnTarget(self,event):
		try:

			target = eval(self.equation)
			self.equation = str(target)
			self.textprint.SetValue(self.equation)
		except SyntaxError:
			dlg = wx.MessageDialog(self, u'请输入正确的等式',u'错误',wx.OK|wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()
	def OnExit(self, event):
		self.Close()
if __name__ == '__main__':

	app = wx.App()
	CalcFrame(title = 'Calculator')
	app.MainLoop()
