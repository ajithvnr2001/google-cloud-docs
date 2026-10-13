---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.SourceConfig
title: Class SourceConfig (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:07.108083+00:00
---

# Class SourceConfig (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.SourceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SourceConfig (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    SourceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The source configuration for the standby Autonomous Database.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`autonomous_database` |  `str`   
Optional. The name of the primary Autonomous Database that is used to create a Peer Autonomous Database from a source.   
`automatic_backups_replication_enabled` |  `bool`   
Optional. This field specifies if the replication of automatic backups is enabled when creating a Data Guard.   
`source_type` |  `[google.cloud.oracledatabase_v1.types.SourceConfig.SourceType](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.SourceConfig.SourceType)`   
Optional. The source type of the Autonomous Database.   
`clone_type` |  `[google.cloud.oracledatabase_v1.types.SourceConfig.CloneType](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.SourceConfig.CloneType)`   
Optional. The clone type of the Autonomous Database. This field is only applicable in case of cloning   
`refreshable_mode` |  `[google.cloud.oracledatabase_v1.types.SourceConfig.RefreshableMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.SourceConfig.RefreshableMode)`   
Optional. The refresh mode of the clone.   
`auto_refresh_frequency_seconds` |  `int`   
Optional. The frequency in seconds a refreshable clone is refreshed after auto-refresh is enabled.   
`auto_refresh_point_lag_seconds` |  `int`   
Optional. The time, in seconds, the data of the automatic refreshable clone lags the primary database at the point of refresh. This field is a member of `oneof`_ `_auto_refresh_point_lag_seconds`.   
`auto_refresh_start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The date and time that auto-refreshing will begin for an Autonomous Database refreshable clone. This value controls only the start time for the first refresh operation.   
`autonomous_database_backup` |  `str`   
Optional. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup} Required when source_type is BACKUP_FROM_ID.   
`backup_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The timestamp specified for the point-in-time clone of the source Autonomous Database. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type and when use_latest_available_backup is false.   
`use_latest_available_backup` |  `bool`   
Optional. Clone from latest available backup timestamp. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type.   
  
## Classes 

### CloneType
    
    
    CloneType(value)

The clone type of the Autonomous Database.

### RefreshableMode
    
    
    RefreshableMode(value)

The refresh mode of a refreshable clone.

### SourceType
    
    
    SourceType(value)

Specifies the source of the database. For example, a clone or peer from an existing database. This enum may be expanded to include other source types in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
