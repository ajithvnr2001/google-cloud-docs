---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequestOrBuilder
title: Interface CreateClipRequestOrBuilder (0.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:47.970599+00:00
---

# Interface CreateClipRequestOrBuilder (0.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateClipRequestOrBuilder (0.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.101.0 (latest)  0.97.0  0.96.0  0.95.0  0.93.0  0.90.0  0.89.0  0.87.0  0.85.0  0.84.0  0.82.0  0.80.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.72.0  0.70.0  0.69.0  0.66.0  0.65.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.8  0.3.0 
    
    
    public interface CreateClipRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClip()
    
    
    public abstract Clip getClip()

Required. The resource being created

` .google.cloud.video.livestream.v1.Clip clip = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Clip](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Clip)` | The clip.  
  
### getClipId()
    
    
    public abstract String getClipId()

Required. The ID of the clip resource to be created.

This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.

`string clip_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clipId.  
  
### getClipIdBytes()
    
    
    public abstract ByteString getClipIdBytes()

Required. The ID of the clip resource to be created.

This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.

`string clip_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clipId.  
  
### getClipOrBuilder()
    
    
    public abstract ClipOrBuilder getClipOrBuilder()

Required. The resource being created

` .google.cloud.video.livestream.v1.Clip clip = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ClipOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ClipOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent resource name, in the following form: `projects/{project}/locations/{location}/channels/{channel}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource name, in the following form: `projects/{project}/locations/{location}/channels/{channel}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### hasClip()
    
    
    public abstract boolean hasClip()

Required. The resource being created

` .google.cloud.video.livestream.v1.Clip clip = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clip field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
