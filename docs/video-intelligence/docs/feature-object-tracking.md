---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-object-tracking/
title: Object tracking \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:57.010552+00:00
---

# Object tracking  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-object-tracking/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Object tracking Stay organized with collections  Save and categorize content based on your preferences. 

_Object tracking_ can track multiple objects detected in an input video or video segments and return labels (tags) associated with the detected entities along with the location of the entity in the frame.

**Note:** There is a limit on the size of the detected objects. Very small objects in the video might not get detected.

Object tracking differs from [label detection](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels). While label detection provides labels for the entire frame (without bounding boxes), object tracking detects individual objects and provides a label along with a bounding box that describes the location in the frame for each object. For example, a video of vehicles crossing an intersection may produce labels such as "car" , "truck", "bike", "tires", "lights", "window" and so on. Each label includes a series of bounding boxes showing the location of the object in the frame. Each bounding box also has an associated time segment with a time offset (timestamp) that indicates the duration offset from the beginning of the video. The annotation also contains additional entity information including an entity id that you can use to find more information about that entity in the [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).

To make an object tracking request, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1p2beta1/videos/annotate) method and specify [`OBJECT_TRACKING`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1p2beta1/videos#Feature) in the `features` field.

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Object%20Tracking) to see this feature in action.

For an example, see [Object Tracking](https://docs.cloud.google.com/video-intelligence/docs/object-tracking) and [Shot Change Detection](https://docs.cloud.google.com/video-intelligence/docs/shot-detection) tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
