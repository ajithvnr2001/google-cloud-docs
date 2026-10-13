---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-QueryParameter/
title: Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::QueryParameter (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:29.397959+00:00
---

# Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::QueryParameter (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-QueryParameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::QueryParameter (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1 API class Google::Cloud::GeminiDataAnalytics::V1::QueryParameter.

A query parameter message represents a parameter that can be used to parameterize a SQL query.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_type
    
    
    def data_type() -> ::String

**Returns**

  * (::String) — Required. The data type of the parameter, e.g. "STRING", "INT64", "DATE", etc. For valid values, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types). This will be used to populate google.cloud.bigquery.v2.QueryParameterType.type. 



### #data_type=
    
    
    def data_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The data type of the parameter, e.g. "STRING", "INT64", "DATE", etc. For valid values, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types). This will be used to populate google.cloud.bigquery.v2.QueryParameterType.type. 



**Returns**

  * (::String) — Required. The data type of the parameter, e.g. "STRING", "INT64", "DATE", etc. For valid values, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types). This will be used to populate google.cloud.bigquery.v2.QueryParameterType.type. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The description of the parameter that can be used by LLM to extract the parameter value from the user question. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the parameter that can be used by LLM to extract the parameter value from the user question. 



**Returns**

  * (::String) — Optional. The description of the parameter that can be used by LLM to extract the parameter value from the user question. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the parameter reference in the SQL query. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the parameter reference in the SQL query. 



**Returns**

  * (::String) — Required. The name of the parameter reference in the SQL query. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
