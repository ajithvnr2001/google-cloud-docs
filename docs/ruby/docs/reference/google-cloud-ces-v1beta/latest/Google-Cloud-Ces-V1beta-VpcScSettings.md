---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-VpcScSettings/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::VpcScSettings (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:02.593700+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::VpcScSettings (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-VpcScSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::VpcScSettings (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::VpcScSettings.

VPC-SC settings for the app.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allowed_origins
    
    
    def allowed_origins() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls. 



### #allowed_origins=
    
    
    def allowed_origins=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls. 



**Returns**

  * (::Array<::String>) — Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
