---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-explicit-content/
title: Explicit content detection \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:03.439471+00:00
---

# Explicit content detection  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-explicit-content/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Explicit content detection Stay organized with collections  Save and categorize content based on your preferences. 

_Explicit Content Detection_ detects adult content within a video. Adult content is generally inappropriate for those under 18 years of age and includes, but is not limited to, nudity, sexual activities, and pornography. Such content detected in cartoons or anime is also identified.

Explicit content detection annotates a video with explicit content annotations (tags) for entities that are detected in the video or video segments provided. The response returns a video frame timestamp where the explicit content is detected.

To detect explicit content in a video, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specify [`EXPLICIT_CONTENT_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) in the `features` field.

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Explicit%20Content%20Detection) to see this feature in action.

For an example, see [Analyzing Videos for Explicit Content](https://docs.cloud.google.com/video-intelligence/docs/analyze-safesearch).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
