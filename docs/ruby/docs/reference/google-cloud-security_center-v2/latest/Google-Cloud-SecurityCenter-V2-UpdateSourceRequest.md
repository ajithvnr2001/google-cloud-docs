---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateSourceRequest/
title: Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::UpdateSourceRequest (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:27.014863+00:00
---

# Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::UpdateSourceRequest (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateSourceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::UpdateSourceRequest (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Security Command Center V2 API class Google::Cloud::SecurityCenter::V2::UpdateSourceRequest.

Request message for updating a source.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #source
    
    
    def source() -> ::Google::Cloud::SecurityCenter::V2::Source

**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — Required. The source resource to update. 



### #source=
    
    
    def source=(value) -> ::Google::Cloud::SecurityCenter::V2::Source

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — Required. The source resource to update. 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — Required. The source resource to update. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-FieldMask)) — The FieldMask to use when updating the source resource.

If empty all mutable fields will be updated. 




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-FieldMask)) — The FieldMask to use when updating the source resource.

If empty all mutable fields will be updated. 




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-FieldMask)) — The FieldMask to use when updating the source resource.

If empty all mutable fields will be updated. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
