# -*- coding: utf-8 -*-
# from Products.CMFPlone.utils import safe_hasattr
from persistent.dict import PersistentDict
from persistent.list import PersistentList
from plone import api
# from plone import schema
# from plone.autoform.interfaces import IFormFieldProvider
# from plone.supermodel import model
# from yc.facultycv import _
from yc.facultycv.interfaces import IDepartmentVote
from yc.facultycv.interfaces import IDepartmentVoteMarker
# from zope import schema
from zope.annotation.interfaces import IAnnotations
from zope.component import adapter
# from zope.interface import Interface
# from zope.interface import alsoProvides
from zope.interface import implementer


# from zope.interface import provider

KEY = 'yc.facultycv.behaviors.department_vote.DepartmentVote'


@implementer(IDepartmentVote)
@adapter(IDepartmentVoteMarker)
class DepartmentVote(object):
    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        if KEY not in annotations.keys():
            annotations[KEY] = PersistentDict({
                "voted": PersistentList(),
                'votes': PersistentDict(),
            })
        self.annotations = annotations[KEY]

    @property
    def votes(self):
        return self.annotations['votes']

    @property
    def voted(self):
        return self.annotations['voted']

    def up_votes(self):
        try:
            votes = self.annotations.get('votes', {})
            return votes[1]
        except:
            return 0

    def neutral_votes(self):
        try:
            votes = self.annotations.get('votes', {})
            return votes[0]
        except:
            return 0

    def down_votes(self):
        try:
            votes = self.annotations.get('votes', {})
            return votes[-1]
        except:
            return 0

    def user(self, request=None):
        currentUser = api.user.get_current()
        first_name = currentUser.getProperty('first_name') or ' '
        last_name = currentUser.getProperty('last_name') or ' '
        space = ' '
        return "%s%s%s" % (first_name, space, last_name)

    def vote(self, vote, request):
        vote = int(vote)
        if self.already_voted(request):
            raise KeyError("You may not vote twice")
        self.annotations['voted'].append(self.user(request))
        votes = self.annotations.get('votes', {})
        if vote not in votes:
            votes[vote] = 1
        else:
            votes[vote] += 1

    def total_votes(self):
        return sum(self.annotations.get('votes', {}).values())

    def average_vote(self):
        total_votes = sum(self.annotations.get('votes', {}).values())
        if total_votes == 0:
            return 0
        total_points = sum([vote * count for (vote, count) in
                            self.annotations.get('votes', {}).items()])
        return float(total_points) / total_votes

    def has_votes(self):
        return len(self.annotations.get('votes', {})) != 0

    def already_voted(self, request):
        return self.user(request) in self.annotations['voted']

    def has_voted(self):
        return self.annotations['voted']

    def clear(self):
        annotations = IAnnotations(self.context)
        annotations[KEY] = PersistentDict({'voted': PersistentList(),
                                           'votes': PersistentDict(),
                                           })
        self.annotations = annotations[KEY]

    def who_voted(self):
        data = list(self.has_voted())
        for entry in data:
            return entry
