# -*- coding: utf-8 -*-
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
from zope.interface import Invalid
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


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

CompetencyPriorityVocab = SimpleVocabulary([
    SimpleTerm(value=u'', title=_(u'')),
    SimpleTerm(value=u'Critical', title=_(u'Critical')),
    SimpleTerm(value=u'Necessary', title=_(u'Necessary')),
    SimpleTerm(value=u'Useful', title=_(u'Useful')),
])

PerformarnceAssesmentCompetencyVocab = SimpleVocabulary([
    SimpleTerm(value=u'Outstanding', title=_(u'Outstanding')),
    SimpleTerm(value=u'Effective', title=_(u'Effective')),
    SimpleTerm(value=u'Needs Improvement', title=_(u'Needs Improvement')),
    SimpleTerm(value=u'Unsatisfactory', title=_(u'Unsatisfactory')),
    SimpleTerm(value=u'Not Observed', title=_(u'Not Observed')),
])

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
    SimpleTerm(value=u'world_languages_literatures_humanities',
               title=_(u'World Languages, Literatures, and Humanities')),
    SimpleTerm(value=u'special', title=_(u'Special Circumstances (See Academic Affairs)')),
])


def managers_validator(value):
    if (value and len(value) == 0) or value == '':
        raise Invalid('You must select at least one')
    return True


