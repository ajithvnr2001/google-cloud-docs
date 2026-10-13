---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupProperties
title: Class CloudSqlInstanceBackupProperties (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:52.132462+00:00
---

# Class CloudSqlInstanceBackupProperties (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudSqlInstanceBackupProperties (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    CloudSqlInstanceBackupProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

## Attributes  
  
---  
**Name** | **Description**  
`database_installed_version` |  `str`   
Output only. The installed database version of the Cloud SQL instance when the backup was taken.   
`final_backup` |  `bool`   
Output only. Whether the backup is a final backup.   
`source_instance` |  `str`   
Output only. The source instance of the backup. Format: projects/{project}/instances/{instance}   
`instance_create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The instance creation timestamp.   
`instance_tier` |  `str`   
Output only. The tier (or machine type) for this instance. Example: `db-custom-1-3840`  
`instance_delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The instance delete timestamp.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
