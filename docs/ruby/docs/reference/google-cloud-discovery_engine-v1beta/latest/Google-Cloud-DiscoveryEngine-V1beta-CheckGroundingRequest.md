---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CheckGroundingRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:52.684435+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CheckGroundingRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingRequest.

Request message for [GroundedGenerationService.CheckGrounding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GroundedGenerationService-Client#Google__Cloud__DiscoveryEngine__V1beta__GroundedGenerationService__Client_check_grounding_instance_ "Google::Cloud::DiscoveryEngine::V1beta::GroundedGenerationService::Client#check_grounding \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #answer_candidate
    
    
    def answer_candidate() -> ::String

**Returns**

  * (::String) — Answer candidate to check. It can have a maximum length of 4096 tokens. 



### #answer_candidate=
    
    
    def answer_candidate=(value) -> ::String

**Parameter**

  * **value** (::String) — Answer candidate to check. It can have a maximum length of 4096 tokens. 



**Returns**

  * (::String) — Answer candidate to check. It can have a maximum length of 4096 tokens. 



### #facts
    
    
    def facts() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::GroundingFact>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::GroundingFact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GroundingFact)>) — List of facts for the grounding check. We support up to 200 facts. 



### #facts=
    
    
    def facts=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::GroundingFact>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::GroundingFact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GroundingFact)>) — List of facts for the grounding check. We support up to 200 facts. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::GroundingFact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GroundingFact)>) — List of facts for the grounding check. We support up to 200 facts. 



### #grounding_config
    
    
    def grounding_config() -> ::String

**Returns**

  * (::String) — Required. The resource name of the grounding config, such as `projects/*/locations/global/groundingConfigs/default_grounding_config`. 



### #grounding_config=
    
    
    def grounding_config=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the grounding config, such as `projects/*/locations/global/groundingConfigs/default_grounding_config`. 



**Returns**

  * (::String) — Required. The resource name of the grounding config, such as `projects/*/locations/global/groundingConfigs/default_grounding_config`. 



### #grounding_spec
    
    
    def grounding_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CheckGroundingSpec)) — Configuration of the grounding check. 



### #grounding_spec=
    
    
    def grounding_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CheckGroundingSpec)) — Configuration of the grounding check. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::CheckGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CheckGroundingSpec)) — Configuration of the grounding check. 



### #user_labels
    
    
    def user_labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




### #user_labels=
    
    
    def user_labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The user labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
