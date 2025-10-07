# -*- coding: utf-8 -*-
# from Products.CMFCore.utils import getToolByName
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import api
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from yc.facultycv import _
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class IOfficeHoursRow(Interface):
    day = schema.TextLine(title=_('Day'), required=False)
    time = schema.TextLine(title=_('Time'), required=False)


getDegreeVocabulary = SimpleVocabulary([
    SimpleTerm(value='AA', title=_('AA')),
    SimpleTerm(value='AAS', title=_('AAS')),
    SimpleTerm(value='AB', title=_('AB')),
    SimpleTerm(value='ALM', title=_('ALM')),
    SimpleTerm(value='BA', title=_('BA')),
    SimpleTerm(value='BBA', title=_('BBA')),
    SimpleTerm(value='BE', title=_('BE')),
    SimpleTerm(value='BFA', title=_('BFA')),
    SimpleTerm(value='BM', title=_('BM')),
    SimpleTerm(value='BS', title=_('BS')),
    SimpleTerm(value='certificate', title=_('certificate')),
    SimpleTerm(value='DBA', title=_('DBA')),
    SimpleTerm(value='DC', title=_('DC')),
    SimpleTerm(value='DHSc', title=_('DHSc')),
    SimpleTerm(value='DMA', title=_('DMA')),
    SimpleTerm(value='DNS', title=_('DNS')),
    SimpleTerm(value='DPhil', title=_('DPhil')),
    SimpleTerm(value='DSW', title=_('DSW')),
    SimpleTerm(value='EDD', title=_('EDD')),
    SimpleTerm(value='JD', title=_('JD')),
    SimpleTerm(value='LLB', title=_('LLB')),
    SimpleTerm(value='LLM', title=_('LLM')),
    SimpleTerm(value='M Ed', title=_('M Ed')),
    SimpleTerm(value='MA', title=_('MA')),
    SimpleTerm(value='MBA', title=_('MBA')),
    SimpleTerm(value='MD', title=_('MD')),
    SimpleTerm(value='MFA', title=_('MFA')),
    SimpleTerm(value='MIA', title=_('MIA')),
    SimpleTerm(value='MLIS', title=_('MLIS')),
    SimpleTerm(value='MLS', title=_('MLS')),
    SimpleTerm(value='MM', title=_('MM')),
    SimpleTerm(value='MPA', title=_('MPA')),
    SimpleTerm(value='MPhil', title=_('MPhil')),
    SimpleTerm(value='MS', title=_('MS')),
    SimpleTerm(value='MSN', title=_('MSN')),
    SimpleTerm(value='MSW', title=_('MSW')),
    SimpleTerm(value='MVP', title=_('MVP')),
    SimpleTerm(value='non-degree', title=_('non-degree')),
    SimpleTerm(value='PhD', title=_('PhD')),
    SimpleTerm(value='PhDc', title=_('PhDc')),
    SimpleTerm(value='SB', title=_('SB')),
])

getStatusVocabulary = SimpleVocabulary([
    SimpleTerm(value='ife', title=_('In Field of Expertise')),
    SimpleTerm(value='other', title=_('Other Publication')),
    SimpleTerm(value='wip', title=_('Work in Progress')),
    SimpleTerm(value='submitted', title=_('Submitted to Journals')),
    SimpleTerm(value='rip', title=_('Research in Progress')),
])


class IEducationRow(Interface):
    # degree = schema.Choice(
    #     title=_('Degree'),
    #     required=False,
    #     vocabulary=getDegreeVocabulary
    # )
    degree = schema.TextLine(title=_('Degree'), required=False, default=u'')
    institution = schema.TextLine(title=_('Institution'), required=False, default=u'')
    area = schema.TextLine(title=_('Field'), required=False, default=u'')
    year = schema.TextLine(title=_('Year'), required=False, default=u'')


class IExperienceFT(Interface):
    institution = schema.TextLine(title=_('Institution'), required=False)
    rank = schema.TextLine(title=_('Rank'), required=False)
    area = schema.TextLine(title=_('Area'), required=False)
    dates = schema.TextLine(title=_('Dates'), required=False)


