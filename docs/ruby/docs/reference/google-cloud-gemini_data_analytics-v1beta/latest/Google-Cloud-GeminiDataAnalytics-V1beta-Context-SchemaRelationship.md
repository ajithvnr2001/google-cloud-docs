---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:24.177282+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship.

The relationship between two tables, including referencing and referenced columns. This is a derived context retrieved from Dataplex Dataset Insights.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #confidence_score
    
    
    def confidence_score() -> ::Float

**Returns**

  * (::Float) — Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score. 



### #confidence_score=
    
    
    def confidence_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score. 



**Returns**

  * (::Float) — Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score. 



### #left_schema_paths
    
    
    def left_schema_paths() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list. 



### #left_schema_paths=
    
    
    def left_schema_paths=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list. 



### #right_schema_paths
    
    
    def right_schema_paths() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list. 



### #right_schema_paths=
    
    
    def right_schema_paths=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::SchemaPaths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-SchemaPaths)) — An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list. 



### #sources
    
    
    def sources() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::Source>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-Source)>) — Optional. Sources which generated the schema relation edge. 



### #sources=
    
    
    def sources=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::Source>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-Source)>) — Optional. Sources which generated the schema relation edge. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Context::SchemaRelationship::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Context-SchemaRelationship-Source)>) — Optional. Sources which generated the schema relation edge. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
