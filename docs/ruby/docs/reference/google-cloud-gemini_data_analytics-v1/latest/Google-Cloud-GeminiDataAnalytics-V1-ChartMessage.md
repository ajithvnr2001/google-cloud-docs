---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartMessage/
title: Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::ChartMessage (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:51.201391+00:00
---

# Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::ChartMessage (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::ChartMessage (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1 API class Google::Cloud::GeminiDataAnalytics::V1::ChartMessage.

A message produced during chart generation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #query
    
    
    def query() -> ::Google::Cloud::GeminiDataAnalytics::V1::ChartQuery

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::ChartQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartQuery)) — A query for generating a chart.

Note: The following fields are mutually exclusive: `query`, `result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query=
    
    
    def query=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1::ChartQuery

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1::ChartQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartQuery)) — A query for generating a chart.

Note: The following fields are mutually exclusive: `query`, `result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::ChartQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartQuery)) — A query for generating a chart.

Note: The following fields are mutually exclusive: `query`, `result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result
    
    
    def result() -> ::Google::Cloud::GeminiDataAnalytics::V1::ChartResult

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::ChartResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartResult)) — The result of a chart generation query.

Note: The following fields are mutually exclusive: `result`, `query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result=
    
    
    def result=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1::ChartResult

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1::ChartResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartResult)) — The result of a chart generation query.

Note: The following fields are mutually exclusive: `result`, `query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::ChartResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-ChartResult)) — The result of a chart generation query.

Note: The following fields are mutually exclusive: `result`, `query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
