---
url: https://docs.cloud.google.com/transcoder/docs/concepts/frame-rate/
title: Calculate frame rate \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:16.232948+00:00
---

# Calculate frame rate  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/concepts/frame-rate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Calculate frame rate Stay organized with collections  Save and categorize content based on your preferences. 

The Transcoder API calculates the frame rate for the output video given the frame rate of the input video and the output frame rate you specify. You specify the output frame rate, in frames per second (FPS), using the [`frameRate`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.frame_rate) field. The provided [`frameRate`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.frame_rate) must always be less than or equal to 120 FPS.

If the provided [`frameRate`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.frame_rate) is a non-standard value, then it is rounded to the closest value with three decimal places. For example, the value 23.12345 is rounded to 23.123 and results in a time base of 1000/23123.

## Frame rate conversion strategies

In cases where the output frame rate does not match the input frame rate, two frame rate conversion strategies are supported using the [`frameRateConversionStrategy`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.frame_rate_conversion_strategy) field. Set the field to one of the following:

  * `DROP_DUPLICATE`: Drops or duplicates frames to match the specified output frame rate. To set an exact FPS value, set the `frameRateConversionStrategy` to this option. You must also disable optimization for the job (set [`optimization`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.optimization) to [`DISABLED`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#optimizationstrategy)).

With this option, you can set an exact output FPS value for any given input FPS value.

  * `DOWNSAMPLE`: The default frame rate conversion strategy if no strategy is specified. Keeps every _N_ th frame. _N_ is the downsample factor that is determined by the formula (input frame rate / target frame rate).

For the `DOWNSAMPLE` option, the target video frame rate:

    * Defaults to the input frame rate if the target frame rate is larger than the input frame rate; the Transcoder API does not create new video frames.
    * Is always larger than or equal to the actual output frame rate. The input frame rate is divisible by the actual output frame rate.



For the `DOWNSAMPLE` option, the following table shows the computed output video frame rate given the input frame rate (in the first column) and the target frame rate (in subsequent columns). All frame rates are given in FPS.

Input | (30) | (60) | (25) | (50)  
---|---|---|---|---  
240 | Fail | Fail | Fail | Fail  
120 | 30 | 60 | 20 | 40  
100 | 25 | 50 | 25 | 50  
50 | 25 | 50 | 25 | 50  
60 | 30 | 60 | 20 | 30  
59.94 | 29.97 | 59.94 | 19.98 | 29.97  
48 | 24 | 48 | 24 | 48  
30 | 30 | 30 | 15 | 30  
25 | 25 | 25 | 25 | 25  
24 | 24 | 24 | 24 | 24  
23.976 | 23.976 | 23.976 | 23.976 | 23.976  
15 | 15 | 15 | 15 | 15  
12 | 12 | 12 | 12 | 12  
10 | 10 | 10 | 10 | 10  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
