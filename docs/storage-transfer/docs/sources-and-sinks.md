---
url: https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks/
title: Sources and sinks \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:03.061431+00:00
---

# Sources and sinks  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Sources and sinks Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can transfer data from a number of sources to a number of destinations. The table below details the supported sources and destinations.

Storage system | Source | Destination | Notes  
---|---|---|---  
Cloud Storage | check_circle | check_circle | Cloud Storage is a valid sink for transfers from all sources. Transfers from Cloud Storage, Amazon S3, and Azure to Cloud Storage do not require agents or agent pools; they are managed entirely by Storage Transfer Service. To configure Cloud Storage as a source and/or sink, refer to the following pages:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)

  
Amazon Simple Storage Service (Amazon S3) | check_circle |  | Transfers to Cloud Storage only. Does not require agents or agent pools. To configure Amazon S3, refer to [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3).  
S3-compatible storage | check_circle |  | Transfers to Cloud Storage only. Requires agents and agent pools. To configure S3-compatible storage, refer to [Configure access to a source: S3-compatible storage](https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible).  
Azure Blob Storage, including Azure Data Lake Storage Gen2 | check_circle |  | Transfers to Cloud Storage only. Does not require agents or agent pools. To configure Azure storage options, refer to [Configure access to a source: Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure).  
Publicly accessible or signed HTTP and HTTPs URLs | check_circle |  | Storage Transfer Service accepts a TSV file specifying a list of URLs to transfer. Transfers to Cloud Storage only. Does not require agents or agent pools. See [Create a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list) for details.  
File system | check_circle | check_circle | Storage Transfer Service supports transfers:

  * From file systems to Cloud Storage
  * From Cloud Storage to file systems
  * Between two file systems

Transfers involving file systems require agents and agent pools. See [Manage agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) to get started.   
Hadoop distributed file system (HDFS) | check_circle |  | Transfers to Cloud Storage only. Requires agents and agent pools.  To configure a transfer from an HDFS source, refer to [Transfer from HDFS to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/hdfs).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
