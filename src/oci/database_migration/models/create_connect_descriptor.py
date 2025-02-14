# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectDescriptor(object):
    """
    Note: Deprecated. Use the new resource model APIs instead.
    Connect Descriptor details. Required for Manual and UserManagerOci connection types.
    If a Private Endpoint was specified for the Connection, the host should contain a valid IP address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectDescriptor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this CreateConnectDescriptor.
        :type host: str

        :param port:
            The value to assign to the port property of this CreateConnectDescriptor.
        :type port: int

        :param database_service_name:
            The value to assign to the database_service_name property of this CreateConnectDescriptor.
        :type database_service_name: str

        :param connect_string:
            The value to assign to the connect_string property of this CreateConnectDescriptor.
        :type connect_string: str

        """
        self.swagger_types = {
            'host': 'str',
            'port': 'int',
            'database_service_name': 'str',
            'connect_string': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port',
            'database_service_name': 'databaseServiceName',
            'connect_string': 'connectString'
        }

        self._host = None
        self._port = None
        self._database_service_name = None
        self._connect_string = None

    @property
    def host(self):
        """
        Gets the host of this CreateConnectDescriptor.
        Host or IP address of the connect descriptor. Required if no connectString was specified.


        :return: The host of this CreateConnectDescriptor.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this CreateConnectDescriptor.
        Host or IP address of the connect descriptor. Required if no connectString was specified.


        :param host: The host of this CreateConnectDescriptor.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this CreateConnectDescriptor.
        Port of the connect descriptor. Required if no connectString was specified.


        :return: The port of this CreateConnectDescriptor.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateConnectDescriptor.
        Port of the connect descriptor. Required if no connectString was specified.


        :param port: The port of this CreateConnectDescriptor.
        :type: int
        """
        self._port = port

    @property
    def database_service_name(self):
        """
        Gets the database_service_name of this CreateConnectDescriptor.
        Database service name. Required if no connectString was specified.


        :return: The database_service_name of this CreateConnectDescriptor.
        :rtype: str
        """
        return self._database_service_name

    @database_service_name.setter
    def database_service_name(self, database_service_name):
        """
        Sets the database_service_name of this CreateConnectDescriptor.
        Database service name. Required if no connectString was specified.


        :param database_service_name: The database_service_name of this CreateConnectDescriptor.
        :type: str
        """
        self._database_service_name = database_service_name

    @property
    def connect_string(self):
        """
        Gets the connect_string of this CreateConnectDescriptor.
        Connect String. Required if no host, port nor databaseServiceName were specified.
        If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address.
        Supported formats:
        Easy connect: <host>:<port>/<db_service_name>
        Long format: (description= (address=(port=<port>)(host=<host>))(connect_data=(service_name=<db_service_name>)))


        :return: The connect_string of this CreateConnectDescriptor.
        :rtype: str
        """
        return self._connect_string

    @connect_string.setter
    def connect_string(self, connect_string):
        """
        Sets the connect_string of this CreateConnectDescriptor.
        Connect String. Required if no host, port nor databaseServiceName were specified.
        If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address.
        Supported formats:
        Easy connect: <host>:<port>/<db_service_name>
        Long format: (description= (address=(port=<port>)(host=<host>))(connect_data=(service_name=<db_service_name>)))


        :param connect_string: The connect_string of this CreateConnectDescriptor.
        :type: str
        """
        self._connect_string = connect_string

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
