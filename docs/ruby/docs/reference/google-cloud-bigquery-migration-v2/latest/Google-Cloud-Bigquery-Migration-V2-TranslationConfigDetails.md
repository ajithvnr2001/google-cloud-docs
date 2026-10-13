---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationConfigDetails/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:14.327503+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationConfigDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::TranslationConfigDetails.

The translation config to capture necessary settings for a translation task and subtask.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #gcs_source_path
    
    
    def gcs_source_path() -> ::String

**Returns**

  * (::String) — The Cloud Storage path for a directory of files to translate in a task. 



### #gcs_source_path=
    
    
    def gcs_source_path=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud Storage path for a directory of files to translate in a task. 



**Returns**

  * (::String) — The Cloud Storage path for a directory of files to translate in a task. 



### #gcs_target_path
    
    
    def gcs_target_path() -> ::String

**Returns**

  * (::String) — The Cloud Storage path to write back the corresponding input files to. 



### #gcs_target_path=
    
    
    def gcs_target_path=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud Storage path to write back the corresponding input files to. 



**Returns**

  * (::String) — The Cloud Storage path to write back the corresponding input files to. 



### #name_mapping_list
    
    
    def name_mapping_list() -> ::Google::Cloud::Bigquery::Migration::V2::ObjectNameMappingList

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::ObjectNameMappingList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ObjectNameMappingList)) — The mapping of objects to their desired output names in list form. 



### #name_mapping_list=
    
    
    def name_mapping_list=(value) -> ::Google::Cloud::Bigquery::Migration::V2::ObjectNameMappingList

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::ObjectNameMappingList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ObjectNameMappingList)) — The mapping of objects to their desired output names in list form. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::ObjectNameMappingList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ObjectNameMappingList)) — The mapping of objects to their desired output names in list form. 



### #request_source
    
    
    def request_source() -> ::String

**Returns**

  * (::String) — The indicator to show translation request initiator. 



### #request_source=
    
    
    def request_source=(value) -> ::String

**Parameter**

  * **value** (::String) — The indicator to show translation request initiator. 



**Returns**

  * (::String) — The indicator to show translation request initiator. 



### #source_dialect
    
    
    def source_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::Dialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The dialect of the input files. 



### #source_dialect=
    
    
    def source_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::Dialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The dialect of the input files. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The dialect of the input files. 



### #source_env
    
    
    def source_env() -> ::Google::Cloud::Bigquery::Migration::V2::SourceEnv

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SourceEnv](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnv)) — The default source environment values for the translation. 



### #source_env=
    
    
    def source_env=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SourceEnv

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SourceEnv](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnv)) — The default source environment values for the translation. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SourceEnv](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnv)) — The default source environment values for the translation. 



### #target_dialect
    
    
    def target_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::Dialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The target dialect for the engine to translate the input to. 



### #target_dialect=
    
    
    def target_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::Dialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The target dialect for the engine to translate the input to. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect)) — The target dialect for the engine to translate the input to. 



### #target_types
    
    
    def target_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The types of output to generate, e.g. sql, metadata etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



### #target_types=
    
    
    def target_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The types of output to generate, e.g. sql, metadata etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



**Returns**

  * (::Array<::String>) — The types of output to generate, e.g. sql, metadata etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
