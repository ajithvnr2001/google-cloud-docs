---
url: https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials/
title: Interstitials \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:59.128015+00:00
---

# Interstitials  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)



Send feedback 

#  Interstitials Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * VodSessionAdBreak
    * JSON representation
  * VodSessionAd
    * JSON representation
  * VodSessionContent
    * JSON representation



Describes what was stitched into a VOD session's manifest.

JSON representation  
---  
      
    
    {
      "adBreaks": [
        {
          object ([VodSessionAdBreak](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionAdBreak))
        }
      ],
      "sessionContent": {
        object ([VodSessionContent](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionContent))
      }
    }  
  
Fields  
---  
`adBreaks[]` |  `object (`[VodSessionAdBreak](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionAdBreak)`)` List of ad breaks ordered by time.  
`sessionContent` |  `object (`[VodSessionContent](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionContent)`)` Information related to the content of the VOD session.  
  
## VodSessionAdBreak

Metadata for an inserted ad break.

JSON representation  
---  
      
    
    {
      "progressEvents": [
        {
          object ([ProgressEvent](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/ProgressEvent))
        }
      ],
      "ads": [
        {
          object ([VodSessionAd](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionAd))
        }
      ],
      "endTimeOffset": string,
      "startTimeOffset": string
    }  
  
Fields  
---  
`progressEvents[]` |  `object (`[ProgressEvent](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/ProgressEvent)`)` List of events that are expected to be triggered, ordered by time.  
`ads[]` |  `object (`[VodSessionAd](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Interstitials#VodSessionAd)`)` Ordered list of ads stitched into the ad break.  
`endTimeOffset` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Ad break end time in seconds relative to the start of the VOD asset.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`startTimeOffset` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Ad break start time in seconds relative to the start of the VOD asset.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## VodSessionAd

Metadata for an inserted ad in a VOD session.

JSON representation  
---  
      
    
    {
      "duration": string,
      "companionAds": {
        object ([CompanionAds](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/CompanionAds))
      },
      "activityEvents": [
        {
          object ([Event](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Event))
        }
      ]
    }  
  
Fields  
---  
`duration` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Duration in seconds of the ad.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`companionAds` |  `object (`[CompanionAds](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/CompanionAds)`)` Metadata of companion ads associated with the ad.  
`activityEvents[]` |  `object (`[Event](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/Event)`)` The list of progress tracking events for the ad break. These can be of the following IAB types: `MUTE`, `UNMUTE`, `PAUSE`, `CLICK`, `CLICK_THROUGH`, `REWIND`, `RESUME`, `ERROR`, `FULLSCREEN`, `EXIT_FULLSCREEN`, `EXPAND`, `COLLAPSE`, `ACCEPT_INVITATION_LINEAR`, `CLOSE_LINEAR`, `SKIP`.  
  
## VodSessionContent

Metadata for the entire stitched content in a VOD session.

JSON representation  
---  
      
    
    {
      "duration": string
    }  
  
Fields  
---  
`duration` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The total duration in seconds of the content including the ads stitched in.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
