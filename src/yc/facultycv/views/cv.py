# -*- coding: utf-8 -*-
# from Products.CMFCore.permissions import ViewManagementScreens
# from Products.CMFCore.utils import getToolByName
from plone import api
from plone.protect.authenticator import createToken
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.security import checkPermission


class Cv(BrowserView):
    """A standard view of the CV
    """
    index = ViewPageTemplateFile('cv.pt')

    def __call__(self):
        return self.index()

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

    def token(self):
        return createToken()

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

    def serviceDepartment(self):
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

    def serviceSchool(self):
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

    def serviceCollege(self):
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

    def serviceGraduateCenter(self):
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

    def serviceUniversity(self):
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

    def coursesTaught(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'dept': faculty.dept,
                'number': faculty.number,
                'description': faculty.description,
            })
        return results

    def developed(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'description': faculty.description,
                'title': faculty.title,
            })
        return results

    def experienceFT(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'institution': faculty.institution,
                'rank': faculty.rank,
                'area': faculty.area,
                'dates': faculty.dates,
            })
        return results

    def experiencePT(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'institution': faculty.institution,
                'rank': faculty.rank,
                'area': faculty.area,
                'dates': faculty.dates,
            })
        return results

    def experienceNA(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'institution': faculty.institution,
                'rank': faculty.rank,
                'dates': faculty.dates,
            })
        return results

    def employmentRecord(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'rank': faculty.rank,
                'dates': faculty.dates,
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

    def patents(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'patent': faculty.patent,
                'title': faculty.title,
                'date': faculty.date,
                'inventor': faculty.inventor,
                'filed': faculty.filed,
                'issue': faculty.issue,
                'country': faculty.country,
                'url': faculty.getURL(),
            })
        return results

    def hideCv(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'hideCv': faculty.hideCv,
            })
        return results

    def scholarEnhance(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'scholarEnhance': faculty.scholarEnhance,
            })
        return results

    def teachEnhance(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'teachEnhance': faculty.teachEnhance,
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

    def pubEnhance(self):
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        brains = portal_catalog(path=current_path, portal_type='faculty2')
        for brain in brains:
            faculty = brain.getObject()
            results.append({
                'pubEnhance': faculty.pubEnhance,
            })
        return results

    def ife_method(self):
        """ Funky condition

        self.context = object for which this view was traversed
        """
        if self.context.status().startswith("ife"):
            return True
        else:
            return False

    def wip_method(self):
        """ Funky condition

        self.context = object for which this view was traversed
        """
        if self.context.status().startswith("wip"):
            return True
        else:
            return False

    def submitted_method(self):
        """ Funky condition

        self.context = object for which this view was traversed
        """
        if self.context.status().startswith("submitted"):
            return True
        else:
            return False

    def rip_method(self):
        """ Funky condition

        self.context = object for which this view was traversed
        """
        if self.context.status().startswith("rip"):
            return True
        else:
            return False

    def other_method(self):
        """ Funky condition

        self.context = object for which this view was traversed
        """
        if self.context.status().startswith("other"):
            return True
        else:
            return False

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
