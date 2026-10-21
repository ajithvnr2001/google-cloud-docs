---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-shot-change-detection/
title: Live shot change detection \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:47.112969+00:00
---

# Live shot change detection  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-shot-change-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Live shot change detection Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Video Intelligence Streaming API supports live shot change detection with live streaming input of media data, and real-time streaming output of analysis results.

The following [configuration JSON object](https://github.com/google/aistreamer/tree/master/ingestion/client/cpp/config/shot.json) shows how to use [AIStreamer](https://github.com/google/aistreamer/tree/master/ingestion) live shot change detection to annotate a streaming video.
    
    
    {
        "video_config": {
            "feature": "STREAMING_SHOT_CHANGE_DETECTION"
        }
    }

The AIStreamer returns a response similar to the following example.
    
    
    Reading response.
    Shot: 0.0s to 4.170837s
    Shot: 4.204204s to 7.107107s
    Shot: 7.140473s to 11.778445s
    Shot: 11.811811s to 17.28395s
    Shot: 17.317317s to 20.82082s
    Shot: 20.854187s to 24.591257s
    Shot: 24.624624s to 30.063396s

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
