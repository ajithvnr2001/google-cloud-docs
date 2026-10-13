---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendResponse-RecommendationResult/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::RecommendResponse::RecommendationResult (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:47.213113+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::RecommendResponse::RecommendationResult (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendResponse-RecommendationResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::RecommendResponse::RecommendationResult (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::RecommendResponse::RecommendationResult.

RecommendationResult represents a generic recommendation result with associated metadata.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #document
    
    
    def document() -> ::Google::Cloud::DiscoveryEngine::V1beta::Document

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Set if `returnDocument` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)"). 



### #document=
    
    
    def document=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::Document

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Set if `returnDocument` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)"). 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Set if `returnDocument` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)"). 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Resource ID of the recommended Document. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Resource ID of the recommended Document. 



**Returns**

  * (::String) — Resource ID of the recommended Document. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::Google::Protobuf::Value}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Protobuf::Value}) — 

Additional Document metadata or annotations.

Possible values:

    * `score`: Recommendation score in double value. Is set if `returnScore` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)").



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::Google::Protobuf::Value}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Protobuf::Value}) — 

Additional Document metadata or annotations.

Possible values:

    * `score`: Recommendation score in double value. Is set if `returnScore` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)").



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Protobuf::Value}) — 

Additional Document metadata or annotations.

Possible values:

    * `score`: Recommendation score in double value. Is set if `returnScore` is set to true in [RecommendRequest.params](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-RecommendRequest#Google__Cloud__DiscoveryEngine__V1beta__RecommendRequest_params_instance_ "Google::Cloud::DiscoveryEngine::V1beta::RecommendRequest#params \(method\)").



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
