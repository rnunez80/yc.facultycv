# -*- coding: utf-8 -*-

# from yc.facultycv import _
from plone.protect.authenticator import createToken
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OverviewStaff(BrowserView):
    _template = ViewPageTemplateFile('overview_staff.pt')

    def render(self):
        return self._template()

    def token(self):
        return createToken()
