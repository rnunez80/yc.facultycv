# -*- coding: utf-8 -*-
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


class IPbactionportfoliob(model.Schema):
    """ Marker interface and Dexterity Python Schema for Pbactionportfoliob
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
    directives.read_permission(appealLetter='yc.facultycv.AddPbactionportfoliob')
    directives.write_permission(appealLetter='yc.facultycv.EditAppeal')
    directives.read_permission(appealLetter='yc.facultycv.ViewAppeal')
    appealLetter = NamedBlobFile(
        title=_('Appeal letter to the President/P&B Committee'),
        description=_('Appeal letter to the President/P&B Committee'),
        required=False,
    )

    primary('appealOther')
    directives.write_permission(appealOther='yc.facultycv.AddFaculty')
    directives.read_permission(appealOther='yc.facultycv.AddPbactionportfoliob')
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
    directives.write_permission(moreDocs='yc.facultycv.AddPbactionportfoliob')
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

    directives.write_permission(FramingStatement='yc.facultycv.AddPbactionportfoliob')
    FramingStatement = NamedBlobFile(
        title=_(u"Candidate's Letter"),
        required=False,
    )

    directives.omitted(u'ReflectiveStatement')
    directives.write_permission(
        ReflectiveStatement='yc.facultycv.AddPbactionportfoliob')
    ReflectiveStatement = NamedBlobFile(
        title=_(u"Reflective Statement"),
        required=False,
        description=_(u"This is an intrinsically philosophical and more personal statement "
                      u"designed to pull together the disparate pieces of the faculty's background. "
                      u"It is intended to answer the why of goals in terms of professional values and philosophy."
                      u" This statement gives the candidate an opportunity to present a fuller picture of her-/himself"
                      u" to those evaluating the portfolio."),
    )

    directives.write_permission(chairMemo='yc.facultycv.EditPBMemo')
    chairMemo = NamedBlobFile(
        title=_(u"Memorandum of Evaluation"),
        required=False,
        description=_(
            u"The Memorandum of Evaluation should have the chair's signature"),
    )

    directives.write_permission(classroomObservations1='yc.facultycv.EditPBMemo')
    directives.read_permission(classroomObservations1='yc.facultycv.ViewPBDeptCommittees')
    classroomObservations1 = NamedBlobFile(
        title=_(u'Classroom Observations and Conferences 1'),
        description=_(
            u'Classroom Observations by faculty peers and notes from follow-up conference '
            u'for the last available two semesters.'),
        required=False,
    )

    directives.write_permission(classroomObservations2='yc.facultycv.EditPBMemo')
    directives.read_permission(classroomObservations2='yc.facultycv.ViewPBDeptCommittees')
    classroomObservations2 = NamedBlobFile(
        title=_(u'Classroom Observations and Conferences 2'),
        description=_(u'additional Classroom Observations'),
        required=False,
    )

    directives.write_permission(studentEvaluation1='yc.facultycv.EditPBMemo')
    directives.read_permission(studentEvaluation1='yc.facultycv.ViewPBDeptCommittees')
    studentEvaluation1 = NamedBlobFile(
        title=_(u'Student Evaluation of Teaching Effectiveness 1'),
        description=_(
            u'Student Evaluation summaries for the last available two semesters.'
        ),
        required=False,
    )

    directives.write_permission(studentEvaluation2='yc.facultycv.EditPBMemo')
    directives.read_permission(studentEvaluation2='yc.facultycv.ViewPBDeptCommittees')
    studentEvaluation2 = NamedBlobFile(
        title=_(u'Student Evaluation of Teaching Effectiveness 2'),
        required=False,
    )

    directives.omitted('SamplesAndCommentary1')
    directives.write_permission(
        SamplesAndCommentary1='yc.facultycv.AddPbactionportfoliob')
    SamplesAndCommentary1 = NamedBlobFile(
        title=_(u"Samples and Commentary 1"),
        required=False,
        description=_(
            u"The selection of two samples and commentaries will be used to illustrate two areas of expertise,"
            u" i.e., advisement (case study), syllabi (samples illustrating changes in teaching areas, "
            u"preparation of diverse number of courses etc.) for reappointments."
            u" For the tenure decision a third sample and commentary should be provided."
        ),
    )

    directives.omitted('SamplesAndCommentary2')
    directives.write_permission(
        SamplesAndCommentary2='yc.facultycv.AddPbactionportfoliob')
    SamplesAndCommentary2 = NamedBlobFile(
        title=_(u"Samples and Commentary 2"),
        required=False,
    )

    directives.omitted('SamplesAndCommentary3')
    directives.write_permission(
        SamplesAndCommentary3='yc.facultycv.AddPbactionportfoliob')
    SamplesAndCommentary3 = NamedBlobFile(
        title=_(u"Samples and Commentary 3"),
        required=False,
    )

    directives.write_permission(
        PublicationsAndOtherScholarlyWorks1='yc.facultycv.AddPbactionportfoliob')
    PublicationsAndOtherScholarlyWorks1 = NamedBlobFile(
        title=_(u"Publications And Other Scholarly Works"),
        required=False,
        description=_(u"Copies of publications and other scholarly works should be uploaded to the P&B online page in a"
                      u"commonly available electronic file format (e.g., MS Word, Adobe PDF, JPEG). Bulky materials,"
                      u"materials that cannot be made available in common electronic file formats,"
                      u"or that would go beyond the available"
                      u"space in the online submission,"
                      u"and which are submitted as part of a Portfolio may be deposited in the Office of"
                      u"Academic Affairs (2H07). If necessary,"
                      u"a list of the attached publications should be provided for clarity's sake."
                      ),
    )

    directives.write_permission(
        PublicationsAndOtherScholarlyWorks2='yc.facultycv.AddPbactionportfoliob')
    PublicationsAndOtherScholarlyWorks2 = NamedBlobFile(
        title=_(u"Publications And Other Scholarly Works"),
        required=False,
    )

    directives.write_permission(
        PublicationsAndOtherScholarlyWorks3='yc.facultycv.AddPbactionportfoliob')
    PublicationsAndOtherScholarlyWorks3 = NamedBlobFile(
        title=_(u"Publications And Other Scholarly Works"),
        required=False,
    )

    directives.write_permission(
        PublicationsAndOtherScholarlyWorks4='yc.facultycv.AddPbactionportfoliob')
    PublicationsAndOtherScholarlyWorks4 = NamedBlobFile(
        title=_(u"Publications And Other Scholarly Works"),
        required=False,
    )

    directives.write_permission(
        PublicationsAndOtherScholarlyWorks5='yc.facultycv.AddPbactionportfoliob')
    PublicationsAndOtherScholarlyWorks5 = NamedBlobFile(
        title=_(u"Publications And Other Scholarly Works"),
        required=False,
    )

    directives.write_permission(
        researchStatement='yc.facultycv.AddPbactionportfoliob')
    researchStatement = NamedBlobFile(
        title=_(u"Research Statement"),
        description=_(u"""A research statement framing the publication would be advisable, but is not mandatory."""),
        required=False,
    )

    directives.write_permission(
        ExternalPeerReviewOfScholarship1='yc.facultycv.EditPBMemo')
    directives.read_permission(
        ExternalPeerReviewOfScholarship1='yc.facultycv.ViewPBDeptCommittees'
    )
    ExternalPeerReviewOfScholarship1 = NamedBlobFile(
        title=_(u"External Peer Review Of Scholarship 1"),
        required=False,
        description=_(u"""There shall be three external peer evaluators, to be selected by the Department Chair in
        consultation with the Provost and with the input of the faculty candidate, each of whom will be sent the CV
        and a sample of the scholarship/creative work of the candidate by the Department Chair.<br /> In a case where
        the candidate is a Department Chair the consultation will be held with an Academic Dean and the Provost,
        and the evaluation invitation will be issued by an Academic Dean. All three external evaluations will be
        submitted by the Department Chair and become part of the candidate's online Portfolio."""),
    )

    directives.write_permission(
        ExternalPeerReviewOfScholarship2='yc.facultycv.EditPBMemo')
    directives.read_permission(
        ExternalPeerReviewOfScholarship2='yc.facultycv.ViewPBDeptCommittees'
    )
    ExternalPeerReviewOfScholarship2 = NamedBlobFile(
        title=_(u"External Peer Review Of Scholarship 2"),
        required=False,
    )

    directives.write_permission(
        ExternalPeerReviewOfScholarship3='yc.facultycv.EditPBMemo')
    directives.read_permission(
        ExternalPeerReviewOfScholarship3='yc.facultycv.ViewPBDeptCommittees'
    )
    ExternalPeerReviewOfScholarship3 = NamedBlobFile(
        title=_(u"External Peer Review Of Scholarship 3"),
        required=False,
    )

    directives.write_permission(appendix='yc.facultycv.AddPbactionportfoliob')
    appendix = NamedBlobFile(
        title=_(u"Appendix"),
        required=False,
        description=_(u"""Additional material considered relevant for the Portfolio (not mandatory)."""),
    )

    directives.omitted('DeanLetter')
    directives.write_permission(DeanLetter='yc.facultycv.AddPbactionportfoliob')
    DeanLetter = NamedBlobFile(
        title=_(u"Dean's Letter"),
        required=False,
        description=_(u"For tenure-track faculty only!"),
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


@implementer(IPbactionportfoliob)
class Pbactionportfoliob(Item):
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
