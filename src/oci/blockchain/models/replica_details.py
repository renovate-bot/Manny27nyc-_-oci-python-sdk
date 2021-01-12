# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicaDetails(object):
    """
    Number of replicas of service components like Rest Proxy, CA and Console
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param proxy_count:
            The value to assign to the proxy_count property of this ReplicaDetails.
        :type proxy_count: int

        :param ca_count:
            The value to assign to the ca_count property of this ReplicaDetails.
        :type ca_count: int

        :param console_count:
            The value to assign to the console_count property of this ReplicaDetails.
        :type console_count: int

        """
        self.swagger_types = {
            'proxy_count': 'int',
            'ca_count': 'int',
            'console_count': 'int'
        }

        self.attribute_map = {
            'proxy_count': 'proxyCount',
            'ca_count': 'caCount',
            'console_count': 'consoleCount'
        }

        self._proxy_count = None
        self._ca_count = None
        self._console_count = None

    @property
    def proxy_count(self):
        """
        Gets the proxy_count of this ReplicaDetails.
        Number of REST proxy replicas


        :return: The proxy_count of this ReplicaDetails.
        :rtype: int
        """
        return self._proxy_count

    @proxy_count.setter
    def proxy_count(self, proxy_count):
        """
        Sets the proxy_count of this ReplicaDetails.
        Number of REST proxy replicas


        :param proxy_count: The proxy_count of this ReplicaDetails.
        :type: int
        """
        self._proxy_count = proxy_count

    @property
    def ca_count(self):
        """
        Gets the ca_count of this ReplicaDetails.
        Number of CA replicas


        :return: The ca_count of this ReplicaDetails.
        :rtype: int
        """
        return self._ca_count

    @ca_count.setter
    def ca_count(self, ca_count):
        """
        Sets the ca_count of this ReplicaDetails.
        Number of CA replicas


        :param ca_count: The ca_count of this ReplicaDetails.
        :type: int
        """
        self._ca_count = ca_count

    @property
    def console_count(self):
        """
        Gets the console_count of this ReplicaDetails.
        Number of console replicas


        :return: The console_count of this ReplicaDetails.
        :rtype: int
        """
        return self._console_count

    @console_count.setter
    def console_count(self, console_count):
        """
        Sets the console_count of this ReplicaDetails.
        Number of console replicas


        :param console_count: The console_count of this ReplicaDetails.
        :type: int
        """
        self._console_count = console_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
