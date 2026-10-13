---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:21.871559+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest.

Request for ListControls method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — 

Optional. A filter to apply on the list results. Supported features:

    * List all the products under the parent branch if [filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest#Google__Cloud__DiscoveryEngine__V1beta__ListControlsRequest_filter_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest#filter \(method\)") is unset. Currently this field is unsupported.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. A filter to apply on the list results. Supported features:

    * List all the products under the parent branch if [filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest#Google__Cloud__DiscoveryEngine__V1beta__ListControlsRequest_filter_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest#filter \(method\)") is unset. Currently this field is unsupported.



**Returns**

  * (::String) — 

Optional. A filter to apply on the list results. Supported features:

    * List all the products under the parent branch if [filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest#Google__Cloud__DiscoveryEngine__V1beta__ListControlsRequest_filter_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest#filter \(method\)") is unset. Currently this field is unsupported.



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum number of results to return. If unspecified, defaults to 50. Max allowed value is 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum number of results to return. If unspecified, defaults to 50. Max allowed value is 1000. 



**Returns**

  * (::Integer) — Optional. Maximum number of results to return. If unspecified, defaults to 50. Max allowed value is 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous `ListControls` call. Provide this to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous `ListControls` call. Provide this to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. A page token, received from a previous `ListControls` call. Provide this to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. 



**Returns**

  * (::String) — Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
