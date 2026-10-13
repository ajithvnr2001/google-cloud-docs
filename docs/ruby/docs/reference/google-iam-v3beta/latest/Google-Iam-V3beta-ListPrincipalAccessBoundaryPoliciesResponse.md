---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-ListPrincipalAccessBoundaryPoliciesResponse/
title: Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPrincipalAccessBoundaryPoliciesResponse (v0.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:54.794042+00:00
---

# Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPrincipalAccessBoundaryPoliciesResponse (v0.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-ListPrincipalAccessBoundaryPoliciesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPrincipalAccessBoundaryPoliciesResponse (v0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3BETA API class Google::Iam::V3beta::ListPrincipalAccessBoundaryPoliciesResponse.

Response message for ListPrincipalAccessBoundaryPolicies method.

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

  * (::String) — Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #principal_access_boundary_policies
    
    
    def principal_access_boundary_policies() -> ::Array<::Google::Iam::V3beta::PrincipalAccessBoundaryPolicy>

**Returns**

  * (::Array<[::Google::Iam::V3beta::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-PrincipalAccessBoundaryPolicy)>) — The principal access boundary policies from the specified parent. 



### #principal_access_boundary_policies=
    
    
    def principal_access_boundary_policies=(value) -> ::Array<::Google::Iam::V3beta::PrincipalAccessBoundaryPolicy>

**Parameter**

  * **value** (::Array<[::Google::Iam::V3beta::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-PrincipalAccessBoundaryPolicy)>) — The principal access boundary policies from the specified parent. 



**Returns**

  * (::Array<[::Google::Iam::V3beta::PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-PrincipalAccessBoundaryPolicy)>) — The principal access boundary policies from the specified parent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
