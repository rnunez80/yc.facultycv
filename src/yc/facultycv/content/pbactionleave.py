# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import api
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from plone.supermodel.directives import primary
from yc.facultycv import _
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
import transaction

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


collegeVotesVocab = SimpleVocabulary([
    SimpleTerm(value='', title=_('')),
    SimpleTerm(value='0', title=_('0')),
    SimpleTerm(value='1', title=_('1')),
    SimpleTerm(value='2', title=_('2')),
    SimpleTerm(value='3', title=_('3')),
    SimpleTerm(value='4', title=_('4')),
    SimpleTerm(value='5', title=_('5')),
    SimpleTerm(value='6', title=_('6')),
    SimpleTerm(value='7', title=_('7')),
    SimpleTerm(value='8', title=_('8')),
    SimpleTerm(value='9', title=_('9')),
    SimpleTerm(value='10', title=_('10')),
    SimpleTerm(value='11', title=_('11')),
    SimpleTerm(value='12', title=_('12')),
    SimpleTerm(value='13', title=_('13')),
    SimpleTerm(value='14', title=_('14')),
    SimpleTerm(value='15', title=_('15')),
    SimpleTerm(value='16', title=_('16')),
    SimpleTerm(value='17', title=_('17')),
    SimpleTerm(value='18', title=_('18')),
    SimpleTerm(value='19', title=_('19')),
    SimpleTerm(value='20', title=_('20')),
    SimpleTerm(value='21', title=_('21')),
    SimpleTerm(value='22', title=_('22')),
    SimpleTerm(value='23', title=_('23')),
    SimpleTerm(value='24', title=_('24')),
    SimpleTerm(value='25', title=_('25')),
    SimpleTerm(value='26', title=_('26')),
    SimpleTerm(value='27', title=_('27')),
    SimpleTerm(value='28', title=_('28')),
])

deptVotesVocab = SimpleVocabulary([
    SimpleTerm(value='', title=_('')),
    SimpleTerm(value='0', title=_('0')),
    SimpleTerm(value='1', title=_('1')),
    SimpleTerm(value='2', title=_('2')),
    SimpleTerm(value='3', title=_('3')),
    SimpleTerm(value='4', title=_('4')),
    SimpleTerm(value='5', title=_('5')),
])

DurationOptionsVocab = SimpleVocabulary([
    SimpleTerm(value='', title=_('')),
    SimpleTerm(value='Full Year/80% Of Annual Salary', title=_('Full Year/80% Of Annual Salary')),
    SimpleTerm(value='Half Year/Full Pay', title=_('Half Year/Full Pay')),
])


class IDuration(Interface):
    # options = schema.Choice(title=_(u'Options'),
    #                         required=False,
    #                         vocabulary=DurationOptionsVocab)
    options = schema.TextLine(title=_(u'Options'), required=False, default=u'')
    semester = schema.TextLine(title=_(u'Semester(s)'), required=False, default=u'')


class IDates(Interface):
    dates = schema.TextLine(title=_(u'Dates'), required=False, default=u'')
    # semester = schema.TextLine(title=_(u'Semester(s)'), required=False, default=u'')
    Purpose = schema.TextLine(title=_(u'Purpose'), required=False, default=u'')


departmentsVocab = SimpleVocabulary([
            SimpleTerm(value=u'accounting_finance', title=_(u'Accounting and Finance')),
            SimpleTerm(value=u'behavioral_sciences', title=_(u'Behavioral Sciences')),
            SimpleTerm(value=u'biology', title=_(u'Biology')),
            SimpleTerm(value=u'business_economics', title=_(u'Business and Economics')),
            SimpleTerm(value=u'chemistry', title=_(u'Chemistry')),
            SimpleTerm(value=u'earth_physical_sciences', title=_(u'Earth and Physical Sciences')),
            SimpleTerm(value=u'english', title=_(u'English')),
            SimpleTerm(value=u'health_professions', title=_(u'Health Professions')),
            SimpleTerm(value=u'health_human_performance', title=_(u'Health and Human Performance')),
            SimpleTerm(value=u'history_philosophy_anthropology', title=_(u'History, Philosophy, and Anthropology')),
            SimpleTerm(value=u'library', title=_(u'Library')),
            SimpleTerm(value=u'mathematics_computer_science', title=_(u'Mathematics and Computer Science')),
            SimpleTerm(value=u'nursing', title=_(u'Nursing')),
            SimpleTerm(value=u'occupational_therapy', title=_(u'Occupational Therapy')),
            SimpleTerm(value=u'performing_fine_arts', title=_(u'Performing and Fine Arts')),
            SimpleTerm(value=u'social_work', title=_(u'Social Work')),
            SimpleTerm(value=u'teacher_education', title=_(u'Teacher Education')),
            SimpleTerm(value=u'world_languages_literatures_humanities', title=_(u'World Languages, Literatures, and Humanities')),
            SimpleTerm(value=u'special', title=_(u'Special Circumstances (See Academic Affairs)')),
        ])


