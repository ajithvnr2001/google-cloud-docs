---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference-ChunkInfo/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:16.622523+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference-ChunkInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo.

Chunk information.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #chunk
    
    
    def chunk() -> ::String

**Returns**

  * (::String) — Chunk resource name. 



### #chunk=
    
    
    def chunk=(value) -> ::String

**Parameter**

  * **value** (::String) — Chunk resource name. 



**Returns**

  * (::String) — Chunk resource name. 



### #content
    
    
    def content() -> ::String

**Returns**

  * (::String) — Chunk textual content. 



### #content=
    
    
    def content=(value) -> ::String

**Parameter**

  * **value** (::String) — Chunk textual content. 



**Returns**

  * (::String) — Chunk textual content. 



### #document_metadata
    
    
    def document_metadata() -> ::Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo::DocumentMetadata

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo::DocumentMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference-ChunkInfo-DocumentMetadata)) — Document metadata. 



### #document_metadata=
    
    
    def document_metadata=(value) -> ::Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo::DocumentMetadata

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo::DocumentMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference-ChunkInfo-DocumentMetadata)) — Document metadata. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::Reference::ChunkInfo::DocumentMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference-ChunkInfo-DocumentMetadata)) — Document metadata. 



### #relevance_score
    
    
    def relevance_score() -> ::Float

**Returns**

  * (::Float) — The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation. 



### #relevance_score=
    
    
    def relevance_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation. 



**Returns**

  * (::Float) — The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
