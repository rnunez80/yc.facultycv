# -*- coding: utf-8 -*-
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from plone.restapi.deserializer import json_body
from plone.restapi.services import Service
from yc.facultycv import CanClearVotes
from yc.facultycv import DoCollegeVote
from yc.facultycv import ViewCollegeVote
from yc.facultycv.interfaces import ICollegeVote
from zExceptions import Unauthorized
from zope.globalrequest import getRequest
from zope.interface import alsoProvides


class Vote(Service):
    """Vote for an object"""

    def reply(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        can_vote = api.user.has_permission(DoCollegeVote, obj=self.context)
        if not can_vote:
            raise Unauthorized("User not authorized to vote.")
        voting = ICollegeVote(self.context)
        data = json_body(self.request)
        vote = data['rating']
        voting.vote(vote, self.request)

        return vote_info(self.context, self.request)


class Delete(Service):
    """Unlock an object"""

    def reply(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        can_clear_votes = api.user.has_permission(CanClearVotes, obj=self.context)
        if not can_clear_votes:
            raise Unauthorized("User not authorized to clear votes.")
        voting = ICollegeVote(self.context)
        voting.clear()
        return vote_info(self.context, self.request)


class Votes(Service):
    """Voting information about the current object"""

    def reply(self):
        can_view_votes = api.user.has_permission(ViewCollegeVote, obj=self.context)
        if not can_view_votes:
            raise Unauthorized("User not authorized to view votes.")
        return vote_info(self.context, self.request)


def vote_info(obj, request=None):
    """Returns voting information about the given object."""
    if not request:
        request = getRequest()
    voting = ICollegeVote(obj)
    can_vote = api.user.has_permission(DoCollegeVote, obj=obj)
    can_clear_votes = api.user.has_permission(CanClearVotes, obj=obj)
    info = {
        'average_vote': voting.average_vote(),
        'total_votes': voting.total_votes(),
        'has_votes': voting.has_votes(),
        'already_voted': voting.already_voted(request),
        'can_vote': can_vote,
        'can_clear_votes': can_clear_votes,
        'up_votes': voting.up_votes(),
        'neutral_votes': voting.neutral_votes(),
        'down_votes': voting.down_votes(),
        'has_voted': voting.who_voted()
    }
    return info
