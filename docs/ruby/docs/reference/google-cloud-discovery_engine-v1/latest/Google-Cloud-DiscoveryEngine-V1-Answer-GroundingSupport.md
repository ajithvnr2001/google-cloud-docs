---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-GroundingSupport/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:16.089932+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-GroundingSupport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport.

Grounding support for a claim in `answer_text`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_index
    
    
    def end_index() -> ::Integer

**Returns**

  * (::Integer) — Required. End of the claim, exclusive. 



### #end_index=
    
    
    def end_index=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. End of the claim, exclusive. 



**Returns**

  * (::Integer) — Required. End of the claim, exclusive. 



### #grounding_check_required
    
    
    def grounding_check_required() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates that this claim required grounding check. When the system decided this claim didn't require attribution/grounding check, this field is set to false. In that case, no grounding check was done for the claim and therefore `grounding_score`, `sources` is not returned. 



### #grounding_check_required=
    
    
    def grounding_check_required=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates that this claim required grounding check. When the system decided this claim didn't require attribution/grounding check, this field is set to false. In that case, no grounding check was done for the claim and therefore `grounding_score`, `sources` is not returned. 



**Returns**

  * (::Boolean) — Indicates that this claim required grounding check. When the system decided this claim didn't require attribution/grounding check, this field is set to false. In that case, no grounding check was done for the claim and therefore `grounding_score`, `sources` is not returned. 



### #grounding_score
    
    
    def grounding_score() -> ::Float

**Returns**

  * (::Float) — A score in the range of [0, 1] describing how grounded is a specific claim by the references. Higher value means that the claim is better supported by the reference chunks. 



### #grounding_score=
    
    
    def grounding_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — A score in the range of [0, 1] describing how grounded is a specific claim by the references. Higher value means that the claim is better supported by the reference chunks. 



**Returns**

  * (::Float) — A score in the range of [0, 1] describing how grounded is a specific claim by the references. Higher value means that the claim is better supported by the reference chunks. 



### #sources
    
    
    def sources() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::CitationSource>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::CitationSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-CitationSource)>) — Optional. Citation sources for the claim. 



### #sources=
    
    
    def sources=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::CitationSource>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::CitationSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-CitationSource)>) — Optional. Citation sources for the claim. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::CitationSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-CitationSource)>) — Optional. Citation sources for the claim. 



### #start_index
    
    
    def start_index() -> ::Integer

**Returns**

  * (::Integer) — Required. Index indicates the start of the claim, measured in bytes (UTF-8 unicode). 



### #start_index=
    
    
    def start_index=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. Index indicates the start of the claim, measured in bytes (UTF-8 unicode). 



**Returns**

  * (::Integer) — Required. Index indicates the start of the claim, measured in bytes (UTF-8 unicode). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
