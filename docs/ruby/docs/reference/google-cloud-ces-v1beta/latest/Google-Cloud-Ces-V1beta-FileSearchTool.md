---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-FileSearchTool/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::FileSearchTool (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:23.600004+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::FileSearchTool (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-FileSearchTool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::FileSearchTool (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::FileSearchTool.

The file search tool allows the agent to search across the files uploaded by the app/agent developer. It has presets to give relatively good quality search over the uploaded files and summarization of the retrieved results.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #corpus_type
    
    
    def corpus_type() -> ::Google::Cloud::Ces::V1beta::FileSearchTool::CorpusType

**Returns**

  * ([::Google::Cloud::Ces::V1beta::FileSearchTool::CorpusType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-FileSearchTool-CorpusType)) — Optional. The type of the corpus. Default is FULLY_MANAGED. 



### #corpus_type=
    
    
    def corpus_type=(value) -> ::Google::Cloud::Ces::V1beta::FileSearchTool::CorpusType

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::FileSearchTool::CorpusType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-FileSearchTool-CorpusType)) — Optional. The type of the corpus. Default is FULLY_MANAGED. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::FileSearchTool::CorpusType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-FileSearchTool-CorpusType)) — Optional. The type of the corpus. Default is FULLY_MANAGED. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The tool description. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The tool description. 



**Returns**

  * (::String) — Optional. The tool description. 



### #file_corpus
    
    
    def file_corpus() -> ::String

**Returns**

  * (::String) — Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus} 



### #file_corpus=
    
    
    def file_corpus=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus} 



**Returns**

  * (::String) — Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus} 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The tool name. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The tool name. 



**Returns**

  * (::String) — Required. The tool name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
