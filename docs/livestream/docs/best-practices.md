---
url: https://docs.cloud.google.com/livestream/docs/best-practices/
title: Best practices for the Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:55.949345+00:00
---

# Best practices for the Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Best practices for the Live Stream API Stay organized with collections  Save and categorize content based on your preferences. 

This page contains a summary of best practices for the Live Stream API. If you are just starting out with the Live Stream API, refer to one of the [Quickstarts](https://docs.cloud.google.com/livestream/docs/quickstarts).

## Use the SRT protocol if possible

When creating the input endpoint, there are two options for the source stream protocol: [`RTMP_PUSH` and `SRT_PUSH`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#type). The SRT protocol is preferred over RTMP because SRT is more advanced and provides additional features such as the following:

  * Packet drop recovery
  * Forward error correction
  * Support for multiple audio elementary streams
  * Higher bandwidth



The choice of streaming protocol requires a proper encoder/transcoder that provides that feature. Most professional-grade encoders support SRT.

## Recommended bitrates

Use the following bitrates depending on the source resolution and framerate. Higher bitrates directly correlate to higher quality.

Resolution (ScanMode)/Framerate  | H.264 Bitrate (Mbps)  | H.265 Bitrate (Mbps)   
---|---|---  
576i/25 and 480i/29.97  | 3  | 2.7   
720p/25/30  | 8  | 7.2   
720p/50/60  | 15  | 13.5   
1080i/25 and 1080i/29.97  | 12  | 9   
1080p/50 and 1080p/60  | 20  | 15   
2160p/50 and 2160p/60  | 50  | 37.5   
  
For the output channel resolution and bitrate, depending on the input resolution/frame rate (60 FPS), add the higher frame rate step for 60 FPS if it applies. Note that adding additional steps requires more computing power. The following is the recommended ladder:

Resolution (ScanMode)/Framerate  | H.264 High Profile Bitrate (Kbps)   
---|---  
416x234 p25/30  | 150   
640x360 p25/30  | 400   
768x432 p25/30  | 750   
768x432 p25/30  | 1100   
960x540 p25/30  | 2200   
1280x720 p25/30  | 3300   
1280x720 p50/60  | 5500   
1920x1080 p25/30  | 6000   
1920x1080 p50/60  | 9000   
2560x1440 p25/30  | 10000   
2560x1440 p50/60  | 13500   
3840x2160 p25/30  | 15000   
3840x2160 p50/60  | 25000   
  
For audio, the recommendations are based on the number of channels:

Channels  | AAC Bitrate (Kbps)   
---|---  
2.0  | 64   
2.0  | 160   
5.1  | 384   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
