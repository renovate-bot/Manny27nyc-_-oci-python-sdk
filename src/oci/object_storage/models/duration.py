# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Duration(object):
    """
    The amount of time that objects in the bucket should be preserved for and which is calculated in relation to
    each object's Last-Modified timestamp. If duration is not present, then there is no time limit and the objects
    in the bucket will be preserved indefinitely.
    """

    #: A constant which can be used with the time_unit property of a Duration.
    #: This constant has a value of "YEARS"
    TIME_UNIT_YEARS = "YEARS"

    #: A constant which can be used with the time_unit property of a Duration.
    #: This constant has a value of "DAYS"
    TIME_UNIT_DAYS = "DAYS"

    def __init__(self, **kwargs):
        """
        Initializes a new Duration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_amount:
            The value to assign to the time_amount property of this Duration.
        :type time_amount: int

        :param time_unit:
            The value to assign to the time_unit property of this Duration.
            Allowed values for this property are: "YEARS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_unit: str

        """
        self.swagger_types = {
            'time_amount': 'int',
            'time_unit': 'str'
        }

        self.attribute_map = {
            'time_amount': 'timeAmount',
            'time_unit': 'timeUnit'
        }

        self._time_amount = None
        self._time_unit = None

    @property
    def time_amount(self):
        """
        **[Required]** Gets the time_amount of this Duration.
        The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation
        to each object's Last-Modified timestamp.


        :return: The time_amount of this Duration.
        :rtype: int
        """
        return self._time_amount

    @time_amount.setter
    def time_amount(self, time_amount):
        """
        Sets the time_amount of this Duration.
        The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation
        to each object's Last-Modified timestamp.


        :param time_amount: The time_amount of this Duration.
        :type: int
        """
        self._time_amount = time_amount

    @property
    def time_unit(self):
        """
        **[Required]** Gets the time_unit of this Duration.
        The unit that should be used to interpret timeAmount.

        Allowed values for this property are: "YEARS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The time_unit of this Duration.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """
        Sets the time_unit of this Duration.
        The unit that should be used to interpret timeAmount.


        :param time_unit: The time_unit of this Duration.
        :type: str
        """
        allowed_values = ["YEARS", "DAYS"]
        if not value_allowed_none_or_none_sentinel(time_unit, allowed_values):
            time_unit = 'UNKNOWN_ENUM_VALUE'
        self._time_unit = time_unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
