# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVaultDetails(object):
    """
    Note: Deprecated. Use the new resource model APIs instead.
    OCI Vault details to store migration and connection credentials secrets. An empty object would result in the removal of the stored details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateVaultDetails.
        :type compartment_id: str

        :param vault_id:
            The value to assign to the vault_id property of this UpdateVaultDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateVaultDetails.
        :type key_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'vault_id': 'str',
            'key_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'vault_id': 'vaultId',
            'key_id': 'keyId'
        }

        self._compartment_id = None
        self._vault_id = None
        self._key_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateVaultDetails.
        OCID of the compartment where the secret containing the credentials will be created.


        :return: The compartment_id of this UpdateVaultDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateVaultDetails.
        OCID of the compartment where the secret containing the credentials will be created.


        :param compartment_id: The compartment_id of this UpdateVaultDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this UpdateVaultDetails.
        OCID of the vault


        :return: The vault_id of this UpdateVaultDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this UpdateVaultDetails.
        OCID of the vault


        :param vault_id: The vault_id of this UpdateVaultDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this UpdateVaultDetails.
        OCID of the vault encryption key


        :return: The key_id of this UpdateVaultDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this UpdateVaultDetails.
        OCID of the vault encryption key


        :param key_id: The key_id of this UpdateVaultDetails.
        :type: str
        """
        self._key_id = key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
