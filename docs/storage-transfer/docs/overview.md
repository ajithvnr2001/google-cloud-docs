---
url: https://docs.cloud.google.com/storage-transfer/docs/overview/
title: Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:38.610854+00:00
---

# Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Storage Transfer Service Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service enables seamless data movement across object and file storage systems, including:

  * Amazon S3, Azure Blob Storage, or Cloud Storage to Cloud Storage
  * On-premises storage to Cloud Storage, or Cloud Storage to on-premises
  * Between on-premises storage systems
  * From publicly-accessible URLs to Cloud Storage
  * From HDFS to Cloud Storage



Storage Transfer Service is optimized for transfers involving more than 1TiB of data. For smaller transfers, see our [recommendations](https://docs.cloud.google.com/storage-transfer/docs/transfer-options).

With Storage Transfer Service, you can:

  * **Automate data transfers** : Eliminate the need for manual processes and custom scripts.
  * **Transfer data at scale** : Move petabytes of data quickly and reliably.
  * **Optimize network performance** : Choose between Google-managed transfers for simplicity or self-hosted agents for granular control over network routing and bandwidth consumption.
  * **Support diverse storage systems** : Transfer data seamlessly between cloud providers and on-premises environments.



* * *

## Use cases

**Migrating data to Cloud Storage** : Storage Transfer Service can be used to migrate data from other cloud storage providers, on-premises data centers, or HTTP/HTTPS URLs to Cloud Storage. 

**Backup** : Replicate your data to Google Cloud, or create a copy of a Cloud Storage bucket in another region

**Data processing pipelines** : Move data generated on other clouds, your data center, and the edge to Google Cloud for analytics using [BigQuery](https://docs.cloud.google.com/bigquery) or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc).

**Archival** : Move cold data from costly on-premises storage systems to Cloud Storage to reduce storage cost.

## Benefits

**Secure**

  * End-to-end encryption protects your data in transit. Storage Transfer Service supports TLS 1.3 for all HTTPS communication.
  * Data integrity validation ensures that your data is not corrupted during transfer.



**Performant**

  * Highly-parallelized architecture accelerates transfer speeds.
  * Automatic retries and load balancing ensure reliable transfers.



**Fully managed**

  * No need to manage infrastructure or write code.
  * Focus on your applications, not data transfer.



## Get started

Check to see if your [source and sink combination is supported](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks).

There are a number of ways that you can work with Storage Transfer Service:

  * The Google Cloud console
  * REST APIs
  * The `gcloud` command-line tool
  * Java and Python client libraries



See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) to get started.

## Service Level Agreement

Storage Transfer Service does not provide an SLA, including for transfer performance or latency, and some performance fluctuations may occur. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
