---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateMirrorRequest/
title: Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::UpdateMirrorRequest (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:56.452349+00:00
---

# Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::UpdateMirrorRequest (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateMirrorRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::UpdateMirrorRequest (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud Managed Lustre V1 API class Google::Cloud::Lustre::V1::UpdateMirrorRequest.

Request for UpdateMirror.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mirror
    
    
    def mirror() -> ::Google::Cloud::Lustre::V1::Mirror

**Returns**

  * ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)) — Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`



### #mirror=
    
    
    def mirror=(value) -> ::Google::Cloud::Lustre::V1::Mirror

**Parameter**

  * **value** ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)) — Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`



**Returns**

  * ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)) — Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in the same update request being executed for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in the same update request being executed for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




**Returns**

  * (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in the same update request being executed for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Protobuf-FieldMask)) — Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Protobuf-FieldMask)) — Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Protobuf-FieldMask)) — Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
