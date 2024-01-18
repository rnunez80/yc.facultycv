# -*- coding: utf-8 -*-

from plone import api
from plone.protect.authenticator import createToken
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


# from yc.facultycv import _




class ProfileStaff(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    index = ViewPageTemplateFile('profile_staff.pt')

    def __call__(self):
        return self.index()

    def Email(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('email') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def OfficeLocation(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('location') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def OfficePhone(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('phone') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def TeachingTitle(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('functionalTitle') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def OtherTitle(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('personalTitle') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def Department(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('department') or ' '
            return str(member_info)
        except AttributeError:
            return None

    def DepartmentURL(self):
        user = api.user.get(username=self.context.userid)
        try:
            member_info = user.getProperty('department') or ' '
            space = member_info.replace(' ', '-').lower()
            return 'academics/departments/' + str(space)
        except AttributeError:
            return None

    def Title(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='staff2')
        for brain in brains:
            staff = brain.getObject()
            results.append({
                'Title': brain.Title,
            })
        return results

    def officeHours(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='staff2')
        for brain in brains:
            staff = brain.getObject()
            results.append({
                'day': brain.day,
                'time': brain.time,
            })
        return results

    # def moreStaff(self):
    #     results = []
    #     portal_catalog = api.portal.get_tool('portal_catalog')
    #     current_path = "/".join(self.context.getPhysicalPath())
    #     brains = portal_catalog(path=current_path, portal_type='staff2')
    #     for brain in brains:
    #         staff = brain.getObject()
    #         results.append({
    #             'Senior': brain.Senior,
    #             'mobilePhone': brain.mobilePhone,
    #             'uUID': brain.UID,
    #             'supervisor': brain.supervisor,
    #             'backup': brain.backup,
    #         })
    #     return results

    # def ApplicationsServers(self):
    #     results = []
    #     portal_catalog = api.portal.get_tool('portal_catalog')
    #     current_path = "/".join(self.context.getPhysicalPath())
    #     brains = portal_catalog(path=current_path, portal_type='staff2')
    #     for brain in brains:
    #         staff = brain.getObject()
    #         results.append({
    #             'name': brain.name,
    #             'description': brain.description,
    #             'url': brain.url,
    #         })
    #     return results

    def token(self):
        return createToken()
