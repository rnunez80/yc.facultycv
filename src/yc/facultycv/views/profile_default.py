# -*- coding: utf-8 -*-

# from Products.CMFCore.permissions import ViewManagementScreens
# from Products.CMFCore.utils import getToolByName
from plone import api
from plone.protect.authenticator import createToken
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.security import checkPermission


class ProfileDefault(BrowserView):
    """A default view of the CV
    """

    index = ViewPageTemplateFile('profile_default.pt')

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
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'Title': brain.Title,
            })
        return results

    def areaExpertise(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'areaExpertise': str(faculty.areaExpertise, encoding='utf-8'),
            })
        return results

    def briefBio(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'briefBio': faculty.briefBio,
            })
        return results

    def books(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'title': faculty.title,
                'place': faculty.place,
                'publisher': faculty.publisher,
                'date': faculty.date,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def articles(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'journalTitle': faculty.journalTitle,
                'title': faculty.title,
                'date': faculty.date,
                'volume': faculty.volume,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def refereedProceedings(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'title': faculty.title,
                'place': faculty.place,
                'publisher': faculty.publisher,
                'date': faculty.date,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def nonRefereedProceedings(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'title': faculty.title,
                'place': faculty.place,
                'publisher': faculty.publisher,
                'date': faculty.date,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def chapters(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'title': faculty.title,
                'place': faculty.place,
                'publisher': faculty.publisher,
                'date': faculty.date,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def monographs(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'authors': faculty.authors,
                'title': faculty.title,
                'place': faculty.place,
                'publisher': faculty.publisher,
                'date': faculty.date,
                'pages': faculty.pages,
                'reference': faculty.reference,
                'url': faculty.getURL(),
            })
        return results

    def reviews(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'status': faculty.status,
                'publication': faculty.publication,
                'date': faculty.date,
                'pages': faculty.pages,
                'url': faculty.getURL(),
            })
        return results

    def presented(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'title': faculty.title,
                'date': faculty.date,
                'audience': faculty.audience,
                'url': faculty.getURL(),
            })
        return results

    def professional(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'description': faculty.description,
                'dates': faculty.dates,
            })
        return results

    def grants(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'agency': faculty.agency,
                'title': faculty.title,
                'dates': faculty.dates,
                'amount': faculty.amount,
            })
        return results

    def officeHeld(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'description': faculty.description,
                'dates': faculty.dates,
            })
        return results

    def activities(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'description': faculty.description,
                'dates': faculty.dates,
            })
        return results

    def token(self):
        return createToken()

    def is_chair(self):
        if self.context.orgStatus == 'Chair':
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus)
        elif self.context.orgStatus != 'Chair':
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus == 'N/A')
        else:
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus)

    def is_acting_chair(self):
        if self.context.orgStatus == 'Acting Chair':
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus)
        elif self.context.orgStatus != 'Chair':
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus == 'N/A')
        else:
            return checkPermission('yc.facultycv.show_view', self.context.orgStatus)
