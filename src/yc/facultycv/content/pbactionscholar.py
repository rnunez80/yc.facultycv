# -*- coding: utf-8 -*-
from plone import api
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from yc.facultycv import _
from zope import schema
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory


@provider(IContextAwareDefaultFactory)
def get_container_first_name(context):
    try:
        return str(context.aq_parent.first_name)
    except:
        pass


@provider(IContextAwareDefaultFactory)
def get_container_last_name(context):
    try:
        return str(context.aq_parent.last_name)
    except:
        pass


@provider(IContextAwareDefaultFactory)
def get_container_employeeID(context):
    try:
        return str(context.aq_parent.employeeID)
    except:
        pass


@provider(IContextAwareDefaultFactory)
def getTeachingTitle(context):
    try:
        return str(context.aq_parent.teachingTitle)
    except:
        pass


@provider(IContextAwareDefaultFactory)
def getOrgStatus(context):
    try:
        return str(context.aq_parent.orgStatus)
    except:
        pass


@provider(IContextAwareDefaultFactory)
def getDept(context):
    try:
        return str(context.aq_parent.dept)
    except:
        pass


class IPbactionscholar(model.Schema):
    """ Marker interface and Dexterity Python Schema for Pbactionscholar
    """
    title = schema.TextLine(
        title=_('Title'),
        description=u'',
        required=False,
    )

    directives.mode(orgStatus='hidden')
    orgStatus = schema.TextLine(
        title=_('orgStatus'),
        required=False,
        defaultFactory=getOrgStatus,
    )

    directives.mode(first_name='hidden')
    first_name = schema.TextLine(
        title=_('First Name'),
        required=False,
        defaultFactory=get_container_first_name,
    )
    directives.mode(last_name='hidden')
    last_name = schema.TextLine(
        title=_('Last Name'),
        required=False,
        defaultFactory=get_container_last_name,
    )

    directives.mode(employeeID='hidden')
    employeeID = schema.TextLine(
        title=_('Employee ID'),
        required=False,
        defaultFactory=get_container_employeeID,
    )

    directives.mode(teachingTitle='hidden')
    teachingTitle = schema.TextLine(
        title=_('Title'),
        required=False,
        description=_('Enter Current Teaching Title'),
        defaultFactory=getTeachingTitle,
    )

    directives.mode(dept='hidden')
    dept = schema.TextLine(
        title=_('Department'),
        required=False,
        defaultFactory=getDept,
    )


@implementer(IPbactionscholar)
class Pbactionscholar(Item):
    """
    """

    # @property
    # def description(self):
    #     try:
    #         first_name = str(self.first_name)
    #         last_name = str(self.last_name)
    #         dept = str(self.dept)
    #         AND = ' and '
    #         orgStatus = str(self.orgStatus)
    #         functionalTitle = str(self.teachingTitle)
    #         YearsOfService = str(self.title) if self.title else str(self.Type())
    #         space = ' '
    #         of = ' - '
    #         Chair = first_name + space + last_name + of + functionalTitle + AND + orgStatus + of + dept + of + YearsOfService
    #         NotChair = first_name + space + last_name + of + functionalTitle + of + dept + of + YearsOfService
    #         if orgStatus.startswith('Chair') or orgStatus.startswith('Acting Chair'):
    #             return Chair
    #         return NotChair
    #     except:
    #         pass
    #
    # @description.setter
    # def description(self, value):
    #     pass

    # @property
    # def title(self):
    #     try:
    #         if self.title:
    #             years_of_service = str(self.title)
    #         else:
    #             years_of_service = str(self.Type())
    #         return years_of_service
    #     except:
    #         pass
    #
    # @title.setter
    # def title(self, value):
    #     pass

    # def setManagers(self, managers):
    #     """
    #     """
    #
    #     field = self.getField('managers')
    #     currentManagers = field.get(self)
    #     field.set(self, managers)
    #     userId = 'unit-' + managers + '-committee'
    #     self.manage_setLocalRoles(userId, ['PBdept', 'Reader'])
    #     deptchair = 'unit-' + managers + '-chair'
    #     self.manage_setLocalRoles(deptchair, ['PBdeptChair', 'Reader'])
    #     collegechair = 'unit-college-chair'
    #     self.manage_setLocalRoles(collegechair, ['PBhead', 'Reader'])
    #     PandB = 'unit-college-committee'
    #     self.manage_setLocalRoles(PandB, ['PBcollege', 'Reader'])
