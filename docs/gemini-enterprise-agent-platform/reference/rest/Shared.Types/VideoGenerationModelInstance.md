---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance/
title: VideoGenerationModelInstance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:12:57.531646+00:00
---

# VideoGenerationModelInstance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoGenerationModelInstance Stay organized with collections  Save and categorize content based on your preferences. 

An instance for a video generation prediction request.

Fields  
  
`prompt` `string` A text description of the video you want to generate. The prompt should specify the subject, style, and any specific elements or actions that should appear in the video. | `image` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image)`)` An optional image to use as a starting point for video generation, used as the first frame of the generated video. If `image` is provided, `video` and `referenceImages` cannot be used. | `video` `object (`[Video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Video)`)` An optional input video to use as a starting point for video generation. If `video` is provided, `image` and `referenceImages` cannot be used. If `mask` is also provided, the input video will be edited based on the mask. If `mask` is not provided, the input video will be extended in duration. | `lastFrame` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image)`)` Image to use as the last frame of the generated video. This field can only be used if `image` is also provided. | `cameraControl` `string` The camera motion to apply to the generated video. This field can only be used if `image` is also provided. Supported values: - `fixed`: No camera motion. - `pan_left`: Pan camera to the left. - `pan_right`: Pan camera to the right. - `tilt_up`: Tilt camera up. - `tilt_down`: Tilt camera down. - `truck_left`: Move camera to the left. - `truck_right`: Move camera to the right. - `pedestal_up`: Move camera up. - `pedestal_down`: Move camera down. - `push_in`: Move camera closer to the subject. - `pull_out`: Move camera away from the subject. | `mask` `object (`[Mask](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Mask)`)` An optional mask to apply to the input `video` for video editing tasks like inserting or removing objects, or outpainting. | `referenceImages[]` `object (`[ReferenceImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#ReferenceImage)`)` Optional reference images to guide video generation. If `referenceImages` are provided, `prompt` must also be provided, and `image`, `video`, and `lastFrame` cannot be used. You can provide up to 3 `asset` images or 1 `style` image. | JSON representation  
---  
      
    
    {
      "prompt": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image))
      },
      "video": {
        object ([Video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Video))
      },
      "lastFrame": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image))
      },
      "cameraControl": string,
      "mask": {
        object ([Mask](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Mask))
      },
      "referenceImages": [
        {
          object ([ReferenceImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#ReferenceImage))
        }
      ]
    }  
  
## Image

Defines the input image format.

Fields  
  
`mimeType` `string` The MIME type of the image. Supported MIME types: - image/jpeg - image/png | `data` `Union type`  
  
The image data. The image can be provided as either base64 encoded bytes or a Google Cloud Storage URI. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bytesBase64Encoded` `string` The image bytes encoded in base64. | `gcsUri` `string` A Google Cloud Storage URI pointing to the image file. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // data
      "bytesBase64Encoded": string,
      "gcsUri": string
      // Union type
    }  
  
## Video

Defines the input video format.

Fields  
  
`mimeType` `string` The MIME type of the video. Supported MIME types: - video/mov - video/mpeg - video/mp4 - video/mpg - video/avi - video/wmv - video/mpegps - video/flv | `data` `Union type`  
  
The video data. The video can be provided as either base64 encoded bytes or a Google Cloud Storage URI. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsUri` `string` A Google Cloud Storage URI pointing to the video file. | `bytesBase64Encoded` `string` The video bytes encoded in base64. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // data
      "gcsUri": string,
      "bytesBase64Encoded": string
      // Union type
    }  
  
## Mask

Defines the input mask format for video editing. A mask specifies regions of a video or image to modify or preserve.

Fields  
  
`mimeType` `string` The MIME type of the mask. Supported MIME types: - image/png - image/jpeg - image/webp - video/mov - video/mpeg - video/mp4 - video/mpg - video/avi - video/wmv - video/mpegps - video/flv | `maskMode` `string` Specifies how the mask is applied to the input video for editing. For `insert`, `remove`, and `remove_static` modes, the mask must have the same aspect ratio as the input video. For `outpaint` mode, the mask can be 9:16 or 16:9. Supported values: - `insert`: The mask defines a rectangular region in the first frame of the input video. The object described in the `prompt` is inserted into this region and appears in subsequent frames. - `remove`: The mask identifies an object in the first frame to track and remove from the video. - `remove_static`: The mask identifies a static region in the video from which to remove objects. - `outpaint`: The mask defines a region where the input video is placed. The area outside this region is generated based on the `prompt`. Video masks are not supported for outpainting. | `data` `Union type`  
  
The mask data. The mask can be provided as either base64 encoded bytes or a Google Cloud Storage URI. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bytesBase64Encoded` `string` The mask bytes encoded in base64. | `gcsUri` `string` A Google Cloud Storage URI pointing to the mask file. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "mimeType": string,
      "maskMode": string,
    
      // data
      "bytesBase64Encoded": string,
      "gcsUri": string
      // Union type
    }  
  
## ReferenceImage

Defines the input reference image format. A reference image provides additional context to guide video generation, such as style or assets.

Fields  
  
`image` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image)`)` The image data for the reference image. | `referenceType` `string` The type of reference image, which defines how it influences video generation. Supported values: - `asset`: The reference image provides assets to the generated video, such as the scene, an object, or a character. - `style`: The aesthetics of the reference image (e.g., colors, lighting, texture) are used to define the style of the generated video, such as 'anime', 'photography', or 'origami'. | JSON representation  
---  
      
    
    {
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance#Image))
      },
      "referenceType": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
