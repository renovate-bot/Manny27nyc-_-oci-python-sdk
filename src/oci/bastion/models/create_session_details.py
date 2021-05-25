# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSessionDetails(object):
    """
    The configuration details for a new bastion session. A session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.
    """

    #: A constant which can be used with the key_type property of a CreateSessionDetails.
    #: This constant has a value of "PUB"
    KEY_TYPE_PUB = "PUB"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSessionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSessionDetails.
        :type display_name: str

        :param bastion_id:
            The value to assign to the bastion_id property of this CreateSessionDetails.
        :type bastion_id: str

        :param target_resource_details:
            The value to assign to the target_resource_details property of this CreateSessionDetails.
        :type target_resource_details: oci.bastion.models.CreateSessionTargetResourceDetails

        :param key_type:
            The value to assign to the key_type property of this CreateSessionDetails.
            Allowed values for this property are: "PUB"
        :type key_type: str

        :param key_details:
            The value to assign to the key_details property of this CreateSessionDetails.
        :type key_details: oci.bastion.models.PublicKeyDetails

        :param session_ttl_in_seconds:
            The value to assign to the session_ttl_in_seconds property of this CreateSessionDetails.
        :type session_ttl_in_seconds: int

        """
        self.swagger_types = {
            'display_name': 'str',
            'bastion_id': 'str',
            'target_resource_details': 'CreateSessionTargetResourceDetails',
            'key_type': 'str',
            'key_details': 'PublicKeyDetails',
            'session_ttl_in_seconds': 'int'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'bastion_id': 'bastionId',
            'target_resource_details': 'targetResourceDetails',
            'key_type': 'keyType',
            'key_details': 'keyDetails',
            'session_ttl_in_seconds': 'sessionTtlInSeconds'
        }

        self._display_name = None
        self._bastion_id = None
        self._target_resource_details = None
        self._key_type = None
        self._key_details = None
        self._session_ttl_in_seconds = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSessionDetails.
        The name of the session.


        :return: The display_name of this CreateSessionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSessionDetails.
        The name of the session.


        :param display_name: The display_name of this CreateSessionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def bastion_id(self):
        """
        **[Required]** Gets the bastion_id of this CreateSessionDetails.
        The unique identifier (OCID) of the bastion on which to create this session.


        :return: The bastion_id of this CreateSessionDetails.
        :rtype: str
        """
        return self._bastion_id

    @bastion_id.setter
    def bastion_id(self, bastion_id):
        """
        Sets the bastion_id of this CreateSessionDetails.
        The unique identifier (OCID) of the bastion on which to create this session.


        :param bastion_id: The bastion_id of this CreateSessionDetails.
        :type: str
        """
        self._bastion_id = bastion_id

    @property
    def target_resource_details(self):
        """
        **[Required]** Gets the target_resource_details of this CreateSessionDetails.

        :return: The target_resource_details of this CreateSessionDetails.
        :rtype: oci.bastion.models.CreateSessionTargetResourceDetails
        """
        return self._target_resource_details

    @target_resource_details.setter
    def target_resource_details(self, target_resource_details):
        """
        Sets the target_resource_details of this CreateSessionDetails.

        :param target_resource_details: The target_resource_details of this CreateSessionDetails.
        :type: oci.bastion.models.CreateSessionTargetResourceDetails
        """
        self._target_resource_details = target_resource_details

    @property
    def key_type(self):
        """
        Gets the key_type of this CreateSessionDetails.
        The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.

        Allowed values for this property are: "PUB"


        :return: The key_type of this CreateSessionDetails.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this CreateSessionDetails.
        The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.


        :param key_type: The key_type of this CreateSessionDetails.
        :type: str
        """
        allowed_values = ["PUB"]
        if not value_allowed_none_or_none_sentinel(key_type, allowed_values):
            raise ValueError(
                "Invalid value for `key_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._key_type = key_type

    @property
    def key_details(self):
        """
        **[Required]** Gets the key_details of this CreateSessionDetails.

        :return: The key_details of this CreateSessionDetails.
        :rtype: oci.bastion.models.PublicKeyDetails
        """
        return self._key_details

    @key_details.setter
    def key_details(self, key_details):
        """
        Sets the key_details of this CreateSessionDetails.

        :param key_details: The key_details of this CreateSessionDetails.
        :type: oci.bastion.models.PublicKeyDetails
        """
        self._key_details = key_details

    @property
    def session_ttl_in_seconds(self):
        """
        Gets the session_ttl_in_seconds of this CreateSessionDetails.
        The amount of time the session can remain active.


        :return: The session_ttl_in_seconds of this CreateSessionDetails.
        :rtype: int
        """
        return self._session_ttl_in_seconds

    @session_ttl_in_seconds.setter
    def session_ttl_in_seconds(self, session_ttl_in_seconds):
        """
        Sets the session_ttl_in_seconds of this CreateSessionDetails.
        The amount of time the session can remain active.


        :param session_ttl_in_seconds: The session_ttl_in_seconds of this CreateSessionDetails.
        :type: int
        """
        self._session_ttl_in_seconds = session_ttl_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
