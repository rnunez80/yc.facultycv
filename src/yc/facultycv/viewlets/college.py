# encoding=utf-8
from plone.app.layout.viewlets import ViewletBase
from plone.protect.authenticator import createToken
from Products.CMFCore.permissions import ViewManagementScreens
from Products.CMFCore.utils import getToolByName
from yc.facultycv import CanClearVotes
from yc.facultycv import DoCollegeVote
from yc.facultycv import ViewCollegeVote
from yc.facultycv.interfaces import ICollegeVote
from zope.security import checkPermission


class Vote(ViewletBase):
    vote = None
    is_manager = None
    can_clear_votes = None
    can_view_votes = None
    can_vote = None

    def update(self):
        super(Vote, self).update()
        if self.vote is None:
            self.vote = ICollegeVote(self.context)
        if self.is_manager is None:
            membership_tool = getToolByName(self.context, 'portal_membership')
            self.is_manager = membership_tool.checkPermission(
                ViewManagementScreens,
                self.context
            )

            self.can_view_votes = membership_tool.checkPermission(
                ViewCollegeVote, self.context
            )
            self.can_vote = membership_tool.checkPermission(
                DoCollegeVote,
                self.context
            )
            self.can_clear_votes = membership_tool.checkPermission(
                CanClearVotes, self.context
            )

    def voted(self):
        return self.vote.already_voted(self.request)

    def average(self):
        return self.vote.average_vote()

    def has_votes(self):
        return self.vote.has_votes()

    def has_voted(self):
        return self.vote.has_voted()

    def up_votes(self):
        return self.vote.up_votes()

    def neutral_votes(self):
        return self.vote.neutral_votes()

    def down_votes(self):
        return self.vote.down_votes()

    def token(self):
        return createToken()

    def visible(self):
        return checkPermission('yc.facultycv.show_view', self.context)
