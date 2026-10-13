---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-UpdateViewRequest/
title: Cloud Logging V2 API - Class Google::Cloud::Logging::V2::UpdateViewRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:26.146534+00:00
---

# Cloud Logging V2 API - Class Google::Cloud::Logging::V2::UpdateViewRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-UpdateViewRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Logging V2 API - Class Google::Cloud::Logging::V2::UpdateViewRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.0  0.8.1  0.7.0  0.6.0  0.5.6 

Reference documentation and code samples for the Cloud Logging V2 API class Google::Cloud::Logging::V2::UpdateViewRequest.

The parameters to `UpdateView`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The full resource name of the view to update
        
        "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
        

For example:

`"projects/my-project/locations/global/buckets/my-bucket/views/my-view"`




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The full resource name of the view to update
        
        "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
        

For example:

`"projects/my-project/locations/global/buckets/my-bucket/views/my-view"`




**Returns**

  * (::String) — Required. The full resource name of the view to update
        
        "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
        

For example:

`"projects/my-project/locations/global/buckets/my-bucket/views/my-view"`




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Protobuf-FieldMask)) — Optional. Field mask that specifies the fields in `view` that need an update. A field will be overwritten if, and only if, it is in the update mask. `name` and output only fields cannot be updated.

For a detailed `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

For example: `updateMask=filter`




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Protobuf-FieldMask)) — Optional. Field mask that specifies the fields in `view` that need an update. A field will be overwritten if, and only if, it is in the update mask. `name` and output only fields cannot be updated.

For a detailed `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

For example: `updateMask=filter`




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Protobuf-FieldMask)) — Optional. Field mask that specifies the fields in `view` that need an update. A field will be overwritten if, and only if, it is in the update mask. `name` and output only fields cannot be updated.

For a detailed `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask

For example: `updateMask=filter`




### #view
    
    
    def view() -> ::Google::Cloud::Logging::V2::LogView

**Returns**

  * ([::Google::Cloud::Logging::V2::LogView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-LogView)) — Required. The updated view. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Logging::V2::LogView

**Parameter**

  * **value** ([::Google::Cloud::Logging::V2::LogView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-LogView)) — Required. The updated view. 



**Returns**

  * ([::Google::Cloud::Logging::V2::LogView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-LogView)) — Required. The updated view. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
