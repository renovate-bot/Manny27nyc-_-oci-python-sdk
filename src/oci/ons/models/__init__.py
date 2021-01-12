# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .backoff_retry_policy import BackoffRetryPolicy
from .change_compartment_details import ChangeCompartmentDetails
from .confirmation_result import ConfirmationResult
from .create_subscription_details import CreateSubscriptionDetails
from .create_topic_details import CreateTopicDetails
from .delivery_policy import DeliveryPolicy
from .message_details import MessageDetails
from .notification_topic import NotificationTopic
from .notification_topic_summary import NotificationTopicSummary
from .publish_result import PublishResult
from .subscription import Subscription
from .subscription_summary import SubscriptionSummary
from .topic_attributes_details import TopicAttributesDetails
from .update_subscription_details import UpdateSubscriptionDetails

# Maps type names to classes for ons services.
ons_type_mapping = {
    "BackoffRetryPolicy": BackoffRetryPolicy,
    "ChangeCompartmentDetails": ChangeCompartmentDetails,
    "ConfirmationResult": ConfirmationResult,
    "CreateSubscriptionDetails": CreateSubscriptionDetails,
    "CreateTopicDetails": CreateTopicDetails,
    "DeliveryPolicy": DeliveryPolicy,
    "MessageDetails": MessageDetails,
    "NotificationTopic": NotificationTopic,
    "NotificationTopicSummary": NotificationTopicSummary,
    "PublishResult": PublishResult,
    "Subscription": Subscription,
    "SubscriptionSummary": SubscriptionSummary,
    "TopicAttributesDetails": TopicAttributesDetails,
    "UpdateSubscriptionDetails": UpdateSubscriptionDetails
}
