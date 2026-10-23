---
url: https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer/
title: Pub/Sub notifications \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:39.328534+00:00
---

# Pub/Sub notifications  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

After you complete a Storage Transfer Service transfer, you might want to start another task, handle an error encountered during a transfer, or log that a transfer occurred. Pub/Sub provides a queue that your programs subscribe to to receive messages when a transfer completes. This enables you to reuse code and to program next steps based on the state of a transfer.

For more information about Pub/Sub, see [What is Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview)

## Prerequisites

Before you can use this feature, do the following:

  1. [Enable the Pub/Sub API](https://docs.cloud.google.com/service-usage/docs/enable-disable) for the project receiving Pub/Sub notifications.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)

  2. [Have an existing Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic) that you want to send notifications to.

  3. [Get the email address of the service account](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts) associated with the project that contains your Storage Transfer Service bucket.

     1. [Grant the service account the IAM role `roles.pubsub.publisher`](https://docs.cloud.google.com/pubsub/docs/access-control#console) for the desired Pub/Sub topic.
**Note:** There might be a delay of several seconds between assigning the role and having it applied to your service account. If you grant this permission programmatically, wait 30 seconds before configuring Storage Transfer Service.



## Configuring notification settings

To configure Storage Transfer Service Pub/Sub notification settings, you use the [Storage Transfer Service transferJobs API](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs), to create `NotificationConfig` message. The topic will receive notifications on the configured Pub/Sub channel.

Specify the following in your `NotificationConfig` message:

  * The Pub/Sub topic to send notifications to
  * The format of the message, `"JSON"` or `"NONE"`
  * The desired event types, corresponding to completed [`TransferOperation.Statuses`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#status):

    * `"TRANSFER_OPERATION_SUCCESS"`
    * `"TRANSFER_OPERATION_FAILED"`
    * `"TRANSFER_OPERATION_ABORTED"`



The following is an example `NotificationConfig` message:
    
    
    {
       ...
       "notificationConfig": {
         "pubsubTopic": "projects/project-id/topics/topic-id",
         "eventTypes": ["TRANSFER_OPERATION_SUCCESS"],
         "payloadFormat": "JSON"
       },
       ...
    }
    

Replace the following:

  * `project-id`: The Google Cloud project ID of the transfer
  * `topic-id`: The Pub/Sub topic name



For more information, see [Storage Transfer Service Pub Sub REST specification](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/NotificationConfig).

## Notification format

Notifications sent to the Pub/Sub topic consist of two parts:

  * **Attributes** : A set of key:value pairs describing the event.
  * **Payload** : A string that contains the metadata of the changed object.



### Attributes

Attributes are key:value pairs contained in all notifications sent by Storage Transfer Service to your Pub/Sub topic. Notifications always contain the following set of key:value pairs, regardless of the notification's payload:

See [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) for more information about the Pub/Sub message format.

Attribute name | Example | Description  
---|---|---  
`eventType` | `TRANSFER_OPERATION_SUCCESS` | Status of the `TransferOperation`, from [`NotificationConfig.EventType`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/NotificationConfig#eventtype)  
`payloadFormat` | `"JSON"` | Format of the message, either `"JSON"` or `"NONE"`. From [`NotificationConfig.PayloadFormat`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/NotificationConfig#payloadformat).  
`projectId` | `project-3` | ID of the transfer host project.  
`transferJobName` | `transferJobs/123` | Name of the transfer job.  
`transferOperationName` | `transferOperations/456` | Name of the transfer operation.  
  
### Payload

The payload contains the `TransferOperation` metadata. When you create a notification configuration, you specify a type of payload to include in notifications triggered by that configuration. You can specify the following types of payload:

Payload type | Description  
---|---  
**NONE** | No payload is included with the notification.  
**JSON** | The payload is formatted as a [JSON response](https://developers.google.com/protocol-buffers/docs/proto3), in application/json.  
  
## Example Pub/Sub notification configurations

### Notifying for failed transfers only

To receive messages for failed transfers only, submit a `TransferJob` with a `NotificationConfig` that filters for failed transfers only:
    
    
    // REST JSON format:
    //   https://cloud.google.com/storage-transfer/docs/create-manage-transfer-program
    {
       ...
       "notificationConfig": {
         "pubsubTopic": "projects/project-id/topics/topic-id",
         "eventTypes": ["TRANSFER_OPERATION_FAILED"],
         "payloadFormat: "JSON"
       },
       ...
    }
    

Replace the following:

  * `project-id`: The Google Cloud project ID of the transfer
  * `topic-id`: The Pub/Sub topic name



### Notify on all completed transfers

To notify on all completed transfers, regardless of status, submit a `TransferJob` with a `NotificationConfig` without `EventType` filters:
    
    
    // REST JSON format:
    //   https://cloud.google.com/storage-transfer/docs/create-manage-transfer-program
    {
       ...
       "notificationConfig": {
         "pubsubTopic": "projects/project-id/topics/topic-id",
         "payloadFormat: "JSON"
       },
       ...
    }
    

Replace the following:

  * `project-id`: The Google Cloud project ID of the transfer
  * `topic-id`: The Pub/Sub topic name



### Performing arbitrary actions on a transfer

To perform an arbitrary action, you create a Pub/Sub notification using a [Cloud function with a Pub/Sub trigger](https://docs.cloud.google.com/functions/docs/calling/pubsub) paired with a [background cloud function](https://docs.cloud.google.com/functions/docs/writing/background). For more information, see the [Cloud Pub/Sub tutorial](https://docs.cloud.google.com/functions/docs/tutorials/pubsub).

Examples of arbitrary actions include:

  * [Sending an email](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail)
  * [Starting a Dataflow job](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python)
  * [Recording metadata in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-functions)
  * [Recording metadata in Spanner](https://docs.cloud.google.com/spanner/docs/reference/libraries)



## Delivery guarantees

**Important:** There is currently no SLA for delivery time, but notifications are typically delivered within seconds. In some circumstances notifications might be delayed substantially longer.

Storage Transfer Service sends notifications for any `TransferOperations` started after you add a notification configuration, and guarantees at-least-once delivery to Pub/Sub. Pub/Sub also offers at-least-once delivery to the recipient, which means that you could receive multiple messages, with multiple IDs, that represent the same Storage Transfer Service event.

Notifications are not guaranteed to be published in the order Pub/Sub receives them.

If a notification consistently cannot be delivered to a Pub/Sub topic, Storage Transfer Service might delete the notification after 7 days. Delivery failure can occur when the Pub/Sub topic no longer exists, when Storage Transfer Service no longer has permission to publish to the topic, or when the project that owns the topic exceeds its publishing quota.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
