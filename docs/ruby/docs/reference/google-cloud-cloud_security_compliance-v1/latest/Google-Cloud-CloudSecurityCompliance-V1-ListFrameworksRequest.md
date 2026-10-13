---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-ListFrameworksRequest/
title: Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworksRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:24.889100+00:00
---

# Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworksRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-ListFrameworksRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworksRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Cloud Security Compliance V1 API class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworksRequest.

Request message for [ListFrameworks][].

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

  * (::Integer) — Optional. The maximum number of frameworks to return. The default value is `500`.

If you exceed the maximum value of `1000`, then the service uses the maximum value. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of frameworks to return. The default value is `500`.

If you exceed the maximum value of `1000`, then the service uses the maximum value. 




**Returns**

  * (::Integer) — Optional. The maximum number of frameworks to return. The default value is `500`.

If you exceed the maximum value of `1000`, then the service uses the maximum value. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A pagination token returned from a previous request to list frameworks. Provide this token to retrieve the next page of results. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A pagination token returned from a previous request to list frameworks. Provide this token to retrieve the next page of results. 



**Returns**

  * (::String) — Optional. A pagination token returned from a previous request to list frameworks. Provide this token to retrieve the next page of results. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent resource name, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `projects/{project}/locations/{location}`.

The only supported location is `global`. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent resource name, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `projects/{project}/locations/{location}`.

The only supported location is `global`. 




**Returns**

  * (::String) — Required. The parent resource name, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `projects/{project}/locations/{location}`.

The only supported location is `global`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
