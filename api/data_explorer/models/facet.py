# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from data_explorer.models.base_model_ import Model
from data_explorer import util


class Facet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self,
                 name=None,
                 description=None,
                 es_field_name=None,
                 es_field_type=None,
                 value_names=None,
                 value_counts=None,
                 time_names=None,
                 time_series_value_counts=None):  # noqa: E501
        """Facet - a model defined in Swagger

        :param name: The name of this Facet.  # noqa: E501
        :type name: str
        :param description: The description of this Facet.  # noqa: E501
        :type description: str
        :param es_field_name: The es_field_name of this Facet.  # noqa: E501
        :type es_field_name: str
        :param es_field_type: The es_field_type of this Facet.  # noqa: E501
        :type es_field_type: str
        :param value_names: The value_names of this Facet.  # noqa: E501
        :type value_names: List[str]
        :param value_counts: The value_counts of this Facet.  # noqa: E501
        :type value_counts: List[int]
        :param time_names: The time_names of this Facet.  # noqa: E501
        :type time_names: List[str]
        :param time_series_value_counts: The time_series_value_counts of this Facet.  # noqa: E501
        :type time_series_value_counts: List[List[int]]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'es_field_name': str,
            'es_field_type': str,
            'value_names': List[str],
            'value_counts': List[int],
            'time_names': List[str],
            'time_series_value_counts': List[List[int]]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'es_field_name': 'es_field_name',
            'es_field_type': 'es_field_type',
            'value_names': 'value_names',
            'value_counts': 'value_counts',
            'time_names': 'time_names',
            'time_series_value_counts': 'time_series_value_counts'
        }

        self._name = name
        self._description = description
        self._es_field_name = es_field_name
        self._es_field_type = es_field_type
        self._value_names = value_names
        self._value_counts = value_counts
        self._time_names = time_names
        self._time_series_value_counts = time_series_value_counts

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Facet of this Facet.  # noqa: E501
        :rtype: Facet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Facet.

        Facet name, for example, \"Gender\".  # noqa: E501

        :return: The name of this Facet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Facet.

        Facet name, for example, \"Gender\".  # noqa: E501

        :param name: The name of this Facet.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Facet.

        Optional facet description.  # noqa: E501

        :return: The description of this Facet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Facet.

        Optional facet description.  # noqa: E501

        :param description: The description of this Facet.
        :type description: str
        """

        self._description = description

    @property
    def es_field_name(self):
        """Gets the es_field_name of this Facet.

        The Elasticsearch field name.  # noqa: E501

        :return: The es_field_name of this Facet.
        :rtype: str
        """
        return self._es_field_name

    @es_field_name.setter
    def es_field_name(self, es_field_name):
        """Sets the es_field_name of this Facet.

        The Elasticsearch field name.  # noqa: E501

        :param es_field_name: The es_field_name of this Facet.
        :type es_field_name: str
        """

        self._es_field_name = es_field_name

    @property
    def es_field_type(self):
        """Gets the es_field_type of this Facet.

        The Elasticsearch field type.  # noqa: E501

        :return: The es_field_type of this Facet.
        :rtype: str
        """
        return self._es_field_type

    @es_field_type.setter
    def es_field_type(self, es_field_type):
        """Sets the es_field_type of this Facet.

        The Elasticsearch field type.  # noqa: E501

        :param es_field_type: The es_field_type of this Facet.
        :type es_field_type: str
        """

        self._es_field_type = es_field_type

    @property
    def value_names(self):
        """Gets the value_names of this Facet.

        Array of names of possible facet values.   # noqa: E501

        :return: The value_names of this Facet.
        :rtype: List[str]
        """
        return self._value_names

    @value_names.setter
    def value_names(self, value_names):
        """Sets the value_names of this Facet.

        Array of names of possible facet values.   # noqa: E501

        :param value_names: The value_names of this Facet.
        :type value_names: List[str]
        """

        self._value_names = value_names

    @property
    def value_counts(self):
        """Gets the value_counts of this Facet.

        Array of counts for each facet value.  # noqa: E501

        :return: The value_counts of this Facet.
        :rtype: List[int]
        """
        return self._value_counts

    @value_counts.setter
    def value_counts(self, value_counts):
        """Sets the value_counts of this Facet.

        Array of counts for each facet value.  # noqa: E501

        :param value_counts: The value_counts of this Facet.
        :type value_counts: List[int]
        """

        self._value_counts = value_counts

    @property
    def time_names(self):
        """Gets the time_names of this Facet.

        Array of times.  # noqa: E501

        :return: The time_names of this Facet.
        :rtype: List[str]
        """
        return self._time_names

    @time_names.setter
    def time_names(self, time_names):
        """Sets the time_names of this Facet.

        Array of times.  # noqa: E501

        :param time_names: The time_names of this Facet.
        :type time_names: List[str]
        """

        self._time_names = time_names

    @property
    def time_series_value_counts(self):
        """Gets the time_series_value_counts of this Facet.

        2-dimensional array of facet value counts, indexed by time then value; indexes correspond to time_names and then value_names.   # noqa: E501

        :return: The time_series_value_counts of this Facet.
        :rtype: List[List[int]]
        """
        return self._time_series_value_counts

    @time_series_value_counts.setter
    def time_series_value_counts(self, time_series_value_counts):
        """Sets the time_series_value_counts of this Facet.

        2-dimensional array of facet value counts, indexed by time then value; indexes correspond to time_names and then value_names.   # noqa: E501

        :param time_series_value_counts: The time_series_value_counts of this Facet.
        :type time_series_value_counts: List[List[int]]
        """

        self._time_series_value_counts = time_series_value_counts
