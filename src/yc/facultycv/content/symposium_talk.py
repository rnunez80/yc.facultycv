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


class ISymposiumTalk(model.Schema):
    """ Marker interface for SymposiumTalk
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

    description = schema.Text(
        title=_('Summary'),
        required=False,
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


@implementer(ISymposiumTalk)
class SymposiumTalk(Item):
    """
    """

    # @property
    # def first_name(self):
    #     return self.first_name
    #
    # @first_name.setter
    # def first_name(self, value):
    #     pass
    #
    # @property
    # def last_name(self):
    #     return self.last_name
    #
    # @last_name.setter
    # def last_name(self, value):
    #     pass
    #
    # @property
    # def dept(self):
    #     return self.dept
    #
    # @dept.setter
    # def dept(self, value):
    #     pass
    #
    # @property
    # def orgStatus(self):
    #     return self.orgStatus
    #
    # @orgStatus.setter
    # def orgStatus(self, value):
    #     pass
    #
    # @property
    # def teachingTitle(self):
    #     return self.teachingTitle
    #
    # @teachingTitle.setter
    # def teachingTitle(self, value):
    #     pass
    #
    # @property
    # def employeeID(self):
    #     return self.employeeID
    #
    # @employeeID.setter
    # def employeeID(self, value):
    #     pass
