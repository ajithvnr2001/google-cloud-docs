---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-ListCustomConstraintsResponse/
title: Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::ListCustomConstraintsResponse (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:30.146293+00:00
---

# Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::ListCustomConstraintsResponse (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-ListCustomConstraintsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::ListCustomConstraintsResponse (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Cloud::OrgPolicy::V2::ListCustomConstraintsResponse.

The response returned from the [ListCustomConstraints] [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints] method. It will be empty if no custom or managed constraints are set on the organization resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_constraints
    
    
    def custom_constraints() -> ::Array<::Google::Cloud::OrgPolicy::V2::CustomConstraint>

**Returns**

  * (::Array<[::Google::Cloud::OrgPolicy::V2::CustomConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-CustomConstraint)>) — All custom and managed constraints that exist on the organization resource. It will be empty if no custom constraints are set. 



### #custom_constraints=
    
    
    def custom_constraints=(value) -> ::Array<::Google::Cloud::OrgPolicy::V2::CustomConstraint>

**Parameter**

  * **value** (::Array<[::Google::Cloud::OrgPolicy::V2::CustomConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-CustomConstraint)>) — All custom and managed constraints that exist on the organization resource. It will be empty if no custom constraints are set. 



**Returns**

  * (::Array<[::Google::Cloud::OrgPolicy::V2::CustomConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-CustomConstraint)>) — All custom and managed constraints that exist on the organization resource. It will be empty if no custom constraints are set. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. 



**Returns**

  * (::String) — Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
