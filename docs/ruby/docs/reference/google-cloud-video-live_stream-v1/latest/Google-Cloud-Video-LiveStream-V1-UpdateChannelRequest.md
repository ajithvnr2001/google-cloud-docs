---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-UpdateChannelRequest/
title: Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::UpdateChannelRequest (v2.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:35.356130+00:00
---

# Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::UpdateChannelRequest (v2.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-UpdateChannelRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::UpdateChannelRequest (v2.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.1 (latest)  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.9.0  0.8.2  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Live Stream V1 API class Google::Cloud::Video::LiveStream::V1::UpdateChannelRequest.

Request message for "LivestreamService.UpdateChannel".

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #channel
    
    
    def channel() -> ::Google::Cloud::Video::LiveStream::V1::Channel

**Returns**

  * ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be updated. 



### #channel=
    
    
    def channel=(value) -> ::Google::Cloud::Video::LiveStream::V1::Channel

**Parameter**

  * **value** ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be updated. 



**Returns**

  * ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be updated. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported `(00000000-0000-0000-0000-000000000000)`. 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported `(00000000-0000-0000-0000-000000000000)`. 




**Returns**

  * (::String) — A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported `(00000000-0000-0000-0000-000000000000)`. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Channel resource by the update. You can only update the following fields:

    * [`inputAttachments`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputattachment)
    * [`inputConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig)
    * [`output`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output)
    * [`elementaryStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream)
    * [`muxStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream)
    * [`manifests`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest)
    * [`spriteSheets`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet)
    * [`logConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig)
    * [`timecodeConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#timecodeconfig)
    * [`encryptions`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption)

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the mask is not present, then each field from the list above is updated if the field appears in the request payload. To unset a field, add the field to the update mask and remove it from the request payload. 




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Channel resource by the update. You can only update the following fields:

    * [`inputAttachments`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputattachment)
    * [`inputConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig)
    * [`output`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output)
    * [`elementaryStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream)
    * [`muxStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream)
    * [`manifests`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest)
    * [`spriteSheets`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet)
    * [`logConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig)
    * [`timecodeConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#timecodeconfig)
    * [`encryptions`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption)

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the mask is not present, then each field from the list above is updated if the field appears in the request payload. To unset a field, add the field to the update mask and remove it from the request payload. 




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Channel resource by the update. You can only update the following fields:

    * [`inputAttachments`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputattachment)
    * [`inputConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig)
    * [`output`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output)
    * [`elementaryStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream)
    * [`muxStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream)
    * [`manifests`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest)
    * [`spriteSheets`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet)
    * [`logConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig)
    * [`timecodeConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#timecodeconfig)
    * [`encryptions`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption)

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the mask is not present, then each field from the list above is updated if the field appears in the request payload. To unset a field, add the field to the update mask and remove it from the request payload. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