def managers_validator(value):
    if (value and len(value) == 0) or value == '':
        raise Invalid('You must select at least one')
    return True


class IPbactionleave(model.Schema):
    """ Marker interface and Dexterity Python Schema for Pbactionleave
    """
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

    primary('appealLetter')
    directives.write_permission(appealLetter='yc.facultycv.AddFaculty')
    directives.read_permission(appealLetter='yc.facultycv.AddPbaction')
    directives.write_permission(appealLetter='yc.facultycv.EditAppeal')
    directives.read_permission(appealLetter='yc.facultycv.ViewAppeal')
    appealLetter = NamedBlobFile(
        title=_('Appeal letter to the President/P&B Committee'),
        description=_('Appeal letter to the President/P&B Committee'),
        required=False,
    )

    primary('appealOther')
    directives.write_permission(appealOther='yc.facultycv.AddFaculty')
    directives.read_permission(appealOther='yc.facultycv.AddPbaction')
    directives.write_permission(appealOther='yc.facultycv.EditAppeal')
    directives.read_permission(appealOther='yc.facultycv.ViewAppeal')
    appealOther = NamedBlobFile(
        title=_('Additional Appeal Materials'),
        description=_(
            'Please feel free to include any additional appeal materials'),
        required=False,
    )

    directives.write_permission(YearsOfService='yc.facultycv.AddPbaction')
    directives.mode(YearsOfService='hidden')
    YearsOfService = schema.TextLine(
        title=_('Years Of Service'),
        required=False,
    )

    primary('managers')
    directives.write_permission(managers='yc.facultycv.AddPbaction')
    directives.omitted('managers')
    directives.no_omit(IAddForm, 'managers')
    directives.no_omit(IEditForm, 'managers')
    managers = schema.Choice(
      title=_('Department P&B Committees'),
      vocabulary=departmentsVocab,
      required=False,
      constraint=managers_validator,
   )

    directives.write_permission(deptVotesYes='yc.facultycv.EditPBDeptChair')
    directives.read_permission(deptVotesYes='yc.facultycv.ViewPBDeptCommittees')
    deptVotesYes = schema.Choice(
        title=_('Yes (Dept.)'),
        required=False,
        description=_('Yes Votes by the Department P&B'),
        vocabulary=deptVotesVocab,
    )

    directives.write_permission(deptVotesAbstain='yc.facultycv.EditPBDeptChair')
    directives.read_permission(deptVotesAbstain='yc.facultycv.ViewPBDeptCommittees')
    deptVotesAbstain = schema.Choice(
        title=_('Abstain (Dept.)'),
        required=False,
        description=_('Abstain Votes by the Department P&B'),
        vocabulary=deptVotesVocab,
    )

    directives.write_permission(deptVotesNo='yc.facultycv.EditPBDeptChair')
    directives.read_permission(deptVotesNo='yc.facultycv.ViewPBDeptCommittees')
    deptVotesNo = schema.Choice(
        title=_('No (Dept.)'),
        required=False,
        description=_('No Votes by the Department P&B'),
        vocabulary=deptVotesVocab,
    )

    directives.write_permission(collegeVotesYes='yc.facultycv.EditPBCollegeChair')
    directives.read_permission(collegeVotesYes='yc.facultycv.ViewPBCollegeCommittees')
    collegeVotesYes = schema.Choice(
        title=_('Yes (College)'),
        required=False,
        description=_('Yes Votes by the college P&B'),
        vocabulary=collegeVotesVocab,
    )

    directives.write_permission(collegeVotesAbstain='yc.facultycv.EditPBCollegeChair')
    directives.read_permission(collegeVotesAbstain='yc.facultycv.ViewPBCollegeCommittees')
    collegeVotesAbstain = schema.Choice(
        title=_('Abstain (College)'),
        required=False,
        description=_('Abstain Votes by the college P&B'),
        vocabulary=collegeVotesVocab,
    )

    directives.write_permission(collegeVotesNo='yc.facultycv.EditPBCollegeChair')
    directives.read_permission(collegeVotesNo='yc.facultycv.ViewPBCollegeCommittees')
    collegeVotesNo = schema.Choice(
        title=_('No (College)'),
        required=False,
        description=_('No Votes by the college P&B'),
        vocabulary=collegeVotesVocab,
    )

    directives.write_permission(eligibleCollegeVoters='yc.facultycv.EditPBCollegeChair')
    directives.read_permission(eligibleCollegeVoters='yc.facultycv.ViewPBCollegeCommittees')
    eligibleCollegeVoters = schema.Choice(
        title=_('Eligible College Voters'),
        required=False,
        vocabulary=collegeVotesVocab,
    )

    directives.write_permission(eligibleDeptVoters='yc.facultycv.EditPBDeptChair')
    directives.read_permission(eligibleDeptVoters='yc.facultycv.ViewPBDeptCommittees')
    eligibleDeptVoters = schema.Choice(
        title=_('Eligible Dept Voters'),
        required=False,
        vocabulary=deptVotesVocab,
    )

    primary('moreDocs')
    directives.write_permission(moreDocs='yc.facultycv.AddPbaction')
    directives.widget(moreDocs=RadioFieldWidget)
    moreDocs = schema.Choice(
        title=_('Additional Material Located in the Provost office?'),
        values=['', 'no', 'yes'],
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

    directives.write_permission(duration='yc.facultycv.AddPbaction')
    directives.widget(duration=DataGridFieldFactory)
    duration = schema.List(
        title=
        _(u"A. Duration and Dates of the proposed fellowship leave (check one only)"
          ),
        value_type=DictRow(title=_(u"Data"), schema=IDuration),
        required=False,
    )

    directives.mode(purpose='hidden')
    directives.write_permission(purpose='yc.facultycv.AddPbaction')
    purpose = schema.Text(
        title=_(u'B. Briefly describe the purpose or purposes of the proposed fellowship leave:'
                ),
        description=_(u'Research  (including study and related):_'),
        required=False,
    )

    directives.mode(improvement='hidden')
    directives.write_permission(improvement='yc.facultycv.AddPbaction')
    improvement = schema.TextLine(
        title=_(u'Improvement of Teaching'),
        required=False,
    )

    directives.mode(creative='hidden')
    directives.write_permission(creative='yc.facultycv.AddPbaction')
    creative = schema.TextLine(
        title=_(u'Creative work in literature of the arts'),
        required=False,
    )

    directives.mode(educational='hidden')
    directives.write_permission(educational='yc.facultycv.AddPbaction')
    educational = schema.TextLine(
        title=_(
            u'Educational Travel (only persons appointed prior to July 1, 1965)'
        ),
        required=False,
    )

    directives.mode(activities='hidden')
    directives.write_permission(activities='yc.facultycv.AddPbaction')
    activities = schema.Text(
        title=_(
            u'C. Briefly describe any activities which you have undertaken '
            u'and/or completed to date in conjuction with the proposed fellowship leave:'
        ),
        required=False,
        description=_(u'If None just leave it blank.'),
    )

    directives.mode(list='hidden')
    directives.write_permission(list='yc.facultycv.AddPbaction')
    list = schema.Text(
        title=_(u'D. List the location(s) where the activities '
                u'associated with the proposed fellowship leave will occur:'),
        required=False,
    )

    directives.mode(sponsored='hidden')
    directives.write_permission(sponsored='yc.facultycv.AddPbaction')
    sponsored = schema.Text(
        title=_(
            u'E.Outside sponsorship and/or service- '
            u'Will any of the activities associated with the proposed fellowship '
            u'leave be sponsored or facilitated by an institution other than'
            u' The City University of New York?'),
        required=False,
        description=_(u'If yes, please name the institution(s) and describe the '
                      u'nature of the sponsorship or facilitation(i.e laboratory privileges,'
                      u' use of private archives or collections, collaborations with staff, etc.):'
                      ),
    )

    directives.mode(anticipate='hidden')
    directives.write_permission(anticipate='yc.facultycv.AddPbaction')
    anticipate = schema.Text(
        title=_(
            u'Do you anticipate performing a service for any institution other '
            u'than The City University of New York during the proposed fellowship leave?'
        ),
        required=False,
        description=_(
            u'If yes, please name the insitution(s), '
            u'describe the service which you anticipate performing and '
            u'state the nature and amount of any compensation which '
            u'you expect to receive for performing such service:'),
    )

    directives.mode(nature='hidden')
    directives.write_permission(nature='yc.facultycv.AddPbaction')
    nature = schema.Text(
        title=
        _(u'List the nature and amount of any funding for the proposed'
          u'fellowship leave (other than your University salary and personal resources) '
          u'which you have been awarded or for which you have applied or intend to apply:'
          ),
        required=False,
        description=_(u'If None just leave it blank.'),
    )

    directives.write_permission(dates='yc.facultycv.AddPbaction')
    directives.widget(dates=DataGridFieldFactory)
    dates = schema.List(
        title=
        _(u"F. Indicate the dates and purpose of any leaves taken during the prior ten (10) years:"
          ),
        value_type=DictRow(title=_(u"Data"), schema=IDates),
        required=False,
    )

    directives.mode(attestation='hidden')
    directives.write_permission(attestation='yc.facultycv.AddPbaction')
    attestation = schema.Text(
        title=_(u'III. Attestation of Applicant'),
        required=False,
    )

    directives.mode(chairperson='hidden')
    directives.write_permission(chairperson='yc.facultycv.EditPBMemo')
    chairperson = schema.Text(
        title=_(u'IV. To be completed by the department chairperson'),
        required=False,
        description=_(
            u'Briefly describe how the stated purpose of the applicant '
            u'for the fellowship leave is consonant with the mission of the department:'
        ),
    )

    directives.mode(intentCover='hidden')
    intentCover = schema.Text(
        title=_(u'Course Coverage'),
        required=False,
        description=_(
            u'How does the department intent to cover the  courses '
            u'and related responsibilities of the applicant'
            u' at the college during the period of the proposed leave:'),
    )

    directives.write_permission(chairMemo='yc.facultycv.EditPBMemo')
    directives.write_permission(chairMemo='yc.facultycv.AddPbaction')
    directives.read_permission(chairMemo='yc.facultycv.ViewPBDeptCommittees')
    chairMemo = NamedBlobFile(
        title=_(u'Signed Form'),
        required=False,
        description=_(u"The form should have the chair's signature"),
    )

    directives.write_permission(facultyMemo='yc.facultycv.AddPbaction')
    directives.read_permission(facultyMemo='yc.facultycv.ViewPBDeptCommittees')
    facultyMemo = NamedBlobFile(
        title=_(u'Additional Documentation'),
        required=False,
        description=
        _(u'You can attach an additional file to support your case, DO NOT INCLUDE the signed leave form'
          ),
    )

    directives.mode(preview='hidden')
    directives.read_permission(preview='yc.facultycv.PreviewFile')
    preview = schema.TextLine(
        title=_('Preview'),
        required=False,
        default=u'True',
    )

    # directives.write_permission(eligibleCollegeVoters='yc.facultycv.EditPBCollegeChair')
    # directives.read_permission(eligibleCollegeVoters='yc.facultycv.ViewPBCollegeCommittees')
    # eligibleCollegeVoters = schema.Choice(
    #     title=_('Eligible College Voters'),
    #     required=False,
    #     vocabulary=collegeVotesVocab,
    # )
    #
    # directives.write_permission(eligibleDeptVoters='yc.facultycv.EditPBDeptChair')
    # directives.read_permission(eligibleDeptVoters='yc.facultycv.ViewPBDeptCommittees')
    # eligibleDeptVoters = schema.Choice(
    #     title=_('Eligible Dept Voters'),
    #     required=False,
    #     vocabulary=deptVotesVocab,
    # )

    directives.write_permission(expirationDate='yc.facultycv.EditPBCollegeChair')
    directives.read_permission(expirationDate='yc.facultycv.EditPBCollegeChair')
    expirationDate = schema.Datetime(
        title=_('Expiration Date'),
        required=False,
    )


@implementer(IPbactionleave)
class Pbactionleave(Item):
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
    #         YearsOfService = str(self.YearsOfService) if self.YearsOfService else str(self.Type())
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

    @property
    def title(self):
        if self.YearsOfService:
            years_of_service = str(self.YearsOfService)
        else:
            years_of_service = str(self.Type())
        return years_of_service

    @title.setter
    def title(self, value):
        pass

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
