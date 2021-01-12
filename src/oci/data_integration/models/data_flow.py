# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataFlow(object):
    """
    The data flow type contains the audit summary information and the definition of the data flow.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataFlow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DataFlow.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this DataFlow.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this DataFlow.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DataFlow.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this DataFlow.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this DataFlow.
        :type identifier: str

        :param object_version:
            The value to assign to the object_version property of this DataFlow.
        :type object_version: int

        :param nodes:
            The value to assign to the nodes property of this DataFlow.
        :type nodes: list[oci.data_integration.models.FlowNode]

        :param parameters:
            The value to assign to the parameters property of this DataFlow.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param description:
            The value to assign to the description property of this DataFlow.
        :type description: str

        :param flow_config_values:
            The value to assign to the flow_config_values property of this DataFlow.
        :type flow_config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this DataFlow.
        :type object_status: int

        :param metadata:
            The value to assign to the metadata property of this DataFlow.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this DataFlow.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'identifier': 'str',
            'object_version': 'int',
            'nodes': 'list[FlowNode]',
            'parameters': 'list[Parameter]',
            'description': 'str',
            'flow_config_values': 'ConfigValues',
            'object_status': 'int',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'identifier': 'identifier',
            'object_version': 'objectVersion',
            'nodes': 'nodes',
            'parameters': 'parameters',
            'description': 'description',
            'flow_config_values': 'flowConfigValues',
            'object_status': 'objectStatus',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._identifier = None
        self._object_version = None
        self._nodes = None
        self._parameters = None
        self._description = None
        self._flow_config_values = None
        self._object_status = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this DataFlow.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :return: The key of this DataFlow.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataFlow.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :param key: The key of this DataFlow.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this DataFlow.
        The type of the object.


        :return: The model_type of this DataFlow.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataFlow.
        The type of the object.


        :param model_type: The model_type of this DataFlow.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this DataFlow.
        The model version of an object.


        :return: The model_version of this DataFlow.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataFlow.
        The model version of an object.


        :param model_version: The model_version of this DataFlow.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DataFlow.

        :return: The parent_ref of this DataFlow.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DataFlow.

        :param parent_ref: The parent_ref of this DataFlow.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this DataFlow.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DataFlow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataFlow.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DataFlow.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this DataFlow.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataFlow.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataFlow.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataFlow.
        :type: str
        """
        self._identifier = identifier

    @property
    def object_version(self):
        """
        Gets the object_version of this DataFlow.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataFlow.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataFlow.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataFlow.
        :type: int
        """
        self._object_version = object_version

    @property
    def nodes(self):
        """
        Gets the nodes of this DataFlow.
        An array of nodes.


        :return: The nodes of this DataFlow.
        :rtype: list[oci.data_integration.models.FlowNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this DataFlow.
        An array of nodes.


        :param nodes: The nodes of this DataFlow.
        :type: list[oci.data_integration.models.FlowNode]
        """
        self._nodes = nodes

    @property
    def parameters(self):
        """
        Gets the parameters of this DataFlow.
        An array of parameters.


        :return: The parameters of this DataFlow.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this DataFlow.
        An array of parameters.


        :param parameters: The parameters of this DataFlow.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def description(self):
        """
        Gets the description of this DataFlow.
        Detailed description for the object.


        :return: The description of this DataFlow.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataFlow.
        Detailed description for the object.


        :param description: The description of this DataFlow.
        :type: str
        """
        self._description = description

    @property
    def flow_config_values(self):
        """
        Gets the flow_config_values of this DataFlow.

        :return: The flow_config_values of this DataFlow.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._flow_config_values

    @flow_config_values.setter
    def flow_config_values(self, flow_config_values):
        """
        Sets the flow_config_values of this DataFlow.

        :param flow_config_values: The flow_config_values of this DataFlow.
        :type: oci.data_integration.models.ConfigValues
        """
        self._flow_config_values = flow_config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this DataFlow.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataFlow.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataFlow.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataFlow.
        :type: int
        """
        self._object_status = object_status

    @property
    def metadata(self):
        """
        Gets the metadata of this DataFlow.

        :return: The metadata of this DataFlow.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DataFlow.

        :param metadata: The metadata of this DataFlow.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this DataFlow.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this DataFlow.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this DataFlow.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this DataFlow.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
