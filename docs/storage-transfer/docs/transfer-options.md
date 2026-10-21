---
url: https://docs.cloud.google.com/storage-transfer/docs/transfer-options/
title: Data transfer options \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:02.366299+00:00
---

# Data transfer options  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/transfer-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Data transfer options Stay organized with collections  Save and categorize content based on your preferences. 

Google offers multiple solutions for transferring your data to or from Cloud Storage, or between file systems.

Transfer scenario  |  Recommendation   
---|---  
Transferring from another cloud storage provider  |  Use Storage Transfer Service.   
Transferring less than 1 TB from on-premises  |  Use [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage).   
Transferring more than 1 TB from on-premises  |  Use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) or [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview).   
Transferring less than 1 TB from another Cloud Storage region  |  Use [gcloud storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage).   
Transferring more than 1 TB from another Cloud Storage region  |  Use Storage Transfer Service.   
  
Use this guidance as a starting point. The specific details of your transfer scenario will also help you determine which tool is more appropriate.

## Move or back up data from another cloud provider to Cloud Storage

We recommend using [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) to move or back up your data from other cloud storage providers to Cloud Storage.

We support transfers from the following cloud storage providers:

  * Amazon S3
  * Microsoft Azure Blob Storage



To get started, see [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## Move data between Cloud Storage buckets

We recommend using Storage Transfer Service to move large amounts of data between Cloud Storage buckets.

You can alternatively use the Google Cloud CLI to transfer between Cloud Storage buckets. This can be helpful for moving data between bucket locations.

To get started, see:

  * [Transfer between Cloud Storage buckets with Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage).

  * [Move data from one bucket to another](https://docs.cloud.google.com/storage/docs/moving-buckets#move-buckets) using the command line (`gcloud storage`).




## Move or back up data from on-premises storage

We offer several solutions for moving or backing up on-premises data, depending on your specific situation:

### Locations with good internet connectivity

We offer the following solutions for on-premises data:

  * You can use Storage Transfer Service. For file system transfers, you install a small piece of software, called an agent, on a machine with access to your file system. The agent runs within a Docker container and has access to your locally-mounted NFS data. We upload the data you specify to Cloud Storage.

To get started, see [Manage agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools).

  * You can use a Transfer Appliance with online mode enabled. You connect the Transfer Appliance to your network, and copy data directly to it. The appliance transfers the data you copy to it to Cloud Storage.

To get started, see the [Transfer Appliance documentation](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide).




### Locations with poor or no internet connectivity

We recommend using Transfer Appliance to move or back up your on-premises data if you have poor or no internet connectivity. You connect Transfer Appliance to your network, and copy data directly to it. When the appliance is full, you send it back to us to copy to Cloud Storage. When we finish copying your data, we wipe the device for its next use.

To get started, see the [Transfer Appliance documentation](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide).

## Transfer from Cloud to a file system

We recommend using Storage Transfer Service to move data from Cloud Storage to your file system storage. With this method, you install a small piece of software, called an agent, in your private data center. The agent runs within a Docker container and has access to your locally mounted NFS data. We download the data you specify from Cloud Storage.

To get started, see [Requirements for file system transfers](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up).

For small data sets you can use [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync). Use `gcloud storage rsync` to transfer data between Cloud Storage and other cloud storage providers, or between Cloud Storage and your file system data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
