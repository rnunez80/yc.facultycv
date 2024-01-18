# -*- coding: utf-8 -*-

# from plone import api
from plone.protect.authenticator import createToken
# from yc.facultycv import _
# from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides


class Pbactiontypeview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('pbactiontypeview.pt')

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        return self.template()

    def token(self):
        return createToken()
