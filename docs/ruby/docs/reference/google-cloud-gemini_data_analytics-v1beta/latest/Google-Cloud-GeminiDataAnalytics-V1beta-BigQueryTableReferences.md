---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryTableReferences/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReferences (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:24.985042+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReferences (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryTableReferences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReferences (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReferences.

Message representing references to BigQuery tables and property graphs. At least one of `table_references`, `property_graph_references`, or `search_scope` must be populated.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent_context_reference
    
    
    def agent_context_reference() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentContextReference

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentContextReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentContextReference)) — Optional. Parameters for retrieving data from Agent Context. 



### #agent_context_reference=
    
    
    def agent_context_reference=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::AgentContextReference

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentContextReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentContextReference)) — Optional. Parameters for retrieving data from Agent Context. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::AgentContextReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AgentContextReference)) — Optional. Parameters for retrieving data from Agent Context. 



### #property_graph_references
    
    
    def property_graph_references() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryPropertyGraphReference>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryPropertyGraphReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryPropertyGraphReference)>) — Optional. References to BigQuery graphs.

Note: "property graph" is the former name for BigQuery Graph. The field and message names retain the original term for backward compatibility; both refer to the same resource. 




### #property_graph_references=
    
    
    def property_graph_references=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryPropertyGraphReference>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryPropertyGraphReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryPropertyGraphReference)>) — Optional. References to BigQuery graphs.

Note: "property graph" is the former name for BigQuery Graph. The field and message names retain the original term for backward compatibility; both refer to the same resource. 




**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryPropertyGraphReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryPropertyGraphReference)>) — Optional. References to BigQuery graphs.

Note: "property graph" is the former name for BigQuery Graph. The field and message names retain the original term for backward compatibility; both refer to the same resource. 




### #table_references
    
    
    def table_references() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReference>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryTableReference)>) — Optional. References to BigQuery tables. 



### #table_references=
    
    
    def table_references=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReference>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryTableReference)>) — Optional. References to BigQuery tables. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::BigQueryTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-BigQueryTableReference)>) — Optional. References to BigQuery tables. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
