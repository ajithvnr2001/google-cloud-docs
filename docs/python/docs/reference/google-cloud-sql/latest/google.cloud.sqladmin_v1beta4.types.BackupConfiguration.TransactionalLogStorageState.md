---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupConfiguration.TransactionalLogStorageState
title: Class TransactionalLogStorageState (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:23.070244+00:00
---

# Class TransactionalLogStorageState (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupConfiguration.TransactionalLogStorageState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TransactionalLogStorageState (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    TransactionalLogStorageState(value)

This value contains the storage location of the transactional logs used to perform point-in-time recovery (PITR) for the database.

## Enums  
  
---  
**Name** | **Description**  
`TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED` | Unspecified.  
`DISK` | The transaction logs used for PITR for the instance are stored on a data disk.  
`SWITCHING_TO_CLOUD_STORAGE` | The transaction logs used for PITR for the instance are switching from being stored on a data disk to being stored in Cloud Storage. Only applicable to MySQL.  
`SWITCHED_TO_CLOUD_STORAGE` | The transaction logs used for PITR for the instance are now stored in Cloud Storage. Previously, they were stored on a data disk. Only applicable to MySQL.  
`CLOUD_STORAGE` | The transaction logs used for PITR for the instance are stored in Cloud Storage. Only applicable to MySQL and PostgreSQL.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
