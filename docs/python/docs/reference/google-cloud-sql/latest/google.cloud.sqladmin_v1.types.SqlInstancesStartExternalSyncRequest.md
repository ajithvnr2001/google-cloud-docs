---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.SqlInstancesStartExternalSyncRequest
title: Class SqlInstancesStartExternalSyncRequest (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:12.044372+00:00
---

# Class SqlInstancesStartExternalSyncRequest (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.SqlInstancesStartExternalSyncRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SqlInstancesStartExternalSyncRequest (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    SqlInstancesStartExternalSyncRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Instance start external sync request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`instance` |  `str`   
Cloud SQL instance ID. This does not include the project ID.   
`project` |  `str`   
ID of the project that contains the instance.   
`sync_mode` |  `[google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode)`   
External sync mode.   
`skip_verification` |  `bool`   
Whether to skip the verification step (VESS).   
`mysql_sync_config` |  `[google.cloud.sqladmin_v1.types.MySqlSyncConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.MySqlSyncConfig)`   
MySQL-specific settings for start external sync. This field is a member of `oneof`_ `sync_config`.   
`sync_parallel_level` |  `[google.cloud.sqladmin_v1.types.ExternalSyncParallelLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.ExternalSyncParallelLevel)`   
Optional. Parallel level for initial data sync. Currently only applicable for MySQL.   
`migration_type` |  `[google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType)`   
Optional. MigrationType configures the migration to use physical files or logical dump files. If not set, then the logical dump file configuration is used. Valid values are `LOGICAL` or `PHYSICAL`. Only applicable to MySQL.   
`replica_overwrite_enabled` |  `bool`   
Optional. MySQL only. True if end-user has confirmed that this SES call will wipe replica databases overlapping with the proposed selected_objects. If this field is not set and there are both overlapping and additional databases proposed, an error will be returned.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
