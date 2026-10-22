---
url: https://docs.cloud.google.com/application-design-center/docs/configure-pubsub/
title: Configure a Pub/Sub topic and subscription \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:52.796712+00:00
---

# Configure a Pub/Sub topic and subscription  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Pub/Sub topic and subscription Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub is an asynchronous and scalable messaging service that decouples services producing messages from services processing those messages. For more information, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview)

This document describes the connections and parameters you can configure when using App Design Center to create a Pub/Sub topic and subscription. The configuration parameters are based on the [terraform-google-pubsub](https://github.com/terraform-google-modules/terraform-google-pubsub) Terraform module.

## Component connections

The following table includes the components that you can connect to a Pub/Sub topic or subscription, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can publish to and receive messages from the Pub/Sub topic.
  * The Pub/Sub topic ID is added to the Compute Engine instance template metadata.

| [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can manage Pub/Sub topics, and pull messages from subscriptions.
  * The `roles/pubsub.editor` role is added to the service account.
  * The service account name and email information is added to the Pub/Sub pull subscription.

| [Access control with IAM](https://docs.cloud.google.com/pubsub/docs/access-control)  
[BigQuery](https://docs.cloud.google.com/application-design-center/docs/configure-bigquery) | 

  * The Pub/Sub subscription can write messages to the BigQuery dataset.
  * The BigQuery dataset information is added to the BigQuery subscription fields.

| [BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can receive messages or publish to the Pub/Sub topic.
  * The Pub/Sub topic ID is added to the Cloud Run environment variables.
  * The `roles/pubsub.publisher` and `roles/pubsub.subscriber` roles are added to the Cloud Run service account.
  * The Cloud Run service is added to the Pub/Sub push and pull subscription fields.

| [Use Pub/Sub with Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/pubsub)  
[Cloud Storage](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage) | 

  * The Pub/Sub subscription can write messages to the Cloud Storage bucket.
  * The Cloud Storage bucket information is added to the Pub/Sub subscription fields.

| [Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/cloudstorage)  
  
## Required configuration parameters

If your template includes a Pub/Sub component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Pub/Sub resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Topic** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic.FIELDS.name) | [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Create Topic** | By default, a topic is created. Clear the checkbox if you don't want to create a topic. | [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic)  
| **Create Subscriptions** | By default, a subscription is created. Clear the checkbox if you don't want to create a subscription. | [Subscription overview](https://docs.cloud.google.com/pubsub/docs/subscription-overview)  
Topic Labels | **Key** | [labels](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic.FIELDS.labels) | [Reporting usage with labels](https://docs.cloud.google.com/pubsub/docs/labels)  
**Value** | [labels](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic.FIELDS.value) | [Reporting usage with labels](https://docs.cloud.google.com/pubsub/docs/labels)  
Push Subscriptions | **Name** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.name) | [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)  
**Ack Deadline Seconds** | [ackDeadlineSeconds](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.ack_deadline_seconds) | [Acknowledgment deadline](https://docs.cloud.google.com/pubsub/docs/subscription-properties#ack_deadline)  
**Push Endpoint** | [pushEndpoint](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#PushConfig.FIELDS.push_endpoint) | [Endpoints](https://docs.cloud.google.com/pubsub/docs/subscription-properties#endpoint)  
**X-goog-version** | The Pub/Sub API format of the pushed message. For example, v1beta1. | [attributes](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#PushConfig.FIELDS.attributes)  
**OIDC Service Account email** | [serviceAccountEmail](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#OidcToken.FIELDS.service_account_email) | [Authentication](https://docs.cloud.google.com/pubsub/docs/subscription-properties#authentication)  
**Audience** | [audience](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#OidcToken.FIELDS.audience) | [Authentication](https://docs.cloud.google.com/pubsub/docs/subscription-properties#authentication)  
**Expiration Policy** | [expirationPolicy](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.expiration_policy) | [Expiration period](https://docs.cloud.google.com/pubsub/docs/subscription-properties#expiration_period)  
**Dead Letter Topic** | [deadLetterTopic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.dead_letter_topic) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Retain Acked Messages** | [retainAckedMessages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.retain_acked_messages) | [Retain acknowledged messages](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retain-acknowledged-messages)  
**Message Retention Duration** | [messageRetentionDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.message_retention_duration) | [Message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration)  
**Max Delivery Attempts** | [maxDeliveryAttempts](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.max_delivery_attempts) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Maximum Backoff** | [maximumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.maximum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Minimum Backoff** | [minimumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.minimum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Filter** | [filter](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.filter) | [Subscription filter](https://docs.cloud.google.com/pubsub/docs/subscription-properties#subscription_filter)  
**Enable Message Ordering** | [enableMessageOrdering](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.enable_message_ordering) | [Message ordering](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message_ordering)  
Pull Subscriptions | **Name** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.name) | [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)  
**Ack Deadline Seconds** | [ackDeadlineSeconds](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.ack_deadline_seconds) | [Acknowledgment deadline](https://docs.cloud.google.com/pubsub/docs/subscription-properties#ack_deadline)  
**Dead Letter Topic** | [deadLetterTopic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.dead_letter_topic) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Max Delivery Attempts** | [maxDeliveryAttempts](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.max_delivery_attempts) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Retain Acked Messages** | [retainAckedMessages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.retain_acked_messages) | [Retain acknowledged messages](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retain-acknowledged-messages)  
**Message Retention Duration** | [messageRetentionDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.message_retention_duration) | [Message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration)  
**Maximum Backoff** | [maximumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.maximum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Minimum Backoff** | [minimumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.retry_policy_minimum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Filter** | [filter](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.filter) | [Subscription filter](https://docs.cloud.google.com/pubsub/docs/subscription-properties#subscription_filter)  
**Enable Message Ordering** | [enableMessageOrdering](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.enable_message_ordering) | [Message ordering](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message_ordering)  
**Service Account** | [](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub/) | [](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub/)  
**Enable Exactly Once Delivery** | [enableExactlyOnceDelivery](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.enable_exactly_once_delivery) | [Exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/subscription-properties#exactly-once-delivery)  
BigQuery Subscriptions | **Name** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.name) | [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)  
**Table** | [table](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#BigQueryConfig.FIELDS.table) | [Create BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription)  
**Use Topic Schema** | [useTopicSchema](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#BigQueryConfig.FIELDS.use_topic_schema) | [Use topic subscription](https://docs.cloud.google.com/pubsub/docs/subscription-properties#use-topic-schema)  
**Use Table Schema** | [useTableSchema](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#BigQueryConfig.FIELDS.use_table_schema) | [Use table schema](https://docs.cloud.google.com/pubsub/docs/subscription-properties#use-table-schema)  
**Write Metadata** | [writeMetadata](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#BigQueryConfig.FIELDS.write_metadata) | [Write metadata](https://docs.cloud.google.com/pubsub/docs/subscription-properties#write-metadata)  
**Drop Unknown Fields** | [dropUnknownFields](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#BigQueryConfig.FIELDS.drop_unknown_fields) | [Drop unknown fields](https://docs.cloud.google.com/pubsub/docs/subscription-properties#drop-unknown-fields)  
**Ack Deadline Seconds** | [ackDeadlineSeconds](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.ack_deadline_seconds) | [Acknowledgment deadline](https://docs.cloud.google.com/pubsub/docs/subscription-properties#ack_deadline)  
**Retain Acked Messages** | [retainAckedMessages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.retain_acked_messages) | [Retain acknowledged messages](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retain-acknowledged-messages)  
**Message Retention Duration** | [messageRetentionDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.message_retention_duration) | [Message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration)  
**Enable Message Ordering** | [enableMessageOrdering](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.enable_message_ordering) | [Message ordering](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message_ordering)  
**Expiration Policy** | [expirationPolicy](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.expiration_policy) | [Expiration period](https://docs.cloud.google.com/pubsub/docs/subscription-properties#expiration_period)  
**Filter** | [filter](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.filter) | [Subscription filter](https://docs.cloud.google.com/pubsub/docs/subscription-properties#subscription_filter)  
**Dead Letter Topic** | [deadLetterTopic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.dead_letter_topic) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Maximum Backoff** | [maximumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.maximum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Minimum Backoff** | [minimumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.minimum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
Cloud Storage Subscriptions | **Name** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.name) | [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)  
**Bucket** | [bucket](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.bucket) | [Bucket name](https://docs.cloud.google.com/pubsub/docs/subscription-properties#bucket_name)  
**Filename Prefix** | [filenamePrefix](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.filename_prefix) | [Filename prefix, suffix, and datetime](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_names)  
**Filename Suffix** | [filenameSuffix](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.filename_suffix) | [Filename prefix, suffix, and datetime](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_names)  
**Filename Datetime Format** | [filenameDatetimeFormat](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.filename_datetime_format) | [Filename prefix, suffix, and datetime](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_names)  
**Max Duration** | [maxDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.max_duration) | [File batching](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_batch)  
**Max Bytes** | [maxBytes](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.max_bytes) | [File batching](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_batch)  
**Max Messages** | [maxMessages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#CloudStorageConfig.FIELDS.max_messages) | [File batching](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_batch)  
**Output Format** | [textConfig](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#textconfig) or [avroConfig](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#avroconfig) | [File format](https://docs.cloud.google.com/pubsub/docs/subscription-properties#file_format)  
**Write Metadata** | [writeMetadata](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#AvroConfig.FIELDS.write_metadata) | [Write metadata](https://docs.cloud.google.com/pubsub/docs/subscription-properties#write-metadata)  
**Use Topic Schema** | [useTopicSchema](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#AvroConfig.FIELDS.use_topic_schema) | [Use topic schema](https://docs.cloud.google.com/pubsub/docs/subscription-properties#use-topic-schema)  
**Ack Deadline Seconds** | [ackDeadlineSeconds](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.ack_deadline_seconds) | [Acknowledgment deadline](https://docs.cloud.google.com/pubsub/docs/subscription-properties#ack_deadline)  
**Retain Acked Messages** | [](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.retain_acked_messages) | [Retain acknowledged messages](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retain-acknowledged-messages)  
**Message Retention Duration** | [messageRetentionDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.message_retention_duration) | [Message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration)  
**Enable Message Ordering** | [enableMessageOrdering](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.enable_message_ordering) | [Message ordering](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message_ordering)  
**Expiration Policy** | [expirationPolicy](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.expiration_policy) | [Expiration period](https://docs.cloud.google.com/pubsub/docs/subscription-properties#expiration_period)  
**Filter** | [filter](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.filter) | [Subscription filter](https://docs.cloud.google.com/pubsub/docs/subscription-properties#subscription_filter)  
**Dead Letter Topic** | [deadLetterTopic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#DeadLetterPolicy.FIELDS.dead_letter_topic) | [Dead letter topic](https://docs.cloud.google.com/pubsub/docs/subscription-properties#dead_letter_topic)  
**Maximum Backoff** | [maximumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.maximum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
**Minimum Backoff** | [minimumBackoff](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#RetryPolicy.FIELDS.minimum_backoff) | [Retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies)  
Subscription Labels | **Key** | [labels](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.labels) | [Reporting usage with labels](https://docs.cloud.google.com/pubsub/docs/labels)  
**Value** | [labels](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.labels) | [Reporting usage with labels](https://docs.cloud.google.com/pubsub/docs/labels)  
| **Topic Message Retention Duration** | [topicMessageRetentionDuration](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions#Subscription.FIELDS.topic_message_retention_duration) | [Message retention duration](https://docs.cloud.google.com/pubsub/docs/topic-properties#message_retention_duration)  
| **Topic KMS Key Name** | [kmsKeyName](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic.FIELDS.kms_key_name) | [Use a customer-managed encryption key (CMEK)](https://docs.cloud.google.com/pubsub/docs/topic-properties#use_a_customer-managed_encryption_key_cmek)  
| **Grant BigQuery Project Roles** | By default, the [BigQuery Metadata Viewer](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer) and [BigQuery Data Editor](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) roles are granted to default Pub/Sub service account. If you don't want to grant these roles, clear the checkbox. | [Assign BigQuery roles to the Pub/Sub service account](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#assign_bigquery_service_account)  
| **Grant Token Creator** | By default, the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role is granted to default Pub/Sub service account. If you don't want to grant this role, clear the checkbox. | [Set up authentication for Pub/Sub](https://docs.cloud.google.com/pubsub/docs/authentication#authn-how-to)  
Schema | **Name** | [name](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema.FIELDS.name) | [Important information about schemas](https://docs.cloud.google.com/pubsub/docs/schemas#schema-info)  
**Type** | [type](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema.FIELDS.type) | [Types of schemas](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema)  
**Definition** | [definition](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas#Schema.FIELDS.definition) | [Types of schemas](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema)  
**Encoding** | [encoding](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#SchemaSettings.FIELDS.encoding) | [Guidelines to associate a schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic#associate-schema-guidelines)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
