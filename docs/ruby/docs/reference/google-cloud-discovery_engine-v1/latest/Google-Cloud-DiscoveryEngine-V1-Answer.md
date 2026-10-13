---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:15.137159+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::Answer (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::Answer.

Defines an answer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #answer_skipped_reasons
    
    
    def answer_skipped_reasons() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::AnswerSkippedReason>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::AnswerSkippedReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-AnswerSkippedReason)>) — Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. 



### #answer_skipped_reasons=
    
    
    def answer_skipped_reasons=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::AnswerSkippedReason>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::AnswerSkippedReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-AnswerSkippedReason)>) — Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::AnswerSkippedReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-AnswerSkippedReason)>) — Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. 



### #answer_text
    
    
    def answer_text() -> ::String

**Returns**

  * (::String) — The textual answer. 



### #answer_text=
    
    
    def answer_text=(value) -> ::String

**Parameter**

  * **value** (::String) — The textual answer. 



**Returns**

  * (::String) — The textual answer. 



### #citations
    
    
    def citations() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Citation>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Citation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Citation)>) — Citations. 



### #citations=
    
    
    def citations=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Citation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Citation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Citation)>) — Citations. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Citation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Citation)>) — Citations. 



### #complete_time
    
    
    def complete_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Protobuf-Timestamp)) — Output only. Answer completed timestamp. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Protobuf-Timestamp)) — Output only. Answer creation timestamp. 



### #grounding_score
    
    
    def grounding_score() -> ::Float

**Returns**

  * (::Float) — A score in the range of [0, 1] describing how grounded the answer is by the reference chunks. 



### #grounding_score=
    
    
    def grounding_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — A score in the range of [0, 1] describing how grounded the answer is by the reference chunks. 



**Returns**

  * (::Float) — A score in the range of [0, 1] describing how grounded the answer is by the reference chunks. 



### #grounding_supports
    
    
    def grounding_supports() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-GroundingSupport)>) — Optional. Grounding supports. 



### #grounding_supports=
    
    
    def grounding_supports=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-GroundingSupport)>) — Optional. Grounding supports. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::GroundingSupport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-GroundingSupport)>) — Optional. Grounding supports. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`



**Returns**

  * (::String) — Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`



### #query_understanding_info
    
    
    def query_understanding_info() -> ::Google::Cloud::DiscoveryEngine::V1::Answer::QueryUnderstandingInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::QueryUnderstandingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-QueryUnderstandingInfo)) — Query understanding information. 



### #query_understanding_info=
    
    
    def query_understanding_info=(value) -> ::Google::Cloud::DiscoveryEngine::V1::Answer::QueryUnderstandingInfo

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::Answer::QueryUnderstandingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-QueryUnderstandingInfo)) — Query understanding information. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::QueryUnderstandingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-QueryUnderstandingInfo)) — Query understanding information. 



### #references
    
    
    def references() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Reference>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference)>) — References. 



### #references=
    
    
    def references=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Reference>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference)>) — References. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Reference)>) — References. 



### #related_questions
    
    
    def related_questions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Suggested related questions. 



### #related_questions=
    
    
    def related_questions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Suggested related questions. 



**Returns**

  * (::Array<::String>) — Suggested related questions. 



### #safety_ratings
    
    
    def safety_ratings() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::SafetyRating>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::SafetyRating](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SafetyRating)>) — Optional. Safety ratings. 



### #safety_ratings=
    
    
    def safety_ratings=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::SafetyRating>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::SafetyRating](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SafetyRating)>) — Optional. Safety ratings. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::SafetyRating](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SafetyRating)>) — Optional. Safety ratings. 



### #state
    
    
    def state() -> ::Google::Cloud::DiscoveryEngine::V1::Answer::State

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-State)) — The state of the answer generation. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::DiscoveryEngine::V1::Answer::State

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::Answer::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-State)) — The state of the answer generation. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::Answer::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-State)) — The state of the answer generation. 



### #steps
    
    
    def steps() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Step>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Step](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Step)>) — Answer generation steps. 



### #steps=
    
    
    def steps=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Answer::Step>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Step](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Step)>) — Answer generation steps. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Answer::Step](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Answer-Step)>) — Answer generation steps. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
