---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-adapters/
title: TIPCommon.adapters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:06.408756+00:00
---

# TIPCommon.adapters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-adapters/

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

Acknowledges the messages associated with the `ackIDs` in the `AcknowledgeRequest` response returned from `PubSubAdapter.pull()`.

Parameters  
---  
`sub_name` | (`str`)The subscription name.  
`ack_ids` | (`list[str])` A list of acknowledgment IDs for the messages being acknowledged. The list is returned by the Pub/Sub system in the `PubSubAdapter.pull()` response.  
  
### _static_ build_pubsub_message

_static_ `build_pubsub_message(message_content, encoding='utf-8', ordering_key=None, **attr)`

Creates a PubSubMessage object.

Parameters  
---  
`message_content` | (`str`) The message content.  
`encoding` | (`str`) The encoding type to encode or decode the message text. The default value is `UTF-8`.  
`ordering_key` | _Optional_ (`str`) If used, the parameter identifies all related messages that must follow the publish order.  
`**attr` | _Optional_(`str`)The attributes to pass as message object attributes.  
  
#### Returns

`TIPCommon.adapters.pubsub.PubSubMessage` object.

#### Return type

`PubSubMessage`

### create_subscription

`create_subscription(sub_name, topic, **attr)`

Creates a Pub/Sub subscription for the specified topic.

Parameters  
---  
`sub_name` | (`str`) The subscription name.  
`topic` | (`str`) A Pub/Sub topic name to create the subscription for.  
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
`topic_name` | (`str`) The name of the topic. The name must correspond to the Google Cloud [resource name rules](https://docs.cloud.google.com/pubsub/docs/admin#resource_names).  
  
#### Returns

`TIPCommon.adapters.pubsub.Topic` object of the created topic.

#### Return type

`Topic`

### delete_subscription

`delete_subscription(sub_name)`

Deletes a Pub/Sub subscription from a Google Cloud project.

Parameters  
---  
`sub_name` | (`str`) The subscription name to remove.  
  
### delete_topic

`delete_topic(topic_name)`

Deletes a Pub/Sub topic from a Google Cloud project.

Parameters  
---  
`topic_name` | (`str`)The topic to remove.  
  
### _static_ from_credentials

_static_ `from_credentials(credentials, project_id=None, verify_ssl=True, quota_project=None, logger=None, region=None)`

Creates PubSubAdapter object from `google.oauth2.credentials.Credentials` object.

Parameters  
---  
`credentials` | (`google.oauth2.credentials.Credentials`) A `google.oauth2.credentials.Credentials` object.  
`project_id` | _Optional_ (`str`) The Google Cloud project ID. If not provided, the function attempts to use the project configured in the credentials object by default.  
`verify_ssl` | _Optional_ (`bool`) Specifies whether SSL certificate verification is enabled for HTTP sessions.  
`quota_project` | _Optional_ (`str`) The project to use for quota and billing.  
`logger` | _Optional_ (`SiemplifyLogger`) A `SiemplifyLogger` object.  
`region` | (`str`) The region for Pub/Sub to work in.  
  
#### Returns

A `PubSubAdapter` object.

#### Return type

`PubSubAdapter`

### _static_ from_service_account_info

_static_ `subscription_name(project_id, sub_name)`

Creates a PubSubAdapter object from `service_account` JSON.

Parameters  
---  
`user_service_account` | (`str`) The Google Cloud Service Account JSON in text format.  
`project_id` | _Optional_ (`str`) The Google Cloud project ID. If not provided, the function attempts to use the project configured in the credentials object by default.  
`verify_ssl` | _Optional_ (`bool`) Specifies whether SSL certificate verification is enabled for HTTP sessions.  
`quota_project` | _Optional_ (`str`) The project to use for quota and billing.  
`logger` | _Optional_ (`SiemplifyLogger`) A `SiemplifyLogger` object.  
  
#### Returns

A `PubSubAdapter` object.

#### Return type

`PubSubAdapter`

### get_subscription

`get_subscription(sub_name, topic=None, create_if_not_exist=False, **attr)`

Retrieves a Pub/Sub subscription.

Parameters  
---  
`sub_name` | (`str`) The subscription name.  
`topic` | (`str`) A Pub/Sub topic name to create a subscription for. Mandatory if `create_if_not_exist` is `True`.  
`create_if_not_exist` | Creates the Pub/Sub subscription in Google Cloud if it doesn't exist.  
`**attr` | Additional parameters to pass to the subscription creation request.   
  
#### Returns

`TIPCommon.adapters.pubsub.Subscription` object of the retrieved subscription.

#### Return type

`Subscription`

### get_topic

`get_topic(topic_name, create_if_not_exist=False)`

Retrieves a Pub/Sub topic object from the configured Google Cloud project.

Parameters  
---  
`topic_name` | (`str`)Name of the topic (simplified, without the `projects/``PROJECT_ID``/topics/` prefix).  
`create_if_not_exist` | `bool`Creates the Pub/Sub topic in Google Cloud, if it does not exist.  
  
#### Returns

`TIPCommon.adapters.pubsub.Topic` object of the received topic.

#### Return type

`Topic`

### patch_subscription

`patch_subscription(sub_name, topic_name, push_config=None, bigquery_config=None, cloud_storage_config=None, ack_deadline_seconds=None, retain_acked_messages=None, retention_duration=None, labels=None, enable_message_ordering=None, expiration_policy=None, query_filter=None, dead_letter_policy=None, return_policy=None, detached=None, enable_once_delivery=None)`

Updates an existing subscription.

**Note:** Certain subscription properties are unmodifiable.Parameters  
---  
`sub_name` | (`str`)The subscription name.  
`topic_name` | (`str`)The name of the topic from which this subscription receives messages.  
  
#### Returns

`TIPCommon.adapters.pubsub.Subscription` object of the received subscription.

#### Return type

`Subscription`

### patch_topic

`patch_topic(topic_name, labels=None, message_storage_policy=None, kms_key_name=None, schema_settings=None, satisfies_pzs=None, retention_duration=None)`

Updates an existing topic.

**Note:** Certain topic properties are unmodifiable.Parameters  
---  
`topic_name` | (`str`)The topic name.  
  
#### Returns

`TIPCommon.adapters.pubsub.Topic` object of the received topic.

#### Return type

`Topic`

### publish

`publish(topic_name, messages)`

Publish a list of PubSubMessage objects to a topic.

Parameters  
---  
`topic_name` | (`str`)The name of the topic to publish the messages.  
`messages` | `list`A list of PubSubMessage objects. You can create the list with the `PubSubAdapter.build_message()` static method.  
  
#### Returns

List of message IDs.

#### Return type

`list[str]`

### pull

`pull(sub_name, limit, timeout=60, encoding='utf-8')`

Pull messages from Pub/Sub subscriptions.

Parameters  
---  
`sub_name` | (`str`)The subscription name.  
`limit` | `int`The maximum number of messages to return for this request.  
`timeout` | `int`HTTP request timeout in seconds.Default is 60 seconds.  
`encoding` | (`str`)A Pub/Sub message encoding. Default is `utf-8`.  
  
#### Returns

List of `TIPCommon.adapters.pubsub.ReceivedMessage` objects.

#### Return type

`list[ReceivedMessage]`

### _static_ subscription_name

_static_ `subscription_name(project_id, sub_name)`

Retrieves the full subscription name in the following format: **projects/` project_id`/subscriptions/`subscription_name`**.

Parameters  
---  
`project_id` | (`str`)The project name that contains the resource.  
`sub_name` | (`str`)A Pub/Sub subscription name.  
  
#### Returns

A full subscription name in the following format: **projects/` project_id`/subscriptions/`subscription_name`**.

#### Return type

`str`

### _static_ topic_name

_static_ `topic_name(project_id, topic)`

Retrieves **projects/` project_id`/topics/`topic_name`**.

Parameters  
---  
`project_id` | (`str`)The project name that contains the resource.  
`topic` | (`str`)A Pub/Sub topic name.  
  
#### Returns

A full topic name: **projects/` project_id`/topics/`topic_name`**.

#### Return type

`str`

## _class_ TIPCommon.adapters.pubsub.data_models.PubSubMessage

_class_ `TIPCommon.adapters.pubsub.data_models.PubSubMessage(raw_data: 'dict', data: 'str' = None, attributes: 'dict' = None, message_id: 'str' = None, publish_time: 'int' = None, ordering_key: 'str' = None)`

Bases: **object**

`attributes: dict= None`

`data: str= None`

`json()`

`message_id: str= None`

`ordering_key: str= None`

`publish_time: int= None`

`raw_data: dict`

## _class_ TIPCommon.adapters.pubsub.data_models.ReceivedMessage

_class_ `TIPCommon.adapters.pubsub.data_models.ReceivedMessage(raw_data: 'dict', ack_id: 'str', message: 'PubSubMessage', delivery_attempt: 'int')`

Bases: **object**

`ack_id: str`

`delivery_attempt: int`

`json()`

`message: PubSubMessage`

`raw_data: dict`

## _class_ TIPCommon.adapters.pubsub.data_models.SchemaSettings

_class_ `TIPCommon.adapters.pubsub.data_models.SchemaSettings(raw_data: 'dict', schema: 'str', encoding: 'str' = None, first_revision_id: 'str' = None, last_revision_id: 'str' = None)`

Bases: **object**

`encoding: str= None`

`first_revision_id: str= None`

`json()`

`last_revision_id: str= None`

`raw_data: dict`

`schema: str`

## _class_ TIPCommon.adapters.pubsub.data_models.Subscription

_class_ `TIPCommon.adapters.pubsub.data_models.Subscription(raw_data: 'dict', name: 'str', identifier: 'str', topic_identifier: 'str', state: 'str', ack_deadline_secs: 'int' = None, retain_ack_messages: 'bool' = None, message_retention_duration: 'int' = None, labels: 'dict' = None, message_ordering: 'bool' = None, query_filter: 'str' = None, topic_message_retention_duration: 'int' = None)`

Bases: **object**

`ack_deadline_secs: int= None`

`identifier: str`

`json()`

`labels: dict= None`

`message_ordering: bool= None`

`message_retention_duration: int= None`

`name: str`

`query_filter: str= None`

`raw_data: dict`

`retain_ack_messages: bool= None`

`state: str`

`topic_identifier: str`

`topic_message_retention_duration: int= None`

## _class_ TIPCommon.adapters.pubsub.data_models.Topic

_class_ `TIPCommon.adapters.pubsub.data_models.Topic(raw_data: 'dict', name: 'str', identifier: 'str', labels: 'dict' = None, schema_settings: 'SchemaSettings' = None, message_retention_duration: 'int' = None)`

Bases: **object**

`identifier: str`

`json()`

`labels: dict= None`

`message_retention_duration: int= None`

`name: str`

`raw_data: dict`

`schema_settings: SchemaSettings= None`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
