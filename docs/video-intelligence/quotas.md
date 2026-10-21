---
url: https://docs.cloud.google.com/video-intelligence/quotas/
title: Quotas and Limits \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:03.541721+00:00
---

# Quotas and Limits  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/quotas/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Resources ](https://docs.cloud.google.com/video-intelligence/docs/resources)



Send feedback 

#  Quotas and Limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current content limits and rate quotas for the Video Intelligence API. This page will be updated to reflect any changes to these restrictions and usage limits.

## Content limits

The Video Intelligence API enforces the following limits:

Content limits | Value  
---|---  
Video size | 50GB  
Videos per request | 1  
Video API annotate video length | up to 3 hours  
  
## Rate quotas

The current API usage quotas for the Cloud Video Intelligence API are as follows (and are subject to change):

Quota | Value  
---|---  
Requests per minute per project | 60  
Backend time in seconds per minute per project | 180  
Celebrity Recognition requests per minute | zero  
**Caution:** **Celebrity recognition** is [deprecated](https://docs.cloud.google.com/video-intelligence/docs/deprecations). Before requesting quota, review the conditions for approval in [Recognizing celebrities](https://docs.cloud.google.com/video-intelligence/docs/celebrity-recognition).

_Backend time_ refers to the amount of parallel processing time used to annotate video content. If you regularly send several concurrent video annotation requests, you can adjust this quota to increase the number of videos that are processed in parallel. The default of 180 seconds of backend time per minute means that approximately three videos (180 / 60 = 3) can be processed in parallel. If you regularly send five concurrent video annotation requests, you can increase the **Backend time in seconds per minute** quota to 300 so that approximately five videos are processed in parallel.

You might receive a 'resource exhausted' error if you:

  * Send more than the allowed requests per second. You should limit your rate of requests.

  * Build up too long of a queue. Wait for your current queue to process at the rate of 3 minutes of video per minute of processing by the Video Intelligence API before submitting more requests.




These quotas apply to each Video Intelligence developer project, and are shared across all applications and IP addresses using a given developer project.

## Quota increases

You can edit your quotas up to their maximum values by selecting **Edit Quotas** from the **Quotas** page of the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas) page. To request an increase above the maximum quota, edit your quota with your requested increase and justification and submit your update. You will be notified when your request has been received. You might be contacted for more information regarding your request. After your request has been reviewed, you will be notified whether it has been approved or denied.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
