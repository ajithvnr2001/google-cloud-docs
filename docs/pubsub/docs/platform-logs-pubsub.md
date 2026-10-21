---
url: https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub/
title: Use platform logs to troubleshoot import topics \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:11.428319+00:00
---

# Use platform logs to troubleshoot import topics  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Use platform logs to troubleshoot import topics Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use Google Cloud platform logs to troubleshoot issues when you are using import topics, including the following: Cloud Storage import topics, Azure Event Hubs import topics, Amazon MSK import topics, and Confluent Cloud import topics.

**Note:** You can enable or disable platform logs for Amazon Kinesis Data Streams import topics. However, Kinesis stream data is always compatible with Pub/Sub's message requirements and can be published. Therefore, no logs are written.

## About platform logs

A supported Google Cloud service generates its own set of platform logs, capturing events and activities relevant to that service's operation. These platform logs contain detailed information about what's happening within a service, including successful operations, errors, warnings, and other noteworthy events.

Platform logs are a part of Cloud Logging and share the same features. For example, the following is a list of important features for platform logs:

  * Logs are typically structured as JSON objects that allow for further querying and filtering.

  * You can view platform logs by using [Logging in the console](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * Platform logs can also be integrated with Cloud Monitoring and other monitoring tools to create dashboards, alerts, and other monitoring mechanisms.

  * Log storage incurs [costs based on ingested volume and retention period](https://cloud.google.com/stackdriver/pricing#logging-costs).




For more information about platform logs, see [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs).

## Before you begin

Ensure that you have completed the prerequisites for creating the topic you are using:

  * [Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#before-you-begin)
  * [Azure Event Hubs import topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#before-you-begin)
  * [Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#before-you-begin)
  * [Confluent Cloud import topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic#before-you-begin)



## Required roles and permissions

Before you begin, verify that you have access to Logging. You require the **Logs Viewer** `(roles/logging.viewer)` Identity and Access Management (IAM) role. For more information about Logging access, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

The following describe how to verify and grant IAM access:

  * [View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#view-access) to verify the access that each principal has.

  * [Grant a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) to relevant principals in your project.




## About import topic ingestion failures

Import topics can encounter issues that prevent data from being successfully ingested.

### Cloud Storage import topics

Cloud Storage import topics can encounter issues that prevent data from being successfully ingested. For example, when using a Cloud Storage import topic, you might face issues ingesting a Cloud Storage object or part of an object.

The following list describes reasons for ingestion failure in Cloud Storage import topics that generate platform logs:

  * Message size

    * Individual messages can't be larger than 10 MB. If they are, the entire message is skipped.

    * If you're using the Avro or the Pub/Sub Avro format, Avro blocks can't be larger than 16 MB. Larger Avro blocks are skipped.

  * Message attributes

    * Messages can have a maximum of 100 attributes. Any extra attribute is dropped when the message is ingested.

    * Attribute keys can't be larger than 256 bytes and values can't be larger than 1024 bytes. If the value is larger than the maximum size, the entire key-value pair is dropped from the message when it is ingested.

For more information about the guidelines for using message keys and attributes, see [Use attributes to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes).

  * Avro formatting

    * Make sure your Avro objects are correctly formatted. Incorrect formatting prevents the message from being ingested.
  * Data format

    * Make sure that you're using a [supported Avro version](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#input_format). Unsupported formats are not processed.



### Azure Event Hubs, Amazon MSK, and Confluent Cloud import topics

Azure Event Hubs, Amazon MSK, and Confluent Cloud import topics can encounter issues that prevent data from being successfully ingested.

The following list describes reasons for ingestion failure in import topics that generate platform logs:

  * Message size

    * Individual messages can't be larger than 10 MB. If they are, the entire message is skipped.
  * Message attributes

    * Messages can have a maximum of 100 attributes. Any extra attribute is dropped when the message is ingested.

    * Attribute keys can't be larger than 256 bytes and values can't be larger than 1024 bytes. If the value is larger than the maximum size, the entire key-value pair is dropped from the message when it is ingested.

For more information about the guidelines for using message keys and attributes, see [Use attributes to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes).




## Enable platform logs

Platform logs is disabled by default for import topics. You can enable platform logs when you create or update an import topic. To disable platform logs, update the import topic.

### Enable platform logs while creating an import topic

To enable platform logs when creating an import topic, do the following:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click **Create topic**.

The topic details page opens.

  3. In the **Topic ID** field, enter an ID for your import topic.

For more information about naming topics, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Select **Add a default subscription**.

  5. Select **Enable ingestion**.

  6. Retain the other default settings.
  7. Click **Create topic**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To enable platform logs, ensure the `--ingestion-log-severity` flag is set to `WARNING` or a lower severity level such as `INFO` or `DEBUG`. Run the [ `gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command for the respective topic that you are using:

     * [Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#create-import-topic)
     * [Azure Event Hubs import topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#create-import-topic)
     * [Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#create-import-topic)
     * [Confluent Cloud import topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic#create-import-topic)

For example, to enable platform logs on a Cloud Storage import topic, include the `--ingestion-log-severity=WARNING` flag in your `gcloud pubsub topics create` command.
    
    gcloud pubsub topics create TOPIC_ID \
        --cloud-storage-ingestion-bucket=BUCKET_NAME \
        --cloud-storage-ingestion-input-format=INPUT_FORMAT \
        --ingestion-log-severity=WARNING




### Enable platform logs while updating an import topic

To enable platform logs when updating an import topic, do the following:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the respective import topic that you are using (Cloud Storage import topic, Azure Event Hubs import topic, Amazon MSK import topic, or Confluent Cloud import topic).

  3. In the topic details page, click **Edit**.

  4. Select **Enable platform logs**.
  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To enable platform logs, ensure the ingestion-log-severity is set to `WARNING` or a lower severity level such as `INFO` or `DEBUG`. Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command with all the possible flags that specify settings for the respective topic that you are using:

     * [Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#edit_import_topics)
       * To avoid losing your settings for the Cloud Storage import topic, make sure to re-include the same values you had in your original `create` command, every time you update the topic. If you leave something out, Pub/Sub resets the setting to its default value.
     * [Azure Event Hubs import topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#edit_import_topics)
     * [Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#edit_import_topics)
     * [Confluent Cloud import topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic#edit_import_topics)

For example, to update logs on an existing Cloud Storage import topic, include the `--ingestion-log-severity=WARNING` flag in your `gcloud pubsub topics create` command and include all the possible flag values that specify settings for a Cloud Storage import topic.
    
    gcloud pubsub topics update TOPIC_ID \
        --cloud-storage-ingestion-bucket=BUCKET_NAME \
        --cloud-storage-ingestion-input-format=INPUT_FORMAT \
        --cloud-storage-ingestion-text-delimiter=TEXT_DELIMITER \
        --cloud-storage-ingestion-minimum-object-create-time=MINIMUM_OBJECT_CREATE_TIME \
        --cloud-storage-ingestion-match-glob=MATCH_GLOB
        --ingestion-log-severity=WARNING




## Disable platform logs

To disable platform logs for the respective import topic that you are using, do the following:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the respective import topic that you are using (Cloud Storage import topic, Azure Event Hubs import topic, Amazon MSK import topic, or Confluent Cloud import topic).

  3. In the topic details page, click **Edit**.

  4. Clear **Enable platform logs**.
  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To disable platform logs, ensure the ingestion-log-severity is set to `DISABLED`. Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command with all the possible flags that specify settings for the respective topic that you are using:

     * [Cloud Storage import topic](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic#edit_import_topics)
       * To avoid losing your settings for the Cloud Storage import topic, make sure to re-include the same values you had in your original `create` command, every time you update the topic. If you leave something out, Pub/Sub resets the setting to its original default value.
     * [Azure Event Hubs import topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic#edit_import_topics)
     * [Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#edit_import_topics)
     * [Confluent Cloud import topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic#edit_import_topics)

For example, to disable logs on an existing Cloud Storage import topic, include the `--ingestion-log-severity=DISABLED` flag in your `gcloud pubsub topics update` command and include all the possible flags that specify settings for a Cloud Storage import topic.
    
    gcloud pubsub topics update TOPIC_ID \
        --cloud-storage-ingestion-bucket=BUCKET_NAME \
        --cloud-storage-ingestion-input-format=INPUT_FORMAT \
        --cloud-storage-ingestion-text-delimiter=TEXT_DELIMITER \
        --cloud-storage-ingestion-minimum-object-create-time=MINIMUM_OBJECT_CREATE_TIME \
        --cloud-storage-ingestion-match-glob=MATCH_GLOB
        --ingestion-log-severity=DISABLED




## View platform logs

To view platform logs for the respective import topic that you are using, do the following:

###  Google Cloud console 

  1. In the Google Cloud console, go to **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select a Google Cloud project.

  3. If required, from the **Upgrade** menu, switch from **Legacy Logs Viewer** to **Logs Explorer**.

  4. Click the **Show query** toggle.

  5. To filter your logs to show only entries for the respective import topics that you are using (Cloud Storage import topic, Azure Event Hubs import topic, Amazon MSK import topic, or Confluent Cloud import topic), type `"resource.type=pubsub_topic AND severity=WARNING"` into the query field and click **Run query**.

  6. In the **Query results** pane, click **Edit time** to change the time period for which to return results.




For more information about using the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

###  gcloud CLI 

To use the gcloud CLI to search for platform logs for the respective import topics that you are using, use the [`gcloud logging read`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries) command.

Specify a filter to limit your results to platform logs for the respective import topics that you are using (Cloud Storage import topic, Azure Event Hubs import topic, Amazon MSK import topic, or Confluent Cloud import topic).
    
    
    gcloud logging read "resource.type=pubsub_topic AND severity=WARNING"
    

###  Cloud Logging API 

Use the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) Cloud Logging API method.

To filter your results to include only platform logs for Cloud Storage import topics, use the `filter` field. The following is a sample JSON request object.
    
    
    {
    "resourceNames":
      [
        "projects/my-project-name"
      ],
      "orderBy": "timestamp desc",
      "filter": "resource.type=\"pubsub_topic\" AND severity=WARNING"
    }
    

## View and understand platform log format

The following section includes sample platform logs and describes the fields for platform logs.

All platform log specific fields are contained within a `jsonPayload` object.

### Cloud Storage

###  Avro failure 
    
    
    {
      "insertId": "1xnzx8md4768",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.pubsub.v1.IngestionFailureEvent",
        "cloudStorageFailure": {
          "objectGeneration": "1661148924738910",
          "bucket": "bucket_in_avro_format",
          "objectName": "counts/taxi-2022-08-15T06:10:00.000Z-2022-08-15T06:15:00.000Z-pane-0-last-00-of-01",
          "avroFailureReason": {}
        },
        "topic": "projects/my-project/topics/avro_bucket_topic",
        "errorMessage": "Unable to parse the header of the object. The object won't be ingested."
      },
      "resource": {
        "type": "pubsub_topic",
        "labels": {
          "project_id": "my-project",
          "topic_id": "avro_bucket_topic"
        }
      },
      "timestamp": "2024-10-07T18:55:45.650103193Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/pubsub.googleapis.com%2Fingestion_failures",
      "receiveTimestamp": "2024-10-07T18:55:46.678221398Z"
    }
    

Log field | Description  
---|---  
`insertId` | A unique identifier for the log entry.  
`jsonPayload.@type` | Identifies the event type. Always `type.googleapis.com/google.pubsub.v1.IngestionFailureEvent`.  
`jsonPayload.cloudStorageFailure.objectGeneration` | The generation number of the Cloud Storage object.  
`jsonPayload.cloudStorageFailure.bucket` | The Cloud Storage bucket containing the object.  
`jsonPayload.cloudStorageFailure.objectName` | The name of the Cloud Storage object.  
`jsonPayload.cloudStorageFailure.avroFailureReason` | Contains more specific Avro parsing error details. This field is left empty.  
`jsonPayload.topic` | The Pub/Sub topic the message was intended for.  
`jsonPayload.errorMessage` | A human-readable error message.  
`resource.type` | The resource type. Always `pubsub_topic`.  
`resource.labels.project_id` | The Google Cloud project ID.  
`resource.labels.topic_id` | The Pub/Sub topic ID.  
`timestamp` | Log entry generation timestamp.  
`severity` | Severity level which is `WARNING`.  
`logName` | Name of the log.  
`receiveTimestamp` | Log entry received timestamp.  
  
###  Text failure 
    
    
    {
      "insertId": "1kc4puoag",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.pubsub.v1.IngestionFailureEvent",
        "cloudStorageFailure": {
          "bucket": "bucket_in_text_format",
          "apiViolationReason": {},
          "objectName": "counts/taxi-2022-08-15T06:10:00.000Z-2022-08-15T06:15:00.000Z-pane-0-last-00-of-01",
          "objectGeneration": "1727990048026758"
        },
        "topic": "projects/my-project/topics/large_text_bucket_topic",
        "errorMessage": "The message has exceeded the maximum allowed size of 10000000 bytes. The message won't be published."
      },
      "resource": {
        "type": "pubsub_topic",
        "labels": {
          "topic_id": "large_text_bucket_topic",
          "project_id": "my-project"
        }
      },
      "timestamp": "2024-10-09T14:09:07.760488386Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/pubsub.googleapis.com%2Fingestion_failures",
      "receiveTimestamp": "2024-10-09T14:09:08.483589656Z"
    }
    

Log field | Description  
---|---  
`insertId` | A unique identifier for the log entry.  
`jsonPayload.@type` | Identifies the event type. Always `type.googleapis.com/google.pubsub.v1.IngestionFailureEvent`.  
`jsonPayload.cloudStorageFailure.objectGeneration` | The generation number of the Cloud Storage object.  
`jsonPayload.cloudStorageFailure.bucket` | The Cloud Storage bucket containing the object.  
`jsonPayload.cloudStorageFailure.objectName` | The name of the Cloud Storage object.  
`jsonPayload.cloudStorageFailure.apiViolationReason` | Contains details about the API violation. This field is left empty.  
`jsonPayload.topic` | The Pub/Sub topic.  
`jsonPayload.errorMessage` | A human-readable message.  
`resource.type` | Resource type, always `pubsub_topic`.  
`resource.labels.project_id` | Google Cloud project ID.  
`resource.labels.topic_id` | Pub/Sub topic ID.  
`timestamp` | Log entry generation timestamp.  
`severity` | Severity level which is `WARNING`.  
`logName` | Name of the log.  
`receiveTimestamp` | Time at which the log entry was received by Cloud Logging.  
  
### Amazon MSK

###  API Violation 
    
    
      {
      "insertId": "k3breb2q",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.pubsub.v1.IngestionFailureEvent",
        "awsMskFailure": {
          "apiViolationReason": {},
          "clusterArn": "arn:aws:kafka:us-east-1:291552718126:cluster/cluster-ingestion/abb9faea-4070-4eb76-9c21-f98abca92eaf-2",
          "kafkaTopic": "msk-topic",
          "partitionId": "1",
          "offset": "11"
        },
        "errorMessage": "The value of an attribute in the message exceeded the maximum allowed size of 1024 bytes. Number of bytes in the value: 1025. Key: my header. Value: my very large value …",
        "topic": "projects/my-project/topics/msk-import-topic"
      },
      "resource": {
        "type": "pubsub_topic",
        "labels": {
          "topic_id": "msk-import-topic",
          "project_id": "my-project"
        }
      },
      "timestamp": "2025-02-03T16:18:14.693357960Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/pubsub.googleapis.com%2Fingestion_failures",
      "receiveTimestamp": "2025-02-03T16:18:16.241643258Z"
    }
    

Log field | Description  
---|---  
`insertId` | A unique identifier for the log entry.  
`jsonPayload.@type` | Identifies the event type. Always `type.googleapis.com/google.pubsub.v1.IngestionFailureEvent`.  
`jsonPayload.awsMskFailure.clusterArn` | The ARN of the cluster of the topic being ingested from.  
`jsonPayload.awsMskFailure.kafkaTopic` | The name of the Kafka topic being ingested from.  
`jsonPayload.awsMskFailure.partitionId` | The ID of the partition that contains the message that failed to be ingested.  
`jsonPayload.awsMskFailure.offset` | The offset within the partition of the message that failed to be ingested.  
`jsonPayload.awsMskFailure.apiViolationReason` | Contains details about the API violation. This field is left empty.  
`jsonPayload.topic` | The Pub/Sub topic.  
`jsonPayload.errorMessage` | A human-readable message.  
`resource.type` | Resource type, always `pubsub_topic`.  
`resource.labels.project_id` | Google Cloud project ID.  
`resource.labels.topic_id` | Pub/Sub topic ID.  
`timestamp` | Log entry generation timestamp.  
`severity` | Severity level which is `WARNING`.  
`logName` | Name of the log.  
`receiveTimestamp` | Time at which the log entry was received by Cloud Logging.  
  
### Azure Event Hubs

###  API Violation 
    
    
    {
      "insertId": "i1fbqnb12",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.pubsub.v1.IngestionFailureEvent",
        "azureEventHubsFailure": {
          "apiViolationReason": {},
          "namespace": "my-namespace",
          "eventHub": "my-event-hub",
          "partitionId": "1",
          "offset": "15"
        },
        "errorMessage": "The value of an attribute in the message exceeded the maximum allowed size of 1024 bytes. Number of bytes in the value: 1025. Key: my header. Value: my very large value …",
        "topic": "projects/my-project/topics/event-hubs-import-topic"
      },
      "resource": {
        "type": "pubsub_topic",
        "labels": {
          "topic_id": "event-hubs-import-topic",
          "project_id": "my-project"
        }
      },
      "timestamp": "2025-02-03T16:18:14.693357960Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/pubsub.googleapis.com%2Fingestion_failures",
      "receiveTimestamp": "2025-02-03T14:05:12.338211450Z"
    }
    

Log field | Description  
---|---  
`insertId` | A unique identifier for the log entry.  
`jsonPayload.@type` | Identifies the event type. Always `type.googleapis.com/google.pubsub.v1.IngestionFailureEvent`.  
`jsonPayload.azureEventHubsFailure.namespace` | The namespace containing the event hub being ingested from.  
`jsonPayload.azureEventHubsFailure.eventHub` | The name of the event hub being ingested from.  
`jsonPayload.azureEventHubsFailure.partitionId` | The ID of the partition that contains the message that failed to be ingested.  
`jsonPayload.azureEventHubsFailure.offset` | The offset within the partition of the message that failed to be ingested.  
`jsonPayload.azureEventHubsFailure.apiViolationReason` | Contains details about the API violation. This field is left empty.  
`jsonPayload.topic` | The Pub/Sub topic.  
`jsonPayload.errorMessage` | A human-readable message.  
`resource.type` | Resource type, always `pubsub_topic`.  
`resource.labels.project_id` | Google Cloud project ID.  
`resource.labels.topic_id` | Pub/Sub topic ID.  
`timestamp` | Log entry generation timestamp.  
`severity` | Severity level which is `WARNING`.  
`logName` | Name of the log.  
`receiveTimestamp` | Time at which the log entry was received by Cloud Logging.  
  
### Confluent Cloud

###  Text failure 
    
    
    {
      "insertId": "i1fbqnb14",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.pubsub.v1.IngestionFailureEvent",
        "confluentCloudFailure": {
          "apiViolationReason": {},
          "clusterId": "lma-1x18ae",
          "kafkaTopic": "confluent-topic",
          "partitionId": "1",
          "offset": "19"
        },
        "errorMessage": "The value of an attribute in the message exceeded the maximum allowed size of 1024 bytes. Number of bytes in the value: 1025. Key: my header. Value: my very large value …",
        "topic": "projects/my-project/topics/confluent-import-topic"
      },
      "resource": {
        "type": "pubsub_topic",
        "labels": {
          "topic_id": "confluent-import-topic",
          "project_id": "my-project"
        }
      },
      "timestamp": "2025-02-03T16:18:14.693357960Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/pubsub.googleapis.com%2Fingestion_failures",
      "receiveTimestamp": "2025-02-03T17:03:11.428221440Z"
    }
    

Log field | Description  
---|---  
`insertId` | A unique identifier for the log entry.  
`jsonPayload.@type` | Identifies the event type. Always `type.googleapis.com/google.pubsub.v1.IngestionFailureEvent`.  
`jsonPayload.confluentCloudFailure.clusterId` | The cluster ID containing the topic being ingested from.  
`jsonPayload.confluentCloudFailure.kafkaTopic` | The name of the Kafka topic being ingested from.  
`jsonPayload.confluentCloudFailure.partitionId` | The ID of the partition that contains the message that failed to be ingested.  
`jsonPayload.confluentCloudFailure.offset` | The offset within the partition of the message that failed to be ingested.  
`jsonPayload.confluentCloudFailure.apiViolationReason` | Contains details about the API violation. This field is left empty.  
`jsonPayload.topic` | The Pub/Sub topic.  
`jsonPayload.errorMessage` | A human-readable message.  
`resource.type` | Resource type, always `pubsub_topic`.  
`resource.labels.project_id` | Google Cloud project ID.  
`resource.labels.topic_id` | Pub/Sub topic ID.  
`timestamp` | Log entry generation timestamp.  
`severity` | Severity level which is `WARNING`.  
`logName` | Name of the log.  
`receiveTimestamp` | Time at which the log entry was received by Cloud Logging.  
  
_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
