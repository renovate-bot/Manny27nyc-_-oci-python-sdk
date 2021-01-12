# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatisticAggregation(object):
    """
    SQL Statistics
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatisticAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlStatisticAggregation.
        :type sql_identifier: str

        :param database_details:
            The value to assign to the database_details property of this SqlStatisticAggregation.
        :type database_details: oci.opsi.models.DatabaseDetails

        :param category:
            The value to assign to the category property of this SqlStatisticAggregation.
        :type category: list[str]

        :param statistics:
            The value to assign to the statistics property of this SqlStatisticAggregation.
        :type statistics: oci.opsi.models.SqlStatistics

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'database_details': 'DatabaseDetails',
            'category': 'list[str]',
            'statistics': 'SqlStatistics'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'database_details': 'databaseDetails',
            'category': 'category',
            'statistics': 'statistics'
        }

        self._sql_identifier = None
        self._database_details = None
        self._category = None
        self._statistics = None

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlStatisticAggregation.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlStatisticAggregation.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlStatisticAggregation.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlStatisticAggregation.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def database_details(self):
        """
        **[Required]** Gets the database_details of this SqlStatisticAggregation.

        :return: The database_details of this SqlStatisticAggregation.
        :rtype: oci.opsi.models.DatabaseDetails
        """
        return self._database_details

    @database_details.setter
    def database_details(self, database_details):
        """
        Sets the database_details of this SqlStatisticAggregation.

        :param database_details: The database_details of this SqlStatisticAggregation.
        :type: oci.opsi.models.DatabaseDetails
        """
        self._database_details = database_details

    @property
    def category(self):
        """
        **[Required]** Gets the category of this SqlStatisticAggregation.
        SQL belongs to one or more categories based on the insights.


        :return: The category of this SqlStatisticAggregation.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SqlStatisticAggregation.
        SQL belongs to one or more categories based on the insights.


        :param category: The category of this SqlStatisticAggregation.
        :type: list[str]
        """
        self._category = category

    @property
    def statistics(self):
        """
        Gets the statistics of this SqlStatisticAggregation.

        :return: The statistics of this SqlStatisticAggregation.
        :rtype: oci.opsi.models.SqlStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SqlStatisticAggregation.

        :param statistics: The statistics of this SqlStatisticAggregation.
        :type: oci.opsi.models.SqlStatistics
        """
        self._statistics = statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
