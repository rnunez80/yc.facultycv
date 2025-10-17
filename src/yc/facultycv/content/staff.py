# -*- coding: utf-8 -*-
# from Products.CMFCore.utils import getToolByName
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone.app.z3cform.widgets.select import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from yc.facultycv import _
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from zope.schema.fieldproperty import FieldProperty
from AccessControl import getSecurityManager
from plone import api
from zExceptions import Unauthorized
from zope.security import checkPermission

class IOfficeHoursRow(Interface):
    day = schema.TextLine(title=_('Day'), required=False)
    time = schema.TextLine(title=_('Time'), required=False)


class IStaff(model.Schema):
    """ Marker interface and Dexterity Python Schema for Staff
    """

    directives.mode(title='hidden')
    title = schema.TextLine(
        title=_('Title'),
        required=False,
    )

    directives.omitted('employeeID')
    directives.read_permission(employeeID='cmf.ModifyPortalContent')
    employeeID = schema.TextLine(
        title=_('Employee ID'),
        required=False,
    )

    directives.read_permission(userid='cmf.ModifyPortalContent')
    userid = schema.TextLine(
        title=_('User ID'),
        required=False,
    )

    directives.omitted('employeeType')
    employeeType = schema.TextLine(
        title=_('Employee Type'),
        required=False,
    )

    directives.omitted('first_name')
    first_name = schema.TextLine(
        title=_('First Name'),
        required=False,

    )

    directives.omitted('last_name')
    last_name = schema.TextLine(
        title=_('Last Name'),
        required=False,
    )

    directives.omitted('teachingTitle')
    teachingTitle = schema.TextLine(
        title=_('Functional Title'),
        required=False,
        description=_('Enter Current Teaching Title'),
    )

    directives.omitted('otherTitle')
    otherTitle = schema.TextLine(
        title=_('Other Title'),
        required=False,
        description=_(
            'Enter Other Titles That you have Ex. WAC Program Coordinator'),
    )

    directives.omitted('email')
    email = schema.TextLine(
        title=_('Email'),
        required=False,
    )

    # website = schema.URI(
    #     title=_('Personal Website'),
    #     required=False,
    #     description=
    #     _('External Web address with more info about the faculty. http:// is required'
    #       ),
    # )
    website = schema.TextLine(
        title=_('Personal Website'),
        required=False,
        default=u'',
    )

    directives.omitted('officePhone')
    officePhone = schema.TextLine(
        title=_('Office Phone Number'),
        required=False,
        description=_(
            'Please use the full number in the following format 718-262-****'),
    )

    directives.omitted('officeLocation')
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

    directives.omitted('dept')
    dept = schema.TextLine(
        title=_('Department'),
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

    directives.read_permission(subjects='zope2.View')
    directives.write_permission(subjects='cmf.ModifyPortalContent')
    directives.no_omit("subjects")
    subjects = schema.Tuple(
        title=_("label_tags", default="Tags"),
        description=_(
            "help_tags",
            default="Tags are commonly used for ad-hoc organization of " + "content.",
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        "subjects", AjaxSelectFieldWidget, vocabulary="plone.app.vocabularies.Keywords"
    )

@implementer(IStaff)
class Staff(Container):
    """
    """

    @property
    def title(self):
        user = api.user.get(username=str(self.userid))
        first_name = user.getProperty('first_name') or ' '
        last_name = user.getProperty('last_name') or ' '
        space = ', '
        return str(last_name) + space + str(first_name)

    @title.setter
    def title(self, value):
        pass

    # def setTitle(self):
    #     self.title = self.computeFullname()

    # def setCurrentStatus(self):
    #     self.currentStatus = self.computeCurrentStatus()
    #
    # def computeCurrentStatus(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('currentStatus') or ' '
    #     return str(member_info)

    @property
    def currentStatus(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('currentStatus') or ' '
        return str(member_info)

    @currentStatus.setter
    def currentStatus(self, value):
        pass

    # def Title(self):
    #     return self.computeFullname()
    #
    # def computeFullname(self):
    #     user = api.user.get(username=str(self.userid))
    #     first_name = user.getProperty('first_name') or ' '
    #     last_name = user.getProperty('last_name') or ' '
    #     space = ', '
    #     return str(last_name) + space + str(first_name)

    # def setDescription(self):
    #     self.description = self.computeDescription()
    #
    # def Description(self):
    #     return self.computeDescription()
    #
    # def computeDescription(self):
    #     user = api.user.get(username=str(self.userid))
    #     first_name = user.getProperty('first_name') or ' '
    #     last_name = user.getProperty('last_name') or ' '
    #     fullname = user.getProperty('fullname') or ' '
    #     dept = user.getProperty('department') or ' '
    #     teachingTitle = user.getProperty('functionalTitle') or ' '
    #     officePhone = user.getProperty('phone') or ' '
    #     email = user.getProperty('email') or ' '
    #     space = ' '
    #     of = ' - '
    #     return str(fullname) + space + str(teachingTitle) + of + str(dept) + of + str(
    #         officePhone) + of + str(email)
    @property
    def description(self):
        user = api.user.get(username=str(self.userid))
        # first_name = user.getProperty('first_name') or ' '
        # last_name = user.getProperty('last_name') or ' '
        dept = user.getProperty('department') or ' '
        teachingTitle = user.getProperty('functionalTitle') or ' '
        officePhone = user.getProperty('phone') or ' '
        email = user.getProperty('email') or ' '
        AND = ' and '
        orgStatus = user.getProperty('orgStatus') or ' '
        space = ' '
        of = ' - '
        if orgStatus == 'Chair':
            return str(teachingTitle) + AND + str(orgStatus) + of + str(dept) + of + str(officePhone) + of + str(email)
        elif orgStatus == 'Acting Chair':
            return str(teachingTitle) + AND + str(orgStatus) + of + str(dept) + of + str(officePhone) + of + str(email)
        return str(teachingTitle) + of + str(dept) + of + str(officePhone) + of + str(email)

    @description.setter
    def description(self, value):
        pass

    # def setFirst_name(self):
    #     self.first_name = self.computeFirst_name()
    #
    # def computeFirst_name(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('first_name') or ' '
    #     return str(member_info)

    @property
    def first_name(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('first_name') or ' '
        return str(member_info)

    @first_name.setter
    def first_name(self, value):
        pass

    # def setLast_name(self):
    #     self.last_name = self.computeLast_name()
    #
    # def computeLast_name(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('last_name') or ' '
    #     return str(member_info)

    @property
    def last_name(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('last_name') or ' '
        return str(member_info)

    @last_name.setter
    def last_name(self, value):
        pass

    # def setTeachingTitle(self):
    #     self.teachingTitle = self.computeTeachingTitle()
    #
    # def computeTeachingTitle(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('functionalTitle') or ' '
    #     return str(member_info)

    @property
    def teachingTitle(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('functionalTitle') or ' '
        return str(member_info)

    @teachingTitle.setter
    def teachingTitle(self, value):
        pass

    # def setOtherTitle(self):
    #     self.otherTitle = self.computeOtherTitle()
    #
    # def computeOtherTitle(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('personalTitle') or ' '
    #     return str(member_info)

    @property
    def otherTitle(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('personalTitle') or ' '
        return str(member_info)

    @otherTitle.setter
    def otherTitle(self, value):
        pass

    # def setEmail(self):
    #     self.email = self.computeEmail()
    #
    # def computeEmail(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('email') or ' '
    #     return str(member_info)

    @property
    def email(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('email') or ' '
        return str(member_info)

    @email.setter
    def email(self, value):
        pass

    # def setOfficePhone(self):
    #     self.officePhone = self.computeOfficePhone()
    #
    # def computeOfficePhone(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('phone') or ' '
    #     return str(member_info)

    @property
    def officePhone(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('phone') or ' '
        return str(member_info)

    @officePhone.setter
    def officePhone(self, value):
        pass

    # def setOfficeLocation(self):
    #     self.officeLocation = self.computeLocation()
    #
    # def computeLocation(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('location') or ' '
    #     return str(member_info)

    @property
    def officeLocation(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('location') or ' '
        return str(member_info)

    @officeLocation.setter
    def officeLocation(self, value):
        pass

    # def setDept(self):
    #     self.dept = self.computeDept()
    #
    # def computeDept(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('department') or ' '
    #     return str(member_info)

    @property
    def dept(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('department') or ' '
        return str(member_info)

    @dept.setter
    def dept(self, value):
        pass

    # def setEmployeeType(self):
    #     self.employeeType = self.computeEmployeeType()
    #
    # def computeEmployeeType(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('employeeType') or ' '
    #     return str(member_info)

    @property
    def employeeType(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('employeeType') or ' '
        return str(member_info)

    @employeeType.setter
    def employeeType(self, value):
        pass

    # def setDivision(self):
    #     self.school = self.computeDivision()
    #
    # def computeDivision(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('division') or ' '
    #     return str(member_info)

    @property
    def division(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('division') or ' '
        return str(member_info)

    @division.setter
    def division(self, value):
        pass

    # def setOrgStatus(self):
    #     self.orgStatus = self.computeOrgStatus()
    #
    # def computeOrgStatus(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = member.getProperty('orgStatus') or ' '
    #     return str(member_info)

    @property
    def orgStatus(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('orgStatus') or ' '
        return str(member_info)

    @orgStatus.setter
    def orgStatus(self, value):
        pass

    @property
    def username(self):
        return str(self.userid)

    @username.setter
    def username(self, value):
        pass

    # backing attribute
    _subjects = ()

    @property
    def subjects(self):
        return getattr(self, "_subjects", ())

    @subjects.setter
    def subjects(self, value):
        # Permission check
        member = api.user.get_current()
        roles = api.user.get_roles(username=member.getUserName())
        if "Site Administrator" not in roles:
            raise Unauthorized("Only Site Administrators can modify the 'Tags' field.")

        # Normalize value to tuple
        if value is None:
            value = ()
        elif isinstance(value, list):
            value = tuple(value)
        elif not isinstance(value, tuple):
            value = (value,)

        # Set backing attribute
        self._subjects = value

        # Reindex the Subject index so the Contents/Folder view updates immediately
        self.reindexObject(idxs=["Subject"])
