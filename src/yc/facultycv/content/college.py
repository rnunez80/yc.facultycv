# -*- coding: utf-8 -*-
# from plone.app.z3cform.widget import SelectFieldWidget
# from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from yc.facultycv import _
from zope import schema
from zope.interface import implementer


class ICollege(model.Schema):
    """ Marker interface and Dexterity Python Schema for College
    """
    # directives.widget(schoolsVocab=SelectFieldWidget)
    # schoolsVocab = schema.Choice(
    #     title=_('Schools Vocabulary'),
    #     required=False,
    #     values=('Arts and Sciences', 'Business and Information Systems', 'Health and Behavioral Sciences', ' '),
    # )

    # directives.widget(departmentVocab=SelectFieldWidget)
    # departmentVocab = schema.Choice(
    #     title=_('Department Vocabulary'),
    #     required=False,
    #     values=("", "accounting-finance",
    #             "behavioral-sciences", "biology",
    #             "business-economics", "chemistry",
    #             "earth-physical-sciences", "english",
    #             "foreign-languages",
    #             "health-physical-education",
    #             "health-professions",
    #             "history-philosophy", "library", "math",
    #             "nursing", "occupational-therapy",
    #             "performing-fine-arts", "social-sciences",
    #             "student-development", "teacher-education",
    #             "school-of-arts-and-sciences",
    #             "school-of-business-and-information-systems",
    #             "school-of-health-and-behavioral-sciences"),
    # )

    # directives.widget(programVocab=SelectFieldWidget)
    # programVocab = schema.Choice(
    #     title=_('Program Vocabulary'),
    #     required=False,
    #     values=("English", "Math"),
    # )

    # directives.widget(degreeVocab=SelectFieldWidget)
    # degreeVocab = schema.Choice(
    #     title=_('Degree Vocabulary'),
    #     required=False,
    #     values=('', 'AA', 'AAS', 'AB', 'BA', 'BBA',
    #             'BE', 'BEng', 'BFA', 'BS',
    #             'certificate', 'DBA', 'DC', 'DNS',
    #             'DPhil', 'DSW', 'DrPH', 'DrPH (c)',
    #             'EDD', 'JD', 'LLB', 'LLM', 'M Ed',
    #             'MA', 'MBA', 'MD', 'MFA', 'MIA',
    #             'MLIS', 'MLS', 'MM', 'MPA', 'MPhil',
    #             'MS', 'MSc', 'MSN', 'MSW', 'MVP',
    #             'SB', 'non-degree', 'PhD', 'PhDc',
    #             'BM'),
    # )

    # directives.widget(teachingTitleVocab=SelectFieldWidget)
    # teachingTitleVocab = schema.Choice(
    #     title=_('Teaching Title Vocabulary'),
    #     required=False,
    #     values=('', 'Professor', 'Associate Professor', 'Assistant Professor', 'Lecturer', 'Instructor',
    #             'Distinguish Lecturers', 'Visiting Professor', 'Visiting',
    #             'Visiting Associate Professor', 'Substitute Professor', 'Substitute Assistant Professor',
    #             'Substitute Associate Professor', 'Substitute Lecturer', 'Substitute Instructor',
    #             'Professor Emeritus',
    #             'Chair', 'Associate Dean', 'Dean', 'Provost/Senior VP', 'Assistant Provost', 'Adjunct',
    #             'Adjunct Professor', 'Adjunct Associate Professor', 'Adjunct Assistant Professor',
    #             'Adjunct Lecturer',
    #             'Doctoral Lecturer'),
    # )

    title = schema.TextLine(
        title=_('Title'),
        required=False,
        default=u'Directory',
    )


@implementer(ICollege)
class College(Container):
    """
    """

    @property
    def id(self):
        return 'directory'

    @id.setter
    def id(self, value):
        pass

