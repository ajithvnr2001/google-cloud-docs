---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationTask/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationTask (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:07.496912+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationTask (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationTask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationTask (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::MigrationTask.

A single task for a migration which has details about the configuration of the task.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #assessment_task_details
    
    
    def assessment_task_details() -> ::Google::Cloud::Bigquery::Migration::V2::AssessmentTaskDetails

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::AssessmentTaskDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AssessmentTaskDetails)) — Task configuration for Assessment.

Note: The following fields are mutually exclusive: `assessment_task_details`, `translation_config_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #assessment_task_details=
    
    
    def assessment_task_details=(value) -> ::Google::Cloud::Bigquery::Migration::V2::AssessmentTaskDetails

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::AssessmentTaskDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AssessmentTaskDetails)) — Task configuration for Assessment.

Note: The following fields are mutually exclusive: `assessment_task_details`, `translation_config_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::AssessmentTaskDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AssessmentTaskDetails)) — Task configuration for Assessment.

Note: The following fields are mutually exclusive: `assessment_task_details`, `translation_config_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the task was created. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Output only. Immutable. The unique identifier for the migration task. The ID is server-generated. 



### #last_update_time
    
    
    def last_update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the task was last updated. 



### #metrics
    
    
    def metrics() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::TimeSeries>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::TimeSeries](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TimeSeries)>) — Output only. The metrics for the task. 



### #processing_error
    
    
    def processing_error() -> ::Google::Rpc::ErrorInfo

**Returns**

  * ([::Google::Rpc::ErrorInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Rpc-ErrorInfo)) — Output only. An explanation that may be populated when the task is in FAILED state. 



### #resource_error_count
    
    
    def resource_error_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number or resources with errors. Note: This is not the total number of errors as each resource can have more than one error. This is used to indicate truncation by having a `resource_error_count` that is higher than the size of `resource_error_details`. 



### #resource_error_details
    
    
    def resource_error_details() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::ResourceErrorDetail>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::ResourceErrorDetail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ResourceErrorDetail)>) — Output only. Provides details to errors and issues encountered while processing the task. Presence of error details does not mean that the task failed. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::Migration::V2::MigrationTask::State

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationTask::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationTask-State)) — Output only. The current state of the task. 



### #task_result
    
    
    def task_result() -> ::Google::Cloud::Bigquery::Migration::V2::MigrationTaskResult

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationTaskResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationTaskResult)) — Output only. The result of the task. 



### #total_processing_error_count
    
    
    def total_processing_error_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Count of all the processing errors in this task and its subtasks. 



### #total_resource_error_count
    
    
    def total_resource_error_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Count of all the resource errors in this task and its subtasks. 



### #translation_config_details
    
    
    def translation_config_details() -> ::Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationConfigDetails)) — Task configuration for CW Batch/Offline SQL Translation.

Note: The following fields are mutually exclusive: `translation_config_details`, `assessment_task_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #translation_config_details=
    
    
    def translation_config_details=(value) -> ::Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationConfigDetails)) — Task configuration for CW Batch/Offline SQL Translation.

Note: The following fields are mutually exclusive: `translation_config_details`, `assessment_task_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationConfigDetails)) — Task configuration for CW Batch/Offline SQL Translation.

Note: The following fields are mutually exclusive: `translation_config_details`, `assessment_task_details`, `translation_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #translation_details
    
    
    def translation_details() -> ::Google::Cloud::Bigquery::Migration::V2::TranslationDetails

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TranslationDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationDetails)) — Task details for unified SQL Translation.

Note: The following fields are mutually exclusive: `translation_details`, `assessment_task_details`, `translation_config_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #translation_details=
    
    
    def translation_details=(value) -> ::Google::Cloud::Bigquery::Migration::V2::TranslationDetails

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::TranslationDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationDetails)) — Task details for unified SQL Translation.

Note: The following fields are mutually exclusive: `translation_details`, `assessment_task_details`, `translation_config_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TranslationDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationDetails)) — Task details for unified SQL Translation.

Note: The following fields are mutually exclusive: `translation_details`, `assessment_task_details`, `translation_config_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of the task. This must be one of the supported task types.

Assessment:

    * `Assessment_Hive` \- Assessment for Hive.
    * `Assessment_Redshift` \- Assessment for Redshift.
    * `Assessment_Snowflake` \- Assessment for Snowflake.
    * `Assessment_Teradata_v2` \- Assessment for Teradata.
    * `Assessment_Oracle` \- Assessment for Oracle.
    * `Assessment_Hadoop` \- Assessment for Hadoop.
    * `Assessment_Informatica` \- Assessment for Informatica.

Translation: See [Supported Task Types](https://docs.cloud.google.com/bigquery/docs/api-sql-translator#supported_task_types) for a list of supported task types. 




### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the task. This must be one of the supported task types.

Assessment:

    * `Assessment_Hive` \- Assessment for Hive.
    * `Assessment_Redshift` \- Assessment for Redshift.
    * `Assessment_Snowflake` \- Assessment for Snowflake.
    * `Assessment_Teradata_v2` \- Assessment for Teradata.
    * `Assessment_Oracle` \- Assessment for Oracle.
    * `Assessment_Hadoop` \- Assessment for Hadoop.
    * `Assessment_Informatica` \- Assessment for Informatica.

Translation: See [Supported Task Types](https://docs.cloud.google.com/bigquery/docs/api-sql-translator#supported_task_types) for a list of supported task types. 




**Returns**

  * (::String) — The type of the task. This must be one of the supported task types.

Assessment:

    * `Assessment_Hive` \- Assessment for Hive.
    * `Assessment_Redshift` \- Assessment for Redshift.
    * `Assessment_Snowflake` \- Assessment for Snowflake.
    * `Assessment_Teradata_v2` \- Assessment for Teradata.
    * `Assessment_Oracle` \- Assessment for Oracle.
    * `Assessment_Hadoop` \- Assessment for Hadoop.
    * `Assessment_Informatica` \- Assessment for Informatica.

Translation: See [Supported Task Types](https://docs.cloud.google.com/bigquery/docs/api-sql-translator#supported_task_types) for a list of supported task types. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
