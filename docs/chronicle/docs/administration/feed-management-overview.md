---
url: https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview/
title: Data feeds overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:13.974791+00:00
---

# Data feeds overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data feeds overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This page provides an overview of Google SecOps feed management. You can create and manage feeds using the feed management UI or the feed management API.

The feed management UI is built on the feed management API. You can use Google SecOps data feeds to ingest log data into your Google SecOps instance from the following sources:

  * Cloud Storage services that are supported by Google SecOps, such as Google Cloud Storage and Amazon S3
  * Third-party data sources that are supported by Google SecOps and accessed through API, such as Microsoft 365
  * Files accessible directly using HTTP(S) requests
  * Sources that support HTTPS push ingestion, such as webhooks, Pub/Sub, and Amazon Data Firehose. You can push logs using an HTTPS endpoint from these sources.



Each feed that you create is composed of a data _source type_ and a _log type_. Google Cloud Storage, third-party APIs, and HTTP-accessible files are examples of source types. For each data source type that Google SecOps supports, Google SecOps also supports specific log types. For example, for the Google Cloud Storage source type, Google SecOps supports the Carbon Black log type and many others. The list of supported log types varies by source type.

When you create a feed, you specify the source type, log type, required permissions, authentication details, and other information that is based on the log type. As part of its security design, Google SecOps stores user credentials (for example, credentials that you provide so that a Google SecOps feed can ingest log data from a third-party API) in [Secret Manager](https://docs.cloud.google.com/secret-manager).

**Note:** Each Google SecOps instance is deployed as a completely separate and isolated environment. Data and credentials are not shared or accessible between these isolated tenants.

If Google SecOps provides a [default parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) for the log type, then the ingested log data is stored in both Google SecOps Unified Data Model (UDM) format and raw log format.

## Supported source types and log types

**Note:** To restrict access using Google Cloud public IP range, open a support ticket.

Google SecOps supports the following source types:

**Feed source type** | **Description** | Third-party API | Ingest data from a third-party API.  
---|---  
Pub/Sub | Ingest data using a Pub/Sub push subscription.  
Google Cloud Storage (Deprecated) | Ingest data from a Google Cloud Storage bucket.  
  
**Note:** This connector is deprecated, and will be discontinued on March 15, 2027. We recommend using **Google Cloud Storage v2** for improved reliability, scalability, and performance.  
Amazon Data Firehose | Ingest data using Amazon Data Firehose.  
Amazon S3 (Deprecated) | Ingest data from an Amazon Simple Storage Service bucket.  
  
**Note:** This connector is deprecated, and will be discontinued on March 15, 2027. We recommend using **Amazon S3 v2** for improved reliability, scalability, and performance.  
Amazon SQS (Deprecated) | Ingest data from an Amazon Simple Queue Service queue whose entries point to files stored in S3.  
  
**Note:** This connector is deprecated, and will be discontinued on March 15, 2027. We recommend using **Amazon SQS v2** for improved reliability, scalability, and performance.  
Azure Blobstore (Deprecated) | Ingest data from Azure Blob Storage.  
  
**Note:** This connector is deprecated, and will be discontinued on March 15, 2027. We recommend using **Azure Blobstore v2** for improved reliability, scalability, and performance.  
HTTP(S) | Ingest data from files accessible by an HTTP(S) request. Do **not** use this source type to interact with third-party APIs. Use the `API` feed source type for third-party APIs supported by Google SecOps.  
Webhook | Ingest data using an HTTPS webhook.  
  
**Note:** Bucket-based feeds such as Cloud Storage, Amazon S3, and Azure Blobstore don't ingest logs in real-time. The log latency depends on the pull frequency of the corresponding feed.

There are several ways to view a list of supported log types:

  * **Google SecOps UI** : For information about how to view the list of supported log types for each source type, see [Add a feed](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#add-new-feed).

  * **API reference documentation** : To view a list of supported log types for third-party API feeds, see [Configuration by log type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#api-log-types).

  * **Feed Schema API** : To view log types for any source type, you can also use the [Feed Schema API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed-schema-api-reference).


**Note:** The log types listed in third-party endpoints in the Feed UI are not listed in any other Cloud Storage options like AWS S3, AWS SQS, Google Cloud Storage, and Azure Blob Store.

## Feed health and monitoring

To monitor the health of your data feeds and troubleshoot ingestion issues, you can inspect feed status details in the UI or view logs in Cloud Logging. For detailed analysis and troubleshooting of feed activity, see [Analyze feed activity with Cloud Logging](https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging).

## What's next

  * Learn how to [create and manage feeds using the feed management UI](https://docs.cloud.google.com/chronicle/docs/administration/feed-management).
  * Learn how to [create and manage feeds using the Feed management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
