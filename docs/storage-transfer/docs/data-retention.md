---
url: https://docs.cloud.google.com/storage-transfer/docs/data-retention/
title: Data retention \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:41.556552+00:00
---

# Data retention  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/data-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Support ](https://docs.cloud.google.com/storage-transfer/docs/support)



Send feedback 

#  Data retention Stay organized with collections  Save and categorize content based on your preferences. 

This document describes data that we retain while performing transfers for Storage Transfer Service. This data is necessary to complete transfers on your behalf, but isn't directly related to the data that you're transferring.

## User credentials

To complete a transfer job, you supply us with user credentials that we use to complete transfer jobs on your behalf. We encrypt and retain the user credentials for as long as a [`TransferJob`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#resource:-transferjob) exists. We delete the user credentials provided when the associated `TransferJob` is deleted.

The following account types are examples of user credentials that we retain for the duration of a `TransferJob` to complete work on your behalf:

  * Amazon S3
  * Microsoft Azure Storage



When using [federated identity](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3#federated_identity) to authenticate to Amazon S3, AWS provides temporary credentials to Storage Transfer Service. Temporary credentials expire after a set period, after which they cannot be used to access your S3 resources. See [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
