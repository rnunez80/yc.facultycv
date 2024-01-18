# -*- coding: utf-8 -*-
from collective.exportimport.export_content import ExportContent
from collective.exportimport.export_content import fix_portal_type
from logging import getLogger
from plone import api
from plone.restapi.interfaces import ISerializeToJson
from zope.component import getMultiAdapter
from zope.globalrequest import getRequest


logger = getLogger(__name__)

REVIEW_STATE_MAPPING = {
    'draft': 'draft',
    'pendingChair': 'pendingChair',
    'deptReviewing': 'deptReviewing',
    'collegeReviewing': 'collegeReviewing',
    'deptRejected': 'deptRejected',
    'collegeReviewingAppeal': 'collegeReviewingAppeal',
    'unsatisfactory': 'unsatisfactory',
    'satisfactory': 'satisfactory',
    'internally_published': 'internally_published',
    'pending_committee': 'pending_committee',
    'pending_head': 'pending_head',
    'pending_vp': 'pending_vp',
    'private': 'private',
    'published': 'published',
    'pending_review': 'pending_review',
    'feedback_shared': 'feedback_shared',
    'pending': 'pending',
    'visible': 'visible',
    'approved': 'approved',
    'committeeReviewing': 'committeeReviewing',
    'rejected': 'rejected',
}

pbActionTypes = [
    "pbaction2",
    "pbactionclt2",
    "pbactionleave2",
    "pbactionportfolioa",
    "pbactionportfoliob",
    "pbactionportfolioc",
    "pbactionscholar2",
    "symposium_talk",
    "pbActionCLT",
    "pbActionPortfolio0",
    "pbActionPortfolio1",
    "pbActionPortfolio2",
    "pbActionLeave",
    "pbActionScholar",
    "pb",
    "pbAction",
    "pbActionPortfolio",
]
TYPES_TO_EXPORT = [
    "college",
    "pbActionCLT",
    "pbActionPortfolio0",
    "pbActionPortfolio1",
    "pbActionPortfolio2",
    "pbActionLeave",
    "pbActionScholar",
    "Faculty",
    "pb",
    "pbAction",
    "pbActionPortfolio",
    "CVUsers",
    "Staff",
    # "Collection",
    # "Document",
    # "Folder",
    # "Link",
    # "File",
    # "Image",
    # "News Item",
    # "Event",
    # "scholarship_entry",
    # "Announcement",
    # "good_practice_entry",
    # "assessment_document",
    # "academic_assessment_document",
    # "Video",
    # "Audio",
    # "Pad",
    # "Dashboard",
    # "EasyForm",
    # "it-maintenance",
    # "tech_fee_committee_rfp",
    "faculty2",
    "directory",
    "staff2",
    "pbaction2",
    "pbactionclt2",
    "pbactionleave2",
    "pbactionportfolioa",
    "pbactionportfoliob",
    "pbactionportfolioc",
    "pbactionscholar2",
    "symposium_talk",
    # "assessment_unit",
    # "unit_goal",
    # "unit_report",
    # "reported_activity",
    # "unit_plan",
    # "planned_activity",
    # "collection_evaluation",
    # "planned_rational",
    # "assessment_unit_program",
    # "unit_plan_program",
    # "planned_activity_program",
    # "unit_midyear",
    # "unit_midyear_program",
    # "planned_data_analysis",
    # "reported_attachment",
    # "reported_changes_implemented",
    # "reported_other_activity",
    # "reported_data_analysis",
    # "reported_activity_new",
    # "unit_report_program",
    # "reported_program_activity",
    # "reported_program_activity_new",
    # "reported_program_changes_implemented",
    # "unit_plan_program_review",
    # "unit_report_program_review",
    # "unit_plan_review",
    # "unit_report_review",
    # "program_review_selfstudy",
    # "unit_review_selfstudy",
    # "program_review_report",
    # "program_review_actionplan",
    # "unit_review_actionplan",
    # "unit_review_report",
    # "procurement_access_request",
]

PATHS_TO_EXPORT = []

MARKER_INTERFACES_TO_EXPORT = []

ANNOTATIONS_TO_EXPORT = []

ANNOTATIONS_KEY = "exportimport.annotations"

MARKER_INTERFACES_KEY = "exportimport.marker_interfaces"


class VoltoMigration(ExportContent):
    QUERY = {
    }

    DROP_PATHS = [
    ]

    DROP_UIDS = [
    ]

    def global_dict_hook(self, item, obj):
        """Use this to modify or skip the serialized data.
        Return None if you want to skip this particular object.
        """
        try:
            if item["@type"] in pbActionTypes and item["managers"]:
                item["managers"] = str(item["managers"]) or None
            for portal_type in TYPES_TO_EXPORT:
                if not obj.portal_type == portal_type:
                    return item
            # this item is already exported to replace its container in dict_hook_folder
            if item["UID"] in self.transformed_default_pages:
                return
            if item.get("review_state") in REVIEW_STATE_MAPPING:
                item["review_state"] = REVIEW_STATE_MAPPING[item["review_state"]]
            if not item:
                return
            return item
        except:
            pass

    def update(self):
        self.transformed_default_pages = []

    def dict_hook_folder(self, item, obj):
        # handle default pages
        default_page = obj.getDefaultPage()
        if not default_page:
            # has no default-page, we keep it as a folder
            return item

        dp_obj = obj.get(default_page)
        dp_obj = self.global_obj_hook(dp_obj)
        if not dp_obj:
            return

        if dp_obj.portal_type not in TYPES_TO_EXPORT:
            # keep the old Folder for non-folderish content (Link)
            return item

        self.safe_portal_type = fix_portal_type(dp_obj.portal_type)
        serializer = getMultiAdapter((dp_obj, self.request), ISerializeToJson)
        dp_item = serializer(include_items=False)
        dp_item = self.fix_url(dp_item, dp_obj)
        dp_item = self.export_constraints(dp_item, dp_obj)
        dp_item = self.export_workflow_history(dp_item, dp_obj)
        if self.migration:
            dp_item = self.update_data_for_migration(dp_item, dp_obj)
        dp_item = self.global_dict_hook(dp_item, dp_obj)
        if not dp_item:
            logger.info(u"Skipping %s", dp_obj.absolute_url())
            return obj
        dp_item = self.custom_dict_hook(dp_item, dp_obj)
        if dp_item["@type"] != "Document":
            logger.info(u"Default page is type %s for %s: %s", dp_item["@type"], item["@id"], dp_obj.absolute_url())

        dp_item["parent"] = item["parent"]
        dp_item["@id"] = item["@id"]
        dp_item["id"] = item["id"]
        dp_item["is_folderish"] = True
        # prevent importing the default page obj again
        self.transformed_default_pages.append(dp_item["UID"])
        return dp_item

    def migrate_folders(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Folder']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_files(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view(
            'migrate_from_atct', portal, request)
        content_types = ['BlobFile', 'File']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_images(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['BlobImage', 'Image']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_documents(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Document']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_collections(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Collection']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_events(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Event']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_links(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Link']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_newsitems(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['News Item']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )

    def migrate_topics(context=None):
        portal = api.portal.get()
        request = getRequest()
        pac_migration = api.content.get_view('migrate_from_atct', portal, request)
        content_types = ['Topic']
        pac_migration(
            migrate=True,
            content_types=content_types,
            migrate_schemaextended_content=True,
            reindex_catalog=False,
            patch_searchabletext=True,
        )
