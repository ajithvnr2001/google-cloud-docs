---
url: https://docs.cloud.google.com/profiler/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:52.239017+00:00
---

# Quotas and limits  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Resources ](https://docs.cloud.google.com/profiler/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This page provides details on the limits that apply to using Cloud Profiler.

## Profiler API quotas and limits

The Profiler API quotas place limits on the number of API requests that the Profiler backend can support for a specific Google Cloud project. The quotas include limits on the following:

  * Number of new [profiler-agent deployments](https://docs.cloud.google.com/profiler/docs/concepts-profiling#collection) per day.
  * Number of update requests per minute.

An update request is issued each time a deployment collects a [profile type](https://docs.cloud.google.com/profiler/docs/about-profiler#types_of_profiling_available). Deployments that collect two profile types issue twice as many update requests as deployments that collect one profile type.

  * Number of update requests per day.

  * Number of list-profiles requests per day.

A list-profiles request can be issued to retrieve the profiles for your existing deployments.




If you exceed a quota, the Profiler backend rejects the API request. For example, assume that the quota for the number of new deployments per day is 75. If 80 new deployments are created in one day, then no profiling data is collected for 5 of the deployments.

As a second example, assume that you have 10 deployments for a service that collects Heap and Wall time profiling. In this case, the quota for the number of update requests per minute must be at least 20:
    
    
    10 deployments x 2 profile types per deployment x 1 update request per profile type per minute
      = 20 update requests per minute (on average)
    

If this quota is less than 20, then some profiles aren't transmitted successfully to the Profiler backend.

**Note:** Before creating a deployment, ensure that this action doesn't result in you exceeding any of the Profiler API quotas.

## Managing your quota

You can view, decrease, and increase your Profiler API quota. For more information about quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview):

  * To view your **Profiler API** quota and current usage, from the Google Cloud console, go to **Quotas** :

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

To limit your view to the Profiler API usage, set the **Service** menu to select only the **Profiler API**.

  * To decrease your Profiler API quota, see [Create a quota override](https://docs.cloud.google.com/docs/quotas/view-manage#create_override).

  * To request an increase in your Profiler API quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).




## Data retention periods

Data collected by Cloud Profiler is retained for 30 days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
