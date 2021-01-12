# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    The network connection results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address:
            The value to assign to the address property of this Connection.
        :type address: str

        :param port:
            The value to assign to the port property of this Connection.
        :type port: int

        """
        self.swagger_types = {
            'address': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'address': 'address',
            'port': 'port'
        }

        self._address = None
        self._port = None

    @property
    def address(self):
        """
        Gets the address of this Connection.
        The connection IP address.


        :return: The address of this Connection.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Connection.
        The connection IP address.


        :param address: The address of this Connection.
        :type: str
        """
        self._address = address

    @property
    def port(self):
        """
        Gets the port of this Connection.
        The port.


        :return: The port of this Connection.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Connection.
        The port.


        :param port: The port of this Connection.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
