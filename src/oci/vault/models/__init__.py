# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .base64_secret_content_details import Base64SecretContentDetails
from .change_secret_compartment_details import ChangeSecretCompartmentDetails
from .create_secret_details import CreateSecretDetails
from .schedule_secret_deletion_details import ScheduleSecretDeletionDetails
from .schedule_secret_version_deletion_details import ScheduleSecretVersionDeletionDetails
from .secret import Secret
from .secret_content_details import SecretContentDetails
from .secret_expiry_rule import SecretExpiryRule
from .secret_reuse_rule import SecretReuseRule
from .secret_rule import SecretRule
from .secret_summary import SecretSummary
from .secret_version import SecretVersion
from .secret_version_summary import SecretVersionSummary
from .update_secret_details import UpdateSecretDetails

# Maps type names to classes for vault services.
vault_type_mapping = {
    "Base64SecretContentDetails": Base64SecretContentDetails,
    "ChangeSecretCompartmentDetails": ChangeSecretCompartmentDetails,
    "CreateSecretDetails": CreateSecretDetails,
    "ScheduleSecretDeletionDetails": ScheduleSecretDeletionDetails,
    "ScheduleSecretVersionDeletionDetails": ScheduleSecretVersionDeletionDetails,
    "Secret": Secret,
    "SecretContentDetails": SecretContentDetails,
    "SecretExpiryRule": SecretExpiryRule,
    "SecretReuseRule": SecretReuseRule,
    "SecretRule": SecretRule,
    "SecretSummary": SecretSummary,
    "SecretVersion": SecretVersion,
    "SecretVersionSummary": SecretVersionSummary,
    "UpdateSecretDetails": UpdateSecretDetails
}
