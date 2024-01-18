# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from yc.facultycv import _
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget


class IOfficeHoursRow(Interface):
    day = schema.TextLine(title=_('Day'), required=False)
    time = schema.TextLine(title=_('Time'), required=False)


class IPoe(model.Schema):
    """ Marker interface and Dexterity Python Schema for Poe
    """
    directives.mode(title='hidden')
    title = schema.TextLine(
        title=_('Title'),
        required=False,
    )

    first_name = schema.TextLine(
        title=_('First Name'),
        required=False,
    )

    last_name = schema.TextLine(
        title=_('Last Name'),
        required=False,
    )

    dept = schema.TextLine(
        title=_('Department'),
        required=False,
    )

    teachingTitle = schema.TextLine(
        title=_('Functional Title'),
        required=False,
        description=_('Enter Current Teaching Title'),
    )

    otherTitle = schema.TextLine(
        title=_('Other Title'),
        required=False,
        description=_(
            'Enter Other Titles That you have Ex. WAC Program Coordinator'),
    )

    email = schema.TextLine(
        title=_('Email'),
        required=False,
    )

    website = schema.TextLine(
        title=_('Personal Website'),
        required=False,
        default=u'',
    )

    officePhone = schema.TextLine(
        title=_('Office Phone Number'),
        required=False,
        description=_(
            'Please use the full number in the following format 718-262-****'),
    )

    officeLocation = schema.TextLine(
        title=_('Office Location'),
        required=False,
        description=_(
            'Please use the Building Code, a dash and the Room Number (AC-1H14)'
        ),
    )

    directives.widget(officeHours=DataGridFieldFactory)
    officeHours = schema.List(
        title=_("Office Hours"),
        value_type=DictRow(title=_("Office Hours"), schema=IOfficeHoursRow),
        required=False,
        description=_('Enter Your Office Hours'),
    )

    image = NamedBlobImage(
        title=_('Portrait'),
        description=_(''),
        required=False,
    )

    directives.mode(preview='hidden')
    directives.read_permission(preview='cmf.ReviewPortalContent')
    preview = schema.TextLine(
        title=_('Preview'),
        required=False,
        default=u'True',
    )

    directives.widget(briefBio=WysiwygFieldWidget)
    briefBio = schema.Text(
        title=_('Brief Biography/Faculty Expert'),
        required=False,
        description=_(
            'Brief Biography containing CV information or more than 1000 characters '
            '(including html tags) will be REJECTED'),
    )


@implementer(IPoe)
class Poe(Container):
    """ Content-type class for IPoe
    """

    @property
    def title(self):
        first_name = str(self.first_name) or ' '
        last_name = str(self.last_name) or ' '
        space = ', '
        return str(last_name) + space + str(first_name)

    @title.setter
    def title(self, value):
        pass

    @property
    def description(self):
        dept = str(self.dept) or ' '
        teachingTitle = str(self.teachingTitle) or ' '
        officePhone = str(self.officePhone) or ' '
        email = str(self.email) or ' '
        of = ' - '
        return str(teachingTitle) + of + str(dept) + of + str(officePhone) + of + str(email)

    @description.setter
    def description(self, value):
        pass

