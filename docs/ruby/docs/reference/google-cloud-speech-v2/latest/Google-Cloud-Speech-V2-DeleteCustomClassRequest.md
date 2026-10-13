---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteCustomClassRequest/
title: Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::DeleteCustomClassRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:19.746986+00:00
---

# Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::DeleteCustomClassRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteCustomClassRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::DeleteCustomClassRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Speech-to-Text V2 API class Google::Cloud::Speech::V2::DeleteCustomClassRequest.

Request message for the [DeleteCustomClass](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-Speech-Client#Google__Cloud__Speech__V2__Speech__Client_delete_custom_class_instance_ "Google::Cloud::Speech::V2::Speech::Client#delete_custom_class \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — If set to true, and the CustomClass is not found, the request will succeed and be a no-op (no Operation is recorded in this case). 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set to true, and the CustomClass is not found, the request will succeed and be a no-op (no Operation is recorded in this case). 



**Returns**

  * (::Boolean) — If set to true, and the CustomClass is not found, the request will succeed and be a no-op (no Operation is recorded in this case). 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. 



**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the CustomClass to delete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the CustomClass to delete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`



**Returns**

  * (::String) — Required. The name of the CustomClass to delete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — If set, validate the request and preview the deleted CustomClass, but do not actually delete it. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set, validate the request and preview the deleted CustomClass, but do not actually delete it. 



**Returns**

  * (::Boolean) — If set, validate the request and preview the deleted CustomClass, but do not actually delete it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
