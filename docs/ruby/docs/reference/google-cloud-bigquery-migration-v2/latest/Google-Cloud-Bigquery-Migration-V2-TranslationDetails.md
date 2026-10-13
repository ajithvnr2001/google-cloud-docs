---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationDetails/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationDetails (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:14.575769+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationDetails (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TranslationDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TranslationDetails (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::TranslationDetails.

The translation details to capture the necessary settings for a translation job.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #source_environment
    
    
    def source_environment() -> ::Google::Cloud::Bigquery::Migration::V2::SourceEnvironment

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SourceEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnvironment)) — The default source environment values for the translation. 



### #source_environment=
    
    
    def source_environment=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SourceEnvironment

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SourceEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnvironment)) — The default source environment values for the translation. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SourceEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnvironment)) — The default source environment values for the translation. 



### #source_target_mapping
    
    
    def source_target_mapping() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::SourceTargetMapping>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::SourceTargetMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceTargetMapping)>) — The mapping from source to target SQL. 



### #source_target_mapping=
    
    
    def source_target_mapping=(value) -> ::Array<::Google::Cloud::Bigquery::Migration::V2::SourceTargetMapping>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Bigquery::Migration::V2::SourceTargetMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceTargetMapping)>) — The mapping from source to target SQL. 



**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::SourceTargetMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceTargetMapping)>) — The mapping from source to target SQL. 



### #suggestion_config
    
    
    def suggestion_config() -> ::Google::Cloud::Bigquery::Migration::V2::SuggestionConfig

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SuggestionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SuggestionConfig)) — The configuration for the suggestion if requested as a target type. 



### #suggestion_config=
    
    
    def suggestion_config=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SuggestionConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SuggestionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SuggestionConfig)) — The configuration for the suggestion if requested as a target type. 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SuggestionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SuggestionConfig)) — The configuration for the suggestion if requested as a target type. 



### #target_base_uri
    
    
    def target_base_uri() -> ::String

**Returns**

  * (::String) — The base URI for all writes to persistent storage. 



### #target_base_uri=
    
    
    def target_base_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The base URI for all writes to persistent storage. 



**Returns**

  * (::String) — The base URI for all writes to persistent storage. 



### #target_return_literals
    
    
    def target_return_literals() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of literal targets that will be directly returned to the response. Each entry consists of the constructed path, EXCLUDING the base path. Not providing a target_base_uri will prevent writing to persistent storage. 



### #target_return_literals=
    
    
    def target_return_literals=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of literal targets that will be directly returned to the response. Each entry consists of the constructed path, EXCLUDING the base path. Not providing a target_base_uri will prevent writing to persistent storage. 



**Returns**

  * (::Array<::String>) — The list of literal targets that will be directly returned to the response. Each entry consists of the constructed path, EXCLUDING the base path. Not providing a target_base_uri will prevent writing to persistent storage. 



### #target_types
    
    
    def target_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The types of output to generate, e.g. sql, metadata, lineage_from_sql_scripts, etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



### #target_types=
    
    
    def target_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The types of output to generate, e.g. sql, metadata, lineage_from_sql_scripts, etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



**Returns**

  * (::Array<::String>) — The types of output to generate, e.g. sql, metadata, lineage_from_sql_scripts, etc. If not specified, a default set of targets will be generated. Some additional target types may be slower to generate. See the documentation for the set of available target types. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
