---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:44.230057+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec.

Specification of tools that are used to serve the request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #image_generation_spec
    
    
    def image_generation_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::ImageGenerationSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::ImageGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-ImageGenerationSpec)) — Optional. Specification of the image generation tool. 



### #image_generation_spec=
    
    
    def image_generation_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::ImageGenerationSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::ImageGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-ImageGenerationSpec)) — Optional. Specification of the image generation tool. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::ImageGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-ImageGenerationSpec)) — Optional. Specification of the image generation tool. 



### #vertex_ai_search_spec
    
    
    def vertex_ai_search_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VertexAiSearchSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VertexAiSearchSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VertexAiSearchSpec)) — Optional. Specification of the Vertex AI Search tool. 



### #vertex_ai_search_spec=
    
    
    def vertex_ai_search_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VertexAiSearchSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VertexAiSearchSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VertexAiSearchSpec)) — Optional. Specification of the Vertex AI Search tool. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VertexAiSearchSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VertexAiSearchSpec)) — Optional. Specification of the Vertex AI Search tool. 



### #video_generation_spec
    
    
    def video_generation_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VideoGenerationSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VideoGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VideoGenerationSpec)) — Optional. Specification of the video generation tool. 



### #video_generation_spec=
    
    
    def video_generation_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VideoGenerationSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VideoGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VideoGenerationSpec)) — Optional. Specification of the video generation tool. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::VideoGenerationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-VideoGenerationSpec)) — Optional. Specification of the video generation tool. 



### #web_grounding_spec
    
    
    def web_grounding_spec() -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::WebGroundingSpec

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::WebGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-WebGroundingSpec)) — Optional. Specification of the web grounding tool. If field is present, enables grounding with web search. Works only if [Assistant.web_grounding_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant#Google__Cloud__DiscoveryEngine__V1beta__Assistant_web_grounding_type_instance_ "Google::Cloud::DiscoveryEngine::V1beta::Assistant#web_grounding_type \(method\)") is [WEB_GROUNDING_TYPE_GOOGLE_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_GOOGLE_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_GOOGLE_SEARCH \(constant\)") or [WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH \(constant\)"). 



### #web_grounding_spec=
    
    
    def web_grounding_spec=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::WebGroundingSpec

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::WebGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-WebGroundingSpec)) — Optional. Specification of the web grounding tool. If field is present, enables grounding with web search. Works only if [Assistant.web_grounding_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant#Google__Cloud__DiscoveryEngine__V1beta__Assistant_web_grounding_type_instance_ "Google::Cloud::DiscoveryEngine::V1beta::Assistant#web_grounding_type \(method\)") is [WEB_GROUNDING_TYPE_GOOGLE_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_GOOGLE_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_GOOGLE_SEARCH \(constant\)") or [WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH \(constant\)"). 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::StreamAssistRequest::ToolsSpec::WebGroundingSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-StreamAssistRequest-ToolsSpec-WebGroundingSpec)) — Optional. Specification of the web grounding tool. If field is present, enables grounding with web search. Works only if [Assistant.web_grounding_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant#Google__Cloud__DiscoveryEngine__V1beta__Assistant_web_grounding_type_instance_ "Google::Cloud::DiscoveryEngine::V1beta::Assistant#web_grounding_type \(method\)") is [WEB_GROUNDING_TYPE_GOOGLE_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_GOOGLE_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_GOOGLE_SEARCH \(constant\)") or [WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Assistant-WebGroundingType#Google__Cloud__DiscoveryEngine__V1beta__Assistant__WebGroundingType__WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH "Google::Cloud::DiscoveryEngine::V1beta::Assistant::WebGroundingType::WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH \(constant\)"). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
