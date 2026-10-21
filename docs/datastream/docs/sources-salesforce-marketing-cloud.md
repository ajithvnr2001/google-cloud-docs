---
url: https://docs.cloud.google.com/datastream/docs/sources-salesforce-marketing-cloud/
title: Stream data from Salesforce Marketing Cloud \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:52.370951+00:00
---

# Stream data from Salesforce Marketing Cloud  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-salesforce-marketing-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Salesforce Marketing Cloud Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Datastream supports replicating data from Salesforce Marketing Cloud (formerly known as ExactTarget). Salesforce Marketing Cloud is a digital marketing platform that includes tools for email marketing, social media marketing, and cross-channel campaign management.

This page contains information about:

  * The key terms that you need to understand when replicating from Salesforce Marketing Cloud.
  * The behavior of how Datastream handles data that's being pulled from a Salesforce Marketing Cloud source.
  * The Salesforce Marketing Cloud versions that Datastream supports.
  * The objects that Datastream replicates.
  * Known limitations for using Salesforce Marketing Cloud as a source.



## Key terms

Salesforce Marketing Cloud is an entirely separate product from the standard Salesforce platform, featuring distinct concepts and APIs. To better understand how Datastream replicates data from Salesforce Marketing Cloud, and the objects it supports, familiarize yourself with the following terms:

  * **Asset** : a piece of content, such as an image, a document, a text file, or a code snippet stored in Content Builder.
  * **Content Builder** : a Salesforce tool that consolidates images, documents, and content in a single location for use in Salesforce Marketing Cloud.
  * **Campaign** : a collection of marketing activities and communications.
  * **Data extension** : a table within the application database that contains your data. Data extensions are used to store custom objects and data.
  * **Journey** : a multi-step marketing campaign that guides customers through a series of interactions.
  * **Polling interval** : the interval between consecutive polls for objects that support incremental synchronization.



## Behavior

Datastream uses the Salesforce Marketing Cloud REST APIs to replicate data.

When replicating data from a Salesforce Marketing Cloud source, the following behavior is observed:

  * **Initial load (backfill)** : Datastream retrieves all existing records for the selected objects. For large datasets, Datastream uses standard REST API queries with automatic pagination.
  * **Incremental synchronization (incremental sync)** : Datastream identifies new and updated records by polling the Salesforce Marketing Cloud API at regular intervals.
  * **Full periodic synchronization** : a separate interval for objects that don't support incremental sync, such as data extensions. These objects are replicated using a periodic full refresh.
  * Datastream replicates changes such as inserts and updates for the specified objects.



## Versions

Datastream supports Salesforce Marketing Cloud formerly known as ExactTarget.

## Supported objects

The following table lists the objects that Datastream supports and their replication types:

Object | Replication type  
---|---  
Assets  
 _Includes text, files, emails, and messages_ | Backfill, incremental sync  
Email definitions | Backfill, incremental sync  
Push definitions | Backfill, incremental sync  
OTT definitions | Backfill, incremental sync  
SMS definitions | Backfill, incremental sync  
Campaigns | Backfill, incremental sync  
Data extensions  
 _Also known as custom objects_ | Backfill, periodic full refresh  
Journeys | Backfill, incremental sync  
Security events | Backfill, incremental sync  
Audit events | Backfill, incremental sync  
Contacts | Backfill, incremental sync  
  
## Known limitations

Known limitations for using Salesforce Marketing Cloud as a source include:

  * Datastream doesn't support integration with Marketing Cloud Account Engagement.
  * Datastream doesn't support integration with Agentforce Marketing.
  * Datastream doesn't support replicating delete events.
  * Datastream doesn't support replicating SOAP-only objects, such as lists, subscriptions, and links.



## What's next

  * Learn how to [configure a Salesforce Marketing Cloud source](https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
