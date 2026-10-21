---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-text-detection/
title: Text Detection \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:39.860817+00:00
---

# Text Detection  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-text-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Text Detection Stay organized with collections  Save and categorize content based on your preferences. 

_Text Detection_ performs Optical Character Recognition (OCR) to detect visible text from frames in a video, or video segments, and returns the detected text along with information about the frame-level location and timestamp in the video for that text.

Text Detection is particularly useful for media & entertainment use cases, including, detecting and extracting cast lists at the end of shows and movies, or detecting the presence of burnt-in subtitles.

Text detection is available for the [languages](https://docs.cloud.google.com/vision/docs/languages) supported by the Cloud Vision API.

To detect visible text from a video or video segments, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1p2beta1/videos/annotate) method and specify [`TEXT_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1p2beta1/videos#Feature) in the `features` field.

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Text%20Detection) to see this feature in action.

For examples of requesting text detection and getting the annotated results, see [Text Detection](https://docs.cloud.google.com/video-intelligence/docs/text-detection).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
