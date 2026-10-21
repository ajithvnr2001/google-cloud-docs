---
url: https://docs.cloud.google.com/speech-to-text/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:03.650002+00:00
---

# Quotas and limits  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/quotas/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Speech-to-Text.

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

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Cloud STT resources. System limits can't be changed. 

This document contains the current API restrictions and usage limits for Cloud Speech-to-Text. This page will be updated to reflect any changes to these restrictions and usage limits. We reserve the right to change these limits.

**Note:** The time limits listed refer to the length of the audio file, regardless of whether it is [multi-channel](https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel) audio. Be aware, however, that each channel is billed individually. This can lead to situations where you are billed for more time than than the duration of the audio file. See the [pricing page](https://docs.cloud.google.com/speech-to-text/pricing) for more information.

## Content Limits

Content to Cloud Speech-to-Text is provided as audio data, either directly within the `content` field of the request or referenced within a Cloud Storage URI in the `uri` field of the request. There is a limit of 10 MB on all single requests sent to the API using **local files**. In the case of the [`Recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize) and [`LongRunningRecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize) methods, this limit applies to the size of the request sent. In the case of the [`StreamingRecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#streamingrecognitionconfig) method, the 10 MB limit applies to both the initial `StreamingRecognize` request and the size of each individual message in the stream. Exceeding this limit will throw an error. There is no size limit on requests sent using audio data stored in a Cloud Storage bucket.

The API contains the following limits on the size of this content (and are subject to change).

Content Limit | Audio Length  
---|---  
Synchronous Requests | ~1 Minute  
Asynchronous Requests | ~480 Minutes*  
Streaming Requests | ~5 Minutes  
  
* Audio longer than ~1 minute must [use the `uri` field](https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize) to reference an audio file in Cloud Storage.

For `StreamingRecognize` requests, audio must be sent at a rate that approximates real time.

Attempting to process content in excess of these content limits will produce an error. For more information, see [Error messages](https://docs.cloud.google.com/speech-to-text/docs/v1/error-messages) and [Troubleshooting](https://docs.cloud.google.com/speech-to-text/docs/v1/troubleshooting).

Within any request, you may also supply a [PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/v1/adaptation) resource containing a list of phrases specific to the request. (A single word counts as a phrase in this context.) The following limits apply to such a context:

Speech Adaptation Limit | Value  
---|---  
Phrases per request | 5000  
Total characters per request | 100,000  
Characters per phrase | 100  
  
## Request Limits

The current API usage limits for Cloud Speech-to-Text are as follows (and are subject to change):

Type of Limit | Usage Limit  
---|---  
Recognition Requests per 60 seconds* | 900  
Adaptation resource requests per 60 seconds* | 10  
Processing per day | 480 hours of audio  
**Note:** Daily quotas refresh at midnight (0:00) Pacific Standard Time (PST) or Pacific Daylight Time (PDT), depending on the time of year.

* Each `StreamingRecognize` session is considered a single request even though it includes multiple frames of `StreamingRecognizeRequest` audio within the stream.

Requests or attempts at audio processing in excess of these limits will produce an error. For more information, see [Error messages](https://docs.cloud.google.com/speech-to-text/docs/v1/error-messages) and [Troubleshooting](https://docs.cloud.google.com/speech-to-text/docs/v1/troubleshooting).

These limits apply to each Cloud Speech-to-Text developer project, and are shared across all applications and IP addresses using a given a developer project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
