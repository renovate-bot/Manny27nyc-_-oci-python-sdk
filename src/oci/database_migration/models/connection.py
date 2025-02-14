# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    Note: Deprecated. Use the new resource model APIs instead.
    Database Connection resource used for migrations.
    """

    #: A constant which can be used with the database_type property of a Connection.
    #: This constant has a value of "MANUAL"
    DATABASE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the database_type property of a Connection.
    #: This constant has a value of "AUTONOMOUS"
    DATABASE_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the database_type property of a Connection.
    #: This constant has a value of "USER_MANAGED_OCI"
    DATABASE_TYPE_USER_MANAGED_OCI = "USER_MANAGED_OCI"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Connection.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Connection.
        :type compartment_id: str

        :param database_type:
            The value to assign to the database_type property of this Connection.
            Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param display_name:
            The value to assign to the display_name property of this Connection.
        :type display_name: str

        :param database_id:
            The value to assign to the database_id property of this Connection.
        :type database_id: str

        :param connect_descriptor:
            The value to assign to the connect_descriptor property of this Connection.
        :type connect_descriptor: oci.database_migration.models.ConnectDescriptor

        :param credentials_secret_id:
            The value to assign to the credentials_secret_id property of this Connection.
        :type credentials_secret_id: str

        :param certificate_tdn:
            The value to assign to the certificate_tdn property of this Connection.
        :type certificate_tdn: str

        :param ssh_details:
            The value to assign to the ssh_details property of this Connection.
        :type ssh_details: oci.database_migration.models.SshDetails

        :param admin_credentials:
            The value to assign to the admin_credentials property of this Connection.
        :type admin_credentials: oci.database_migration.models.AdminCredentials

        :param private_endpoint:
            The value to assign to the private_endpoint property of this Connection.
        :type private_endpoint: oci.database_migration.models.PrivateEndpointDetails

        :param vault_details:
            The value to assign to the vault_details property of this Connection.
        :type vault_details: oci.database_migration.models.VaultDetails

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Connection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Connection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this Connection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Connection.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Connection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Connection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Connection.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'database_type': 'str',
            'display_name': 'str',
            'database_id': 'str',
            'connect_descriptor': 'ConnectDescriptor',
            'credentials_secret_id': 'str',
            'certificate_tdn': 'str',
            'ssh_details': 'SshDetails',
            'admin_credentials': 'AdminCredentials',
            'private_endpoint': 'PrivateEndpointDetails',
            'vault_details': 'VaultDetails',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'database_type': 'databaseType',
            'display_name': 'displayName',
            'database_id': 'databaseId',
            'connect_descriptor': 'connectDescriptor',
            'credentials_secret_id': 'credentialsSecretId',
            'certificate_tdn': 'certificateTdn',
            'ssh_details': 'sshDetails',
            'admin_credentials': 'adminCredentials',
            'private_endpoint': 'privateEndpoint',
            'vault_details': 'vaultDetails',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._database_type = None
        self._display_name = None
        self._database_id = None
        self._connect_descriptor = None
        self._credentials_secret_id = None
        self._certificate_tdn = None
        self._ssh_details = None
        self._admin_credentials = None
        self._private_endpoint = None
        self._vault_details = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Connection.
        The OCID of the resource


        :return: The id of this Connection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Connection.
        The OCID of the resource


        :param id: The id of this Connection.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Connection.
        OCID of the compartment


        :return: The compartment_id of this Connection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Connection.
        OCID of the compartment


        :param compartment_id: The compartment_id of this Connection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this Connection.
        Database connection type.

        Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this Connection.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this Connection.
        Database connection type.


        :param database_type: The database_type of this Connection.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Connection.
        Database Connection display name identifier.


        :return: The display_name of this Connection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Connection.
        Database Connection display name identifier.


        :param display_name: The display_name of this Connection.
        :type: str
        """
        self._display_name = display_name

    @property
    def database_id(self):
        """
        Gets the database_id of this Connection.
        The OCID of the cloud database.


        :return: The database_id of this Connection.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this Connection.
        The OCID of the cloud database.


        :param database_id: The database_id of this Connection.
        :type: str
        """
        self._database_id = database_id

    @property
    def connect_descriptor(self):
        """
        Gets the connect_descriptor of this Connection.

        :return: The connect_descriptor of this Connection.
        :rtype: oci.database_migration.models.ConnectDescriptor
        """
        return self._connect_descriptor

    @connect_descriptor.setter
    def connect_descriptor(self, connect_descriptor):
        """
        Sets the connect_descriptor of this Connection.

        :param connect_descriptor: The connect_descriptor of this Connection.
        :type: oci.database_migration.models.ConnectDescriptor
        """
        self._connect_descriptor = connect_descriptor

    @property
    def credentials_secret_id(self):
        """
        Gets the credentials_secret_id of this Connection.
        OCID of the Secret in the OCI vault containing the Database Connection credentials.


        :return: The credentials_secret_id of this Connection.
        :rtype: str
        """
        return self._credentials_secret_id

    @credentials_secret_id.setter
    def credentials_secret_id(self, credentials_secret_id):
        """
        Sets the credentials_secret_id of this Connection.
        OCID of the Secret in the OCI vault containing the Database Connection credentials.


        :param credentials_secret_id: The credentials_secret_id of this Connection.
        :type: str
        """
        self._credentials_secret_id = credentials_secret_id

    @property
    def certificate_tdn(self):
        """
        Gets the certificate_tdn of this Connection.
        This name is the distinguished name used while creating the certificate on target database.


        :return: The certificate_tdn of this Connection.
        :rtype: str
        """
        return self._certificate_tdn

    @certificate_tdn.setter
    def certificate_tdn(self, certificate_tdn):
        """
        Sets the certificate_tdn of this Connection.
        This name is the distinguished name used while creating the certificate on target database.


        :param certificate_tdn: The certificate_tdn of this Connection.
        :type: str
        """
        self._certificate_tdn = certificate_tdn

    @property
    def ssh_details(self):
        """
        Gets the ssh_details of this Connection.

        :return: The ssh_details of this Connection.
        :rtype: oci.database_migration.models.SshDetails
        """
        return self._ssh_details

    @ssh_details.setter
    def ssh_details(self, ssh_details):
        """
        Sets the ssh_details of this Connection.

        :param ssh_details: The ssh_details of this Connection.
        :type: oci.database_migration.models.SshDetails
        """
        self._ssh_details = ssh_details

    @property
    def admin_credentials(self):
        """
        Gets the admin_credentials of this Connection.

        :return: The admin_credentials of this Connection.
        :rtype: oci.database_migration.models.AdminCredentials
        """
        return self._admin_credentials

    @admin_credentials.setter
    def admin_credentials(self, admin_credentials):
        """
        Sets the admin_credentials of this Connection.

        :param admin_credentials: The admin_credentials of this Connection.
        :type: oci.database_migration.models.AdminCredentials
        """
        self._admin_credentials = admin_credentials

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this Connection.

        :return: The private_endpoint of this Connection.
        :rtype: oci.database_migration.models.PrivateEndpointDetails
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this Connection.

        :param private_endpoint: The private_endpoint of this Connection.
        :type: oci.database_migration.models.PrivateEndpointDetails
        """
        self._private_endpoint = private_endpoint

    @property
    def vault_details(self):
        """
        Gets the vault_details of this Connection.

        :return: The vault_details of this Connection.
        :rtype: oci.database_migration.models.VaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this Connection.

        :param vault_details: The vault_details of this Connection.
        :type: oci.database_migration.models.VaultDetails
        """
        self._vault_details = vault_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Connection.
        The current state of the Connection resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Connection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Connection.
        The current state of the Connection resource.


        :param lifecycle_state: The lifecycle_state of this Connection.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Connection.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :return: The lifecycle_details of this Connection.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Connection.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Connection.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Connection.
        The time the Connection resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Connection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Connection.
        The time the Connection resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Connection.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Connection.
        The time of the last Connection resource details update. An RFC3339 formatted datetime string.


        :return: The time_updated of this Connection.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Connection.
        The time of the last Connection resource details update. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Connection.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Connection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Connection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Connection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Connection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Connection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Connection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Connection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Connection.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Connection.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Connection.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
