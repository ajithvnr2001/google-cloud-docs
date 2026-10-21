---
url: https://docs.cloud.google.com/transcoder/docs/how-to/insert-ad-breaks/
title: Inserting ad breaks \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:31.310929+00:00
---

# Inserting ad breaks  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/insert-ad-breaks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Inserting ad breaks Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to programmatically insert keyframes for ad breaks in a transcoded video. The Transcoder API does not insert or play ads, or stop media playback; video player clients are responsible for handling the keyframe.

Use the [`adBreaks`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) array to insert [ad break keyframes](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#adbreak) in the output video. You can add this configuration to a [job template](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates) or include it in an [ad-hoc job configuration](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc).

The following REST/JSON configuration inserts ad break keyframes at 4, 7, and 11 seconds in the timeline of the output video:
    
    
    "adBreaks": [
      {
        "startTimeOffset": "4s"
      },
      {
        "startTimeOffset": "7s"
      },
      {
        "startTimeOffset": "11s"
      }
    ],
    

You can use a tool like [`ffprobe`](https://ffmpeg.org/ffprobe.html) to verify that the keyframes were inserted. The following output shows a sample output video _without_ ad break keyframes inserted:
    
    
    $ ffprobe -loglevel error -skip_frame nokey -select_streams v:0 -show_entries \
        frame=pkt_pts_time -of csv=print_section=0 hd.mp4
    0.000000
    3.000000
    6.000000
    9.000000
    12.000000
    ...
    

The following output shows the same output video timeline with ad break keyframes inserted:
    
    
    $ ffprobe -loglevel error -skip_frame nokey -select_streams v:0 -show_entries \
        frame=pkt_pts_time -of csv=print_section=0 hd.mp4
    0.000000
    3.000000
    4.000000 <<< Inserted keyframe here
    6.000000
    7.000000 <<< Inserted keyframe here
    9.000000
    11.000000 <<< Inserted keyframe here
    12.000000
    ...
    

You can also check the output [manifest file](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#manifest) to verify that the ad break tags were inserted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
