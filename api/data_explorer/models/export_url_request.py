# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from data_explorer.models.base_model_ import Model
from data_explorer import util


class ExportUrlRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cohort_name=None, filter=None,
                 data_explorer_url=None):  # noqa: E501
        """ExportUrlRequest - a model defined in Swagger

        :param cohort_name: The cohort_name of this ExportUrlRequest.  # noqa: E501
        :type cohort_name: str
        :param filter: The filter of this ExportUrlRequest.  # noqa: E501
        :type filter: List[str]
        :param data_explorer_url: The data_explorer_url of this ExportUrlRequest.  # noqa: E501
        :type data_explorer_url: str
        """
        self.swagger_types = {
            'cohort_name': str,
            'filter': List[str],
            'data_explorer_url': str
        }

        self.attribute_map = {
            'cohort_name': 'cohortName',
            'filter': 'filter',
            'data_explorer_url': 'dataExplorerUrl'
        }

        self._cohort_name = cohort_name
        self._filter = filter
        self._data_explorer_url = data_explorer_url

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The exportUrlRequest of this ExportUrlRequest.  # noqa: E501
        :rtype: ExportUrlRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cohort_name(self):
        """Gets the cohort_name of this ExportUrlRequest.


        :return: The cohort_name of this ExportUrlRequest.
        :rtype: str
        """
        return self._cohort_name

    @cohort_name.setter
    def cohort_name(self, cohort_name):
        """Sets the cohort_name of this ExportUrlRequest.


        :param cohort_name: The cohort_name of this ExportUrlRequest.
        :type cohort_name: str
        """

        self._cohort_name = cohort_name

    @property
    def filter(self):
        """Gets the filter of this ExportUrlRequest.


        :return: The filter of this ExportUrlRequest.
        :rtype: List[str]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ExportUrlRequest.


        :param filter: The filter of this ExportUrlRequest.
        :type filter: List[str]
        """

        self._filter = filter

    @property
    def data_explorer_url(self):
        """Gets the data_explorer_url of this ExportUrlRequest.


        :return: The data_explorer_url of this ExportUrlRequest.
        :rtype: str
        """
        return self._data_explorer_url

    @data_explorer_url.setter
    def data_explorer_url(self, data_explorer_url):
        """Sets the data_explorer_url of this ExportUrlRequest.


        :param data_explorer_url: The data_explorer_url of this ExportUrlRequest.
        :type data_explorer_url: str
        """

        self._data_explorer_url = data_explorer_url
