---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Cloud-CloudControlsPartner-V1beta-ListAccessApprovalRequestsResponse/
title: Cloud Controls Partner V1BETA API - Class Google::Cloud::CloudControlsPartner::V1beta::ListAccessApprovalRequestsResponse (v0.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:04.414802+00:00
---

# Cloud Controls Partner V1BETA API - Class Google::Cloud::CloudControlsPartner::V1beta::ListAccessApprovalRequestsResponse (v0.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Cloud-CloudControlsPartner-V1beta-ListAccessApprovalRequestsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1BETA API - Class Google::Cloud::CloudControlsPartner::V1beta::ListAccessApprovalRequestsResponse (v0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Controls Partner V1BETA API class Google::Cloud::CloudControlsPartner::V1beta::ListAccessApprovalRequestsResponse.

Response message for list access requests.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_approval_requests
    
    
    def access_approval_requests() -> ::Array<::Google::Cloud::CloudControlsPartner::V1beta::AccessApprovalRequest>

**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1beta::AccessApprovalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Cloud-CloudControlsPartner-V1beta-AccessApprovalRequest)>) — List of access approval requests 



### #access_approval_requests=
    
    
    def access_approval_requests=(value) -> ::Array<::Google::Cloud::CloudControlsPartner::V1beta::AccessApprovalRequest>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudControlsPartner::V1beta::AccessApprovalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Cloud-CloudControlsPartner-V1beta-AccessApprovalRequest)>) — List of access approval requests 



**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1beta::AccessApprovalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Cloud-CloudControlsPartner-V1beta-AccessApprovalRequest)>) — List of access approval requests 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Locations that could not be reached. 



**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
