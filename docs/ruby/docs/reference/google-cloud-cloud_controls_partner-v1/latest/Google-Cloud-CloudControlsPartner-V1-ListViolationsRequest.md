---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListViolationsRequest/
title: Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::ListViolationsRequest (v2.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:48.496974+00:00
---

# Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::ListViolationsRequest (v2.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListViolationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::ListViolationsRequest (v2.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.1 (latest)  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Cloud Controls Partner V1 API class Google::Cloud::CloudControlsPartner::V1::ListViolationsRequest.

Message for requesting list of Violations

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

  * (::String) — Optional. Filtering results 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filtering results 



**Returns**

  * (::String) — Optional. Filtering results 



### #interval
    
    
    def interval() -> ::Google::Type::Interval

**Returns**

  * ([::Google::Type::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Type-Interval)) — Optional. Specifies the interval for retrieving violations. if unspecified, all violations will be returned. 



### #interval=
    
    
    def interval=(value) -> ::Google::Type::Interval

**Parameter**

  * **value** ([::Google::Type::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Type-Interval)) — Optional. Specifies the interval for retrieving violations. if unspecified, all violations will be returned. 



**Returns**

  * ([::Google::Type::Interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Type-Interval)) — Optional. Specifies the interval for retrieving violations. if unspecified, all violations will be returned. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Hint for how to order the results 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Hint for how to order the results 



**Returns**

  * (::String) — Optional. Hint for how to order the results 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of customers row to return. The service may return fewer than this value. If unspecified, at most 10 customers will be returned. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of customers row to return. The service may return fewer than this value. If unspecified, at most 10 customers will be returned. 



**Returns**

  * (::Integer) — Optional. The maximum number of customers row to return. The service may return fewer than this value. If unspecified, at most 10 customers will be returned. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous `ListViolations` call. Provide this to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous `ListViolations` call. Provide this to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. A page token, received from a previous `ListViolations` call. Provide this to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent resource Format `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent resource Format `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



**Returns**

  * (::String) — Required. Parent resource Format `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