class IExperiencePT(Interface):
    institution = schema.TextLine(title=_('Institution'), required=False)
    rank = schema.TextLine(title=_('Rank'), required=False)
    area = schema.TextLine(title=_('Area'), required=False)
    dates = schema.TextLine(title=_('Dates'), required=False)


class IExperienceNA(Interface):
    institution = schema.TextLine(title=_('Institution'), required=False)
    rank = schema.TextLine(title=_('Rank'), required=False)
    dates = schema.TextLine(title=_('Dates'), required=False)


class IEmploymentRecord(Interface):
    rank = schema.TextLine(title=_('Rank'), required=False)
    dates = schema.TextLine(title=_('Dates'), required=False)


class IBooks(Interface):
    # status = schema.Choice(
    #     title=_('Status'),
    #     vocabulary=getStatusVocabulary,
    #     required=False
    # )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    place = schema.TextLine(title=_('Place'), required=False, default=u'')
    publisher = schema.TextLine(title=_('Publisher'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IArticles(Interface):
#     status = schema.Choice(
#         title=_('Status'),
#         vocabulary=getStatusVocabulary,
#         required=False
#     )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    journalTitle = schema.TextLine(title=_('Journal Title'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    volume = schema.TextLine(title=_('Volume'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IRefereedProceedings(Interface):
#     status = schema.Choice(
#         title=_('Status'),
#         vocabulary=getStatusVocabulary,
#         required=False
#     )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    journalTitle = schema.TextLine(title=_('Journal Title'), required=False, default=u'')
    volume = schema.TextLine(title=_('Volume'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class INonRefereedProceedings(Interface):
#     status = schema.Choice(
#         title=_('Status'),
#         vocabulary=getStatusVocabulary,
#         required=False
#     )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    journalTitle = schema.TextLine(title=_('Journal Title'), required=False, default=u'')
    volume = schema.TextLine(title=_('Volume'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IChapters(Interface):
#     status = schema.Choice(
#         title=_('Status'),
#         vocabulary=getStatusVocabulary,
#         required=False
#     )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    journalTitle = schema.TextLine(title=_('Journal Title'), required=False, default=u'')
    volume = schema.TextLine(title=_('Volume'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IMonographs(Interface):
#     status = schema.Choice(
#         title=_('Status'),
#         vocabulary=getStatusVocabulary,
#         required=False
#     )
    status = schema.TextLine(title=_('Status'), required=False)
    authors = schema.TextLine(title=_('Authors'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    journalTitle = schema.TextLine(title=_('Journal Title'), required=False, default=u'')
    volume = schema.TextLine(title=_('Volume'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    reference = schema.TextLine(title=_('Reference'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IReviews(Interface):
    # status = schema.Choice(
    #     title=_('Status'),
    #     vocabulary=getStatusVocabulary,
    #     required=True
    # )
    status = schema.TextLine(title=_('Status'), required=False)
    publication = schema.TextLine(title=_('Publication'), required=False, default=u'')
    # title = schema.TextLine(title=_('Book Title'), required=False, default=u'')
    # place = schema.TextLine(title=_('Place'), required=False, default=u'')
    # publisher = schema.TextLine(title=_('Publisher'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    pages = schema.TextLine(title=_('Pages'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IPresented(Interface):
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    date = schema.TextLine(title=_('Date'), required=False, default=u'')
    audience = schema.TextLine(title=_('Audience'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IPatents(Interface):
    patent = schema.TextLine(title=_('Patent Number'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')
    date = schema.TextLine(title=_('Year Issue'), required=False, default=u'')
    inventor = schema.TextLine(title=_('Inventor'), required=False, default=u'')
    filed = schema.TextLine(title=_('Filed Date'), required=False, default=u'')
    issue = schema.TextLine(title=_('Issued Date'), required=False, default=u'')
    country = schema.TextLine(title=_('Country Code'), required=False, default=u'')
    url = schema.TextLine(title=_('URL'), required=False, default=u'')


class IProfessional(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IGrants(Interface):
    agency = schema.TextLine(title=_('Funding Agency'), required=False, default=u'')
    title = schema.TextLine(title=_('Title of Project'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')
    amount = schema.TextLine(title=_('Amount Of Award'), required=False, default=u'')


class IServiceDepartment(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IServiceSchool(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IServiceCollege(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IServiceGraduateCenter(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IServiceUniversity(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IOfficeHeld(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IActivities(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    dates = schema.TextLine(title=_('Dates'), required=False, default=u'')


class IDeveloped(Interface):
    description = schema.TextLine(title=_('Description'), required=False, default=u'')
    title = schema.TextLine(title=_('Title'), required=False, default=u'')


class ICoursesTaught(Interface):
    dept = schema.TextLine(title=_('Department Code (WRIT)'), required=False, default=u'')
    number = schema.TextLine(title=_('Course Number (302)'), required=False, default=u'')
    description = schema.TextLine(title=_('Course Title'), required=False, default=u'')


class IFaculty(model.Schema):
    """ Marker interface and Dexterity Python Schema for Faculty
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

    directives.omitted('dept')
    dept = schema.TextLine(
        title=_('Department'),
        required=False,
    )

    directives.omitted('currentStatus')
    currentStatus = schema.TextLine(
        title=_('Status'),
        required=False,
    )

    directives.omitted('orgStatus')
    orgStatus = schema.TextLine(
        title=_('Chair / Dean'),
        required=False,
        default=u'',
    )

    directives.omitted('school')
    school = schema.TextLine(
        title=_('School / Division'),
        required=False,
    )

    directives.omitted('prog')
    prog = schema.TextLine(
        title=_('Program'),
        required=False,
        default=u'',
    )

    directives.widget(education=DataGridFieldFactory)
    education = schema.List(
        title=_("Education"),
        value_type=DictRow(title=_("Education"), schema=IEducationRow),
        required=False,
        description=_('List most recent first.'),
    )

    website = schema.TextLine(
        title=_('Personal Website'),
        required=False,
        default=u'',
    )

    image = NamedBlobImage(
        title=_('Portrait'),
        description=_('Please upload a 2 x 3 portrait photo in JPEG or PNG format. Ideal size 400px wide by 600px high.'),
        required=False,
    )

    directives.read_permission(userid='cmf.ModifyPortalContent')
    userid = schema.TextLine(
        title=_('User ID'),
        required=True,
    )
    # directives.read_permission(managers='cmf.ManagePortal')
    directives.omitted('managers')
    managers = schema.Tuple(
        title=_('Managers'),
        value_type=schema.TextLine(required=False, default=u''),
        required=False,
    )

    directives.read_permission(allowDiscussion='cmf.ManagePortal')
    directives.omitted('allowDiscussion')
    directives.widget(allowDiscussion=SingleCheckBoxFieldWidget)
    allowDiscussion = schema.Bool(
        title=_('Allow Discussion'),
        required=False,
    )

    directives.read_permission(location='cmf.ManagePortal')
    directives.omitted('location')
    location = schema.TextLine(
        title=_('Location'),
        required=False,
    )

    directives.read_permission(description='cmf.ManagePortal')
    directives.mode(description='hidden')
    description = schema.TextLine(
        title=_('Description'),
        required=False,
    )

    directives.read_permission(effectiveDate='cmf.ManagePortal')
    directives.omitted('effectiveDate')
    effectiveDate = schema.Datetime(
        title=_('Effective Date'),
        required=False,
    )

    directives.read_permission(expirationDate='cmf.ManagePortal')
    directives.omitted('expirationDate')
    expirationDate = schema.Datetime(
        title=_('Expiration Date'),
        required=False,
    )

    fieldset('Experience',
             fields=['areaExpertise', 'briefBio', 'experienceFT', 'experiencePT', 'experienceNA',
                     'employmentRecord'])

    areaExpertise = schema.Tuple(
        title=_('Areas of Expertise'),
        description=_('Enter one area of expertise per line.'),
        value_type=schema.TextLine(),
        required=False,
    )

    directives.widget(briefBio=WysiwygFieldWidget)
    briefBio = schema.Text(
        title=_('Brief Biography/Faculty Expert'),
        required=False,
        description=_(
            'Brief Biography containing CV information or more than 1000 characters '
            '(including html tags) will be REJECTED'),
    )

    directives.widget(experienceFT=DataGridFieldFactory)
    experienceFT = schema.List(
        title=_("Full-Time Academic Experience"),
        value_type=DictRow(title=_("Full-Time Academic Experience"), schema=IExperienceFT),
        required=False,
        description=_('List most recent first'),
    )

    directives.widget(experiencePT=DataGridFieldFactory)
    experiencePT = schema.List(
        title=_("Part-Time Academic Experience"),
        value_type=DictRow(title=_("Part-Time Academic Experience"), schema=IExperiencePT),
        required=False,
        description=_('List most recent first'),
    )

    directives.widget(experienceNA=DataGridFieldFactory)
    experienceNA = schema.List(
        title=_("Non Academic Experience"),
        value_type=DictRow(title=_("Non Academic Experience"), schema=IExperienceNA),
        required=False,
        description=_('List most recent first'),
    )

    directives.widget(employmentRecord=DataGridFieldFactory)
    employmentRecord = schema.List(
        title=_("Employment Record At this Institution"),
        value_type=DictRow(title=_("Employment Record At this Institution"), schema=IEmploymentRecord),
        required=False,
        description=_('List most recent first'),
    )

    fieldset('Publications',
             fields=['books', 'articles', 'refereedProceedings', 'nonRefereedProceedings', 'chapters',
                     'monographs',
                     'reviews', 'presented', 'patents', 'pubEnhance'])
    directives.widget(books=DataGridFieldFactory)
    books = schema.List(
        title=_("Books"),
        value_type=DictRow(title=_("Books"), schema=IBooks),
        required=False,
        description=_('List more recent first. For items accepted but not yet published, '
                      'indicate ""in press"" and number of typewritten pages, single or double-spaced. '
                      'If publication is co-authored, all authors must be listed as they appear in the publication '
                      '(i.e. same order). If sole authored, name of author must be given.'
                      ),
    )

    directives.widget(articles=DataGridFieldFactory)
    articles = schema.List(
        title=_('Articles'),
        value_type=DictRow(title=_('Articles'), schema=IArticles),
        default=[],
        required=False,
        description=_(
            "If an article has not yet been published, "
            "indicate the date of the letter of acceptance,"
            " the name of the journal, "
            "and the number of typed pages, "
            "single or double-spaced. "
            "If the article has been submitted but not accepted, "
            "it must be listed under "
            "Works in Progress"
            " with the date of submission,"
            " the name of the journal, and the number of typed pages, single or double-spaced."
        ),
    )

    directives.widget(refereedProceedings=DataGridFieldFactory)
    refereedProceedings = schema.List(
        title=_("Refereed Proceedings"),
        value_type=DictRow(title=_("Refereed Proceedings"), schema=IRefereedProceedings),
        default=[],
        required=False,
        description=_(
            'If an article has not yet been published, '
            'indicate the date of the letter of acceptance, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced. '
            'If the article has been submitted but not accepted, '
            'it must be listed under ""Works in Progress"" with the date of submission, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced.'),
    )

    directives.widget(nonRefereedProceedings=DataGridFieldFactory)
    nonRefereedProceedings = schema.List(
        title=_("Non-Refereed Proceedings"),
        value_type=DictRow(title=_("Non-Refereed Proceedings"), schema=INonRefereedProceedings),
        default=[],
        required=False,
        description=_(
            'If an article has not yet been published, '
            'indicate the date of the letter of acceptance, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced. '
            'If the article has been submitted but not accepted, '
            'it must be listed under ""Works in Progress"" with the date of submission, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced.'),
    )

    directives.widget(chapters=DataGridFieldFactory)
    chapters = schema.List(
        title=_("Chapters in Books"),
        value_type=DictRow(title=_("Chapters in Books"), schema=IChapters),
        default=[],
        required=False,
        description=_(
            'If an article has not yet been published, '
            'indicate the date of the letter of acceptance, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced. '
            'If the article has been submitted but not accepted, '
            'it must be listed under ""Works in Progress"" with the date of submission, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced.'),
    )

    directives.widget(monographs=DataGridFieldFactory)
    monographs = schema.List(
        title=_("Government Reports or Monographs"),
        value_type=DictRow(title=_("Government Reports or Monographs"), schema=IMonographs),
        default=[],
        required=False,
        description=_(
            'If an article has not yet been published, '
            'indicate the date of the letter of acceptance, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced. '
            'If the article has been submitted but not accepted, '
            'it must be listed under ""Works in Progress"" with the date of submission, '
            'the name of the journal, '
            'and the number of typed pages, '
            'single or double-spaced.'),
    )

    directives.widget(reviews=DataGridFieldFactory)
    reviews = schema.List(
        title=_("Book Reviews"),
        value_type=DictRow(title=_("Book Reviews"), schema=IReviews),
        required=False,
        description=
        _('Give publications in which review appeared, date, and page numbers.'
          ),
    )

    directives.widget(presented=DataGridFieldFactory)
    presented = schema.List(
        title=_(
            "Presented Papers, Lectures, and Exhibitions and Performances"),
        value_type=DictRow(title=_("Presented Papers, Lectures, and Exhibitions and Performances"), schema=IPresented),
        required=False,
        description=_(
            'Give title, date and audience to whom these were presented.'),
    )

    directives.widget(patents=DataGridFieldFactory)
    patents = schema.List(
        title=_("Patents"),
        value_type=DictRow(title=_("Patents"), schema=IPatents),
        required=False,
        description=_('Patents Number, title, date and url'),
    )

    directives.widget(pubEnhance=WysiwygFieldWidget)
    pubEnhance = schema.Text(
        title=_('Publications Enhancements'),
        description=_('Comments on Publications'),
        required=False,
    )

    fieldset('Other Information',
             fields=['professional', 'grants', 'serviceDepartment', 'serviceSchool', 'serviceCollege',
                     'serviceGraduateCenter', 'serviceUniversity', 'officeHeld', 'activities', 'coursesTaught',
                     'developed', 'hidecv', 'scholarEnhance', 'teachEnhance']
             )
    directives.widget(professional=DataGridFieldFactory)
    professional = schema.List(
        title=_("Professional Honors, Prizes, Fellowships"),
        value_type=DictRow(title=_("Professional Honors, Prizes, Fellowships"), schema=IProfessional),
        default=[],
        required=False,
    )

    directives.widget(grants=DataGridFieldFactory)
    grants = schema.List(
        title=_("Grants-In-Aid"),
        value_type=DictRow(title=_("Grants-In-Aid"), schema=IGrants),
        required=False,
        description=
        _('List Full Title Of Funding Agency, Title Of Project, Project Dates, And Amount Of Award.'
          ),
    )

    directives.widget(serviceDepartment=DataGridFieldFactory)
    serviceDepartment = schema.List(
        title=_("Service To The Department"),
        value_type=DictRow(title=_("Service To The Department"), schema=IServiceDepartment),
        required=False,
    )

    directives.widget(serviceSchool=DataGridFieldFactory)
    serviceSchool = schema.List(
        title=_("Service To The School"),
        value_type=DictRow(title=_("Service To The School"), schema=IServiceSchool),
        required=False,
    )

    directives.widget(serviceCollege=DataGridFieldFactory)
    serviceCollege = schema.List(
        title=_("Service To The College"),
        value_type=DictRow(title=_("Service To The College"), schema=IServiceCollege),
        required=False,
    )

    directives.widget(serviceGraduateCenter=DataGridFieldFactory)
    serviceGraduateCenter = schema.List(
        title=_("Service To The Graduate Center"),
        value_type=DictRow(title=_("Service To The Graduate Center"), schema=IServiceGraduateCenter),
        required=False,
    )

    directives.widget(serviceUniversity=DataGridFieldFactory)
    serviceUniversity = schema.List(
        title=_("Service To The University"),
        value_type=DictRow(title=_("Service To The University"), schema=IServiceUniversity),
        required=False,
    )

    directives.widget(officeHeld=DataGridFieldFactory)
    officeHeld = schema.List(
        title=_("Offices Held In Professional Societies"),
        value_type=DictRow(title=_("Offices Held In Professional Societies"), schema=IOfficeHeld),
        required=False,
    )

    directives.widget(activities=DataGridFieldFactory)
    activities = schema.List(
        title=_("Other Professional Activities And Public Service"),
        value_type=DictRow(title=_("Other Professional Activities And Public Service"), schema=IActivities),
        required=False,
    )

    directives.widget(coursesTaught=DataGridFieldFactory)
    coursesTaught = schema.List(
        title=_("Courses Taught"),
        value_type=DictRow(title=_("Courses Taught"), schema=ICoursesTaught),
        required=False,
    )

    directives.widget(developed=DataGridFieldFactory)
    developed = schema.List(
        title=_("New Courses/Programs Developed"),
        value_type=DictRow(title=_("New Courses/Programs Developed"), schema=IDeveloped),
        required=False,
    )

    directives.widget(hidecv=SingleCheckBoxFieldWidget)
    hidecv = schema.Bool(
        title=_('Hide CV from View'),
        description=_("Check this box if you want to hide the Curriculum Vitae view to all users"),
        required=False,
    )

    directives.widget(scholarEnhance=WysiwygFieldWidget)
    scholarEnhance = schema.Text(
        title=_('Scholarship Enhancements'),
        description=_('Comments on Scholarship'),
        required=False,
    )

    directives.widget(teachEnhance=WysiwygFieldWidget)
    teachEnhance = schema.Text(
        title=_('Teaching Enhancements'),
        description=_('Comments on teaching'),
        required=False,
    )

    # directives.read_permission(subject='cmf.ModifyPortalContent')
    # directives.omitted('subject')
    # subject = schema.Tuple(
    #     title=_('Tags'),
    #     value_type=schema.TextLine(),
    #     required=False,
    # )
    #
    # directives.omitted('ssn')
    # directives.read_permission(ssn='cmf.ManagePortal')
    # ssn = schema.TextLine(
    #     title=_('SSN'),
    #     required=False,
    # )
    #
    # directives.omitted('citizen')
    # directives.read_permission(citizen='cmf.ManagePortal')
    # citizen = schema.Bool(
    #     title=_('Citizen'),
    #     required=False,
    # )
    #
    # directives.omitted('tenure')
    # directives.read_permission(tenure='cmf.ManagePortal')
    # tenure = schema.Bool(
    #     title=_('Tenure'),
    #     required=False,
    # )
    #
    # directives.omitted('Senior')
    # directives.read_permission(Senior='cmf.ManagePortal')
    # Senior = schema.Bool(
    #     title=_('Senior'),
    #     required=False,
    # )
    #
    # directives.omitted('street')
    # directives.read_permission(street='cmf.ManagePortal')
    # street = schema.TextLine(
    #     title=_('Street'),
    #     required=False,
    # )
    #
    # directives.omitted('apt')
    # directives.read_permission(apt='cmf.ManagePortal')
    # apt = schema.TextLine(
    #     title=_('Apt'),
    #     required=False,
    # )
    #
    # directives.omitted('city')
    # directives.read_permission(city='cmf.ManagePortal')
    # city = schema.TextLine(
    #     title=_('City'),
    #     required=False,
    # )
    #
    # directives.omitted('state')
    # directives.read_permission(state='cmf.ManagePortal')
    # state = schema.TextLine(
    #     title=_('State'),
    #     required=False,
    # )
    #
    # directives.omitted('zipCode')
    # directives.read_permission(zipCode='cmf.ManagePortal')
    # zipCode = schema.TextLine(
    #     title=_('Zipcode'),
    #     required=False,
    # )
    #
    # directives.omitted('homePhone')
    # directives.read_permission(homePhone='cmf.ManagePortal')
    # homePhone = schema.TextLine(
    #     title=_('Home Phone'),
    #     required=False,
    # )
    #
    # directives.omitted('url')
    # url = schema.TextLine(
    #     title=_('URL of Item'),
    #     required=False,
    # )
    #
    # directives.omitted('language')
    # directives.read_permission(language='cmf.ManagePortal')
    # language = schema.TextLine(
    #     title=_('Language'),
    #     required=False,
    # )
    #
    # directives.omitted('contributors')
    # directives.read_permission(contributors='cmf.ManagePortal')
    # contributors = schema.Tuple(
    #     title=_('Contributors'),
    #     value_type=schema.TextLine(),
    #     required=False,
    # )
    #
    # directives.omitted('creators')
    # directives.read_permission(creators='cmf.ManagePortal')
    # creators = schema.Tuple(
    #     title=_('Creators'),
    #     value_type=schema.TextLine(),
    #     required=False,
    # )
    #
    # directives.omitted('rights')
    # # directives.read_permission(rights='cmf.ManagePortal')
    # rights = schema.Tuple(
    #     title=_('Rights'),
    #     value_type=schema.TextLine(),
    #     required=False,
    # )


    directives.mode(preview='hidden')
    directives.read_permission(preview='cmf.ReviewPortalContent')
    preview = schema.TextLine(
        title=_('Preview'),
        required=False,
        default=u'True',
    )

    directives.mode(can_modify_portal_content='hidden')
    directives.read_permission(can_modify_portal_content='cmf.ModifyPortalContent')
    can_modify_portal_content = schema.TextLine(
        title=_('Can Modify Portal Content'),
        required=False,
        default=u'True',
    )


@implementer(IFaculty)
class Faculty(Container):
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
    #     self.title = api.user.get(userid=self.userid)

    # def setCurrentStatus(self):
    #     self.currentStatus = self.computeCurrentStatus()
    #
    # def computeCurrentStatus(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = user.getProperty('currentStatus') or ' '
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

    # def computeFullname(self):
    #     user = api.user.get(username=str(self.userid))
    #     first_name = user.getProperty('first_name') or ' '
    #     last_name = user.getProperty('last_name') or ' '
    #     space = ', '
    #     return str(last_name) + space + str(first_name)
    @property
    def description(self):
        user = api.user.get(username=str(self.userid))
        # first_name = user.getProperty('first_name') or ' '
        # last_name = user.getProperty('last_name') or ' '
        dept = user.getProperty('department') or ' '
        teachingTitle = user.getProperty('functionalTitle') or ' '
        officePhone = user.getProperty('phone') or ' '
        email = user.getProperty('email') or ' '
        space = ' '
        of = ' - '
        AND = ' and '
        orgStatus = user.getProperty('orgStatus') or ' '
        if orgStatus == 'Chair':
            return str(teachingTitle) + AND + str(orgStatus) + of + str(dept) + of + str(officePhone) + of + str(email)
        elif orgStatus == 'Acting Chair':
            return str(teachingTitle) + AND + str(orgStatus) + of + str(dept) + of + str(officePhone) + of + str(email)
        return str(teachingTitle) + of + str(dept) + of + str(officePhone) + of + str(email)

    @description.setter
    def description(self, value):
        pass

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

    def newOperation(self):
        """
        """
        pass

    # def setFirst_name(self):
    #     self.first_name = self.computeFirst_name()
    #
    # def computeFirst_name(self):
    #     user = api.user.get(username=str(self.userid))
    #     member = self.acl_users.getUserById(user)
    #     member_info = user.getProperty('first_name') or ' '
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
    #     member_info = user.getProperty('last_name') or ' '
    #     return str(member_info)
    #
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
    #     member_info = user.getProperty('functionalTitle') or ' '
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
    #     member_info = user.getProperty('personalTitle') or ' '
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
    #     member_info = user.getProperty('email') or ' '
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
    #     member_info = user.getProperty('phone') or ' '
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
    #     member_info = user.getProperty('location') or ' '
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
    #     member_info = user.getProperty('department') or ' '
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
    #     member_info = user.getProperty('employeeType') or ' '
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
    #     member_info = user.getProperty('division') or ' '
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
    #     member_info = user.getProperty('orgStatus') or ' '
    #     return str(member_info)

    @property
    def orgStatus(self):
        user = api.user.get(username=str(self.userid))
        member_info = user.getProperty('orgStatus') or ' '
        return str(member_info)

    @orgStatus.setter
    def orgStatus(self, value):
        pass

    def setManagers(self, managers):
        """
        """
        field = self.getField('managers')
        currentManagers = field.get(self)
        field.set(self, currentManagers)
        self.manage_setLocalRoles(self.userid, ['Owner', 'Reader'])

    @property
    def username(self):
        return self.userid

    @username.setter
    def username(self, value):
        pass
