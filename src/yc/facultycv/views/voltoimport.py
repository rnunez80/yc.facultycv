# -*- coding: utf-8 -*-
# from plone import api
from collective.exportimport.import_content import ImportContent
from logging import getLogger
from setuptools.config._validate_pyproject import ValidationError


logger = getLogger(__name__)

SIMPLE_SETTER_FIELDS = {}


class VoltoImport(ImportContent):
    CONTAINER = {'college': '/directory'}

    DEFAULTS = {}

    def dict_hook_faculty2(self, item):
        try:
            item["@type"] = "faculty2"
            item["layout"] = "profile-default"
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["website", "prog", "managers", "articles", "refereedProceedings",
                                                       "nonRefereedProceedings",
                                                       "chapters", "monographs"]):

                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbaction2(self, item):
        try:
            item["@type"] = "pbaction2"
            item["layout"] = "view"
            # item["managers"] = str(item["managers"])
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"], ["managers", "deptVotesYes", "deptVotesNo", "deptVotesAbstain",
                                                                      "collegeVotesYes", "collegeVotesNo",
                                                                      "collegeVotesAbstain",
                                                                      "moreDocs"]):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionclt2(self, item):
        try:
            item["@type"] = "pbactionclt2"
            item["layout"] = "view"
#             item["managers"] = str(item["managers"])
            item["YearsOfService"] = str(item["YearsOfService"]).replace('Promotion CTL to Senior CTL',
                                                                         'Promotion CLT to Senior CLT').replace(
                'promotion-ctl-to-senior-ctl', 'Promotion CLT to Senior CLT').replace(
                'Promotion Senior CTL to Chief CTL', 'Promotion Senior CLT to Chief CLT')
            item["aPerformarnceAssesmentCompetency"] = str(item["aPerformarnceAssesmentCompetency"])
            item["bPerformarnceAssesmentCompetency"] = str(item["bPerformarnceAssesmentCompetency"])
            item["cPerformarnceAssesmentCompetency"] = str(item["cPerformarnceAssesmentCompetency"])
            item["dPerformarnceAssesmentCompetency"] = str(item["dPerformarnceAssesmentCompetency"])
            item["ePerformarnceAssesmentCompetency"] = str(item["ePerformarnceAssesmentCompetency"])

            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["managers", "aCompetencyPriority",
                                                       "aPerformarnceAssesmentCompetency",
                                                       "bCompetencyPriority",
                                                       "bPerformarnceAssesmentCompetency",
                                                       "cCompetencyPriority",
                                                       "cPerformarnceAssesmentCompetency",
                                                       "dCompetencyPriority",
                                                       "dPerformarnceAssesmentCompetency",
                                                       "eCompetencyPriority",
                                                       "ePerformarnceAssesmentCompetency"
                                                       ]):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionleave2(self, item):
        try:
            item["@type"] = "pbactionleave2"
            item["layout"] = "view"
#             item["managers"] = str(item["managers"])
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["managers", 'deptVotesYes', 'deptVotesNo',
                                                       'deptVotesAbstain',
                                                       'collegeVotesYes', 'collegeVotesNo', 'collegeVotesAbstain',
                                                       'moreDocs', 'duration', 'dates']):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionportfolioa(self, item):
        try:
            item["@type"] = "pbactionportfolioa"
            item["layout"] = "view"
#             item["managers"] = str(item["managers"])
            item["YearsOfService"] = str(item["YearsOfService"])
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["managers"]):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionportfoliob(self, item):
        try:
            item["@type"] = "pbactionportfoliob"
            item["layout"] = "view"
#             item["managers"] = str(item["managers"])
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["managers"]):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionportfolioc(self, item):
        try:
            item["@type"] = "pbactionportfolioc"
            item["layout"] = "view"
#             item["managers"] = str(item["managers"])
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ["managers"]):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def dict_hook_pbactionscholar2(self, item):
        try:
            item["@type"] = "pbactionscholar2"
            item["layout"] = "view"
            return item
        except ValidationError:
            pass

    def dict_hook_staff2(self, item):
        try:
            item["@type"] = "staff2"
            item["layout"] = "profile-staff"
            simple = {}
            for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"],
                                                      ['website']):
                if fieldname in item:
                    value = item.pop(fieldname)
                    if value:
                        simple[fieldname] = value
            if simple:
                item["exportimport.simplesetter"] = simple
            return item
        except ValidationError:
            pass

    def handle_file_container(self, item):
        """Use this to specify the container in which to create the item in.
        Return the container for this particular object.
        """
        item['@type'] = 'directory'
        return self.portal[item['@type']]
