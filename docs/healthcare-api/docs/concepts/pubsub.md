---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/pubsub/
title: Pub/Sub notifications \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:11.339726+00:00
---

# Pub/Sub notifications  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of using Pub/Sub to receive notifications when clinical events occur in a Cloud Healthcare API data store. To learn how to set up and use Pub/Sub messages, see [Configuring Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub).

## Overview

You can receive notifications using [Pub/Sub](https://docs.cloud.google.com/pubsub) when any of the following clinical events occur:

  * You store a DICOM instance in a DICOM store using the [`dicomStores.dicomWeb.studies.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/storeInstances) method.
  * You import a DICOM instance into a DICOM store using the [`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import) method.
  * A FHIR resource is created, patched, updated, or deleted in a FHIR store. However, notifications are not sent when a FHIR resource is [imported from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#importing_fhir_resources).
  * An HL7v2 message is ingested or created in an HL7v2 store.



Information about each event is added to the corresponding data store's Pub/Sub topic in the form of a message.

You can publish messages to any Pub/Sub topic in any project for which you have sufficient permissions. After the Pub/Sub topic receives the message, the message will be forwarded to any number of subscribers to the topic.

## DICOM notifications

For information on using Pub/Sub notifications with DICOM data, see [DICOM Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/dicom-pubsub).

## FHIR notifications

For information on using Pub/Sub notifications with FHIR data, see [FHIR Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/fhir-pubsub).

## HL7v2 notifications

The following diagram shows the flow of notifications that occur when an HL7v2 message is ingested or created:

![hl7v2_pubsub](https://docs.cloud.google.com/static/healthcare-api/images/hl7v2_pubsub.png)

  1. The Cloud Healthcare API ingests an HL7v2 message from a care system.
  2. The message is stored in an HL7v2 store.
  3. The HL7v2 store creates and sends a Pub/Sub message to the store's Pub/Sub topics that have a filter that matches the HL7v2 message.
  4. Pub/Sub forwards the Pub/Sub message to the topics' subscriptions.
  5. The subscribers receive a notification, in the form of a Pub/Sub message, from their subscription. Each subscription can have one or more subscribers for increased parallelism.



## Notification format

Notifications sent to a Pub/Sub topic consist of two parts:

  * **Attributes** : A set of key:value pairs describing the event. These values can be used to filter which events a client receives by [filtering messages from a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter).
  * **Data** : A string that contains an identifier for the relevant FHIR resource, DICOM instance, or HL7v2 message.



### DICOM instance data

When a DICOM instance is stored in a DICOM store, the following identifier is always included in the `data` field of the Pub/Sub message:
    
    
    projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/series/SERIES_UID/instances/INSTANCE_UID

Notifications for a stored DICOM instance do not contain any `attribute` values.

### HL7v2 message data and attributes

When an HL7v2 message is created or ingested into an HL7v2 store, the following identifier is always included in the `data` field of the Pub/Sub message:
    
    
    projects/PROJECT_ID/locations/us-central1/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/HL7V2_MESSAGE_ID

The following set of key:value pairs is always included in the Pub/Sub message's `attributes` field:

Attribute name | Possible values | Example | Description  
---|---|---|---  
`msgType` | Any HL7v2 message [type](https://www.hl7.org/special/committees/vocab/V26_Appendix_A.pdf). | `ADT` | The type of HL7v2 message that was created or ingested.  
  
## What's next

  * Read the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs).
  * For an in-depth explanation of Pub/Sub, see [What is Cloud Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
