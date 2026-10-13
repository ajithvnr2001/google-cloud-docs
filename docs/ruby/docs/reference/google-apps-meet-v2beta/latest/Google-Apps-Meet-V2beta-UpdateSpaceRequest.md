---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateSpaceRequest/
title: Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::UpdateSpaceRequest (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:08.080002+00:00
---

# Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::UpdateSpaceRequest (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateSpaceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::UpdateSpaceRequest (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.0  0.3.2  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2BETA API class Google::Apps::Meet::V2beta::UpdateSpaceRequest.

Request to update a space.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #space
    
    
    def space() -> ::Google::Apps::Meet::V2beta::Space

**Returns**

  * ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) — Required. Space to be updated. 



### #space=
    
    
    def space=(value) -> ::Google::Apps::Meet::V2beta::Space

**Parameter**

  * **value** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) — Required. Space to be updated. 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) — Required. Space to be updated. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask used to specify the fields to be updated in the space. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask used to specify the fields to be updated in the space. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask used to specify the fields to be updated in the space. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
