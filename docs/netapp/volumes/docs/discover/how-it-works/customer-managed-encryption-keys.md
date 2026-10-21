---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/customer-managed-encryption-keys/
title: Volume replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:56:19.405597+00:00
---

# Volume replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/customer-managed-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Volume replication Stay organized with collections  Save and categorize content based on your preferences. 

NetApp Volumes always encrypts your data with volume-specific keys. Your data is always encrypted at rest.

With customer-managed encryption keys (CMEK), volume keys are wrapped using your keys stored in Cloud KMS. This feature gives you greater control over the encryption keys used and the added security of storing the keys on a system or in a location different from the data. NetApp Volumes supports Cloud KMS capabilities such as hardware security modules, External Key Manager, and the full key management lifecycle—generate, use, rotate, destroy.

NetApp Volumes supports one CMEK policy per region. A CMEK policy is attached to a storage pool and all volumes created in that pool use it. You can have a mix of storage pools with and without CMEK policies in a region. If you have pools without CMEK in a specific region, you can convert them to CMEK by using the migration action of a region's CMEK policy.

Using customer-managed encryption keys is optional.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
