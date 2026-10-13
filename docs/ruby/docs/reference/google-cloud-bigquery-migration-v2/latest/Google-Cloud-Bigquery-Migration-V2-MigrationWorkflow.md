---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:08.510509+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow.

A migration workflow which specifies what needs to be done for an EDW migration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the workflow was created. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The display name of the workflow. This can be set to give a workflow a descriptive name. There is no guarantee or enforcement of uniqueness. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The display name of the workflow. This can be set to give a workflow a descriptive name. There is no guarantee or enforcement of uniqueness. 



**Returns**

  * (::String) — The display name of the workflow. This can be set to give a workflow a descriptive name. There is no guarantee or enforcement of uniqueness. 



### #last_update_time
    
    
    def last_update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the workflow was last updated. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Immutable. Identifier. The unique identifier for the migration workflow. The ID is server-generated.

Example: `projects/123/locations/us/workflows/345`




### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow::State

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow-State)) — Output only. That status of the workflow. 



### #tasks
    
    
    def tasks() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::Migration::V2::MigrationTask}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::Migration::V2::MigrationTask}) — The tasks in a workflow in a named map. The name (i.e. key) has no meaning and is merely a convenient way to address a specific task in a workflow. 



### #tasks=
    
    
    def tasks=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::Migration::V2::MigrationTask}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::Migration::V2::MigrationTask}) — The tasks in a workflow in a named map. The name (i.e. key) has no meaning and is merely a convenient way to address a specific task in a workflow. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::Migration::V2::MigrationTask}) — The tasks in a workflow in a named map. The name (i.e. key) has no meaning and is merely a convenient way to address a specific task in a workflow. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
