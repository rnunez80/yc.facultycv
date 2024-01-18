# -*- coding: utf-8 -*-
from plone import api
from plone.protect.authenticator import createToken
from plone.protect.interfaces import IDisableCSRFProtection
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides


class OverviewCatalogSearch(BrowserView):
    _template = ViewPageTemplateFile('overview_catalog_search.pt')

    def render(self):
        return self._template()

    def last_name(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('last_name') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def pb_actions(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = '/'.join(self.context.getPhysicalPath())
        portal_types = ['pbaction2',
                        'pbactionclt2',
                        'pbactionleave2',
                        'pbactionportfolioa',
                        'pbactionportfoliob',
                        'pbactionportfolioc',
                        'pbactionscholar2',
                        'symposium_talk']
        brains = portal_catalog(portal_type=portal_types, path=current_path,
                                sort_on='sortable_title')
        for brain in brains:
            pb = brain.getObject()
            results.append({
                'Title': brain.Title,
                'URL': brain.getURL(),
            })
        return results

    def token(self):
        return createToken()
