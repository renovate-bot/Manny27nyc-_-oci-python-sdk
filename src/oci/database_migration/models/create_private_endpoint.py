# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateEndpoint(object):
    """
    Note: Deprecated. Use the new resource model APIs instead.
    OCI Private Endpoint configuration details.
    Not required for source container database connections, it will default to the specified Source Database Connection Private Endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePrivateEndpoint.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreatePrivateEndpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreatePrivateEndpoint.
        :type subnet_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId'
        }

        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePrivateEndpoint.
        The `OCID`__ of the compartment to contain the
        private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreatePrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePrivateEndpoint.
        The `OCID`__ of the compartment to contain the
        private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreatePrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreatePrivateEndpoint.
        The `OCID`__ of the VCN where the Private Endpoint will be bound to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this CreatePrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreatePrivateEndpoint.
        The `OCID`__ of the VCN where the Private Endpoint will be bound to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this CreatePrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreatePrivateEndpoint.
        The `OCID`__ of the customer's subnet where the private endpoint VNIC
        will reside.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreatePrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreatePrivateEndpoint.
        The `OCID`__ of the customer's subnet where the private endpoint VNIC
        will reside.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreatePrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
