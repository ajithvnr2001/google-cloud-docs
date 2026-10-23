---
url: https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible/
title: Configure access to a source: S3-compatible storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:42.796278+00:00
---

# Configure access to a source: S3-compatible storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-s3-compatible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: S3-compatible storage Stay organized with collections  Save and categorize content based on your preferences. 

Transferring from S3-compatible sources requires an **access key ID** and a **secret access key**. These are passed to the transfer agent creation command.

The steps to obtain your access key ID and secret access key depend on your storage provider.

When creating your ID and key, make sure the account being used has the following minimum permissions:

  * Read-only permission on source objects, if you don't want to delete objects at source.
  * Full access to source objects, if you choose to delete objects at source as part of your transfer.



Transfers from S3-compatible sources require the installation of transfer agents on VMs close to the data source. You can install agents in Amazon EC2 or EKS within the same region as your bucket. You can also run agents on Google Cloud in the nearest region.

Transfer agents belong to an agent pool. See [Manage agent pools](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) to create an agent pool and install agents into the pool.

## What's next

  * [Transfer from S3-compatible storage to Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agent-based/s3-compatible)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
