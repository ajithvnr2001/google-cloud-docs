---
url: https://docs.cloud.google.com/livestream/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:35.825285+00:00
---

# Quotas and limits  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Resources ](https://docs.cloud.google.com/livestream/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Live Stream API.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Live Stream API resources. System limits can't be changed. 

## General limits

  * Live stream sessions last for 24 hours after you start a channel. After 24 hours in any [`StreamingState`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#streamingstate) other than `STOPPED` or `STOPPING`, the channel may be restarted.

  * A mux stream with a `ts` container must contain exactly one audio stream and up to one video stream.

  * Only HLS manifests can contain mux streams with the `ts` container. Manifests cannot contain a mixture of `ts` and `fmp4` mux streams.

  * Input with H265 codec is only supported for SRT inputs.




## Allocation quotas

The following regional quotas don't reset over time and instead are released when you release the resource:

Quotas per region | Value  
---|---  
Channels | 101  
Inputs | 20  
UHD output streams (H264) | 5  
HD output streams (H264) | 20  
SD output streams (H264) | 40  
H265 UHD output streams | 2  
H265 HD output streams | 3  
H265 SD output streams | 3  
H264 distribution streams | 4  
H265 distribution streams | 4  
Assets | 10  
Auto-generated transcription streams | 25  
  
1Channel quota applies to running channels. You can only run up to 10 channels at a time per region.

## Rate quotas

The following quotas apply to Live Stream API requests:

Quota | Value  
---|---  
API requests per minute | 6000  
Operation requests per minute per region | 1200  
Get requests per minute per region | 1200  
List requests per minute per region | 300  
Mutation requests per minute per region | 300  
  
These quotas apply to each Google Cloud project and are shared across all applications and IP addresses using that project.

## Input limits

Input streams must follow the limits provided below:

Tier | Resolution | Bitrate | FPS  
---|---|---|---  
SD | <720p | <=6 Mbps | <=60  
HD | <=1080p | <=25 Mbps | <=60  
UHD | <=2160p | <=50 Mbps | <=60  
  
## Output limits

Tier | Resolution | Bitrate | FPS  
---|---|---|---  
SD | <720p | <=3 Mbps | <=60  
HD | <=1080p | <=15 Mbps | <=60  
UHD | <=2160p | <=25 Mbps | <=60  
  
## Per-channel resource limits

The following limits apply to each individual channel:

Resource per channel | Value  
---|---  
Events1 | 1000  
Input attachments | 10  
Manifests | 10  
HD video output streams | 3  
UHD video output streams | 2  
Total video output streams | 10  
Distribution streams | 4  
Distributions | 10  
Audio output streams | 20  
Sprite sheet settings | 3  
  
1 Once the limit is reached, you must delete the oldest events to make room for new events.

## Quota increases

If you want to increase any of your quotas for Live Stream API, you can use the Google Cloud console to request a quota increase. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
