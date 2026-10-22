---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-adapters/
title: TIPCommon.adapters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:09.389057+00:00
---

# TIPCommon.adapters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-adapters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.adapters

## _class_ TIPCommon.adapters.pubsub.pubsub.PubSubAdapter

_class_ `TIPCommon.adapters.pubsub.pubsub.PubSubAdapter(session, project_id=None, logger=None, region=None)`

Bases: `object`

Adapter class for managing Google Cloud project Pub/Sub topics and subscriptions.

### ack

`ack(sub_name, ack_ids)`

Acknowledges the messages associated with the `ackIds` in the `AcknowledgeRequest` response returned from `PubSubAdapter.pull()`.

Parameters  
---  
`sub_name` | `str`The subscription name.  
`ack_ids` | `list[str]` A list of acknowledgment IDs for the messages being acknowledged. The list is returned by the Pub/Sub system in the `PubSubAdapter.pull()` response.  
  
### _static_ build_pubsub_message

_static_ `build_pubsub_message(message_content, encoding='utf-8', ordering_key=None, **attr)`

Creates a `PubSubMessage` object.

Parameters  
---  
`message_content` | `str` The message content.  
`encoding` | `str` The encoding type to encode or decode the message text. The default value is `UTF-8`.  
`ordering_key` | `str` Optional. If configured, the parameter identifies all related messages that must follow the publish order.  
`**attr` | `str` Optional. The attributes to pass as message object attributes.  
  
#### Returns

A `TIPCommon.adapters.pubsub.PubSubMessage` object.

#### Return type

`PubSubMessage`

### create_subscription

`create_subscription(sub_name, topic, **attr)`

Creates a Pub/Sub subscription for the specified topic.

Parameters  
---  
`sub_name` | `str` The subscription name.  
`topic` | `str` A Pub/Sub topic name to create the subscription for.  
`**attr` | Additional parameters to pass on to the subscription request.  
  
#### Returns

`TIPCommon.adapters.pubsub.Subscription` object of the created subscription.

#### Return type

`Subscription`

### create_topic

`create_topic(topic_name)`

Creates a Pub/Sub topic in a Google Cloud project.

