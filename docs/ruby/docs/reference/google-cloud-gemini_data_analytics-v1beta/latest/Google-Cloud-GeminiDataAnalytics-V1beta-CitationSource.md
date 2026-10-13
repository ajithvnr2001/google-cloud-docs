---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-CitationSource/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::CitationSource (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:19.648376+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::CitationSource (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-CitationSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::CitationSource (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::CitationSource.

The source of the citation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #example_query
    
    
    def example_query() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::ExampleQuery

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::ExampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-ExampleQuery)) — Output only. The example query used as the source.

Note: The following fields are mutually exclusive: `example_query`, `uri`, `glossary_term`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #glossary_term
    
    
    def glossary_term() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::GlossaryTerm

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::GlossaryTerm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-GlossaryTerm)) — Output only. The glossary term used as the source.

Note: The following fields are mutually exclusive: `glossary_term`, `uri`, `example_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Output only. Unique identifier of the source. This ID is service-generated and is unique within the scope of a single `Citation` message. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — Output only. The title of the source. 



### #uri
    
    
    def uri() -> ::String

**Returns**

  * (::String) — Output only. The uri used as the source, such as a web grounding URL.

Note: The following fields are mutually exclusive: `uri`, `example_query`, `glossary_term`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
