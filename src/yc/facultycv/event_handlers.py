from logging import getLogger
from plone import api
from plone.api.content import get_state
from plone.api.content import transition
from Products.CMFCore.utils import getToolByName
from yc.facultycv.interfaces import ICollegeVote
from yc.facultycv.interfaces import IDepartmentVote
import transaction

log = getLogger('yc.facultycv')


def pbActionModified(obj, event):
    wftool = getToolByName(obj, 'portal_workflow')
    current_state = wftool.getInfoFor(obj, 'review_state', None)
    try:
        if current_state == 'deptVotingClosed':
            yes_votes = 0
            yes_votes_tmp = obj.deptVotesYes
            if yes_votes_tmp is not None:
                yes_votes = int(yes_votes_tmp)
            no_votes = 0
            no_votes_tmp = obj.deptVotesNo
            if no_votes_tmp is not None:
                no_votes = int(no_votes_tmp)
            abstain_votes = 0
            abstain_votes_tmp = obj.deptVotesAbstain
            if abstain_votes_tmp is not None:
                abstain_votes = int(abstain_votes_tmp)
            no_vote = abstain_votes + no_votes
            # eligible_votes = (0.5 * int(obj.eligibleDeptVoters)) + 1
            # if yes_votes > no_vote:
            if yes_votes > 3:
                wftool.doActionFor(obj, 'sendToCollege')
            elif no_vote > yes_votes:
                wftool.doActionFor(obj, 'unsatisfactoryByDept')

        elif current_state in 'collegeVotingClosed':
            yes_votes = 0
            yes_votes_tmp = obj.collegeVotesYes
            if yes_votes_tmp is not None:
                yes_votes = int(yes_votes_tmp)
            no_votes = 0
            no_votes_tmp = obj.collegeVotesNo
            if no_votes_tmp is not None:
                no_votes = int(no_votes_tmp)
            # eligible_votes = (0.5 * int(obj.eligibleCollegeVoters)) + 1
            # if yes_votes > no_votes:
            if yes_votes > 12:
                wftool.doActionFor(obj, 'satisfactory')
            elif no_votes > yes_votes:
                wftool.doActionFor(obj, 'unsatisfactory')
    except Exception:
        log.exception('Failed to transition %s' % '/'.join(obj.getPhysicalPath()))


def department_update(obj, event):
    votable = IDepartmentVote(obj)
    up_votes = votable.up_votes()
    down_votes = votable.down_votes() + votable.neutral_votes()
    if get_state(obj) == 'deptReviewing':
        if (votable.average_vote() > 0.5) and (up_votes > down_votes):
            transition(obj, transition='sendToCollege')
        elif (votable.average_vote() < 0.5) and (up_votes < down_votes):
            transition(obj, transition='unsatisfactoryByDept')


def college_update(obj, event):
    votable = ICollegeVote(obj)
    up_votes = votable.up_votes()
    down_votes = votable.down_votes() + votable.neutral_votes()
    if get_state(obj) == ('collegeReviewing', 'collegeReviewingAppeal'):
        if (votable.average_vote() > 0.5) and (up_votes > down_votes):
            transition(obj, transition='satisfactory')
        elif (votable.average_vote() < 0.5) and (up_votes < down_votes):
            transition(obj, transition='unsatisfactory')


def set_faculty_managers_added(obj, event):
    managers = str(api.user.get(username=str(obj.userid)))
    try:
        api.user.grant_roles(username=managers, roles=['Owner'],
                             obj=obj)
    except:
        pass


def set_faculty_managers_modified(obj, event):
    managers = str(api.user.get(username=str(obj.userid)))
    try:
        api.user.grant_roles(username=managers, roles=['Owner'],
                             obj=obj)
    except:
        pass


def set_pb_dept(obj):
    try:
        pbdept = obj.managers
        return pbdept
    except:
        pass


def set_description(obj):
    try:
        description = obj.aq_parent.first_name + ' ' + obj.aq_parent.last_name + ' - ' + obj.aq_parent.teachingTitle + ' - ' + obj.aq_parent.dept + ' - ' + obj.title
        obj.description = description
        print(obj.description)
        return obj.description
    except:
        pass