Parameters  
---  
`topic_name` | `str` The name of the topic. The name must correspond to Google Cloud [resource name rules](https://docs.cloud.google.com/pubsub/docs/admin#resource_names).  
  
#### Returns

`TIPCommon.adapters.pubsub.Topic` object of the created topic.

#### Return type

`Topic`

### delete_subscription

`delete_subscription(sub_name)`

Deletes a Pub/Sub subscription from a Google Cloud project.

Parameters  
---  
`sub_name` | `str` The subscription name to remove.  
  
### delete_topic

`delete_topic(topic_name)`

Deletes a Pub/Sub topic from a Google Cloud project.

Parameters  
---  
`topic_name` | `str`The topic to remove.  
  
### _static_ from_credentials

_static_ `from_credentials(credentials, project_id=None, verify_ssl=True, quota_project=None, logger=None, region=None)`

Creates a `PubSubAdapter` object from a `google.oauth2.credentials.Credentials` object.

Parameters  
---  
`credentials` | `google.oauth2.credentials.Credentials` A `google.oauth2.credentials.Credentials` object.  
`project_id` | Optional.`str` The Google Cloud project ID. If not provided, the function attempts to use the project configured in the credentials object by default.  
`verify_ssl` | Optional.`bool` Specifies whether SSL certificate verification is enabled for HTTP sessions.  
`quota_project` | Optional.`str` The project to use for quota and billing.  
`logger` | Optional.`SiemplifyLogger` A `SiemplifyLogger` object.  
`region` | `str` The region for Pub/Sub to work in.  
  
#### Returns

A `PubSubAdapter` object.

#### Return type

`PubSubAdapter`

### _static_ from_service_account_info

_static_ `subscription_name(user_service_account, project_id=None, verify_ssl=True, quota_project=None, logger=None)`

Creates a `PubSubAdapter` object from a `service_account` JSON.

Parameters  
---  
`user_service_account` | `str` The Google Cloud Service Account JSON in text format.  
`project_id` | Optional.`str` The Google Cloud project ID. If not provided, the function attempts to use the project configured in the credentials object by default.  
`verify_ssl` | Optional.`bool` Specifies whether SSL certificate verification is enabled for HTTP sessions.  
`quota_project` | Optional.`str` The project to use for quota and billing.  
`logger` | Optional.`SiemplifyLogger` A `SiemplifyLogger` object.  
  
#### Returns

A `PubSubAdapter` object.

#### Return type

`PubSubAdapter`

### get_subscription

`get_subscription(sub_name, topic=None, create_if_not_exist=False, **attr)`

Retrieves a Pub/Sub subscription.

Parameters  
---  
`sub_name` | `str` The subscription name.  
`topic` | `str` A Pub/Sub topic name to create a subscription for. Mandatory if `create_if_not_exist` is `True`.  
`create_if_not_exist` | Creates the Pub/Sub subscription in Google Cloud if it doesn't exist.  
`**attr` | Additional parameters to pass to the subscription creation request.   
  
#### Returns

The `TIPCommon.adapters.pubsub.Subscription` object of the retrieved subscription.

#### Return type

`Subscription`

### get_topic

`get_topic(topic_name, create_if_not_exist=False)`

Retrieves a Pub/Sub topic object from the configured Google Cloud project.

Parameters  
---  
`topic_name` | `str`Name of the topic (simplified, without the `projects/``PROJECT_ID``/topics/` prefix).  
`create_if_not_exist` | `bool`Creates the Pub/Sub topic in Google Cloud if it doesn't exist.  
  
#### Returns

The `TIPCommon.adapters.pubsub.Topic` object of the received topic.

#### Return type

`Topic`

### patch_subscription

`patch_subscription(sub_name, topic_name, push_config=None, bigquery_config=None, cloud_storage_config=None, ack_deadline_seconds=None, retain_acked_messages=None, retention_duration=None, labels=None, enable_message_ordering=None, expiration_policy=None, query_filter=None, dead_letter_policy=None, return_policy=None, detached=None, enable_once_delivery=None)`

Updates an existing subscription.

**Note:** Certain subscription properties are unmodifiable.Parameters  
---  
`sub_name` | `str`The subscription name.  
`topic_name` | `str`The name of the topic from which the subscription receives messages.  
`push_config` | `dict`Optional. Configuration for a push delivery endpoint.  
`bigquery_config` | `dict`Optional. Configuration for a BigQuery subscription.  
`cloud_storage_config` | `dict`Optional. Configuration for a Cloud Storage subscription.  
`ack_deadline_seconds` | `int`Optional. The approximate amount of time Pub/Sub waits for the subscriber to acknowledge a received message before the message is redelivered.  
`retain_acked_messages` | `bool`Optional. Indicates whether to retain acknowledged messages.  
`retention_duration` | `str`Optional. The amount of time to retain unacknowledged messages in the subscription's backlog, from the moment a message is published.  
`labels` | `dict`Optional. A set of key-value pairs used to organize the subscription.  
`enable_message_ordering` | `bool`Optional. If `True`, messages published with the same `ordering_key` in `PubsubMessage` are delivered in the order in which they are received by the Pub/Sub system.  
`expiration_policy` | `dict`Optional. Policy specifying the conditions for this subscription's expiration.  
`query_filter` | `str`Optional. An expression written in the Pub/Sub filter language that specifies which messages are delivered to the subscription.  
`dead_letter_policy` | `dict`Optional. A policy that specifies the conditions for dead-lettering messages in this subscription.  
`return_policy` | `dict`Optional. Policy specifying the conditions for returning messages.  
`detached` | `bool`Optional. Indicates whether the subscription is detached from the topic.  
`enable_once_delivery` | `bool`Optional. If `True`, Pub/Sub provides "exactly-once delivery" for messages in this subscription.  
  
#### Returns

The `TIPCommon.adapters.pubsub.Subscription` object of the received subscription.

#### Return type

`Subscription`

### patch_topic

`patch_topic(topic_name, labels=None, message_storage_policy=None, kms_key_name=None, schema_settings=None, satisfies_pzs=None, retention_duration=None)`

Updates an existing topic.

**Note:** Certain topic properties are unmodifiable.Parameters  
---  
`topic_name` | `str`The topic name.  
`labels` | `dict`Optional. A set of key-value pairs used to organize the topic.  
`message_storage_policy` | `dict`Optional. Policy constraining the regions in which messages are stored at rest.  
`kms_key_name` | `str`Optional. The resource name of the Cloud Key Management Service CryptoKey to be used to protect messages published to this topic.  
`schema_settings` | `dict`Optional. Settings for validating messages published against a schema.  
`satisfies_pzs` | `bool`Optional. Reserved for future use. This field is set to `True` if the topic satisfies physical zone separation.  
`retention_duration` | `str`Optional. The amount of time a published message is retained by the topic. If configured, the message will be retained for this duration, regardless of any subscription configurations.  
  
#### Returns

The `TIPCommon.adapters.pubsub.Topic` object of the received topic.

#### Return type

`Topic`

### publish

`publish(topic_name, messages)`

Publishes a list of `PubSubMessage` objects to a topic.

Parameters  
---  
`topic_name` | `str`The name of the target topic for the message publication.  
`messages` | `list`A list containing `PubSubMessage` objects.The `PubSubAdapter.build_message()` static method is used to construct these objects.  
  
#### Returns

A list of message IDs.

#### Return type

`list[str]`

### pull

`pull(sub_name, limit, timeout=60, encoding='utf-8')`

Pulls messages from Pub/Sub subscriptions.

Parameters  
---  
`sub_name` | `str`The subscription name.  
`limit` | `int`The maximum number of messages to return for this request.  
`timeout` | `int`The HTTP request timeout, in seconds. The default value is `60`.  
`encoding` | `str`A Pub/Sub message encoding. The default value is `utf-8`.  
  
#### Returns

A list of `TIPCommon.adapters.pubsub.ReceivedMessage` objects.

#### Return type

`ReceivedMessage`

### _static_ subscription_name

_static_ `subscription_name(project_id, sub_name)`

Retrieves the full subscription name in the following format: `projects/project_id/topics/topic_name`.

Parameters  
---  
`project_id` | `str`The project name that contains the resource.  
`sub_name` | `str`A Pub/Sub subscription name.  
  
#### Returns

The full subscription name in the following format: `projects/project_id/topics/topic_name`.

#### Return type

`str`

### _static_ topic_name

_static_ `topic_name(project_id, topic)`

Retrieves a full topic name in the following format: `projects/project_id/topics/topic_name`.

Parameters  
---  
`project_id` | `str`The project name containing the resource.  
`topic` | `str`A Pub/Sub topic name.  
  
#### Returns

A full topic name: `projects/project_id/topics/topic_name`.

#### Return type

`str`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
