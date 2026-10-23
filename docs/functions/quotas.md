---
url: https://docs.cloud.google.com/functions/quotas/
title: Quotas \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:57.242300+00:00
---

# Quotas  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/quotas/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Resources ](https://docs.cloud.google.com/functions/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas

This document describes the quota limits for Cloud Run functions.

To increase quotas above the defaults listed here, go to the [ Cloud Run functions Quotas Page](https://console.cloud.google.com/iam-admin/quotas?service=cloudfunctions.googleapis.com&usage=ALL&project=_), select the quotas you want to modify, click **Edit quotas** , supply your user information if prompted, and enter the new quota limit for each quota you selected.

Quotas for Cloud Run functions encompass 4 areas:

  * Resource Limits

These affect the total amount of resources your functions can consume.

  * Time Limits

These affect how long things can run.

  * Rate Limits

These affect the rate at which you can call the Cloud Run functions API to manage your functions.

  * Networking Limits

These affect outbound connection and instance limits.




The different types of limits are described in more detail below. Differences between limits for Cloud Run functions (1st gen) and Cloud Run functions (2nd gen) are noted where applicable.

## Resource Limits

Resource limits affect the total amount of resources your functions can consume. The regional scope is per project, and each project maintains its own limits.

Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope  
---|---|---|---|---|---  
Number of functions | The total number of functions that can be deployed per region | 1,000 | 1,000 minus the number of Cloud Run services deployed | No | per region  
Max deployment size | The maximum size of a single function deployment | 100MB (compressed) for sources.  
500MB (uncompressed) for sources plus modules. | N/A | No | per function  
Max uncompressed HTTP request size | Data sent to HTTP Functions in an HTTP request | 10MB | 32MB | No | per invocation  
Max uncompressed HTTP response size | Data sent from HTTP functions in an HTTP response | 10MB | 10MB for streaming responses.  
32MB for non-streaming responses. | No | per invocation  
Max event size for event-driven functions | Data sent in events to background functions | 10MB | 512KB for Eventarc events.  
10MB for legacy events. | No | per event  
Max function memory | Amount of memory each function instance can use | 8GiB | 32GiB | No | per function  
Max project memory | Amount of memory, in By, that a project can use. It is measured by the total sum of user-requested memory across function instances over a 1 minute period. | Depends on selected region. This limit might be greater in high-capacity regions or lower in recently opened regions. | N/A | Yes | per project and region  
Max project CPU | Amount of CPU, in milli vCPU, that a project can use. It is measured by the total sum of user-requested CPU across function instances over a 1 minute period. | Depends on selected region. This limit might be greater in high-capacity regions or lower in recently opened regions. | N/A | Yes | per project and region  
**Note:** If you are triggering a function using Pub/Sub, either via [event-driven functions](https://docs.cloud.google.com/docs/functions/pubsub-events) or as the [HTTP target](https://docs.cloud.google.com/docs/functions/http-events) of a push subscription, be aware that Pub/Sub messages are base64-encoded. A 10 MB Pub/Sub message - the [maximum size](https://cloud.google.com/pubsub/quotas#resource_limits) supported - is larger than 10 MB once it is encoded, and can thus exceed the Cloud Run functions max size limit.

## Time Limits

Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope  
---|---|---|---|---|---  
Max function duration | The maximum amount of time a function can run before being forcibly terminated | 540 seconds | 

  * 60 minutes for HTTP functions.
  * 1800 seconds for scheduled/Task queue functions.
  * 540 seconds for event-driven functions.

| No | per invocation  
  
## Rate Limits

Quota | Description | Limit (1st gen) | Limit (2nd gen) | Can be increased | Scope  
---|---|---|---|---|---  
API calls (READ) | Calls to describe or list functions via the Cloud Run functions API | 5000 per 100 seconds | 1200 per 60 seconds | Only for 1st gen | per project (1st gen)  
per region (2nd gen)  
API calls (WRITE) | Calls to deploy or delete functions via the Cloud Run functions API | 80 per 100 seconds | 60 per 60 seconds | No 1 | per project (1st gen)  
per region (2nd gen)  
API calls (CALL) | Calls to the "call" API | 16 per 100 seconds | N/A | No 2 | per project  
1 You cannot increase the WRITE quota. Insufficient quota generally occurs due to one of the following: 

  * Use of a CI/CD system that deploys many functions concurrently or sequentially at a high rate. 
  * Use of the Firebase CLI to deploy multiple functions simultaneously.



In each case, you can avoid hitting this quota by changing the rate of deployments. For example, if you are deploying using the Firebase CLI, [use the `--only` flag to deploy individual functions](https://firebase.google.com/docs/cli/#deploy_specific_functions). 

2 The CALL API only applies to Cloud Run functions (1st gen). You cannot increase the CALL quota. Insufficient quota generally occurs if you mistakenly use this API to invoke your functions in production. Please keep in mind that this API is meant for testing with the Google Cloud console or [ `gcloud functions call`](https://cloud.google.com/sdk/gcloud/reference/functions/call) CLI, and it cannot handle heavy traffic. 

## Networking limits

For information about Cloud Run functions (2nd gen) networking request and bandwidth limits, see [Networking limits](https://cloud.google.com/run/quotas#networking_limits).

The following networking limits apply to Cloud Run functions (1st gen):

  * Outbound connections per second per instance: 500 (cannot be increased)
  * Outbound DNS resolutions per second per instance: 100 (cannot be increased)
  * Maximum packets per second per instance: 80,000
  * Maximum bits per second per instance: 100,000,000



## Scalability

Cloud Run functions invoked by HTTP scale up quickly to handle incoming traffic, while background functions scale more gradually. A function's ability to scale up is dictated by a few factors, including:

  * The amount of time it takes for a function's execution to complete (short-running functions can generally scale up to handle more concurrent requests).
  * The amount of time it takes for a function to initialize on [cold start](https://docs.cloud.google.com/functions/docs/bestpractices/tips#use_dependencies_wisely). 
  * Your function's error rate.
  * Transient factors, such as regional load and data center capacity. 

  * Your configuration as defined by [minimum instances](https://docs.cloud.google.com/functions/docs/configuring/min-instances), [maximum instances](https://docs.cloud.google.com/functions/docs/configuring/max-instances), and [concurrency](https://docs.cloud.google.com/functions/docs/configuring/concurrency) (concurrency is 2nd gen only).


[Background functions](https://docs.cloud.google.com/functions/docs/writing/background) have additional limits, as explained below. These limits do not apply to 1st gen [HTTP functions](https://docs.cloud.google.com/functions/docs/writing/http). The default [maximum instances limit](https://docs.cloud.google.com/functions/docs/configuring/max-instances) for 2nd gen HTTP functions is 100 and can be increased to 1,000. There is no default maximum instances limit for 1st gen HTTP functions. To avoid unbounded scaling events with 1st gen HTTP functions, we recommend [setting a limit](https://docs.cloud.google.com/functions/docs/configuring/max-instances#setting_maximum_instances_limits), for example, 3000. 

### Additional quotas for background functions

Quota | Description | Limit | Can be increased | Scope | Product version  
---|---|---|---|---|---  
Max concurrent invocations | The maximum concurrent invocations of a single function  
**Example:** if handling each event takes 100 seconds, the invocation rate will be limited to 30 per second on average | 3,000 | Yes | per function | 1st gen only  
Max invocation rate | The maximum rate of events being handled by a single function  
**Example:** if handling an event takes 100ms, the invocation rate will be limited to 1000 per second even if only 100 requests, on average, are handled in parallel | 1000 per second | No | per function | 1st gen only  
Max concurrent event data size | The maximum total size of incoming events to concurrent invocations of a single function  
**Example:** if events are of size 1MB and processing them takes 10 seconds, the average rate will be 1 event per second, because the 11th event will not be processed until processing one of the first 10 events finishes | 10MB | No | per function | 1st gen and 2nd gen  
Max throughput of incoming events | The maximum throughput of incoming events to a single function  
**Example:** if events are of size 1MB, then the invocation rate can be maximum 10 per second, even if functions finish within 100ms | 10MB per second | No | per function | 1st gen and 2nd gen  
  
## When you reach a quota limit

When a function consumes all of an allocated resource, the resource becomes unavailable until the quota is refreshed or increased. This may mean that your function and all other functions in the same project will not work until then. A function returns an HTTP 500 error code when one of the resources is over quota and the function cannot execute.

To increase quotas above the defaults listed here, go to the [ Cloud Run functions Quotas page](https://console.cloud.google.com/iam-admin/quotas?service=cloudfunctions.googleapis.com&usage=ALL&project=_), select the quotas you want to modify, click **Edit quotas** , supply your user information if prompted, and enter the new quota limit for each quota you selected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
