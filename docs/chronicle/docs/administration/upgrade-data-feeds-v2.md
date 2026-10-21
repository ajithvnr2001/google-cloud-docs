---
url: https://docs.cloud.google.com/chronicle/docs/administration/upgrade-data-feeds-v2/
title: Upgrade cloud storage data feeds to the v2 connector framework \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:59.589733+00:00
---

# Upgrade cloud storage data feeds to the v2 connector framework  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/upgrade-data-feeds-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade cloud storage data feeds to the v2 connector framework

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

To improve the reliability, scalability, and performance of data ingestion pipelines, we are upgrading our cloud storage data feeds to the new v2 connector framework. This new framework uses Google Cloud [Storage Transfer Service (STS)](https://docs.cloud.google.com/storage-transfer/docs/overview).

## Benefits of the v2 connector framework

Upgrading to the v2 connector framework unlocks significant improvements for your data feeds, including the following:

  * **Enhanced polling efficiency** : Vastly improved efficiency when polling from sources like AWS.
  * **Improved reliability and security** : Real-time source credential validation makes sure that you have secure and reliable connections.
  * **Expanded identity support** : Built-in support for AWS federated identity.



## Migration timelines

We are discontinuing the v1 connector framework for the following legacy connectors: Cloud Storage, Amazon S3, Amazon SQS, and Azure Blob Storage.

Take note of the following key milestones:

  * **November 1, 2026 - End of support** : No further updates are provided to v1 feeds, and only best-effort support is available. We highly encourage migrating and taking actions so that Google can migrate your feeds before this date to avoid disruptions.
  * **March 15, 2027 - Permanent deactivation** : Legacy connectors reach their end of life. Any data feeds still using v1 connectors after this date cease to function and return an error message.



## Automatic migration and required actions

To facilitate a seamless transition, we provide automatic migration services for all active data feeds using legacy v1 connectors.

Depending on your source type, you must take the following actions to make sure that the automatic migration is successful:

  * **Cloud Storage** : Grant the specific permissions to your new service account as described in the [grant access to the service account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access) documentation.
  * **Amazon S3** : If your environment uses IP allowlisting, you must add the [STS IP ranges](https://www.gstatic.com/storage-transfer-service/ipranges.json) to your bucket policy. Follow the steps to [enable STS access for Amazon S3](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#enable-sts-access-for-amazon-s3-and-azure-storage).
  * **Amazon SQS** : The migration only supports SQS queues that contain messages from a single Amazon S3 bucket. If your queue receives messages from multiple buckets, create a separate feed for each bucket. Verify that your SQS queue is configured correctly and that the access credentials for both the SQS queue and the Amazon S3 bucket are identical.
  * **Microsoft Azure** : If you use firewalls or virtual networks, allow the [STS IP ranges](https://www.gstatic.com/storage-transfer-service/ipranges.json) by following the [Azure STS access instructions](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#enable-sts-access-for-amazon-s3-and-azure-storage).
  * **Failed feeds** : Review your current feeds and fix any that are failing due to incorrect credentials so that they can migrate successfully.



## Safety and reliability

The automatic migration process aims to prevent data loss. The migration features strict, built-in guardrails. Minimal data duplication during the brief duration of the migration window is expected.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