class IPbactionclt(model.Schema):
    """ Marker interface and Dexterity Python Schema for Pbactionclt
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

    directives.write_permission(
        aCompetencyPriority='yc.facultycv.EditPBMemo')
    aCompetencyPriority = schema.Choice(
        title=_(u"COMMUNICATION: Competency's Priority"),
        description=
        _(u'Communicates oral and written information concisely in a form appropriate to the target audience.'
          u'Listens effectively, seeks and provides timely, frank, honest feedback'
          ),
        vocabulary=CompetencyPriorityVocab,
        required=False,
    )

    directives.write_permission(
        aPerformarnceAssesmentCompetency='yc.facultycv.EditPBMemo')
    aPerformarnceAssesmentCompetency = schema.Choice(
        title=_(u"COMMUNICATION: Performance Assessment for this Competency"),
        required=False,
        vocabulary=PerformarnceAssesmentCompetencyVocab,
    )

    directives.write_permission(aComments='yc.facultycv.EditPBMemo')
    aComments = schema.Text(
        title=_(u'COMMUNICATION: Comments'),
        required=False,
    )

    directives.write_permission(
        bCompetencyPriority='yc.facultycv.EditPBMemo')
    bCompetencyPriority = schema.Choice(
        title=_(u"INTERPERSONAL: Competency's Priority"),
        required=False,
        vocabulary=CompetencyPriorityVocab,
    )

    directives.write_permission(
        bPerformarnceAssesmentCompetency='yc.facultycv.EditPBMemo')
    bPerformarnceAssesmentCompetency = schema.Choice(
        title=_(u'INTERPERSONAL: Performance Assessment for this Competency'),
        required=False,
        vocabulary=PerformarnceAssesmentCompetencyVocab,
    )

    directives.write_permission(bComments='yc.facultycv.EditPBMemo')
    bComments = schema.Text(
        title=_(u'INTERPERSONAL: Comments'),
        required=False,
    )

    directives.write_permission(
        cCompetencyPriority='yc.facultycv.EditPBMemo')
    cCompetencyPriority = schema.Choice(
        title=_(u"CUSTOMER SERVICE: Competency's Priority"),
        required=False,
        vocabulary=CompetencyPriorityVocab,
    )

    directives.write_permission(
        cPerformarnceAssesmentCompetency='yc.facultycv.EditPBMemo')
    cPerformarnceAssesmentCompetency = schema.Choice(
        title=_(
            u"CUSTOMER SERVICE: Performance Assessment for this Competency"),
        required=False,
        vocabulary=PerformarnceAssesmentCompetencyVocab,
    )

    directives.write_permission(cComments='yc.facultycv.EditPBMemo')
    cComments = schema.Text(
        title=_(u'CUSTOMER SERVICE: Comments'),
        required=False,
    )

    directives.write_permission(
        dCompetencyPriority='yc.facultycv.EditPBMemo')
    dCompetencyPriority = schema.Choice(
        title=_(u"PROFESSIONALISM: Competency's Priority"),
        required=False,
        vocabulary=CompetencyPriorityVocab,
    )

    directives.write_permission(
        dPerformarnceAssesmentCompetency='yc.facultycv.EditPBMemo')
    dPerformarnceAssesmentCompetency = schema.Choice(
        title=_(u'PROFESSIONALISM: Performance Assessment for this Competency'),
        required=False,
        vocabulary=PerformarnceAssesmentCompetencyVocab,
    )

    directives.write_permission(dComments='yc.facultycv.EditPBMemo')
    dComments = schema.Text(
        title=_(u'PROFESSIONALISM: Comments'),
        required=False,
    )

    directives.write_permission(
        eCompetencyPriority='yc.facultycv.EditPBMemo')
    eCompetencyPriority = schema.Choice(
        title=_(u'DIVERSITY: Priority of the Competency'),
        required=False,
        vocabulary=CompetencyPriorityVocab,
    )

    directives.write_permission(
        ePerformarnceAssesmentCompetency='yc.facultycv.EditPBMemo')
    ePerformarnceAssesmentCompetency = schema.Choice(
        title=_(u'DIVERSITY: Performance Assessment for this Competency'),
        required=False,
        vocabulary=PerformarnceAssesmentCompetencyVocab,
    )

    directives.write_permission(eComments='yc.facultycv.EditPBMemo')
    eComments = schema.Text(
        title=_(u'DIVERSITY: Comments'),
        required=False,
    )

    directives.write_permission(skillSelectRate='yc.facultycv.EditPBMemo')
    skillSelectRate = schema.Text(
        title=_(u'Domain Related Competencies'),
        required=False,
        description=_(u'Select 1 or 2 domain competencies (technical skills) '
                      u'that are important to the position responsibilities '
                      u'of the employee  and identify and rate them below.'),
    )

    directives.write_permission(particularStrengthEmployee='yc.facultycv.EditPBMemo')
    particularStrengthEmployee = schema.Text(
        title=_(u'A. Particular Strengths of Employee'),
        required=False,
    )

    directives.write_permission(improvedDeveloped='yc.facultycv.EditPBMemo')
    improvedDeveloped = schema.Text(
        title=_(u'B. Areas to be Improved and Developed'),
        required=False,
        description=_(u'Indicate means for making improvements.'),
    )

    directives.write_permission(projectGoals='yc.facultycv.EditPBMemo')
    projectGoals = schema.Text(
        title=_(u'C. Projected Goals and Targets for the Coming Year'),
        required=False,
        description=_(u'(To be completed for the next evaluation.) '
                      u'Include any changes/additions to the key responsibilities of the employee. '
                      u'Include goals and targets for the coming year. '
                      u'These should be related to department, division and college goals.'
                      ),
    )

    directives.write_permission(contributeCollege='yc.facultycv.EditPBMemo')
    contributeCollege = schema.Text(
        title=_(u'D. Contributions to the College Community'),
        required=False,
    )

    employeeComments = schema.Text(
        title=_(u"III. Employee's Comments"),
        required=False,
    )

    directives.write_permission(chairsComments='yc.facultycv.EditPBMemo')
    chairsComments = schema.Text(
        title=_(u"IV. Chair's Comments"),
        required=False,
    )

    directives.write_permission(chairMemo='yc.facultycv.EditPBMemo')
    directives.read_permission(chairMemo='yc.facultycv.ViewPBDeptCommittees')
    chairMemo = NamedBlobFile(
        title=_(u"Chair's Report for CLT"),
        description=_(
            u'The Report of Evaluation should have the signature of the chair.'
        ),
        required=False,
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
    # new field
    directives.mode(can_see_votes='hidden')
    directives.read_permission(can_see_votes='yc.facultycv.ShowView')
    can_see_votes = schema.TextLine(
        title=_('Can See Votes'),
        required=False,
        default=u'True',
    )

@implementer(IPbactionclt)
class Pbactionclt(Item):
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
            years_of_service = str(self.YearsOfService).replace('Promotion CTL to Senior CTL',
                                                                'Promotion CLT to Senior CLT').replace(
                'promotion-ctl-to-senior-ctl', 'Promotion CLT to Senior CLT').replace('promotion',
                                                                                      'Promotion')
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
