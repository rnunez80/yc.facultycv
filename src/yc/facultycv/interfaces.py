# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

# from plone import api
# from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
# from plone.supermodel import directives
from plone.supermodel import model
# from zope.interface import alsoProvides
# from zope import schema
from zope.interface import Interface
from zope.interface import provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IYcFacultycvLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollegeVoteLayer(Interface):
    """Marker interface for the Browserlayer
    """


class IDepartmentVoteLayer(Interface):
    """Marker interface for the Browserlayer
    """


class ICollegeVoteMarker(Interface):
    pass


class IDepartmentVoteMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ICollegeVote(model.Schema):
    """
    """

    def vote(request):
        """
        Store the vote information, store the request hash to ensure
        that the user does not vote twice
        """

    def average_vote():
        """
        Return the average voting for an item
        """

    def has_votes():
        """
        Return whether anybody ever voted for this item
        """

    def already_voted(request):
        """
        Return the information wether a person already voted.
        This is not very high level and can be tricked out easily
        """

    def clear():
        """
        Clear the votes. Should only be called by admins
        """

    def has_voted():
        """
        Returns people who have voted for this item
        """

    def up_votes():
        """
        Returns people who have voted up for this item
        """

    def neutral_votes():
        """
        Returns people who have voted neutral for this item
        """

    def down_votes():
        """
        Returns people who have voted down for this item
        """


@provider(IFormFieldProvider)
class IDepartmentVote(model.Schema):
    """
    """

    def vote(request):
        """
        Store the vote information, store the request hash to ensure
        that the user does not vote twice
        """

    def average_vote():
        """
        Return the average voting for an item
        """

    def has_votes():
        """
        Return whether anybody ever voted for this item
        """

    def already_voted(request):
        """
        Return the information wether a person already voted.
        This is not very high level and can be tricked out easily
        """

    def clear():
        """
        Clear the votes. Should only be called by admins
        """

    def has_voted():
        """
        Returns people who have voted for this item
        """

    def up_votes():
        """
        Returns people who have voted up for this item
        """

    def neutral_votes():
        """
        Returns people who have voted neutral for this item
        """

    def down_votes():
        """
        Returns people who have voted down for this item
        """
