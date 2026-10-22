---
url: https://docs.cloud.google.com/pubsub/quotas/
title: Pub/Sub quotas and limits \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:03.040897+00:00
---

# Pub/Sub quotas and limits  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Resources ](https://docs.cloud.google.com/pubsub/docs/resources)



Send feedback 

#  Pub/Sub quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud uses quotas to restrict how much of a particular shared Google Cloud resource that you can use. Each quota represents a specific countable resource, such as API calls to a particular service, the number of bytes sent to a particular service, or the number of streaming connections used concurrently by your project.

Many services also have limits that are unrelated to the quota system. These are fixed constraints, such as maximum message sizes or the number of Pub/Sub resources you can create in a project, which cannot be increased or decreased.

**Key Point:** This document provides information about quotas and resource limits for Pub/Sub. You can request increases to quotas, but limits cannot be adjusted. For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview).

## View and manage quotas

For a given project, you can use the [IAM & admin quotas dashboard](https://console.cloud.google.com/iam-admin/quotas?project=_&service=pubsub.googleapis.com) to view current quota limits and usage. You can also use this dashboard to do the following:

  * Reduce your quota limits
  * Initiate a process to apply for higher quota limits



For more information about monitoring and alerting on your quota usage, see [Monitoring](https://docs.cloud.google.com/pubsub/docs/monitoring#quota).

## Quota usage attribution

For push subscriber throughput, quota usage is charged against the project that contains the push subscription. This is the project that appears in the name of the subscription.

For all other quotas, usage is charged against the project associated with the credentials specified in the request. The quota usage is not charged against the project that contains the requested resource.

For example: If a service account in project A sends a publish request to publish to a topic in project B, the quota is charged to project A. In some cases, you might want quota usage to be charged against another project. You can use the `X-Goog-User-Project` system parameter to change the project for quota attribution. For more information about `X-Goog-User-Project`, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters#definitions).

You can use gcloud CLI to set the project for quota attribution for a specific request. The gcloud CLI sends the `X-Goog-User-Project` request header.

You must have the `roles/serviceusage.serviceUsageConsumer` role or a custom role with the `serviceusage.services.use` permission on the project that you are going to use for quota attribution.

The following example shows how to get a list of subscriptions in the project RESOURCE_PROJECT while charging the _Administrator operations_ quota against the project QUOTA_PROJECT. Run the following command in your Google Cloud CLI terminal:
    
    
    gcloud pubsub subscriptions list --project=
    RESOURCE_PROJECT --billing-project=
    QUOTA_PROJECT
    

Replace `QUOTA_PROJECT` with the ID of the Google Cloud project against which you want to charge quota.

Note that in Pub/Sub, the billed project is always the one that contains the resource. You can change the project only for quota attribution.

## Pub/Sub quotas

The quotas listed in the following table can be viewed and edited on a per-project basis in the [APIs and services quotas dashboard](https://console.cloud.google.com/apis/api/pubsub.googleapis.com/quotas?project=_).

Regional quotas are divided into 3 types: 

  * Large regions: `europe-west1`, `europe-west4`, `us-central1`, `us-east1`, `us-east4`, `us-west1`, `us-west2`
  * Medium regions: `asia-east1`, `asia-northeast1`, `asia-southeast1`, `europe-west2`, `europe-west3`
  * Small regions: all other regions



Exactly-once delivery quotas are region specific. Check the details for each region in the following table.

**Note:** For all throughput quotas, usage is measured in 1 kB units.Quota | Default quota limit | Description  
---|---|---  
Publisher throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 12,000,000 kB per minute (200 MB/s) in small regions

|  `pubsub.googleapis.com/regionalpublisher` Quota usage is based on the size of the published `PubsubMessage`s:

  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) (REST)
  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) (RPC)

Multiple messages can be included in a single publish request, and there is no additional quota charge per message. The size of the message, as calculated for quota usage purposes, also includes the auto-generated `message_id` field.  
Pull subscriber throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 24,000,000 kB per minute (400 MB/s) in small regions

|  `pubsub.googleapis.com/regionalsubscriber` Quota usage is based on the size of the returned `PubsubMessage`s:

  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) (REST)
  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) (RPC)

The size of the message, as calculated for quota usage purposes, also includes the auto-generated `message_id` field.  
Acknowledger throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 24,000,000 kB per minute (400 MB/s) in small regions

