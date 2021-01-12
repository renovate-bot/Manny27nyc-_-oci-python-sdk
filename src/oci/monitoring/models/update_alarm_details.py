# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAlarmDetails(object):
    """
    The configuration details for updating an alarm.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAlarmDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAlarmDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateAlarmDetails.
        :type compartment_id: str

        :param metric_compartment_id:
            The value to assign to the metric_compartment_id property of this UpdateAlarmDetails.
        :type metric_compartment_id: str

        :param metric_compartment_id_in_subtree:
            The value to assign to the metric_compartment_id_in_subtree property of this UpdateAlarmDetails.
        :type metric_compartment_id_in_subtree: bool

        :param namespace:
            The value to assign to the namespace property of this UpdateAlarmDetails.
        :type namespace: str

        :param resource_group:
            The value to assign to the resource_group property of this UpdateAlarmDetails.
        :type resource_group: str

        :param query:
            The value to assign to the query property of this UpdateAlarmDetails.
        :type query: str

        :param resolution:
            The value to assign to the resolution property of this UpdateAlarmDetails.
        :type resolution: str

        :param pending_duration:
            The value to assign to the pending_duration property of this UpdateAlarmDetails.
        :type pending_duration: str

        :param severity:
            The value to assign to the severity property of this UpdateAlarmDetails.
        :type severity: str

        :param body:
            The value to assign to the body property of this UpdateAlarmDetails.
        :type body: str

        :param destinations:
            The value to assign to the destinations property of this UpdateAlarmDetails.
        :type destinations: list[str]

        :param repeat_notification_duration:
            The value to assign to the repeat_notification_duration property of this UpdateAlarmDetails.
        :type repeat_notification_duration: str

        :param suppression:
            The value to assign to the suppression property of this UpdateAlarmDetails.
        :type suppression: oci.monitoring.models.Suppression

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateAlarmDetails.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAlarmDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAlarmDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'metric_compartment_id': 'str',
            'metric_compartment_id_in_subtree': 'bool',
            'namespace': 'str',
            'resource_group': 'str',
            'query': 'str',
            'resolution': 'str',
            'pending_duration': 'str',
            'severity': 'str',
            'body': 'str',
            'destinations': 'list[str]',
            'repeat_notification_duration': 'str',
            'suppression': 'Suppression',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'metric_compartment_id': 'metricCompartmentId',
            'metric_compartment_id_in_subtree': 'metricCompartmentIdInSubtree',
            'namespace': 'namespace',
            'resource_group': 'resourceGroup',
            'query': 'query',
            'resolution': 'resolution',
            'pending_duration': 'pendingDuration',
            'severity': 'severity',
            'body': 'body',
            'destinations': 'destinations',
            'repeat_notification_duration': 'repeatNotificationDuration',
            'suppression': 'suppression',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._metric_compartment_id = None
        self._metric_compartment_id_in_subtree = None
        self._namespace = None
        self._resource_group = None
        self._query = None
        self._resolution = None
        self._pending_duration = None
        self._severity = None
        self._body = None
        self._destinations = None
        self._repeat_notification_duration = None
        self._suppression = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAlarmDetails.
        A user-friendly name for the alarm. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        This name is sent as the title for notifications related to this alarm.

        Example: `High CPU Utilization`


        :return: The display_name of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAlarmDetails.
        A user-friendly name for the alarm. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        This name is sent as the title for notifications related to this alarm.

        Example: `High CPU Utilization`


        :param display_name: The display_name of this UpdateAlarmDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateAlarmDetails.
        The `OCID`__ of the compartment containing the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateAlarmDetails.
        The `OCID`__ of the compartment containing the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this UpdateAlarmDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metric_compartment_id(self):
        """
        Gets the metric_compartment_id of this UpdateAlarmDetails.
        The `OCID`__ of the compartment containing the metric
        being evaluated by the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The metric_compartment_id of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._metric_compartment_id

    @metric_compartment_id.setter
    def metric_compartment_id(self, metric_compartment_id):
        """
        Sets the metric_compartment_id of this UpdateAlarmDetails.
        The `OCID`__ of the compartment containing the metric
        being evaluated by the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param metric_compartment_id: The metric_compartment_id of this UpdateAlarmDetails.
        :type: str
        """
        self._metric_compartment_id = metric_compartment_id

    @property
    def metric_compartment_id_in_subtree(self):
        """
        Gets the metric_compartment_id_in_subtree of this UpdateAlarmDetails.
        When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can
        only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment).
        A true value requires the user to have tenancy-level permissions. If this requirement is not met,
        then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified
        in metricCompartmentId. Default is false.

        Example: `true`


        :return: The metric_compartment_id_in_subtree of this UpdateAlarmDetails.
        :rtype: bool
        """
        return self._metric_compartment_id_in_subtree

    @metric_compartment_id_in_subtree.setter
    def metric_compartment_id_in_subtree(self, metric_compartment_id_in_subtree):
        """
        Sets the metric_compartment_id_in_subtree of this UpdateAlarmDetails.
        When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can
        only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment).
        A true value requires the user to have tenancy-level permissions. If this requirement is not met,
        then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified
        in metricCompartmentId. Default is false.

        Example: `true`


        :param metric_compartment_id_in_subtree: The metric_compartment_id_in_subtree of this UpdateAlarmDetails.
        :type: bool
        """
        self._metric_compartment_id_in_subtree = metric_compartment_id_in_subtree

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateAlarmDetails.
        The source service or application emitting the metric that is evaluated by the alarm.

        Example: `oci_computeagent`


        :return: The namespace of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateAlarmDetails.
        The source service or application emitting the metric that is evaluated by the alarm.

        Example: `oci_computeagent`


        :param namespace: The namespace of this UpdateAlarmDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group(self):
        """
        Gets the resource_group of this UpdateAlarmDetails.
        Resource group that you want to use as a filter. The alarm retrieves metric data associated with the specified resource group only. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :return: The resource_group of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this UpdateAlarmDetails.
        Resource group that you want to use as a filter. The alarm retrieves metric data associated with the specified resource group only. Only one resource group can be applied per metric.
        A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
        Avoid entering confidential information.

        Example: `frontend-fleet`


        :param resource_group: The resource_group of this UpdateAlarmDetails.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def query(self):
        """
        Gets the query of this UpdateAlarmDetails.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally
        specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.
        For details about Monitoring Query Language (MQL), see `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :return: The query of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this UpdateAlarmDetails.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally
        specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.
        For details about Monitoring Query Language (MQL), see `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :param query: The query of this UpdateAlarmDetails.
        :type: str
        """
        self._query = query

    @property
    def resolution(self):
        """
        Gets the resolution of this UpdateAlarmDetails.
        The time between calculated aggregation windows for the alarm. Supported value: `1m`


        :return: The resolution of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this UpdateAlarmDetails.
        The time between calculated aggregation windows for the alarm. Supported value: `1m`


        :param resolution: The resolution of this UpdateAlarmDetails.
        :type: str
        """
        self._resolution = resolution

    @property
    def pending_duration(self):
        """
        Gets the pending_duration of this UpdateAlarmDetails.
        The period of time that the condition defined in the alarm must persist before the alarm state
        changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the
        alarm must persist in breaching the condition for five minutes before the alarm updates its
        state to \"FIRING\".

        The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
        for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

        Under the default value of PT1M, the first evaluation that breaches the alarm updates the
        state to \"FIRING\".

        The alarm updates its status to \"OK\" when the breaching condition has been clear for
        the most recent minute.

        Example: `PT5M`


        :return: The pending_duration of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        """
        Sets the pending_duration of this UpdateAlarmDetails.
        The period of time that the condition defined in the alarm must persist before the alarm state
        changes from \"OK\" to \"FIRING\". For example, a value of 5 minutes means that the
        alarm must persist in breaching the condition for five minutes before the alarm updates its
        state to \"FIRING\".

        The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
        for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

        Under the default value of PT1M, the first evaluation that breaches the alarm updates the
        state to \"FIRING\".

        The alarm updates its status to \"OK\" when the breaching condition has been clear for
        the most recent minute.

        Example: `PT5M`


        :param pending_duration: The pending_duration of this UpdateAlarmDetails.
        :type: str
        """
        self._pending_duration = pending_duration

    @property
    def severity(self):
        """
        Gets the severity of this UpdateAlarmDetails.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`


        :return: The severity of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this UpdateAlarmDetails.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`


        :param severity: The severity of this UpdateAlarmDetails.
        :type: str
        """
        self._severity = severity

    @property
    def body(self):
        """
        Gets the body of this UpdateAlarmDetails.
        The human-readable content of the notification delivered. Oracle recommends providing guidance
        to operators for resolving the alarm condition. Consider adding links to standard runbook
        practices. Avoid entering confidential information.

        Example: `High CPU usage alert. Follow runbook instructions for resolution.`


        :return: The body of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this UpdateAlarmDetails.
        The human-readable content of the notification delivered. Oracle recommends providing guidance
        to operators for resolving the alarm condition. Consider adding links to standard runbook
        practices. Avoid entering confidential information.

        Example: `High CPU usage alert. Follow runbook instructions for resolution.`


        :param body: The body of this UpdateAlarmDetails.
        :type: str
        """
        self._body = body

    @property
    def destinations(self):
        """
        Gets the destinations of this UpdateAlarmDetails.
        A list of destinations to which the notifications for this alarm will be delivered.
        Each destination is represented by an `OCID`__ related to the supported destination service.
        For example, a destination using the Notifications service is represented by a topic OCID.
        Supported destination services: Notifications Service. Limit: One destination per supported destination service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The destinations of this UpdateAlarmDetails.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this UpdateAlarmDetails.
        A list of destinations to which the notifications for this alarm will be delivered.
        Each destination is represented by an `OCID`__ related to the supported destination service.
        For example, a destination using the Notifications service is represented by a topic OCID.
        Supported destination services: Notifications Service. Limit: One destination per supported destination service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param destinations: The destinations of this UpdateAlarmDetails.
        :type: list[str]
        """
        self._destinations = destinations

    @property
    def repeat_notification_duration(self):
        """
        Gets the repeat_notification_duration of this UpdateAlarmDetails.
        The frequency at which notifications are re-submitted, if the alarm keeps firing without
        interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours.
        Minimum: PT1M. Maximum: P30D.

        Default value: null (notifications are not re-submitted).

        Example: `PT2H`


        :return: The repeat_notification_duration of this UpdateAlarmDetails.
        :rtype: str
        """
        return self._repeat_notification_duration

    @repeat_notification_duration.setter
    def repeat_notification_duration(self, repeat_notification_duration):
        """
        Sets the repeat_notification_duration of this UpdateAlarmDetails.
        The frequency at which notifications are re-submitted, if the alarm keeps firing without
        interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours.
        Minimum: PT1M. Maximum: P30D.

        Default value: null (notifications are not re-submitted).

        Example: `PT2H`


        :param repeat_notification_duration: The repeat_notification_duration of this UpdateAlarmDetails.
        :type: str
        """
        self._repeat_notification_duration = repeat_notification_duration

    @property
    def suppression(self):
        """
        Gets the suppression of this UpdateAlarmDetails.
        The configuration details for suppressing an alarm.


        :return: The suppression of this UpdateAlarmDetails.
        :rtype: oci.monitoring.models.Suppression
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        """
        Sets the suppression of this UpdateAlarmDetails.
        The configuration details for suppressing an alarm.


        :param suppression: The suppression of this UpdateAlarmDetails.
        :type: oci.monitoring.models.Suppression
        """
        self._suppression = suppression

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateAlarmDetails.
        Whether the alarm is enabled.

        Example: `true`


        :return: The is_enabled of this UpdateAlarmDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateAlarmDetails.
        Whether the alarm is enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this UpdateAlarmDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAlarmDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this UpdateAlarmDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAlarmDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this UpdateAlarmDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAlarmDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this UpdateAlarmDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAlarmDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this UpdateAlarmDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
