---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListSchemasResponse/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListSchemasResponse (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:50.854737+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListSchemasResponse (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListSchemasResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListSchemasResponse (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::ListSchemasResponse.

Response message for [SchemaService.ListSchemas](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SchemaService-Client#Google__Cloud__DiscoveryEngine__V1__SchemaService__Client_list_schemas_instance_ "Google::Cloud::DiscoveryEngine::V1::SchemaService::Client#list_schemas \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token that can be sent as [ListSchemasRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListSchemasRequest#Google__Cloud__DiscoveryEngine__V1__ListSchemasRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListSchemasRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token that can be sent as [ListSchemasRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListSchemasRequest#Google__Cloud__DiscoveryEngine__V1__ListSchemasRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListSchemasRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token that can be sent as [ListSchemasRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListSchemasRequest#Google__Cloud__DiscoveryEngine__V1__ListSchemasRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListSchemasRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #schemas
    
    
    def schemas() -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Schema>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Schema)>) — The {::Google::Cloud::DiscoveryEngine::V1::Schema Schema}s. 



### #schemas=
    
    
    def schemas=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1::Schema>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Schema)>) — The {::Google::Cloud::DiscoveryEngine::V1::Schema Schema}s. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Schema)>) — The {::Google::Cloud::DiscoveryEngine::V1::Schema Schema}s. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
