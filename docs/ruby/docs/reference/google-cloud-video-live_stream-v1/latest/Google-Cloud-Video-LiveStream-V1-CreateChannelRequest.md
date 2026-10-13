---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-CreateChannelRequest/
title: Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::CreateChannelRequest (v2.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:24.431936+00:00
---

# Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::CreateChannelRequest (v2.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-CreateChannelRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Live Stream V1 API - Class Google::Cloud::Video::LiveStream::V1::CreateChannelRequest (v2.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.1 (latest)  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.9.0  0.8.2  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Live Stream V1 API class Google::Cloud::Video::LiveStream::V1::CreateChannelRequest.

Request message for "LivestreamService.CreateChannel".

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

  * ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be created. 



### #channel=
    
    
    def channel=(value) -> ::Google::Cloud::Video::LiveStream::V1::Channel

**Parameter**

  * **value** ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be created. 



**Returns**

  * ([::Google::Cloud::Video::LiveStream::V1::Channel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream-v1/latest/Google-Cloud-Video-LiveStream-V1-Channel)) — Required. The channel resource to be created. 



### #channel_id
    
    
    def channel_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the channel resource to be created.

This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`. 




### #channel_id=
    
    
    def channel_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the channel resource to be created.

This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`. 




**Returns**

  * (::String) — Required. The ID of the channel resource to be created.

This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. 



**Returns**

  * (::String) — Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. 



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




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
