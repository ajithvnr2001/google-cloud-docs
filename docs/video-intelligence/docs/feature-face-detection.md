---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-face-detection/
title: Face detection \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:04.551688+00:00
---

# Face detection  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-face-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Face detection Stay organized with collections  Save and categorize content based on your preferences. 

The Video Intelligence API **Face detection** feature looks for faces in a video and returns:

  * The video segment, or segments in which a face is detected, across all videos in the given request.

  * Optional: bounding boxes defining the area of the video frame in which the face is detected. To enable this feature, set the `includeBoundingBoxes` field in the [`FaceDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#facedetectionconfig) to `True`.

  * Optional: the detected attributes of the face. To enable attribute detection set the `includeAttributes` field within [`FaceDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#facedetectionconfig) to `True`. (note: You must also set`includeBoundingBoxes` to `True`). Also see [`DetectedAttribute`](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1#detectedattribute).

Possible boolean attributes:


Attribute | Description  
---|---  
`headwear` | The person is wearing a hat, cap, scarf and so on. Does not include small objects that hold the hair (e.g., hair pins).  
`frontal_gaze` | Whether the person's eyes are looking directly into the camera as opposed to simply have both eyes visible.  
`eyes_visible` | [The sclera](https://en.wikipedia.org/wiki/Sclera) (white of the eye) is visible for both eyes.  
`glasses` | The person is wearing glasses on their face and over their eyes. The glasses may be clear or colored. Note: Worn in any other way (e.g., top of head, around the neck) the glasses are ignored.   
`mouth_open` | The person's mouth is open.  
`smiling` | The person is smiling.  
  
For an example, see [Face detection](https://docs.cloud.google.com/video-intelligence/docs/face-detection).

# Video Intelligence API Visualizer

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Face%20Detection) to see this feature in action.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
