# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metric(object):
    """
    Metric and threshold details for triggering an autoscaling action.
    """

    #: A constant which can be used with the metric_type property of a Metric.
    #: This constant has a value of "CPU_UTILIZATION"
    METRIC_TYPE_CPU_UTILIZATION = "CPU_UTILIZATION"

    #: A constant which can be used with the metric_type property of a Metric.
    #: This constant has a value of "MEMORY_UTILIZATION"
    METRIC_TYPE_MEMORY_UTILIZATION = "MEMORY_UTILIZATION"

    def __init__(self, **kwargs):
        """
        Initializes a new Metric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_type:
            The value to assign to the metric_type property of this Metric.
            Allowed values for this property are: "CPU_UTILIZATION", "MEMORY_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_type: str

        :param threshold:
            The value to assign to the threshold property of this Metric.
        :type threshold: oci.autoscaling.models.Threshold

        """
        self.swagger_types = {
            'metric_type': 'str',
            'threshold': 'Threshold'
        }

        self.attribute_map = {
            'metric_type': 'metricType',
            'threshold': 'threshold'
        }

        self._metric_type = None
        self._threshold = None

    @property
    def metric_type(self):
        """
        **[Required]** Gets the metric_type of this Metric.
        Allowed values for this property are: "CPU_UTILIZATION", "MEMORY_UTILIZATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metric_type of this Metric.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this Metric.

        :param metric_type: The metric_type of this Metric.
        :type: str
        """
        allowed_values = ["CPU_UTILIZATION", "MEMORY_UTILIZATION"]
        if not value_allowed_none_or_none_sentinel(metric_type, allowed_values):
            metric_type = 'UNKNOWN_ENUM_VALUE'
        self._metric_type = metric_type

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this Metric.

        :return: The threshold of this Metric.
        :rtype: oci.autoscaling.models.Threshold
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this Metric.

        :param threshold: The threshold of this Metric.
        :type: oci.autoscaling.models.Threshold
        """
        self._threshold = threshold

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
