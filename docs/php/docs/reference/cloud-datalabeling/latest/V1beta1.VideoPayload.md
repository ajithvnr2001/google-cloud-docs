---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.VideoPayload
title: Google Cloud Datalabeling V1beta1 Client - Class VideoPayload (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:40.824711+00:00
---

# Google Cloud Datalabeling V1beta1 Client - Class VideoPayload (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.VideoPayload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Datalabeling V1beta1 Client - Class VideoPayload (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.2  0.6.3  0.5.7  0.4.2  0.3.1  0.2.0  0.1.14 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Datalabeling V1beta1 Client class VideoPayload.

Container of information of a video.

Generated from protobuf message `google.cloud.datalabeling.v1beta1.VideoPayload`

## Namespace

Google \ Cloud \ DataLabeling \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ mime_type` |  `string`   
Video format.  
`↳ video_uri` |  `string`   
Video uri from the user bucket.  
`↳ video_thumbnails` |  `array<[VideoThumbnail](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.VideoThumbnail)>`   
The list of video thumbnails.  
`↳ frame_rate` |  `float`   
FPS of the video.  
`↳ signed_uri` |  `string`   
Signed uri of the video file in the service bucket.  
  
### getMimeType

Video format.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMimeType

Video format.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVideoUri

Video uri from the user bucket.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setVideoUri

Video uri from the user bucket.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVideoThumbnails

The list of video thumbnails.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[VideoThumbnail](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.VideoThumbnail)>` |   
  
### setVideoThumbnails

The list of video thumbnails.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[VideoThumbnail](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.VideoThumbnail)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFrameRate

FPS of the video.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setFrameRate

FPS of the video.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSignedUri

Signed uri of the video file in the service bucket.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSignedUri

Signed uri of the video file in the service bucket.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
