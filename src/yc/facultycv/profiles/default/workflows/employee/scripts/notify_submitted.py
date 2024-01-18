## Script (Python) "notify_submitted"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=sti
##title=
##
## Errors:
##  Line 21: SyntaxError: invalid syntax at statement: 'raise AttributeError, "cant find a Mail Host object"'
##
#This script has been designed to send email to cmf users with the reviewer
#role when a new item has been submitted for publishing. The script should be
#used in conjuction with the workflow tool.  
#parameters review_state


# set up a empty list of email addresses
# loop through the portal membership, pass memberId to check for
# Reviewer role. If successful apend the list of email addresses
# and send them email

mailList=[]
for item in context.portal_membership.listMembers():
    memberId = item.id
    if 'Reviewer' in context.portal_membership.getMemberById(memberId).getRoles():
        if item.email !='':
           mailList.append(item.email)
        try:
           mailhost=getattr(context, context.portal_url.superValues('Mail Host')[0].id)
        except:
           raise AttributeError, "cant find a Mail Host object"

        mMsg = 'Item has been submitted for your review\n  Please review the submitted content. \n ~mailman \n '
        mTo = item.email
        mFrom = 'webmaster@york.cuny.edu'
        mSubj = 'Item Submitted for your review'

        mailhost.send(mMsg, mTo, mFrom, mSubj)
