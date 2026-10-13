---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig/
title: Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::V1::PersistenceConfig (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:50.811981+00:00
---

# Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::V1::PersistenceConfig (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::V1::PersistenceConfig (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.1  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.2  0.14.0  0.13.2  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1 API class Google::Cloud::Redis::V1::PersistenceConfig.

Configuration of the persistence functionality.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #persistence_mode
    
    
    def persistence_mode() -> ::Google::Cloud::Redis::V1::PersistenceConfig::PersistenceMode

**Returns**

  * ([::Google::Cloud::Redis::V1::PersistenceConfig::PersistenceMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-PersistenceMode)) — Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. 



### #persistence_mode=
    
    
    def persistence_mode=(value) -> ::Google::Cloud::Redis::V1::PersistenceConfig::PersistenceMode

**Parameter**

  * **value** ([::Google::Cloud::Redis::V1::PersistenceConfig::PersistenceMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-PersistenceMode)) — Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. 



**Returns**

  * ([::Google::Cloud::Redis::V1::PersistenceConfig::PersistenceMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-PersistenceMode)) — Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. 



### #rdb_next_snapshot_time
    
    
    def rdb_next_snapshot_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Protobuf-Timestamp)) — Output only. The next time that a snapshot attempt is scheduled to occur. 



### #rdb_snapshot_period
    
    
    def rdb_snapshot_period() -> ::Google::Cloud::Redis::V1::PersistenceConfig::SnapshotPeriod

**Returns**

  * ([::Google::Cloud::Redis::V1::PersistenceConfig::SnapshotPeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-SnapshotPeriod)) — Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default. 



### #rdb_snapshot_period=
    
    
    def rdb_snapshot_period=(value) -> ::Google::Cloud::Redis::V1::PersistenceConfig::SnapshotPeriod

**Parameter**

  * **value** ([::Google::Cloud::Redis::V1::PersistenceConfig::SnapshotPeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-SnapshotPeriod)) — Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default. 



**Returns**

  * ([::Google::Cloud::Redis::V1::PersistenceConfig::SnapshotPeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Cloud-Redis-V1-PersistenceConfig-SnapshotPeriod)) — Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default. 



### #rdb_snapshot_start_time
    
    
    def rdb_snapshot_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. 



### #rdb_snapshot_start_time=
    
    
    def rdb_snapshot_start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1/latest/Google-Protobuf-Timestamp)) — Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
