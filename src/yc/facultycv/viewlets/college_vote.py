# encoding=utf-8
from Products.Five.browser import BrowserView
from yc.facultycv.interfaces import ICollegeVote
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent


class Vote(BrowserView):

    def __call__(self, rating):
        voting = ICollegeVote(self.context)
        voting.vote(rating, self.request)
        notify(ObjectModifiedEvent(self.context, "A vote has been submitted"))
        return "success"


class ClearVotes(BrowserView):

    def __call__(self):
        voting = ICollegeVote(self.context)
        voting.clear()
        notify(ObjectModifiedEvent(self.context,
                                   "All votes of this item have been removed"))
        return "success"
