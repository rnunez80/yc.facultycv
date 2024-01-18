## Script (Python) "notify_rejected"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=sti
##title=
##
obj=sti.object
creator = obj.Creator()
history = sti.getHistory()
wf_tool = context.portal_workflow

mMsg = """
The item you submitted or have ownership was declined for posting. See the document history for details.
The url was %s.
The reason was %s.
"""

member = context.portal_membership.getMemberById(creator)
creator = {'member':member,
           'id':member.getId(),
           'fullname':member.getProperty('fullname', 'Fullname missing'),
           'email':member.getProperty('email', None)}

actorid = wf_tool.getInfoFor(obj, 'actor')
actor = context.portal_membership.getMemberById(actorid)
reviewer = {'member':actor,
            'id':actor.getId(),
            'fullname':actor.getProperty('fullname', 'Fullname missing'),
            'email':actor.getProperty('email', None)}

mTo = creator['email']
mFrom = reviewer['email']
mSubj = 'DECLINED for posting'
obj_url = obj.absolute_url() #use portal_url + relative_url
comments = wf_tool.getInfoFor(obj, 'comments')

message = mMsg % (obj_url, comments)
context.MailHost.send(message, mTo, mFrom, mSubj)
