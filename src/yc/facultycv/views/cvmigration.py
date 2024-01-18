# -*- coding: utf-8 -*-

from plone import api
from plone.namedfile.file import NamedBlobFile
from plone.namedfile.file import NamedBlobImage
from plone.protect.authenticator import createToken
from plone.protect.interfaces import IDisableCSRFProtection
from Products.Five.browser import BrowserView
from zope.interface import alsoProvides

import transaction


class Cvmigration(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        # portal = api.portal.get()
        # portal_catalog = api.portal.get_tool('portal_catalog')
        # current_path = '/'.join(self.context.getPhysicalPath())
        portal, portal_catalog, current_path = api.portal.get(), api.portal.get_tool(
            'portal_catalog'), '/'.join(self.context.getPhysicalPath())
        alsoProvides(self.request, IDisableCSRFProtection)

        print('Starting Migration')
        colleges = portal_catalog(portal_type='college')
        for college in colleges:
            print('Creating directory')
            college_id = 'directory'
            collegeLocation = ''.join([current_path, '/', college_id])
            obj = college.getObject()
            # try:
            transaction.begin()
            collegeObject = api.content.create(
                type='directory',
                id=college_id,
                title=obj.title,
                safe_id=True,
                container=portal
            )
            collegeObject.manage_setLocalRoles('admin', ['Owner'])
            state = api.content.get_state(obj=obj)
            api.content.transition(obj=collegeObject, to_state=state)
            transaction.commit()
            print(' '.join(['Directory created', str(collegeObject.absolute_url())]))
            print(collegeLocation)
            # except (AttributeError, IndexError, TypeError) as e:
            #     print(e)
            #     print('Failed to create directory ' + str(obj.absolute_url())

            faculties = portal_catalog(portal_type="Faculty", path='/yc1/portal_college/srodgers')
            # faculties = portal_catalog(portal_type="Faculty")
            for faculty in faculties:
                alsoProvides(self.request, IDisableCSRFProtection)
                object = faculty.getObject()
                facultyLocation = '/'.join(object.getPhysicalPath())
                print(' '.join([str(facultyLocation), '- migrating']))
                try:
                    image = NamedBlobImage(data=object.image.data,
                                           contentType=object.image.content_type,
                                           filename=unicode(object.image.filename))
                except AttributeError:
                    image = None
                try:
                    transaction.begin()
                    facultyObject = api.content.create(
                        container=collegeObject,
                        type='faculty2',
                        id=object.id.lower(),
                        subject=object.subject,
                        userid=object.userid.lower(),
                        employeeType=object.employeeType,
                        first_name=object.first_name,
                        last_name=object.last_name,
                        teachingTitle=object.teachingTitle,
                        otherTitle=object.otherTitle,
                        email=object.email,
                        website=object.website,
                        officePhone=object.officePhone,
                        officeLocation=object.officeLocation,
                        officeHours=object.officeHours,
                        image=image,
                        dept=object.dept,
                        currentStatus=object.currentStatus,
                        orgStatus=object.orgStatus,
                        school=object.school,
                        prog=object.prog,
                        education=object.education,
                        managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace('&',
                                                                                                                      '-').lower(),
                        ssn=object.ssn,
                        citizen=object.citizen,
                        tenure=object.tenure,
                        Senior=object.Senior,
                        street=object.street,
                        apt=object.apt,
                        city=object.city,
                        state=object.state,
                        zipCode=object.zipCode,
                        homePhone=object.homePhone,
                        allowDiscussion=object.allowDiscussion,
                        location=object.location,
                        language=object.language,
                        contributors=object.contributors,
                        creators=object.creators,
                        rights=object.rights,
                        effectiveDate=object.effectiveDate,
                        expirationDate=object.expirationDate,
                        areaExpertise=object.areaExpertise,
                        briefBio=str(object.briefBio),
                        experienceFT=object.experienceFT,
                        experiencePT=object.experiencePT,
                        experienceNA=object.experienceNA,
                        employmentRecord=object.employmentRecord,
                        books=object.books,
                        articles=object.articles or {x.decode('utf-8', 'ignore'): y.decode('utf-8', 'ignore') for (x, y) in object.articles},
                        refereedProceedings=object.refereedProceedings,
                        nonRefereedProceedings=object.nonRefereedProceedings,
                        chapters=object.chapters,
                        monographs=object.monographs,
                        reviews=object.reviews,
                        presented=object.presented,
                        patents=object.patents,
                        pubEnhance=str(object.pubEnhance),
                        professional=object.professional,
                        grants=object.grants,
                        serviceDepartment=object.serviceDepartment,
                        serviceSchool=object.serviceSchool,
                        serviceCollege=object.serviceCollege,
                        serviceGraduateCenter=object.serviceGraduateCenter,
                        serviceUniversity=object.serviceUniversity,
                        officeHeld=object.officeHeld,
                        activities=object.activities,
                        coursesTaught=object.coursesTaught,
                        developed=object.developed,
                        hidecv=object.hidecv,
                        scholarEnhance=str(object.scholarEnhance),
                        teachEnhance=str(object.teachEnhance),
                        safe_id=True,
                    )
                    facultyObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                    state = api.content.get_state(obj=object)
                    api.content.transition(obj=facultyObject, to_state=state)
                    self.faculty_grant_roles(facultyObject)
                    transaction.commit()
                    print(' '.join(['Faculty created', str(facultyObject.absolute_url())]))
                except (AttributeError, IndexError, TypeError, AssertionError) as e:
                    print(e)
                    print(' '.join(['Failed to create Faculty', str(object.absolute_url())]))

                pbActions = portal_catalog(portal_type="pbAction", path=facultyLocation)
                for pbAction in pbActions:
                    object = pbAction.getObject()
                    print(pbAction.Title)
                    try:
                        toPresident = NamedBlobFile(data=object.toPresident.data,
                                                    contentType=object.toPresident.content_type,
                                                    filename=object.toPresident.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        toPresident = None
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=object.appealLetter.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=object.appealOther.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        chairMemo = NamedBlobFile(data=object.chairMemo.data,
                                                  contentType=object.chairMemo.content_type,
                                                  filename=object.chairMemo.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        classroomObservations1 = NamedBlobFile(data=object.classroomObservations1.data,
                                                               contentType=object.classroomObservations1.content_type,
                                                               filename=object.classroomObservations1.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations1 = None
                    try:
                        classroomObservations2 = NamedBlobFile(data=object.classroomObservations2.data,
                                                               contentType=object.classroomObservations2.content_type,
                                                               filename=object.classroomObservations2.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations2 = None
                    try:
                        studentEvaluation1 = NamedBlobFile(data=object.studentEvaluation1.data,
                                                           contentType=object.studentEvaluation1.content_type,
                                                           filename=object.studentEvaluation1.filename.decode(
                                                               'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation1 = None
                    try:
                        studentEvaluation2 = NamedBlobFile(data=object.studentEvaluation2.data,
                                                           contentType=object.studentEvaluation2.content_type,
                                                           filename=object.studentEvaluation2.filename.decode(
                                                               'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation2 = None
                    try:
                        resume = NamedBlobFile(data=object.resume.data,
                                               contentType=object.resume.content_type,
                                               filename=object.resume.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        resume = None
                    try:
                        transaction.begin()
                        pbActionObject = api.content.create(
                            type='pbaction2',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&', '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            toPresident=toPresident,
                            chairMemo=chairMemo,
                            classroomObservations1=classroomObservations1,
                            classroomObservations2=classroomObservations2,
                            studentEvaluation1=studentEvaluation1,
                            studentEvaluation2=studentEvaluation2,
                            resume=resume,
                            safe_id=True,
                            container=facultyObject
                        )
                        pbActionObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionObject.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionObject.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionObject)
                        self.pb_grant_roles(pbActionObject)
                        # self.pb_assign_user_to_groups(pbActionObject)
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionObject, to_state=state)
                        transaction.commit()
                        print(' '.join(['pbAction created', str(pbActionObject.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbAction', str(object.absolute_url())]))

                pbActionCLTs = portal_catalog(portal_type="pbActionCLT", path=facultyLocation)
                for pbActionCLT in pbActionCLTs:
                    object = pbActionCLT.getObject()
                    print(pbActionCLT.Title)
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=unicode(object.appealLetter.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=unicode(object.appealOther.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        chairMemo = NamedBlobFile(data=object.chairMemo.data,
                                                  contentType=object.chairMemo.content_type,
                                                  filename=unicode(object.chairMemo.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        transaction.begin()
                        pbActionCLTObject = api.content.create(
                            type='pbactionclt2',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&', '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            aCompetencyPriority=object.aCompetencyPriority,
                            aPerformarnceAssesmentCompetency=object.aPerformarnceAssesmentCompetency,
                            aComments=object.aComments,
                            bCompetencyPriority=object.bCompetencyPriority,
                            bPerformarnceAssesmentCompetency=object.bPerformarnceAssesmentCompetency,
                            bComments=object.bComments,
                            cCompetencyPriority=object.cCompetencyPriority,
                            cPerformarnceAssesmentCompetency=object.cPerformarnceAssesmentCompetency,
                            cComments=object.cComments,
                            dCompetencyPriority=object.dCompetencyPriority,
                            dPerformarnceAssesmentCompetency=object.dPerformarnceAssesmentCompetency,
                            dComments=object.dComments,
                            eCompetencyPriority=object.eCompetencyPriority,
                            ePerformarnceAssesmentCompetency=object.ePerformarnceAssesmentCompetency,
                            eComments=object.eComments,
                            skillSelectRate=object.skillSelectRate,
                            particularStrengthEmployee=object.particularStrengthEmployee,
                            improvedDeveloped=object.improvedDeveloped,
                            projectGoals=object.projectGoals,
                            contributeCollege=object.contributeCollege,
                            employeeComments=object.employeeComments,
                            chairsComments=object.chairsComments,
                            chairMemo=chairMemo,
                            safe_id=True,
                            container=facultyObject
                        )
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionCLTObject, to_state=state)
                        pbActionCLTObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionCLTObject.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionCLTObject.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionCLTObject)
                        self.pb_grant_roles(pbActionCLTObject)
                        # self.pb_assign_user_to_groups(pbActionCLTObject)
                        transaction.commit()
                        print(' '.join(['pbActionCLT created', str(pbActionCLTObject.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionCLT', str(object.absolute_url())]))

                pbActionLeaves = portal_catalog(portal_type="pbActionLeave", path=facultyLocation)
                for pbActionLeave in pbActionLeaves:
                    object = pbActionLeave.getObject()
                    print(pbActionLeave.Title)
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=unicode(object.appealLetter.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=unicode(object.appealOther.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        chairMemo = NamedBlobFile(data=object.chairMemo.data,
                                                  contentType=object.chairMemo.content_type,
                                                  filename=unicode(object.chairMemo.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        facultyMemo = NamedBlobFile(data=object.facultyMemo.data,
                                                    contentType=object.facultyMemo.content_type,
                                                    filename=object.facultyMemo.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        facultyMemo = None
                    try:
                        transaction.begin()
                        pbActionLeaveObject = api.content.create(
                            type='pbactionleave2',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&', '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            duration=object.duration,
                            purpose=object.purpose,
                            improvement=object.improvement,
                            creative=object.creative,
                            educational=object.educational,
                            activities=object.activities,
                            list=object.list,
                            sponsored=object.sponsored,
                            anticipate=object.anticipate,
                            nature=object.nature,
                            dates=object.dates,
                            attestation=object.attestation,
                            chairperson=object.chairperson,
                            intentCover=object.intentCover,
                            chairMemo=chairMemo,
                            facultyMemo=facultyMemo,
                            safe_id=True,
                            container=facultyObject
                        )

                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionLeaveObject, to_state=state)
                        pbActionLeaveObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionLeaveObject.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionLeaveObject.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionLeaveObject)
                        self.pb_grant_roles(pbActionLeaveObject)
                        # self.pb_assign_user_to_groups(pbActionLeaveObject)
                        transaction.commit()
                        print(' '.join(['pbActionLeave created', str(pbActionLeaveObject.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionLeave', str(object.absolute_url())]))

                pbActionPortfolio0s = portal_catalog(portal_type=["pbActionPortfolio", "pbActionPortfolio0"], path=facultyLocation)
                for pbActionPortfolio0 in pbActionPortfolio0s:
                    object = pbActionPortfolio0.getObject()
                    print(pbActionPortfolio0.Title)
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=object.appealLetter.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=object.appealOther.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        ExternalPeerReviewOfScholarship1 = NamedBlobFile(
                            data=object.ExternalPeerReviewOfScholarship1.data,
                            contentType=object.ExternalPeerReviewOfScholarship1.content_type,
                            filename=object.ExternalPeerReviewOfScholarship1.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship1 = None
                    try:
                        ExternalPeerReviewOfScholarship2 = NamedBlobFile(
                            data=object.ExternalPeerReviewOfScholarship2.data,
                            contentType=object.ExternalPeerReviewOfScholarship2.content_type,
                            filename=object.ExternalPeerReviewOfScholarship2.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship2 = None
                    try:
                        ExternalPeerReviewOfScholarship3 = NamedBlobFile(
                            data=object.ExternalPeerReviewOfScholarship3.data,
                            contentType=object.ExternalPeerReviewOfScholarship3.content_type,
                            filename=object.ExternalPeerReviewOfScholarship3.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship3 = None
                    try:
                        FramingStatement = NamedBlobFile(
                            data=object.FramingStatement.data,
                            contentType=object.FramingStatement.content_type,
                            filename=object.FramingStatement.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        FramingStatement = None
                    try:
                        ReflectiveStatement = NamedBlobFile(
                            data=object.ReflectiveStatement.data,
                            contentType=object.ReflectiveStatement.content_type,
                            filename=object.ReflectiveStatement.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ReflectiveStatement = None
                    try:
                        chairMemo = NamedBlobFile(
                            data=object.chairMemo.data,
                            contentType=object.chairMemo.content_type,
                            filename=object.chairMemo.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        classroomObservations1 = NamedBlobFile(
                            data=object.classroomObservations1.data,
                            contentType=object.classroomObservations1.content_type,
                            filename=object.classroomObservations1.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations1 = None
                    try:
                        classroomObservations2 = NamedBlobFile(
                            data=object.classroomObservations2.data,
                            contentType=object.classroomObservations2.content_type,
                            filename=object.classroomObservations2.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations2 = None
                    try:
                        studentEvaluation1 = NamedBlobFile(
                            data=object.studentEvaluation1.data,
                            contentType=object.studentEvaluation1.content_type,
                            filename=object.studentEvaluation1.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation1 = None
                    try:
                        studentEvaluation2 = NamedBlobFile(
                            data=object.studentEvaluation2.data,
                            contentType=object.studentEvaluation2.content_type,
                            filename=unicode(object.studentEvaluation2.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation2 = None
                    try:
                        SamplesAndCommentary1 = NamedBlobFile(
                            data=object.SamplesAndCommentary1.data,
                            contentType=object.SamplesAndCommentary1.content_type,
                            filename=object.SamplesAndCommentary1.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary1 = None
                    try:
                        SamplesAndCommentary2 = NamedBlobFile(
                            data=object.SamplesAndCommentary2.data,
                            contentType=object.SamplesAndCommentary2.content_type,
                            filename=object.SamplesAndCommentary2.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary2 = None
                    try:
                        SamplesAndCommentary3 = NamedBlobFile(
                            data=object.SamplesAndCommentary3.data,
                            contentType=object.SamplesAndCommentary3.content_type,
                            filename=object.SamplesAndCommentary3.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks1 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks1.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks1.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks1.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks1 = None
                    try:
                        PublicationsAndOtherScholarlyWorks2 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks2.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks2.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks2.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks2 = None
                    try:
                        PublicationsAndOtherScholarlyWorks3 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks3.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks3.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks3.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks4 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks4.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks4.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks4.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks4 = None
                    try:
                        PublicationsAndOtherScholarlyWorks5 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks5.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks5.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks5.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks5 = None
                    try:
                        researchStatement = NamedBlobFile(
                            data=object.researchStatement.data,
                            contentType=object.researchStatement.content_type,
                            filename=object.researchStatement.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        researchStatement = None
                    try:
                        appendix = NamedBlobFile(
                            data=object.appendix.data,
                            contentType=object.appendix.content_type,
                            filename=object.appendix.filename.decode('utf-8', 'ignore'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appendix = None

                    try:
                        transaction.begin()
                        pbActionPortfolio0Object = api.content.create(
                            type='pbactionportfolioa',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&', '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            ExternalPeerReviewOfScholarship1=ExternalPeerReviewOfScholarship1,
                            ExternalPeerReviewOfScholarship2=ExternalPeerReviewOfScholarship2,
                            ExternalPeerReviewOfScholarship3=ExternalPeerReviewOfScholarship3,
                            FramingStatement=FramingStatement,
                            ReflectiveStatement=ReflectiveStatement,
                            chairMemo=chairMemo,
                            classroomObservations1=classroomObservations1,
                            classroomObservations2=classroomObservations2,
                            studentEvaluation1=studentEvaluation1,
                            studentEvaluation2=studentEvaluation2,
                            SamplesAndCommentary1=SamplesAndCommentary1,
                            SamplesAndCommentary2=SamplesAndCommentary2,
                            SamplesAndCommentary3=SamplesAndCommentary3,
                            PublicationsAndOtherScholarlyWorks1=PublicationsAndOtherScholarlyWorks1,
                            PublicationsAndOtherScholarlyWorks2=PublicationsAndOtherScholarlyWorks2,
                            PublicationsAndOtherScholarlyWorks3=PublicationsAndOtherScholarlyWorks3,
                            PublicationsAndOtherScholarlyWorks4=PublicationsAndOtherScholarlyWorks4,
                            PublicationsAndOtherScholarlyWorks5=PublicationsAndOtherScholarlyWorks5,
                            researchStatement=researchStatement,
                            appendix=appendix,
                            safe_id=True,
                            container=facultyObject
                        )
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionPortfolio0Object, to_state=state)
                        pbActionPortfolio0Object.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionPortfolio0Object.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionPortfolio0Object)
                        self.pb_grant_roles(pbActionPortfolio0Object)
                        # self.pb_assign_user_to_groups(pbActionPortfolio0Object)
                        transaction.commit()
                        print(' '.join(['pbActionPortfolio0 created', str(pbActionPortfolio0Object.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionPortfolio0', str(object.absolute_url())]))

                pbActionPortfolio1s = portal_catalog(portal_type="pbActionPortfolio1", path=facultyLocation)
                for pbActionPortfolio1 in pbActionPortfolio1s:
                    object = pbActionPortfolio1.getObject()
                    print(pbActionPortfolio1.Title)
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=unicode(object.appealLetter.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=unicode(object.appealOther.filename))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        DeanLetter = NamedBlobFile(data=object.DeanLetter.data,
                                                   contentType=object.DeanLetter.content_type,
                                                   filename=object.DeanLetter.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        DeanLetter = None
                    try:
                        FramingStatement = NamedBlobFile(data=object.FramingStatement.data,
                                                         contentType=object.FramingStatement.content_type,
                                                         filename=object.FramingStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        FramingStatement = None
                    try:
                        ReflectiveStatement = NamedBlobFile(data=object.ReflectiveStatement.data,
                                                            contentType=object.ReflectiveStatement.content_type,
                                                            filename=object.ReflectiveStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ReflectiveStatement = None
                    try:
                        chairMemo = NamedBlobFile(data=object.chairMemo.data,
                                                  contentType=object.chairMemo.content_type,
                                                  filename=object.chairMemo.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        classroomObservations1 = NamedBlobFile(data=object.classroomObservations1.data,
                                                               contentType=object.classroomObservations1.content_type,
                                                               filename=object.classroomObservations1.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations1 = None
                    try:
                        classroomObservations2 = NamedBlobFile(data=object.classroomObservations2.data,
                                                               contentType=object.classroomObservations2.content_type,
                                                               filename=object.classroomObservations2.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations2 = None
                    try:
                        studentEvaluation1 = NamedBlobFile(data=object.studentEvaluation1.data,
                                                           contentType=object.studentEvaluation1.content_type,
                                                           filename=object.studentEvaluation1.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation1 = None
                    try:
                        studentEvaluation2 = NamedBlobFile(data=object.studentEvaluation2.data,
                                                           contentType=object.studentEvaluation2.content_type,
                                                           filename=object.studentEvaluation2.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation2 = None
                    try:
                        SamplesAndCommentary1 = NamedBlobFile(data=object.SamplesAndCommentary1.data,
                                                              contentType=object.SamplesAndCommentary1.content_type,
                                                              filename=object.SamplesAndCommentary1.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary1 = None
                    try:
                        SamplesAndCommentary2 = NamedBlobFile(data=object.SamplesAndCommentary2.data,
                                                              contentType=object.SamplesAndCommentary2.content_type,
                                                              filename=object.SamplesAndCommentary2.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary2 = None
                    try:
                        SamplesAndCommentary3 = NamedBlobFile(data=object.SamplesAndCommentary3.data,
                                                              contentType=object.SamplesAndCommentary3.content_type,
                                                              filename=object.SamplesAndCommentary3.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks1 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks1.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks1.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks1.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks1 = None
                    try:
                        PublicationsAndOtherScholarlyWorks2 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks2.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks2.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks2.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks2 = None
                    try:
                        PublicationsAndOtherScholarlyWorks3 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks3.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks3.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks3.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks4 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks4.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks4.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks4.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks4 = None
                    try:
                        PublicationsAndOtherScholarlyWorks5 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks5.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks5.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks5.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks5 = None
                    try:
                        researchStatement = NamedBlobFile(data=object.researchStatement.data,
                                                          contentType=object.researchStatement.content_type,
                                                          filename=object.researchStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        researchStatement = None
                    try:
                        ExternalPeerReviewOfScholarship1 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship1.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship1.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship1.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship1 = None
                    try:
                        ExternalPeerReviewOfScholarship2 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship2.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship2.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship2.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship2 = None
                    try:
                        ExternalPeerReviewOfScholarship3 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship3.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship3.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship3.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship3 = None
                    try:
                        appendix = NamedBlobFile(data=object.appendix.data,
                                                 contentType=object.appendix.content_type,
                                                 filename=object.appendix.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appendix = None
                    try:
                        transaction.begin()
                        pbActionPortfolio1Object = api.content.create(
                            type='pbactionportfoliob',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&',
                                '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            DeanLetter=DeanLetter,
                            FramingStatement=FramingStatement,
                            ReflectiveStatement=ReflectiveStatement,
                            chairMemo=chairMemo,
                            classroomObservations1=classroomObservations1,
                            classroomObservations2=classroomObservations2,
                            studentEvaluation1=studentEvaluation1,
                            studentEvaluation2=studentEvaluation2,
                            SamplesAndCommentary1=SamplesAndCommentary1,
                            SamplesAndCommentary2=SamplesAndCommentary2,
                            SamplesAndCommentary3=SamplesAndCommentary3,
                            PublicationsAndOtherScholarlyWorks1=PublicationsAndOtherScholarlyWorks1,
                            PublicationsAndOtherScholarlyWorks2=PublicationsAndOtherScholarlyWorks2,
                            PublicationsAndOtherScholarlyWorks3=PublicationsAndOtherScholarlyWorks3,
                            PublicationsAndOtherScholarlyWorks4=PublicationsAndOtherScholarlyWorks4,
                            PublicationsAndOtherScholarlyWorks5=PublicationsAndOtherScholarlyWorks5,
                            researchStatement=researchStatement,
                            ExternalPeerReviewOfScholarship1=ExternalPeerReviewOfScholarship1,
                            ExternalPeerReviewOfScholarship2=ExternalPeerReviewOfScholarship2,
                            ExternalPeerReviewOfScholarship3=ExternalPeerReviewOfScholarship3,
                            appendix=appendix,
                            safe_id=True,
                            container=facultyObject
                        )
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionPortfolio1Object, to_state=state)
                        pbActionPortfolio1Object.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionPortfolio1Object.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionPortfolio1Object)
                        self.pb_grant_roles(pbActionPortfolio1Object)
                        # self.pb_assign_user_to_groups(pbActionPortfolio1Object)
                        transaction.commit()
                        print(' '.join(['pbActionPortfolio1 created', str(pbActionPortfolio1Object.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionPortfolio1', str(object.absolute_url())]))

                pbActionPortfolio2s = portal_catalog(portal_type="pbActionPortfolio2", path=facultyLocation)
                for pbActionPortfolio2 in pbActionPortfolio2s:
                    object = pbActionPortfolio2.getObject()
                    print(pbActionPortfolio2.Title)
                    try:
                        appealLetter = NamedBlobFile(data=object.appealLetter.data,
                                                     contentType=object.appealLetter.content_type,
                                                     filename=object.appealLetter.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealLetter = None
                    try:
                        appealOther = NamedBlobFile(data=object.appealOther.data,
                                                    contentType=object.appealOther.content_type,
                                                    filename=object.appealOther.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appealOther = None
                    try:
                        FramingStatement = NamedBlobFile(data=object.FramingStatement.data,
                                                         contentType=object.FramingStatement.content_type,
                                                         filename=object.FramingStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        FramingStatement = None
                    try:
                        ReflectiveStatement = NamedBlobFile(data=object.ReflectiveStatement.data,
                                                            contentType=object.ReflectiveStatement.content_type,
                                                            filename=object.ReflectiveStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ReflectiveStatement = None
                    try:
                        chairMemo = NamedBlobFile(data=object.chairMemo.data,
                                                  contentType=object.chairMemo.content_type,
                                                  filename=object.chairMemo.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        chairMemo = None
                    try:
                        classroomObservations1 = NamedBlobFile(data=object.classroomObservations1.data,
                                                               contentType=object.classroomObservations1.content_type,
                                                               filename=object.classroomObservations1.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations1 = None
                    try:
                        classroomObservations2 = NamedBlobFile(data=object.classroomObservations2.data,
                                                               contentType=object.classroomObservations2.content_type,
                                                               filename=object.classroomObservations2.filename.decode(
                                                                   'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        classroomObservations2 = None
                    try:
                        studentEvaluation1 = NamedBlobFile(data=object.studentEvaluation1.data,
                                                           contentType=object.studentEvaluation1.content_type,
                                                           filename=object.studentEvaluation1.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation1 = None
                    try:
                        studentEvaluation2 = NamedBlobFile(data=object.studentEvaluation2.data,
                                                           contentType=object.studentEvaluation2.content_type,
                                                           filename=object.studentEvaluation2.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        studentEvaluation2 = None
                    try:
                        SamplesAndCommentary1 = NamedBlobFile(data=object.SamplesAndCommentary1.data,
                                                              contentType=object.SamplesAndCommentary1.content_type,
                                                              filename=object.SamplesAndCommentary1.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary1 = None
                    try:
                        SamplesAndCommentary2 = NamedBlobFile(data=object.SamplesAndCommentary2.data,
                                                              contentType=object.SamplesAndCommentary2.content_type,
                                                              filename=object.SamplesAndCommentary2.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary2 = None
                    try:
                        SamplesAndCommentary3 = NamedBlobFile(data=object.SamplesAndCommentary3.data,
                                                              contentType=object.SamplesAndCommentary3.content_type,
                                                              filename=object.SamplesAndCommentary3.filename.decode(
                                                                  'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        SamplesAndCommentary3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks1 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks1.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks1.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks1.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks1 = None
                    try:
                        PublicationsAndOtherScholarlyWorks2 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks2.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks2.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks2.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks2 = None
                    try:
                        PublicationsAndOtherScholarlyWorks3 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks3.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks3.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks3.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks3 = None
                    try:
                        PublicationsAndOtherScholarlyWorks4 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks4.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks4.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks4.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks4 = None
                    try:
                        PublicationsAndOtherScholarlyWorks5 = NamedBlobFile(
                            data=object.PublicationsAndOtherScholarlyWorks5.data,
                            contentType=object.PublicationsAndOtherScholarlyWorks5.content_type,
                            filename=object.PublicationsAndOtherScholarlyWorks5.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        PublicationsAndOtherScholarlyWorks5 = None
                    try:
                        researchStatement = NamedBlobFile(data=object.researchStatement.data,
                                                          contentType=object.researchStatement.content_type,
                                                          filename=object.researchStatement.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        researchStatement = None
                    try:
                        ExternalPeerReviewOfScholarship1 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship1.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship1.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship1.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship1 = None
                    try:
                        ExternalPeerReviewOfScholarship2 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship2.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship2.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship2.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship2 = None
                    try:
                        ExternalPeerReviewOfScholarship3 = NamedBlobFile(data=object.ExternalPeerReviewOfScholarship3.data,
                                                                         contentType=object.ExternalPeerReviewOfScholarship3.content_type,
                                                                         filename=object.ExternalPeerReviewOfScholarship3.filename.decode(
                                                                             'utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        ExternalPeerReviewOfScholarship3 = None
                    try:
                        appendix = NamedBlobFile(data=object.appendix.data,
                                                 contentType=object.appendix.content_type,
                                                 filename=object.appendix.filename.decode('utf-8'))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        appendix = None
                    try:
                        transaction.begin()
                        pbActionPortfolio2Object = api.content.create(
                            type='pbactionportfolioc',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            first_name=object.first_name,
                            last_name=object.last_name,
                            teachingTitle=object.teachingTitle,
                            dept=object.dept,
                            appealLetter=appealLetter,
                            appealOther=appealOther,
                            YearsOfService=object.YearsOfService,
                            managers=str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                                '&',
                                '-').lower(),
                            deptVotesYes=object.deptVotesYes,
                            deptVotesAbstain=object.deptVotesAbstain,
                            deptVotesNo=object.deptVotesNo,
                            collegeVotesYes=object.collegeVotesYes,
                            collegeVotesAbstain=object.collegeVotesAbstain,
                            collegeVotesNo=object.collegeVotesNo,
                            moreDocs=object.moreDocs,
                            FramingStatement=FramingStatement,
                            ReflectiveStatement=ReflectiveStatement,
                            chairMemo=chairMemo,
                            classroomObservations1=classroomObservations1,
                            classroomObservations2=classroomObservations2,
                            studentEvaluation1=studentEvaluation1,
                            studentEvaluation2=studentEvaluation2,
                            SamplesAndCommentary1=SamplesAndCommentary1,
                            SamplesAndCommentary2=SamplesAndCommentary2,
                            SamplesAndCommentary3=SamplesAndCommentary3,
                            PublicationsAndOtherScholarlyWorks1=PublicationsAndOtherScholarlyWorks1,
                            PublicationsAndOtherScholarlyWorks2=PublicationsAndOtherScholarlyWorks2,
                            PublicationsAndOtherScholarlyWorks3=PublicationsAndOtherScholarlyWorks3,
                            PublicationsAndOtherScholarlyWorks4=PublicationsAndOtherScholarlyWorks4,
                            PublicationsAndOtherScholarlyWorks5=PublicationsAndOtherScholarlyWorks5,
                            researchStatement=researchStatement,
                            ExternalPeerReviewOfScholarship1=ExternalPeerReviewOfScholarship1,
                            ExternalPeerReviewOfScholarship2=ExternalPeerReviewOfScholarship2,
                            ExternalPeerReviewOfScholarship3=ExternalPeerReviewOfScholarship3,
                            appendix=appendix,
                            safe_id=True,
                            container=facultyObject
                        )
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionPortfolio2Object, to_state=state)
                        pbActionPortfolio2Object.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionPortfolio2Object.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionPortfolio2Object)
                        self.pb_grant_roles(pbActionPortfolio2Object)
                        # self.pb_assign_user_to_groups(pbActionPortfolio2Object)
                        transaction.commit()
                        print(' '.join(['pbActionPortfolio2 created', str(pbActionPortfolio2Object.absolute_url())]))

                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionPortfolio2', str(object.absolute_url())]))

                pbActionScholars = portal_catalog(portal_type="pbActionScholar", path=facultyLocation)
                for pbActionScholar in pbActionScholars:
                    object = pbActionScholar.getObject()
                    print(pbActionScholar.Title)
                    try:
                        transaction.begin()
                        pbActionScholarObject = api.content.create(
                            type='pbactionscholar2',
                            id=object.id.lower(),
                            userid=object.userid.lower(),
                            title=object.title,
                            safe_id=True,
                            container=facultyObject
                        )
                        state = api.content.get_state(obj=object)
                        api.content.transition(obj=pbActionScholarObject, to_state=state)
                        pbActionScholarObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                        # pbdept = str(object.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                        #     '&', '-').replace(' ', '-').lower()
                        # pbActionScholarObject.manage_setLocalRoles('pb-chair', ['PBdeptChair', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-committee', ['PBdept', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-' + pbdept + '-committee', ['PBdept', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-' + pbdept + '-chair', ['PBdeptChair', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-college-chair', ['PBhead', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-college-committee', ['PBcollege', 'Reader'])
                        # pbActionScholarObject.manage_setLocalRoles('pb-all', ['Reader'])
                        self.pb_make_groups(pbActionScholarObject)
                        self.pb_grant_roles(pbActionScholarObject)
                        # self.pb_assign_user_to_groups(pbActionScholarObject)
                        transaction.commit()
                        print(' '.join(['pbActionScholar created', str(pbActionScholarObject.absolute_url())]))
                    except (AttributeError, IndexError, TypeError, AssertionError) as e:
                        print(e)
                        print(' '.join(['Failed to create pbActionScholar', str(object.absolute_url())]))

            staffs = portal_catalog(portal_type="Staff", path='/yc1/portal_college/srodgers')
            # staffs = portal_catalog(portal_type="Staff")
            for staff in staffs:
                object = staff.getObject()
                staffLocation = '/'.join(object.getPhysicalPath())
                print(' '.join([str(staffLocation), '- migrating']))
                try:
                    image = NamedBlobImage(data=object.image.data,
                                           contentType=object.image.content_type,
                                           filename=unicode(object.image.filename))
                except AttributeError:
                    image = None
                try:
                    transaction.begin()
                    staffObject = api.content.create(
                        container=collegeObject,
                        type='staff2',
                        id=object.id.lower(),
                        userid=object.userid.lower(),
                        employeeType=object.employeeType,
                        first_name=object.first_name,
                        last_name=object.last_name,
                        teachingTitle=object.teachingTitle,
                        otherTitle=object.otherTitle,
                        email=object.email,
                        website=object.website,
                        officePhone=object.officePhone,
                        officeLocation=object.officeLocation,
                        officeHours=object.officeHours,
                        image=image,
                        dept=object.dept,
                        safe_id=True,
                    )
                    staffObject.manage_setLocalRoles(object.userid.lower(), ['Owner'])
                    state = api.content.get_state(obj=object)
                    api.content.transition(obj=staffObject, to_state=state)
                    transaction.commit()
                    print(' '.join(['Staff created', str(staffObject.absolute_url())]))
                except (AttributeError, IndexError, TypeError, AssertionError) as e:
                    print(e)
                    print(' '.join(['Failed to create Staff', str(object.absolute_url())]))

                prelink = "<div id='content'><h1 class='documentFirstHeading'>" \
                          "CV Migration Successful</h1><div><a " \
                          "href=' "
                CVLocation = collegeObject.absolute_url()
                postlink = "' class='btn btn-large btn-success'>" \
                           "Click Here to Continue</a></div></div>"
                return prelink + CVLocation + postlink

    def pb_make_groups(self, obj):
        try:
            print('Looking up manager set for ' + (obj.title if obj.title else obj.id))
            pbdept = str(obj.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower() if str(obj.managers).replace('()-',
                                                                                                             '').replace(
                'and', '-').replace(
                ',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower() else str(obj.managers).replace('()-',
                                                                                                               '').replace(
                'and', '-').replace(
                ',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower()
            try:
                if pbdept is not None:
                    print('Manager set to ' + pbdept)
                elif pbdept is None:
                    print('No manager found, continuing...')
            except Exception as e:
                print(e)
            print('Now creating Groups...')
            api.group.create(groupname='unit-' + pbdept + '-chair')
            api.group.create(groupname='unit-' + pbdept + '-committee')
            api.group.create(groupname='unit-college-chair')
            api.group.create(groupname='unit-college-committee')
            print('Groups created successfully')
        except Exception as e:
            print(e)
            print('Creation of Groups Failed')

    def pb_grant_roles(self, obj):
        try:
            print('Looking up manager set for ' + (obj.title if obj.title else obj.id))
            pbdept = str(obj.managers).replace('()-', '').replace('and', '-').replace(',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower() if str(obj.managers).replace('()-',
                                                                                                             '').replace(
                'and', '-').replace(
                ',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower() else str(obj.managers).replace('()-',
                                                                                                               '').replace(
                'and', '-').replace(
                ',', '').replace(
                '&', '-').replace(' ', '-').replace('Grp', 'committee').lower()
            try:
                if pbdept is not None:
                    print('Manager set to ' + pbdept)
                elif pbdept is None:
                    print('No manager found, continuing...')
            except Exception as e:
                print(e)
            print('Now Granting Group Roles...')
            api.group.grant_roles(groupname='unit-' + pbdept + '-chair', roles=['Dept Head', 'PBdeptChair', 'Reader'],
                                  obj=obj)
            api.group.grant_roles(groupname='unit-' + pbdept + '-committee', roles=['PBdept', 'Reader'], obj=obj)
            api.group.grant_roles(groupname='unit-college-chair', roles=['PBhead', 'Reader'], obj=obj)
            api.group.grant_roles(groupname='unit-college-committee', roles=['PBcollege', 'Reader'], obj=obj)
            api.group.grant_roles(groupname='pb-chair', roles=['PBdeptChair', 'Dept Head', 'Reader'], obj=obj)
            api.group.grant_roles(groupname='pb-committee', roles=['PBdept', 'Reader'], obj=obj)
            print('Roles set successfully')
        except Exception as e:
            print(e)
            print('Failed to Grant Roles')

    def faculty_grant_roles(self, obj):
        try:
            print('Now Granting User Roles...')
            api.user.grant_roles(username=obj.userid, roles=['Owner'], obj=obj)
            print('Roles set successfully')
        except Exception as e:
            print(e)
            print('Failed to Grant Roles')

    def token(self):
        return createToken()


