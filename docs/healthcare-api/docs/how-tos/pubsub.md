---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub/
title: Configuring Pub/Sub notifications \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:36.335761+00:00
---

# Configuring Pub/Sub notifications  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Configuring Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can use Pub/Sub to receive notifications when clinical events occur in Cloud Healthcare API data stores. These notifications inform you when:

  * A DICOM instance is stored in a DICOM store using the [`dicomStores.dicomWeb.studies.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/storeInstances) method or [imported from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export#importing_dicom_objects) with [`dicomStores.notificationConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/NotificationConfig).
  * A DICOM instance is stored, imported, updated, or deleted in a DICOM store using [`dicomStores.notificationConfigs`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#DicomNotificationConfig).
  * A FHIR resource is created, updated, or deleted in a FHIR store. However, notifications are not sent when a FHIR resource is [imported from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#importing_fhir_resources).
  * An HL7v2 message is ingested or created in an HL7v2 store for the first time. Duplicate messages will not trigger a notification.



When one of these events occurs, the Cloud Healthcare API publishes a message to a named Pub/Sub resource called a _topic_. The message can then be received by applications _subscribed_ to the topic.

For DICOM and HL7v2, these messages do not contain any personal information. They only include the following:

  * The project for which the message is generated
  * The message ID
  * In HL7v2 messages, the HL7v2 message type



FHIR Pub/Sub messages can contain personal information. For more information, see FHIR notifications containing FHIR resource data.

For an overview of using Pub/Sub notifications with the Cloud Healthcare API, see [Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/concepts/pubsub).

**Note:** This page uses "notifications" and "Pub/Sub messages" interchangeably. All notifications are Pub/Sub messages. Using Pub/Sub with the Cloud Healthcare API to receive notifications of clinical events in your data stores is simply the most common use case.

## Before you begin

### Review Pub/Sub quotas

Before configuring Pub/Sub notifications, familiarize yourself with [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas). For information about how to view quotas, requesting higher quota values, and what happens if you run out of quota, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

### Enable the Pub/Sub API

To enable the Pub/Sub API, click the following button:

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)

### Configure Pub/Sub permissions

To allow messages to be published from the Cloud Healthcare API to Pub/Sub, you must add the `pubsub.publisher` role to your project's **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). See [DICOM, FHIR, and HL7v2 store Pub/Sub permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions) for steps to add the required role.

### Create a Pub/Sub topic

For each data store for which you want to receive notifications, you must configure a Pub/Sub topic. Individual data stores can have their own Pub/Sub topic, or multiple data stores can share the same topic. You can create a topic using the Google Cloud console or the Google Cloud CLI.

When you create a topic, or refer to a topic in a data store's configuration, you need to use a qualified URI in the following format:
    
    
    projects/PROJECT_ID/topics/TOPIC_NAME

where PROJECT_ID is your Google Cloud project ID and TOPIC_NAME is the name of the topic.

To create a topic, complete the following steps:

### Console

  1. Go to the Pub/Sub **Topics** page in the Google Cloud console.

[Go to the Pub/Sub topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click **Create Topic**.

  3. Enter a topic name with the URI:

`projects/PROJECT_ID/topics/TOPIC_NAME`

where PROJECT_ID is your Google Cloud project ID.

  4. Click **Create**.




### gcloud

To create a topic, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
    
    
    gcloud pubsub topics create projects/PROJECT_ID/topics/TOPIC_NAME

If the request is successful, the command returns the following output:
    
    
    Created topic [projects/PROJECT_ID/topics/TOPIC_NAME].

### Create a Pub/Sub subscription

To receive messages published to a topic, you need to create a Pub/Sub [subscription](https://docs.cloud.google.com/pubsub/docs/subscriber). Every Pub/Sub topic should have at least one Pub/Sub subscription.

The subscription connects the topic to a subscriber application that receives and processes messages published to the topic.

Subscriptions can be configured to use a [push model](https://docs.cloud.google.com/pubsub/docs/push) or a [pull model](https://docs.cloud.google.com/pubsub/docs/pull).

Subscriptions can be configured to filter messages based on their attributes; see instructions on [filtering messages from a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter).

To create a subscription, complete the following steps:

### Console

  1. Go to the Pub/Sub **Topics** page in the Google Cloud console.

[Go to the Pub/Sub topics page](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click your project's topic.

  3. Click **Create Subscription**.

  4. Enter a subscription name:

`projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME`

Leave **Delivery Type** set to **Pull**.

  5. Click **Create**.




### gcloud

To create a topic, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command:
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_NAME --topic=TOPIC_NAME

**Note:** Use the optional flag `--ack-deadline` to configure the number of seconds the system waits for acknowledgement from the subscriber before re-attempting delivery. Without this flag, the default deadline is 10 seconds.

If the request is successful, the command returns the following output:
    
    
    Created subscription [projects/PROJECT_ID/subscriptions/TOPIC_NAME].

## View stored DICOM instance notifications

For information on using Pub/Sub notifications with DICOM data, see [DICOM Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/dicom-pubsub).

## View HL7v2 notifications

The [`Hl7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores) resource contains an array [`notificationConfigs`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#Hl7V2Store.FIELDS.notification_configs) where you can specify Pub/Sub topics and filtering criteria.

When an HL7v2 message is ingested or created in an HL7v2 store, the Cloud Healthcare API publishes a message to the Pub/Sub topics that have a filter that matches the HL7v2 message.

To view a notification for an ingested HL7v2 message, complete the following steps:

  1. [Create](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#creating_an_hl7v2_store) or [edit](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#editing_an_hl7v2_store) an HL7v2 store and configure it with a Pub/Sub topic.
  2. [Add the required `pubsub.publisher` role to your project's service account](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions).
  3. [Ingest an HL7v2 message](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#ingesting_hl7v2_messages) into the HL7v2 store. This triggers the Cloud Healthcare API to publish a message to the configured Pub/Sub topic.
  4. To view the message published to the Pub/Sub topic, run the [`gcloud pubsub subscriptions pull`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull) command:
         
         gcloud pubsub subscriptions pull --auto-ack projects/PROJECT_ID/subscriptions/PUBSUB_SUBSCRIPTION

The command returns the following output about the ingested HL7v2 message:
         
         ┌--------------------------------------------------------------------------------------------------------------------|-----------------|---------------┐
         |                                                                 DATA                                               |    MESSAGE_ID   |   ATTRIBUTES  |
         ├--------------------------------------------------------------------------------------------------------------------|-----------------|---------------|
         | projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_MESSAGE_ID | 123456789012345 | msgType=TYPE  |
         └--------------------------------------------------------------------------------------------------------------------|-----------------|---------------┘




## Cloud Healthcare API and Pub/Sub message storage policy

To ensure that your Cloud Healthcare API data and the associated data in Pub/Sub messages reside in the same region, you must set a Pub/Sub [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

You must explicitly set the message storage policy on the Pub/Sub topic configured on the data store to ensure that the data stays in the same region. For example, if your Cloud Healthcare API dataset and FHIR store are in `us-central1`, the message storage policy must only allow the `us-central1` region.

To configure a message storage policy, see [Configuring message store policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#configuring_message_storage_policies).

## Troubleshoot missed Pub/Sub messages

If a notification can't be published to Pub/Sub, an error is logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If the rate of error generation exceeds a limit, errors in excess of the limit aren't submitted to Cloud Logging.

## What's next

Learn how to configure a Pub/Sub topic in:

  * [A DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom#editing_a_dicom_store)
  * [A FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir#editing_a_fhir_store)
  * [An HL7v2 store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#editing_an_hl7v2_store)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
