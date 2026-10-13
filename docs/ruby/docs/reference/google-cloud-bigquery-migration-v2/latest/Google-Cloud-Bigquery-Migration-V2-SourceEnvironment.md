---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnvironment/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::SourceEnvironment (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:11.862889+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::SourceEnvironment (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SourceEnvironment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::SourceEnvironment (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::SourceEnvironment.

Represents the default source environment values for the translation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #default_database
    
    
    def default_database() -> ::String

**Returns**

  * (::String) — The default database name to fully qualify SQL objects when their database name is missing. 



### #default_database=
    
    
    def default_database=(value) -> ::String

**Parameter**

  * **value** (::String) — The default database name to fully qualify SQL objects when their database name is missing. 



**Returns**

  * (::String) — The default database name to fully qualify SQL objects when their database name is missing. 



### #metadata_store_dataset
    
    
    def metadata_store_dataset() -> ::String

**Returns**

  * (::String) — Optional. Expects a validQ BigQuery dataset ID that exists, e.g., project-123.metadata_store_123. If specified, translation will search and read the required schema information from a metadata store in this dataset. If metadata store doesn't exist, translation will parse the metadata file and upload the schema info to a temp table in the dataset to speed up future translation jobs. 



### #metadata_store_dataset=
    
    
    def metadata_store_dataset=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Expects a validQ BigQuery dataset ID that exists, e.g., project-123.metadata_store_123. If specified, translation will search and read the required schema information from a metadata store in this dataset. If metadata store doesn't exist, translation will parse the metadata file and upload the schema info to a temp table in the dataset to speed up future translation jobs. 



**Returns**

  * (::String) — Optional. Expects a validQ BigQuery dataset ID that exists, e.g., project-123.metadata_store_123. If specified, translation will search and read the required schema information from a metadata store in this dataset. If metadata store doesn't exist, translation will parse the metadata file and upload the schema info to a temp table in the dataset to speed up future translation jobs. 



### #schema_search_path
    
    
    def schema_search_path() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The schema search path. When SQL objects are missing schema name, translation engine will search through this list to find the value. 



### #schema_search_path=
    
    
    def schema_search_path=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The schema search path. When SQL objects are missing schema name, translation engine will search through this list to find the value. 



**Returns**

  * (::Array<::String>) — The schema search path. When SQL objects are missing schema name, translation engine will search through this list to find the value. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