def set_managers_added(obj, event):
    # try:
    #     # description = obj.aq_parent.title + ' - ' + obj.aq_parent.description
    #     description = obj.aq_parent.first_name + ' ' + obj.aq_parent.last_name + ' - ' + obj.aq_parent.teachingTitle + ' - ' + obj.aq_parent.dept + ' - ' + obj.title
    #     obj.description = description
    #     print(obj.description)
    #     return obj.description
    # except:
    #     pass
    set_description(obj)
    pbdept = set_pb_dept(obj)
    try:
        current_user = str(api.user.get(username=str(obj.userid)))
        chair = 'pb_' + pbdept + '_chair'
        committee = 'pb_' + pbdept + '_committee'
        college_chair = 'pb_college_chair'
        college_committee = 'pb_college_committee'
        api.user.grant_roles(username=current_user, roles=['Owner'], obj=obj)
        if not api.group.get(groupname=chair):
            api.group.create(groupname=chair, title=chair)
            print('Group added: ' + chair + ' successfully')
        if not api.group.get(groupname=committee):
            api.group.create(groupname=committee, title=committee)
            print('Group added: ' + committee + ' successfully')
        if not api.group.get(groupname=college_chair):
            api.group.create(groupname=college_chair, title=college_chair)
            print('Group added: ' + college_chair + ' successfully')
        if not api.group.get(groupname=college_committee):
            api.group.create(groupname=college_committee, title=college_committee)
            print('Group added: ' + college_committee + ' successfully')
    except:
        pass

    try:
        chair = 'pb_' + pbdept + '_chair'
        committee = 'pb_' + pbdept + '_committee'
        college_chair = 'pb_college_chair'
        college_committee = 'pb_college_committee'
        api.group.grant_roles(groupname=chair,
                              roles=['Dept Head', 'PBdeptChair', 'Reader'],
                              obj=obj)
        api.group.grant_roles(groupname=committee, roles=['PBdept', 'Reader'], obj=obj)
        api.group.grant_roles(groupname=college_chair, roles=['PBhead', 'Reader'], obj=obj)
        api.group.grant_roles(groupname=college_committee, roles=['PBcollege', 'Reader'], obj=obj)
    except:
        pass


def set_managers_modified(obj, event):
    # try:
    #     # description = obj.aq_parent.title + ' - ' + obj.aq_parent.description
    #     description = obj.aq_parent.first_name + ' ' + obj.aq_parent.last_name + ' - ' + obj.aq_parent.teachingTitle + ' - ' + obj.aq_parent.dept + ' - ' + obj.title
    #     obj.description = description
    #     print(obj.description)
    #     return obj.description
    # except:
    #     pass
    set_description(obj)
    pbdept = set_pb_dept(obj)
    try:
        current_user = str(api.user.get(username=str(obj.userid)))
        chair = 'pb_' + pbdept + '_chair'
        committee = 'pb_' + pbdept + '_committee'
        college_chair = 'pb_college_chair'
        college_committee = 'pb_college_committee'
        api.user.grant_roles(username=current_user, roles=['Owner'], obj=obj)
        if not api.group.get(groupname=chair):
            api.group.create(groupname=chair, title=chair)
            print('Group added: ' + chair + ' successfully')
        if not api.group.get(groupname=committee):
            api.group.create(groupname=committee, title=committee)
            print('Group added: ' + committee + ' successfully')
        if not api.group.get(groupname=college_chair):
            api.group.create(groupname=college_chair, title=college_chair)
            print('Group added: ' + college_chair + ' successfully')
        if not api.group.get(groupname=college_committee):
            api.group.create(groupname=college_committee, title=college_committee)
            print('Group added: ' + college_committee + ' successfully')
    except:
        pass

    try:
        chair = 'pb_' + pbdept + '_chair'
        committee = 'pb_' + pbdept + '_committee'
        college_chair = 'pb_college_chair'
        college_committee = 'pb_college_committee'
        api.group.grant_roles(groupname=chair,
                              roles=['Dept Head', 'PBdeptChair', 'Reader'],
                              obj=obj)
        api.group.grant_roles(groupname=committee, roles=['PBdept', 'Reader'], obj=obj)
        api.group.grant_roles(groupname=college_chair, roles=['PBhead', 'Reader'], obj=obj)
        api.group.grant_roles(groupname=college_committee, roles=['PBcollege', 'Reader'], obj=obj)
    except:
        pass