|  `pubsub.googleapis.com/regionalacknowledger` Quota usage is based on the size of `Acknowledge` and `ModifyAckDeadline` requests:

  * [AcknowledgeRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#acknowledgerequest) (RPC)
  * [ModifyAckDeadlineRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#modifyackdeadlinerequest) (RPC)

  
Push subscriptions throughput per region | 

  * 26,400,000 kB per minute (440 MB/s) in large regions
  * 8,400,000 kB per minute (140 MB/s) in medium regions
  * 2,400,000 kB per minute (40 MB/s) in small regions

|  `pubsub.googleapis.com/regionalpushsubscriber` For [push delivery requests](https://docs.cloud.google.com/pubsub/docs/push) made to the push endpoint, quota usage is based on the size of the `PubsubMessage`s sent to the push endpoint.  
[BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull) throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 12,000,000 kB per minute (200 MB/s) in small regions

|  `pubsub.googleapis.com/regionalpushbigquerysubscriber` For requests made to BigQuery, quota usage is based on the size of the `PubsubMessage`s sent to BigQuery.  
[Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull) throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 12,000,000 kB per minute (200 MB/s) in small regions

|  `pubsub.googleapis.com/regionalpushcloudstoragesubscriber` For requests made to Cloud Storage, quota usage is based on the size of the `PubsubMessage`s sent to Cloud Storage.  
[Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull) ([Preview](https://cloud.google.com/products#product-launch-stages)) throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 12,000,000 kB per minute (200 MB/s) in small regions

|  `pubsub.googleapis.com/regionalpushbigtablesubscriber` For requests made to Bigtable, quota usage is based on the size of the `PubsubMessage`s sent to Bigtable.  
StreamingPull subscriber throughput per region | 

  * 240,000,000 kB per minute (4 GB/s) in large regions
  * 48,000,000 kB per minute (800 MB/s) in medium regions
  * 24,000,000 kB per minute (400 MB/s) in small regions

|  `pubsub.googleapis.com/regionalstreamingpullsubscriber` Quota usage is based on the size of the `PubsubMessage`s streamed to the subscriber:

  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) (REST)
  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) (RPC)

Client Libraries use [StreamingPull](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull) operations where possible.  
Number of open StreamingPull connections per region | 

  * 72,000 open connections at a time in large regions
  * 48,000 open connections at a time in medium regions
  * 24,000 open connections at a time in small regions

|  `pubsub.googleapis.com/regionalstreamingpullconnections` The number of open StreamingPull connections at any given time. See [StreamingPull](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull). **Warning:** A high rate of failed requests to open StreamingPull connections might exhaust this quota.   
Administrator operations | 6,000 per minute (100 ops/s) |  `pubsub.googleapis.com/administrator` Each administrator operation charges one unit against this quota. Administrator operations include the following [RPC methods](https://docs.cloud.google.com/pubsub/docs/reference/rpc):  `IAMPolicy`: `GetIamPolicy`, `SetIamPolicy`, `TestIamPermissions` `Publisher`: `CreateTopic`, `DeleteTopic`, `DetachSubscription`, `GetTopic`, `ListTopics`, `ListTopicSnapshots`, `ListTopicSubscriptions`, `UpdateTopic` `SchemaService`: `CommitSchema`, `CreateSchema`, `DeleteSchema`, `DeleteSchemaRevision`, `GetSchema`, `ListSchemaRevisions`, `ListSchemas`, `RollbackSchema`, `ValidateMessage`, `ValidateSchema` `Subscriber`: `CreateSnapshot`, `CreateSubscription`, `DeleteSnapshot`, `DeleteSubscription`, `GetSnapshot`, `GetSubscription`, `ListSnapshots`, `ListSubscriptions`, `ModifyPushConfig`, `Seek`, `UpdateSnapshot`, `UpdateSubscription` **Note:** Under almost all circumstances, it is not necessary to increase the quota for administrator operations. Requests are not typically granted. For more information, see [Using excessive administrator operations](https://docs.cloud.google.com/pubsub/docs/troubleshooting#using_excessive_administrative_operations).  
Number of messages consumed from subscriptions with [exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) enabled per region | 

  * 1,000,000 messages per minute in us-central1
  * 700,000 messages per minute in us-east1
  * 300,000 messages per minute in us-west1
  * 180,000 messages per minute in other regions

|  `pubsub.googleapis.com/exactlyoncedeliveredmessagecount` Quota usage is based on the number of `PubsubMessage`s consumed by the subscriber:

  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) (REST)
  * [PubsubMessage](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) (RPC)

  
Number of messages acknowledged or whose deadline is extended when using subscriptions with [exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) enabled per region | 

  * 10,000,000 messages per minute in us-central1
  * 7,000,000 messages per minute in us-east1
  * 3,000,000 messages per minute in us-west1
  * 1,800,000 messages per minute in other regions

|  `pubsub.googleapis.com/exactlyonceackcount` Quota usage is based on the number of acknowledgment IDs in `Acknowledge` and `ModifyAckDeadline` requests:

  * [AcknowledgeRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#acknowledgerequest) (RPC)
  * [ModifyAckDeadlineRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#modifyackdeadlinerequest) (RPC)

  
  
## Throughput quota units

Throughput quota usage is measured in 1kB units. 1 kB is 1000 bytes. For example, in a `PublishRequest` with 105 messages of 50 bytes each, the user data size is `105 * 50 bytes = 5250 bytes`, so the quota usage is `max(1kB, ceil(5250 bytes/1000)) = 6kB`.

## Resource limits

**Note:** It is not possible to request increases to the following limits.Resource | Limits  
---|---  
Project |  10,000 topics  
10,000 attached or detached subscriptions  
5,000 snapshots  
10,000 schemas   
Topic |  10,000 attached subscriptions  
5,000 attached snapshots  
If [topic message retention](https://docs.cloud.google.com/pubsub/docs/replay-overview#topic_message_retention) is configured, messages published to a topic can be retained in persistent storage for up to 31 days from the time of publication.   
Subscription |  By default, [retains unacknowledged messages](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration) in persistent storage for 7 days from the time of publication. There is no limit on the **number** of retained messages.  
If subscribers don't use a subscription, the subscription expires. The default expiration period is 31 days.   
Schema | Schema size (the `definition` field): 300KB  
Revisions per schema: 20  
Publish request |  10MB (total size)  
1,000 messages   
Message |  Message size (the `data` field): 10MB  
Attributes per message: 100  
Attribute key size: 256 bytes  
Attribute value size: 1024 bytes   
StreamingPull streams | 10 MBps per open stream  
Unary Pull response |  Maximum number of messages in Pull response: 1000   
Maximum size of Pull response: 10 MB   
Pull/StreamingPull messages |  The service might impose limits on the total number of outstanding StreamingPull messages per connection. If you run into such limits, increase the rate at which you acknowledge messages and the number of connections you use.   
Acknowledge and ModifyAckDeadline requests |  512 KB (total size)  
  
Ordering keys |  If messages have [ordering keys](https://docs.cloud.google.com/pubsub/docs/publisher#using_ordering_keys), the maximum publisher throughput is 1 MBps for each ordering key.   
Cloud Storage bucket objects | When using Cloud Storage import topics, the limit for the number of objects in a bucket is 50 million.  
  
## Use a service account for higher quotas

If you use the Google Cloud CLI tool with a normal user account (that is, a non-service account), Pub/Sub operations are limited to a rate suitable for manual operations. Rates in excess of this limit results in the [RESOURCE_EXHAUSTED](https://docs.cloud.google.com/pubsub/docs/error-codes#resource-exhausted) error. The solution is to make sure that you are using service account credentials. If you want to use credentials from the gcloud CLI for automation, [activate a service account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) for your Pub/Sub operations.

## Use locational endpoints to route requests

If you have additional quota in particular regions, you can route requests to these regions using [locational Pub/Sub endpoints](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#service_endpoints). When you publish messages to a global endpoint, the Pub/Sub service might route traffic to a region that does not have sufficient quota.

In regions where quota increase requests have been granted, shifting traffic among the different types of endpoints might result in not immediately having access to all of the granted capacity.

## Quota mismatches

Quota mismatches can happen when published or received messages are smaller than 1000 bytes. For example:

  * If you publish 10 500-byte messages in separate requests, your publisher quota usage will be 10,000 bytes. This is because messages that are smaller than 1000 bytes are automatically rounded up to the next 1000-byte increment.

  * If you receive those 10 messages in a single pull response, your subscriber quota usage might be only 5 kB, since the actual size of each message is combined to determine the overall quota.

  * The inverse is also true. The subscriber quota usage might be greater than the publisher quota usage if you publish multiple messages in a single publish request or receive the messages in separate Pull requests.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
