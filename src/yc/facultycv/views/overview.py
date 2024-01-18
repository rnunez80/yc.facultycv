# -*- coding: utf-8 -*-
from plone.protect.authenticator import createToken
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Overview(BrowserView):
    _template = ViewPageTemplateFile('overview.pt')

    def render(self):
        return self._template()

    def token(self):
        return createToken()
