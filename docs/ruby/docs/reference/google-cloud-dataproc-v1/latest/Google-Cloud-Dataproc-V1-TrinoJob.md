---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-TrinoJob/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::TrinoJob (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:26.080360+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::TrinoJob (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-TrinoJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::TrinoJob (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::TrinoJob.

A Dataproc job for running [Trino](https://trino.io/) queries. **IMPORTANT** : The [Dataproc Trino Optional Component](https://cloud.google.com/dataproc/docs/concepts/components/trino) must be enabled when the cluster is created to submit a Trino job to the cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #client_tags
    
    
    def client_tags() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Trino client tags to attach to this query 



### #client_tags=
    
    
    def client_tags=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Trino client tags to attach to this query 



**Returns**

  * (::Array<::String>) — Optional. Trino client tags to attach to this query 



### #continue_on_failure
    
    
    def continue_on_failure() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



### #continue_on_failure=
    
    
    def continue_on_failure=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



**Returns**

  * (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



### #logging_config
    
    
    def logging_config() -> ::Google::Cloud::Dataproc::V1::LoggingConfig

**Returns**

  * ([::Google::Cloud::Dataproc::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-LoggingConfig)) — Optional. The runtime log config for job execution. 



### #logging_config=
    
    
    def logging_config=(value) -> ::Google::Cloud::Dataproc::V1::LoggingConfig

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-LoggingConfig)) — Optional. The runtime log config for job execution. 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-LoggingConfig)) — Optional. The runtime log config for job execution. 



### #output_format
    
    
    def output_format() -> ::String

**Returns**

  * (::String) — Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats 



### #output_format=
    
    
    def output_format=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats 



**Returns**

  * (::String) — Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats 



### #properties
    
    
    def properties() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI 



### #properties=
    
    
    def properties=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI 



### #query_file_uri
    
    
    def query_file_uri() -> ::String

**Returns**

  * (::String) — The HCFS URI of the script that contains SQL queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_file_uri=
    
    
    def query_file_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The HCFS URI of the script that contains SQL queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The HCFS URI of the script that contains SQL queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_list
    
    
    def query_list() -> ::Google::Cloud::Dataproc::V1::QueryList

**Returns**

  * ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_list=
    
    
    def query_list=(value) -> ::Google::Cloud::Dataproc::V1::QueryList

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
