---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-shot-change/
title: Shot change detection \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:46.226666+00:00
---

# Shot change detection  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-shot-change/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Shot change detection Stay organized with collections  Save and categorize content based on your preferences. 

By default, the Video Intelligence API examines a video, or video segments, by frame. That is, each complete picture in the series that forms the video is examined. You can also have Video Intelligence annotate a video, or video segment, according to each shot that it detects in the input video.

_Shot change detection_ annotates a video with video segments that are generated when detecting abrupt shot changes in the video. In the output annotation, the beginning frame of each video segment indicates an abrupt shot change (i.e., the frames before and after that frame are visually different).

To detect shot changes in a video, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specify [`SHOT_CHANGE_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) in the `features` field.

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Shot%20Detection) to see this feature in action.

For examples, see [Analyzing Videos for Shot Changes](https://docs.cloud.google.com/video-intelligence/docs/analyze-shots) and the [Shot Change Detection Tutorial](https://docs.cloud.google.com/video-intelligence/docs/shot_detection).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
