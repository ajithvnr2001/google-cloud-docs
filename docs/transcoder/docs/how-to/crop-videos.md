---
url: https://docs.cloud.google.com/transcoder/docs/how-to/crop-videos/
title: Cropping a video \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:36.603394+00:00
---

# Cropping a video  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/crop-videos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Cropping a video Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to programmatically remove unwanted outer areas from an input video. For information on how to trim the timeline of input videos, see [Stream mappings](https://docs.cloud.google.com/transcoder/docs/concepts/stream-mappings).

Use the [`crop`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#preprocessingconfig) configuration field to specify the number of pixels to remove from each side of the input video. You can add this configuration to a [job template](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates) or include it in an [ad-hoc job configuration](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc).

The following REST/JSON configuration removes 10 pixels from the top of an input video. The input video is then scaled to meet the dimensions specified by the `widthPixels` and `heightPixels` fields in the specified codec for the [`videoStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#videostream) object. The output video is then generated from this scaled intermediate video.
    
    
    "inputs": [
      {
        "key": "input0",
        "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
        "preprocessingConfig": {
          "crop": {
            "topPixels": 10
          }
        }
      }
    ],
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
