# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogEntry(object):
    """
    Contains the log content with the associated timestamp and ID. Each
    entry should be less than 1 MB size.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data:
            The value to assign to the data property of this LogEntry.
        :type data: str

        :param id:
            The value to assign to the id property of this LogEntry.
        :type id: str

        :param time:
            The value to assign to the time property of this LogEntry.
        :type time: datetime

        """
        self.swagger_types = {
            'data': 'str',
            'id': 'str',
            'time': 'datetime'
        }

        self.attribute_map = {
            'data': 'data',
            'id': 'id',
            'time': 'time'
        }

        self._data = None
        self._id = None
        self._time = None

    @property
    def data(self):
        """
        **[Required]** Gets the data of this LogEntry.
        The log entry content.


        :return: The data of this LogEntry.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this LogEntry.
        The log entry content.


        :param data: The data of this LogEntry.
        :type: str
        """
        self._data = data

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogEntry.
        UUID uniquely representing this logEntry. This is not an OCID related
        to any oracle resource.


        :return: The id of this LogEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogEntry.
        UUID uniquely representing this logEntry. This is not an OCID related
        to any oracle resource.


        :param id: The id of this LogEntry.
        :type: str
        """
        self._id = id

    @property
    def time(self):
        """
        Gets the time of this LogEntry.
        Optional. The timestamp associated with the log entry. An RFC3339-formatted date-time string with milliseconds precision.
        If unspecified, defaults to PutLogsDetails.defaultlogentrytime.


        :return: The time of this LogEntry.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this LogEntry.
        Optional. The timestamp associated with the log entry. An RFC3339-formatted date-time string with milliseconds precision.
        If unspecified, defaults to PutLogsDetails.defaultlogentrytime.


        :param time: The time of this LogEntry.
        :type: datetime
        """
        self._time = time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
