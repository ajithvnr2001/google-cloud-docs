---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerSourceConfig/
title: Datastream V1 API - Class Google::Cloud::Datastream::V1::SqlServerSourceConfig (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:00.507193+00:00
---

# Datastream V1 API - Class Google::Cloud::Datastream::V1::SqlServerSourceConfig (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerSourceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1 API - Class Google::Cloud::Datastream::V1::SqlServerSourceConfig (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Datastream V1 API class Google::Cloud::Datastream::V1::SqlServerSourceConfig.

SQLServer data source configuration

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #change_tables
    
    
    def change_tables() -> ::Google::Cloud::Datastream::V1::SqlServerChangeTables

**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerChangeTables](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerChangeTables)) — CDC reader reads from change tables.

Note: The following fields are mutually exclusive: `change_tables`, `transaction_logs`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #change_tables=
    
    
    def change_tables=(value) -> ::Google::Cloud::Datastream::V1::SqlServerChangeTables

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::SqlServerChangeTables](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerChangeTables)) — CDC reader reads from change tables.

Note: The following fields are mutually exclusive: `change_tables`, `transaction_logs`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerChangeTables](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerChangeTables)) — CDC reader reads from change tables.

Note: The following fields are mutually exclusive: `change_tables`, `transaction_logs`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #exclude_objects
    
    
    def exclude_objects() -> ::Google::Cloud::Datastream::V1::SqlServerRdbms

**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to exclude from the stream. 



### #exclude_objects=
    
    
    def exclude_objects=(value) -> ::Google::Cloud::Datastream::V1::SqlServerRdbms

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to exclude from the stream. 



**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to exclude from the stream. 



### #include_objects
    
    
    def include_objects() -> ::Google::Cloud::Datastream::V1::SqlServerRdbms

**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to include in the stream. 



### #include_objects=
    
    
    def include_objects=(value) -> ::Google::Cloud::Datastream::V1::SqlServerRdbms

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to include in the stream. 



**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerRdbms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerRdbms)) — SQLServer objects to include in the stream. 



### #max_concurrent_backfill_tasks
    
    
    def max_concurrent_backfill_tasks() -> ::Integer

**Returns**

  * (::Integer) — Max concurrent backfill tasks. 



### #max_concurrent_backfill_tasks=
    
    
    def max_concurrent_backfill_tasks=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Max concurrent backfill tasks. 



**Returns**

  * (::Integer) — Max concurrent backfill tasks. 



### #max_concurrent_cdc_tasks
    
    
    def max_concurrent_cdc_tasks() -> ::Integer

**Returns**

  * (::Integer) — Max concurrent CDC tasks. 



### #max_concurrent_cdc_tasks=
    
    
    def max_concurrent_cdc_tasks=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Max concurrent CDC tasks. 



**Returns**

  * (::Integer) — Max concurrent CDC tasks. 



### #transaction_logs
    
    
    def transaction_logs() -> ::Google::Cloud::Datastream::V1::SqlServerTransactionLogs

**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerTransactionLogs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerTransactionLogs)) — CDC reader reads from transaction logs.

Note: The following fields are mutually exclusive: `transaction_logs`, `change_tables`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #transaction_logs=
    
    
    def transaction_logs=(value) -> ::Google::Cloud::Datastream::V1::SqlServerTransactionLogs

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::SqlServerTransactionLogs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerTransactionLogs)) — CDC reader reads from transaction logs.

Note: The following fields are mutually exclusive: `transaction_logs`, `change_tables`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::SqlServerTransactionLogs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-SqlServerTransactionLogs)) — CDC reader reads from transaction logs.

Note: The following fields are mutually exclusive: `transaction_logs`, `change_tables`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
