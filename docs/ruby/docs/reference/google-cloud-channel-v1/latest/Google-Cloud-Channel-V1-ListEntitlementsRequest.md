---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsRequest/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ListEntitlementsRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:28.946713+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ListEntitlementsRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ListEntitlementsRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ListEntitlementsRequest.

Request message for [CloudChannelService.ListEntitlements](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlements_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlements \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100. 



**Returns**

  * (::Integer) — Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token for a page of results other than the first page. Obtained using [ListEntitlementsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse#Google__Cloud__Channel__V1__ListEntitlementsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListEntitlementsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListEntitlements](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlements_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlements \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token for a page of results other than the first page. Obtained using [ListEntitlementsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse#Google__Cloud__Channel__V1__ListEntitlementsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListEntitlementsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListEntitlements](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlements_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlements \(method\)") call. 



**Returns**

  * (::String) — Optional. A token for a page of results other than the first page. Obtained using [ListEntitlementsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListEntitlementsResponse#Google__Cloud__Channel__V1__ListEntitlementsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListEntitlementsResponse#next_page_token \(method\)") of the previous [CloudChannelService.ListEntitlements](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_list_entitlements_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#list_entitlements \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the reseller's customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the reseller's customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id} 



**Returns**

  * (::String) — Required. The resource name of the reseller's customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
