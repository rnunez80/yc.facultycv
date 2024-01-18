# -*- coding: utf-8 -*-

# from plone import api
from plone.dexterity.interfaces import IDexterityContent
from yc.facultycv import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class AvailableDepartments(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'accounting_finance', _(u'Accounting and Finance')),
            VocabItem(u'behavioral_sciences', _(u'Behavioral Sciences')),
            VocabItem(u'biology', _(u'Biology')),
            VocabItem(u'business_economics', _(u'Business and Economics')),
            VocabItem(u'chemistry', _(u'Chemistry')),
            VocabItem(u'earth_physical_sciences', _(u'Earth and Physical Sciences')),
            VocabItem(u'english', _(u'English')),
            VocabItem(u'health_professions', _(u'Health Professions')),
            VocabItem(u'health_human_performance', _(u'Health and Human Performance')),
            VocabItem(u'history_philosophy_anthropology', _(u'History, Philosophy, and Anthropology')),
            VocabItem(u'library', _(u'Library')),
            VocabItem(u'mathematics_computer_science', _(u'Mathematics and Computer Science')),
            VocabItem(u'nursing', _(u'Nursing')),
            VocabItem(u'occupational_therapy', _(u'Occupational Therapy')),
            VocabItem(u'performing_fine_arts', _(u'Performing and Fine Arts')),
            VocabItem(u'social_work', _(u'Social Work')),
            VocabItem(u'teacher_education', _(u'Teacher Education')),
            VocabItem(u'world_languages_literatures_humanities', _(u'World Languages, Literatures, and Humanities')),
            VocabItem(u'special', _(u'Special Circumstances (See Academic Affairs)')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token.encode('utf-8', 'ignore'),
                    token=str(item.token),
                    title=item.value.encode('utf-8', 'ignore'),
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


AvailableDepartmentsFactory = AvailableDepartments()
