---
url: https://docs.cloud.google.com/oracle/database/docs/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:06.117458+00:00
---

# Customer-managed encryption keys (CMEK)  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google Cloud customer-managed encryption keys (CMEK) for Oracle Database@Google Cloud.

Oracle Database@Google Cloud provides the following encryption options to encrypt your data:

  * Google Cloud CMEK: this encryption option lets you manage your keys using [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). You can use this option when you need to control the lifecycle of your encryption keys to meet specific organizational standards. You can grant, revoke, and rotate keys on your own schedule. This page provides an overview of Google Cloud CMEK. To learn how to use it, see [Use CMEK](https://docs.cloud.google.com/oracle/database/docs/use-cmek).
  * Oracle-managed encryption: this encryption option lets you use Oracle-managed encryption options, such as Oracle Vault or Oracle Wallet. To learn about Oracle-managed encryption options, refer to Oracle documentation.



## Google Cloud CMEK

Google Cloud CMEK uses [Cloud KMS](https://docs.cloud.google.com/kms/docs). Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. You own, control, and manage the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data in Cloud KMS.

You can use Google Cloud CMEK with the following Oracle Database@Google Cloud resources:

  * Exadata VM Clusters
  * Exascale VM Clusters
  * Autonomous AI Databases



## About service accounts

To enable Google Cloud CMEK on your Oracle Database@Google Cloud resources, you need to use a service account to request key access from Cloud KMS. This lets you grant precise IAM permissions to Oracle databases to access Google Cloud services.

When you provision an Oracle Database@Google Cloud resource, a service account is automatically created which you can use to enable CMEK on that resource only. The service account has no permissions assigned in your project, so you will need to [assign permissions to the service account](https://docs.cloud.google.com/oracle/database/docs/use-cmek) before it can use a key.

For an Exadata VM Cluster and Exascale VM Cluster, the service account is managed by Google Cloud, and for an Autonomous AI Database, the service account is managed by Oracle.

## Pricing

Using CMEK with Cloud KMS may incur additional costs, depending on your usage patterns. Learn more about [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Key unavailability

**Caution:** If a Cloud KMS key is deleted, any Oracle Database@Google Cloud resources encrypted with that key become permanently inaccessible.

If you disable the Cloud KMS key that is used to encrypt an Oracle Database@Google Cloud resource, it will experience downtime within 30 minutes. Re-enabling the key brings the resource back up.

In rare scenarios, such as during periods when Cloud KMS is unavailable, Oracle Database@Google Cloud might be unable to retrieve the status of your key from Cloud KMS.

After 30 minutes, if Oracle Database@Google Cloud is still unable to connect with Cloud KMS, Oracle Database@Google Cloud begins taking the resources offline as a protective measure. The data in your resource remains inaccessible until your resource can reconnect with Cloud KMS and Cloud KMS responds that the key is active.

If you have insufficient permissions, then also the resources might be inaccessible.

## What's next

  * Learn how to [use CMEK](https://docs.cloud.google.com/oracle/database/docs/use-cmek) with your Oracle Database@Google Cloud resources.
  * Learn about [Cloud KMS](https://docs.cloud.google.com/kms/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
